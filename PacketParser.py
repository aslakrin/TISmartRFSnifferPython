# -*- coding: cp1252 -*-
from __future__ import print_function
import struct


def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['rev'] = reverse
    return type('Enum', (), enums)


########################################################
## PARSING OF DATA
#########################################################

def str2bytes_gen(s):
    for k in s.split(" "):
        yield struct.pack("B", int(k, 16))

def s2b(s):
    return "".join(c for c in str2bytes_gen(s))

def b2ascii(b):
    return ':'.join(["%02X" % struct.unpack('B', y)[0] for y in b])

# Types of PDU channels
ChTypes = enum(ADV = 0x01, DATA = 0x02)

# Types of Advertisement channel PDU
AdvTypes = enum(
    ADV_IND = 0,
    ADV_DIRECT_IND = 1,
    ADV_NON_CONN_IND = 2,
    ADV_SCAN_REQ = 3,
    ADV_SCAN_RSP = 4,
    ADV_CONNECT_REQ = 5,
    ADV_DISCOVER_IND = 6,
    ADV_RESERVED = 7
    )

# Data channel PDU types
DataTypes = enum(
    DATA_RESERVED = 0,
    DATA_LL_L2CAP_CONT = 1,
    DATA_LL_L2CAP_START = 2,
    DATA_LL_CONTROL = 3
    )

# LL Control PDU Op-codes
LLCtlOp = enum(
    LL_CONNECTION_UPDATE_REQ_OPCODE = 0,
    LL_CHANNEL_MAP_REQ_OPCODE = 1,
    LL_TERMINATE_IND_OPCODE = 2,
    LL_ENC_REQ = 3,
    LL_ENC_RSP = 4,
    LL_START_ENC_REQ = 5,
    LL_START_ENC_RSP = 6,
    LL_UNKNOWN_RSP = 7,
    LL_FEATURE_REQ = 8,
    LL_FEATURE_RSP = 9,
    LL_PAUSE_ENC_REQ = 10,
    LL_PAUSE_ENC_RSP = 11,
    LL_VERSION_IND = 12,
    LL_REJECT_IND = 13,
    LL_RESERVED = 14
    )

#L2CAP ATT Opcodes
ATTOp = enum(
  ATT_ERROR_RSP               = 0x01,
  ATT_EXCHANGE_MTU_REQ        = 0x02,
  ATT_EXCHANGE_MTU_RSP        = 0x03,
  ATT_FIND_INFO_REQ           = 0x04,
  ATT_FIND_INFO_RSP           = 0x05,
  ATT_FIND_BY_TYPE_VALUE_REQ  = 0x06,
  ATT_FIND_BY_TYPE_VALUE_RSP  = 0x07,
  ATT_READ_BY_TYPE_VALUE_REQ  = 0x08,
  ATT_READ_BY_TYPE_VALUE_RSP  = 0x09,
  ATT_READ_REQ                = 0x0A,
  ATT_READ_RSP                = 0x0B,
  ATT_READ_BLOB_REQ           = 0x0C,
  ATT_READ_BLOB_RSP           = 0x0D,
  ATT_READ_MULTIPLE_REQ       = 0x0E,
  ATT_READ_MULTIPLE_RSP       = 0x0F,
  ATT_WRITE_COMMAND           = 0x10,
  ATT_WRITE_REQ               = 0x12,
  ATT_WRITE_RSP               = 0x13,
  ATT_WRITE_BLOB_REQ          = 0x14,
  ATT_WRITE_BLOB_RSP          = 0x15,
  ATT_PREPARE_WRITE_REQ       = 0x16,
  ATT_PREPARE_WRITE_RSP       = 0x17,
  ATT_EXE_WRITE_REQ           = 0x18,
  ATT_EXE_WRITE_RSP           = 0x19,
  ATT_HANDLE_VALUE_NOTIFY     = 0x1B,
  ATT_HANDLE_VALUE_IND        = 0x1D,
  ATT_HANDLE_VALUE_CONFIRM    = 0x1E,
  ATT_SIGNED_READ_RSP         = 0x8B,
  ATT_SIGNED_WRITE_CMD        = 0x90,
  ATT_SIGNED_WRITE_REQ        = 0x92,
  ATT_SIGNED_HANDLE_VALUE_NOTIFY = 0x9B,
  ATT_SIGNED_HANDLE_VALUE_IND = 0x9D
  )


ADTypes = enum(
    FLAGS                    = 0x01,
    SERVICES_16BIT_MORE      = 0x02,
    SERVICES_16BIT_COMPLETE  = 0x03,
    SERVICES_32BIT_MORE      = 0x04,
    SERVICES_32BIT_COMPLETE  = 0x05,
    SERVICES_128BIT_MORE     = 0x06,
    SERVICES_128BIT_COMPLETE = 0x07,
    LOCAL_NAME_SHORT         = 0x08,
    LOCAL_NAME_COMPLETE      = 0x09,
    TX_POWER                 = 0x0A,
    OOB_CLASS_OF_DEVICE      = 0x0D,
    OOB_SIMPLEPAIR_HASHC     = 0x0E,
    OOB_SIMPLE_PAIR_RAND     = 0x0F,
    SM_TK                    = 0x10,
    SM_OOB_FLAGS             = 0x11,
    SLAVE_CONN_INT_RANGE     = 0x12,
    SERVICES_LIST_16BIT      = 0x14,
    SERVICES_LIST_128BIT     = 0x15,
    SERVICE_DATA             = 0x16,
    APPEARANCE               = 0x19,
    MANUFACTURER_SPECIFIC    = 0xFF
    )


TRXAdd = enum(
    PUBLIC = 0x00,
    RANDOM = 0x01
    )

ADAppearances = {
    0: "Unknown",
    64: "Generic Phone",
    128: "Generic Computer",
    192: "Generic Watch",
    193: "Watch: Sports Watch",
    256: "Generic Clock",
    320: "Generic Display",
    384: "Generic Remote Control",
    448: "Generic Eye-glasses",
    512: "Generic Tag",
    576: "Generic Keyring",
    640: "Generic Media Player",
    704: "Generic Barcode Scanner",
    768: "Generic Thermometer",
    769: "Thermometer: Ear",
    832: "Generic Heart rate Sensor",
    833: "Heart Rate Sensor: Heart Rate Belt",
    896: "Generic Blood Pressure",
    897: "Blood Pressure: Arm",
    898: "Blood Pressure: Wrist",
    960: "Human Interface Device (HID)",
    961: "Keyboard",
    962: "Mouse",
    963: "Joystick",
    964: "Gamepad",
    965: "Digitizer Tablet",
    966: "Card Reader",
    967: "Digital Pen",
    968: "Barcode Scanner",
    1024: "Generic Glucose Meter",
    1088: "Generic: Running Walking Sensor",
    1089: "Running Walking Sensor: In-Shoe",
    1090: "Running Walking Sensor: On-Shoe",
    1091: "Running Walking Sensor: On-Hip",
    1152: "Generic: Cycling",
    1153: "Cycling: Cycling Computer",
    1154: "Cycling: Speed Sensor",
    1155: "Cycling: Cadence Sensor",
    1156: "Cycling: Power Sensor",
    1157: "Cycling: Speed and Cadence Sensor"
}

def list2int(l):
    ret = 0
    for i, v in enumerate(l):
        ret += v << i * 8
    return ret

def parseAdvData(a):
    advD = a
    ret = dict()
    while len(advD) >= 3:
        aLen = advD[0] - 1
        aType = advD[1]
        if not aType in ADTypes.rev: break
        advD = advD[2:]
        if len(advD) < aLen: break
        ret[aType] = advD[:aLen]
        advD = advD[aLen:]
    return ret
    
def friendlyFormatAdvData(adv):
    """Accepts a tuple of ADType and intlist with data"""
    adtype, advdata = adv
    ret = ""
    if adtype == ADTypes.FLAGS:
        ret += "LE Limited Discoverable mode, " if advdata[0] & 0x01 else ""
        ret += "LE General Discoverable mode, " if advdata[0] & 0x02 else ""
        ret += "BR/EDR Not supported" if advdata[0] & 0x04 else ""

    elif adtype in [ADTypes.SERVICES_16BIT_MORE, ADTypes.SERVICES_16BIT_COMPLETE, ADTypes.SERVICES_LIST_16BIT]:
        while len(advdata) >= 2:
            ret += "0x%04X, " % list2int(advdata[:2])
            advdata = advdata[2:]

    elif adtype in [ADTypes.SERVICES_128BIT_MORE, ADTypes.SERVICES_128BIT_COMPLETE, ADTypes.SERVICES_LIST_128BIT]:
        while len(advdata) >= 16:
            ret += "0x%032X, " % list2int(advdata[:16])
            advdata = advdata[16:]

    elif adtype in [ADTypes.LOCAL_NAME_SHORT, ADTypes.LOCAL_NAME_COMPLETE]:
        ret += ''.join([chr(x) for x in advdata])

    elif adtype == ADTypes.APPEARANCE:
        ret += ADAppearances[list2int(advdata)]
    
    else:
        ret += ":".join(["%02X" % x for x in advdata])

    return ret


class AdvPdu:
    def __init__(self, pdu):
        self.pduType = pdu[0] & 0x0F
        self.txAdd = (pdu[0] & 0x40) >> 6
        self.rxAdd = (pdu[0] & 0x80) >> 7
        self.pduLen = pdu[1] & 0x3F
        self.advPdu = pdu[2:]

        self.advInd        = None
        self.advNonConnInd = None
        self.advAdvScanInd = None
        self.advDirecInd   = None
        self.advScanReq    = None
        self.advScanRsp    = None
        self.advConnectReq = None

        if self.pduType == AdvTypes.ADV_IND:          self.advInd        = self.AdvInd(self.advPdu)
        if self.pduType == AdvTypes.ADV_NON_CONN_IND: self.advNonConnInd = self.AdvNonConnInd(self.advPdu)
        if self.pduType == AdvTypes.ADV_DIRECT_IND:   self.advDirectInd  = self.AdvDirectInd(self.advPdu)
        if self.pduType == AdvTypes.ADV_SCAN_REQ:     self.advScanReq    = self.ScanReq(self.advPdu)
        if self.pduType == AdvTypes.ADV_SCAN_RSP:     self.advScanRsp    = self.ScanRsp(self.advPdu)
        if self.pduType == AdvTypes.ADV_CONNECT_REQ:  self.advConnectReq = self.ConnectReq(self.advPdu)

    # Subclass for parsing Advertisement Indication
    class AdvInd:
        def __init__(self, pdu):
            self.advA = list2int(pdu[0:6])
            self.advData = pdu[6:]
            self.advDataDict = parseAdvData(self.advData)

        def __str__(self):
            s  = "AdvA = 0x%012X, " % self.advA
            s += "AdvData: "
            # s += ":".join("%02X" % x for x in self.advData)
            s += ', '.join("%s: %s" % (ADTypes.rev[k], friendlyFormatAdvData((k,v))) for k,v in self.advDataDict.items())
            return s

    # Non-connectable is equal to AdvInd, so just alias
    class  AdvNonConnInd(AdvInd):
        pass

    # Adv ScanInd is equal to AdvInd
    class AdvScanInd(AdvInd):
        pass

    class AdvDirectInd:
        def __init__(self, pdu):
            self.advA = list2int(pdu[:6])
            self.initA = list2int(pdu[6:])

        def __str__(self):
            s  = "AdvA = 0x%012X, " % self.advA
            s += "InitA = 0x%012X, " % self.initA
            return s

    class ScanReq:
        def __init__(self, pdu):
            self.scanA = list2int(pdu[:6])
            self.advA = list2int(pdu[6:])

        def __str__(self):
            s  = "ScanA = 0x%012X, " % self.scanA
            s += "AdvA = 0x%012X, " % self.advA
            return s

    # ScanRsp is equal to AdvInd
    class ScanRsp(AdvInd):
        pass
    
    class ConnectReq:
        class LLData:
            def __init__(self, lldata):
                self.accessAddr = list2int(lldata[0:4])
                self.CRCInit = list2int(lldata[4:7])
                self.winSize = lldata[7]
                self.winOffset = list2int(lldata[8:10])
                self.interval = list2int(lldata[10:12])
                self.latency = list2int(lldata[12:14])
                self.timeout = list2int(lldata[14:16])
                self.ChM = list2int(lldata[16:21])
                self.hop = (lldata[21] & 0x1F)
                self.sca = (lldata[21] & 0xE0) >> 5
            def __str__(self):
                return "AA: 0x%08X, CRCInit: 0x%06X, winSize: %d, winOffset: %d, Interval: %d, Latency: %d, Timeout: %d, ChM: 0x%010X, Hop: %d, SCA: %d" % \
                    (self.accessAddr, self.CRCInit, self.winSize, self.winOffset, self.interval, self.latency, self.timeout, self.ChM, self.hop, self.sca)
                
        def __init__(self, pdu):
            self.initA = list2int(pdu[0:6])
            self.advA = list2int(pdu[6:12])
            self._llData = pdu[12:]
            self.llData = self.LLData(self._llData)
        def __str__(self):
            s  = "InitA = 0x%012X, " % self.initA
            s += "AdvA = 0x%012X, " % self.advA
            s += str(self.llData)
            return s


    def get_payload(self):
        if self.pduType == AdvTypes.ADV_IND: return self.advInd
        if self.pduType == AdvTypes.ADV_NON_CONN_IND: return self.advNonConnInd
        if self.pduType == AdvTypes.ADV_DIRECT_IND: return self.advDirectInd
        if self.pduType == AdvTypes.ADV_SCAN_REQ: return self.advScanReq
        if self.pduType == AdvTypes.ADV_SCAN_RSP: return self.advScanRsp
        if self.pduType == AdvTypes.ADV_CONNECT_REQ: return self.advConnectReq

        # If it's something we have not implemented
        return None

    def __str__(self):
        s  = "Type: %s, " % AdvTypes.rev[self.pduType]
        s += "TxAdd: %s, RxAdd: %s, Len: %d" % (TRXAdd.rev[self.txAdd], TRXAdd.rev[self.rxAdd], self.pduLen)
        s += "\n"
        return s


###############################################
##  DATA CHANNEL PDU (LL Control and LL Data)
###############################################
class DataPdu:
    def __init__(self, pData):
        self.llid = pData[0] & 0x03
        self.nesn = (pData[0] & 0x04) >> 2
        self.sn   = (pData[0] & 0x08) >> 3
        self.md   = (pData[0] & 0x10) >> 4
        self.len  = pData[1] & 0x1F
        self.dataPdu = pData[2:]

        self.pl = self.get_ll()

    def get_ll(self):
        if self.llid in [DataTypes.DATA_LL_CONTROL]:
            self.pl = self.LLControl(self.dataPdu)
        if self.llid in [DataTypes.DATA_LL_L2CAP_CONT, DataTypes.DATA_LL_L2CAP_START]:
            self.pl = self.LLData(self.dataPdu)

    def get_llid_friendly(self):
        return DataTypes.rev[self.llid]

    class LLData:
        def __init__(self, pData):
            self.llData = pData[:]
            # Todo: Interpret various ATT things etc
            pass
        def __str__(self):
            return ":".join(["%02X" % x for x in self.llData])

    class LLControl:
        def __init__(self, pData):
            # Todo: Interpret various LL_ reqs and rsp
            self.llOpcode = pData[0]
            self.ctrlData = pData[1:]
        def get_llOpcode_friendly(self):
            return LLCtlOp.rev[self.llOpcode]
        def __str__(self):
            return "%s: %s" % (self.get_llOpcode_friendly(), ":".join(["%02X" % x for x in self.ctrlData]))
    
class Frame:
    def __init__(self, pData):
        if len(pData) < 19:
            self.crcOK = False
            self.pData = pData
            self.pNum = -1
            self.tStamp = -1
            self.pLen = 0
            self.ch = 0
            self.crc = 0
            self.crc = 0
            self.pdu = []
            self.sync = 0
            self.advCh = 0
            self.dataCh = 0
            self.pduCh = ChTypes.ADV
            return

        self.pData = pData
        self.pNum = struct.unpack('I', pData[0:4])[0]
        self.tStamp = struct.unpack('Q', pData[4:12])[0]
        self.tStamp = (5000*(self.tStamp >> 16) + (self.tStamp & 0xFFFF))/32 # Weird conversion to get µS
        self.pLen = struct.unpack('B', pData[12])[0]
        self.ch = struct.unpack('B', pData[-1])[0] & 0x3F
        self.crc = pData[-5:-2] + '\x00' # Append 0 because CRC is 24 bit
        self.crc = struct.unpack('I',self.crc)[0]
        self.rssi = struct.unpack('B', pData[-2])[0] - 94 # RSSI offset
        self.crcOK = True if struct.unpack('B', pData[-1])[0] & 0x80 != 0 else False
        self.pdu = [struct.unpack('B', x)[0] for x in pData[19:-5]]

        # Find out what type of PDU channel
        self.sync = struct.unpack('I', pData[15:19])[0]
        self.pduCh = ChTypes.ADV if self.sync == 0x8E89BED6 else ChTypes.DATA #ADV access address

        self.advCh = None
        self.dataCh = None

        # Parse pdu data if CRC is ok
        if self.crcOK:
            if self.pduCh == ChTypes.ADV:
                self.advCh = AdvPdu(self.pdu)
            elif self.pduCh == ChTypes.DATA:
                self.dataCh = DataPdu(self.pdu)

    def get_ch(self):
        if not self.crcOK: return None
        if self.pduCh == ChTypes.ADV:
            return self.advCh
        elif self.pduCh == ChTypes.DATA:
            return self.dataCh
        return None
        
    def __str__(self):
        s =  "#\t %s\n" % self.pNum
        s += "T\t %s\n" % self.tStamp
        s += "Ch\t %s\n" % self.ch
        s += "Rssi\t %s\n" % self.rssi
        s += "CRC\t %s %s\n" % (hex(self.crc), 'OK' if self.crcOK else 'FAIL')
        s += "AAddr\t %X\n" % self.sync
        s += "PDU Ch\t %s\n" % ChTypes.rev[self.pduCh]
        s += "Len\t %s\n" % self.pLen
        #s += "PDU:\t" + tohex(self.pData[12:-3]) + "\n"
        s += str(self.get_ch())
        s += str(self.get_ch().get_payload())
        return s


#                                                       TY LN
# 00 3A 00 00 00 C9 08 37 6C 01 00 00 00 1E D6 BE 89 8E 00 13 8C DF E4 31 18 00 02 01 05 03 19 C0 03 05 02 12 18 0F 18 25 3C 10 33 A5
#    PP PP PP PP TT TT TT TT TT TT TT TT LN AA AA AA AA HH HH SS SS SS SS SS SS DD DD DD DD DD DD DD DD DD DD DD DD DD FF FF FF R? OK
#
#    00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43
#
# [P] Packet 58
# [T] Time +3000, = 14038950
# [ ] Ch0x25
# [A] AccessAddr: 0x8E89BED6
# PDU Type: ADV_PDU -> ADV_IND
# [H] Adv PDU Header:
#  Type = 0, TxAdd = 0, RxAdd = 0, PDU-Len = 19
# [S] AdvA = 0x001831E4DF8C
# [D]AdvData = 02 01 05 03 19 C0 03 05 02 12 18 0F 18
# [F]CRC = 0x103C25
# RSSI = -43


######################################
# Receiver class for BLE UDP data
######################################
class StreamParser:
    SPStates = enum(WAITING_00 = 0x01, WAITING_LEN = 0x02, WAITING_EOF = 0x03)
    STREAM_LEN_OFFSET = 12

    def __init__(self, cb):
        self.p_state = self.SPStates.WAITING_00
        self.p_len = 0
        self.p_parse = ''
        self.callback = cb

    def parse(self, s):
        ret = None
        if s == '': return None
        self.p_parse += s

        if self.p_state == self.SPStates.WAITING_00:
            if len(self.p_parse) >= 1:
                sof = struct.unpack('B', self.p_parse[0])[0] # Expect everything to be in order. Could have done forward sanity check but meh.
                if sof == 1:
                    self.p_state = self.SPStates.WAITING_LEN
                self.p_parse = self.p_parse[1:] # Discard leading byte
            else:
                return None;

        if self.p_state == self.SPStates.WAITING_LEN:
            if len(self.p_parse) >= self.STREAM_LEN_OFFSET:
                self.p_len = struct.unpack('B', self.p_parse[self.STREAM_LEN_OFFSET])[0]
                self.p_state = self.SPStates.WAITING_EOF
            else:
                return None

        if self.p_state == self.SPStates.WAITING_EOF:
            if len(self.p_parse) >= self.STREAM_LEN_OFFSET + self.p_len:
                ret = self.p_parse[ : self.STREAM_LEN_OFFSET + self.p_len + 2]
                self.p_parse = self.p_parse[self.STREAM_LEN_OFFSET + self.p_len + 2 : ]
                self.p_state = self.SPStates.WAITING_00
                if self.callback is not None:
                    self.callback(ret)
            else:
                return None

        return ret


