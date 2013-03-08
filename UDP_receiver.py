# -*- coding: cp1252 -*-
import socket, struct
import msvcrt # For keyboard read


# Enums
from PacketParser import enum, ChTypes, AdvTypes, DataTypes, LLCtlOp, ATTOp, ADTypes, TRXAdd

# Classes
from PacketParser import StreamParser, Frame, AdvPdu



###########################
### Convenience functions
###########################
def tohex(s):
    hexarr = "0123456789ABCDEF"
    return ' '.join([hexarr[struct.unpack('B', b)[0]>>4&0xF]+hexarr[struct.unpack('B', b)[0]&0xF] for b in s])

def kbfunc():
    return ord(msvcrt.getch()) if msvcrt.kbhit() else 0

# Organization of the parsed data into sub-objects:
#
# Frame -> Channel -> Payload
#
# To access data in the Frame object, use
#   f.<frame contains> below, for instance `f.rssi´
#
# To access data in the Advertisement channel object, if the frame is of that type, use
#   f.pl.<channel contains> below (pl here means the payload of the Frame),
#   for instance f.pl.txAdd to see whether the advertised address is public or private.
#   This will cause an error if you try to access f.pl.nesn on an advertisement channel pdu.
#  
#
# To access for instance the initiator address of a ConnReq frame, do
#   f.pl.pl.initA, 
###
### FRAME -- class Frame
# - pNum        Packet number as received from sniffer
# - tStamp      Running µs timestamp from sniffer
# - ch          Physical channel number (0..39)
# - rssi        RSSI as received by sniffer
# - crc         CRC contained in OTA data
# - crcOk       Boolean of whether CRC matches calculated
# - sync        Sync word: Access Address   
# - pduCh       1=ADV, 2=DATA see ChTypes enum
# - pLen        Length of PHY payload
# - pl          Object containing parsed channel payload (AdvPdu or DataPdu object)
#
## ADVERTISEMENT CH PDU -- class AdvPdu
# - pduType     See AdvTypes enum (ADV_IND, SCAN_REQ etc)
# - txAdd       Public or random TX address
# - rxAdd       Public or random RX address (see TRXAdd enum)
# - pduLen      Length of Advertisement channel PDU
# - pl          Object containing parsed advertisement PDU according to pduType
#
# Payload contains, where relevant for Adv data channel PDUs,
# - advA        Address of advertiser
# - initA       Address of initiator
# - scanA       Address of scanner
# - advData     Advertisement data (only for AdvInd, AdvNonConn, ScanInd, ScanRsp)
# - advDataDict Dictionary containing parsed AdvData with ADTypes as key
# - llData      LLData object containing parsed LL data. accessed via llData.<below>
# -- accessAddr
# -- CRCInit    
# -- winSize
# -- winOffset
# -- interval
# -- latency
# -- timeout
# -- ChM
# -- hop
# -- sca


def AnalyzeIncoming(f):
    global frames
    global knownAdvertisers

    # Check if it was a valid packet
    if not f.crcOK: return
    
    frames.append(f)

    # Find out whether it was an advertising packet
    if f.pduCh == ChTypes.ADV:
        # Now check if it was a packet with advA
        if f.pl.pduType in [AdvTypes.ADV_IND, AdvTypes.ADV_DIRECT_IND, AdvTypes.ADV_NON_CONN_IND, AdvTypes.ADV_SCAN_RSP]:
            # Add advA to knownAdvertisers if it's not known
            if not f.pl.pl.advA in knownAdvertisers:
                knownAdvertisers.append(f.pl.pl.advA)
                lname = ""
                if ADTypes.LOCAL_NAME_COMPLETE in f.pl.pl.advDataDict:
                    lname = f.pl.pl.advDataDict[ADTypes.LOCAL_NAME_COMPLETE]
                elif ADTypes.LOCAL_NAME_SHORT in f.pl.pl.advDataDict:
                    lname = f.pl.pl.advDataDict[ADTypes.LOCAL_NAME_SHORT]
                print "New advertiser: 0x%012X, '%s', RSSI: %d, Total: %d" % (f.pl.pl.advA, lname, f.rssi, len(knownAdvertisers))

                                                                  



# Intialize global variables
frames = []
knownAdvertisers = []


def main():
    global frames
    global knownAdvertisers
    
    try:
        ### UDP INIT
        UDP_IP = "127.0.0.1"    # UDP ADDRESS
        UDP_PORT = 5000         # UDP PORT

        sock = socket.socket(socket.AF_INET,    # Internet
                             socket.SOCK_DGRAM) # UDP
        sock.bind((UDP_IP, UDP_PORT))
        sock.setblocking(0)

        
        # Set up the StreamParser callback function.
        # StreamParser sends the raw bytestring, so pass through Frame() to parse
        sp = StreamParser(lambda x: AnalyzeIncoming(Frame(x)))

        while True:
            # Check if key was hit, in that case, reset known counter
            if msvcrt.kbhit() and msvcrt.getch():
                print ">> Keypress detected. Resetting known advertisers\n"
                knownAdvertisers = []
            
            ## RECEIVE UDP
            try:
                data, addr = sock.recvfrom(1024)
                sp.parse(data)
                
            except IOError: # If no data, IOError is raised. Ignore this.
                pass

    finally:
        sock.close()

# Run main function if this file was executed directly and not e.g. imported.
if __name__ == "__main__":
    main()
