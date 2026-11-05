"""Wire constants. Numeric values are part of protocol version 2."""

from enum import IntEnum, IntFlag

MAGIC = b"DM"
VERSION = 2
DEFAULT_PORT = 21300
MAX_DATAGRAM = 1200
MAX_FRAGMENT_PAYLOAD = 1024
MAX_FRAGMENTS = 32
MAX_MESSAGE_SIZE = MAX_FRAGMENT_PAYLOAD * MAX_FRAGMENTS


class MessageKind(IntEnum):
    REQUEST = 1
    RESPONSE = 2
    ERROR = 3


class Opcode(IntEnum):
    HELLO = 1
    GET_STATUS = 2
    GET_CAPABILITIES = 3
    CAPTURE_TEXT_SCREEN = 4
    SEND_KEYS = 5
    PING = 6
    CANCEL = 7
    FILE_READ_BEGIN = 8
    FILE_READ_BLOCK = 9
    FILE_READ_END = 10
    FILE_WRITE_BEGIN = 11
    FILE_WRITE_BLOCK = 12
    FILE_WRITE_COMMIT = 13
    FILE_ABORT = 14
    GRAPHICS_BEGIN = 15
    GRAPHICS_BLOCK = 16
    GRAPHICS_END = 17
    GET_DIAGNOSTICS = 18


class ErrorCode(IntEnum):
    MALFORMED = 1
    UNSUPPORTED_VERSION = 2
    AUTHENTICATION_FAILED = 3
    REPLAYED_REQUEST = 4
    UNSUPPORTED_OPERATION = 5
    INVALID_ARGUMENT = 6
    DENIED = 7
    TARGET_BUSY = 8
    TIMEOUT = 9
    CANCELLED = 10
    INTEGRITY_FAILURE = 11
    INTERNAL_FAILURE = 12


class Capability(IntFlag):
    STATUS = 1 << 0
    TEXT_CAPTURE = 1 << 1
    KEYBOARD = 1 << 2
    FILESYSTEM_READ = 1 << 3
    FILESYSTEM_WRITE = 1 << 4
    EXECUTION = 1 << 5
    MEMORY_READ = 1 << 6
    MEMORY_WRITE = 1 << 7
    PORT_READ = 1 << 8
    PORT_WRITE = 1 << 9
    REBOOT = 1 << 10
    GRAPHICS_CAPTURE = 1 << 11


class Phase(IntEnum):
    STARTING = 1
    OBSERVE_READY = 2
    AGENT_SHELL_READY = 3
    CHILD_RUNNING = 4
    DOS_BUSY = 5
    AWAITING_APPROVAL = 6
    HOST_UNRESPONSIVE = 7


class Adapter(IntEnum):
    UNKNOWN = 0
    MDA = 1
    CGA = 2
    EGA = 3
    VGA = 4
    LINUX_PTY = 254


class GraphicsLayout(IntEnum):
    CGA_2BPP_INTERLEAVED = 1
    CGA_1BPP_INTERLEAVED = 2
    HERCULES_1BPP_INTERLEAVED = 3
    PLANAR_4BPP = 4
    PLANAR_1BPP = 5
    PACKED_8BPP = 6


class ResidentDiagnosticFlag(IntFlag):
    OWNS_INT08 = 1 << 0
    OWNS_INT1C = 1 << 1
    OWNS_INT28 = 1 << 2
    OWNS_INT2F = 1 << 3
    ENABLED = 1 << 4
    RECEIVE_READY = 1 << 5
    SESSION_ACTIVE = 1 << 6
    RESPONSE_PENDING = 1 << 7


class KeyCode(IntEnum):
    ENTER = 1
    ESC = 2
    TAB = 3
    BACKSPACE = 4
    UP = 5
    DOWN = 6
    RIGHT = 7
    LEFT = 8
    HOME = 9
    END = 10
    DELETE = 11
    PAGE_UP = 12
    PAGE_DOWN = 13
    F1 = 14
    F2 = 15
    F3 = 16
    F4 = 17
    F5 = 18
    F6 = 19
    F7 = 20
    F8 = 21
    F9 = 22
    F10 = 23
    F11 = 24
    F12 = 25
    CTRL_C = 26
    CTRL_D = 27
    # Modifier combinations (enhanced-keyboard BIOS scan codes on DOS targets).
    ALT_A = 28
    ALT_B = 29
    ALT_C = 30
    ALT_D = 31
    ALT_E = 32
    ALT_F = 33
    ALT_G = 34
    ALT_H = 35
    ALT_I = 36
    ALT_J = 37
    ALT_K = 38
    ALT_L = 39
    ALT_M = 40
    ALT_N = 41
    ALT_O = 42
    ALT_P = 43
    ALT_Q = 44
    ALT_R = 45
    ALT_S = 46
    ALT_T = 47
    ALT_U = 48
    ALT_V = 49
    ALT_W = 50
    ALT_X = 51
    ALT_Y = 52
    ALT_Z = 53
    ALT_0 = 54
    ALT_1 = 55
    ALT_2 = 56
    ALT_3 = 57
    ALT_4 = 58
    ALT_5 = 59
    ALT_6 = 60
    ALT_7 = 61
    ALT_8 = 62
    ALT_9 = 63
    ALT_F1 = 64
    ALT_F2 = 65
    ALT_F3 = 66
    ALT_F4 = 67
    ALT_F5 = 68
    ALT_F6 = 69
    ALT_F7 = 70
    ALT_F8 = 71
    ALT_F9 = 72
    ALT_F10 = 73
    ALT_F11 = 74
    ALT_F12 = 75
    SHIFT_F1 = 76
    SHIFT_F2 = 77
    SHIFT_F3 = 78
    SHIFT_F4 = 79
    SHIFT_F5 = 80
    SHIFT_F6 = 81
    SHIFT_F7 = 82
    SHIFT_F8 = 83
    SHIFT_F9 = 84
    SHIFT_F10 = 85
    SHIFT_F11 = 86
    SHIFT_F12 = 87
    CTRL_F1 = 88
    CTRL_F2 = 89
    CTRL_F3 = 90
    CTRL_F4 = 91
    CTRL_F5 = 92
    CTRL_F6 = 93
    CTRL_F7 = 94
    CTRL_F8 = 95
    CTRL_F9 = 96
    CTRL_F10 = 97
    CTRL_F11 = 98
    CTRL_F12 = 99
    CTRL_A = 100
    CTRL_B = 101
    CTRL_E = 104
    CTRL_F = 105
    CTRL_G = 106
    CTRL_H = 107
    CTRL_I = 108
    CTRL_J = 109
    CTRL_K = 110
    CTRL_L = 111
    CTRL_M = 112
    CTRL_N = 113
    CTRL_O = 114
    CTRL_P = 115
    CTRL_Q = 116
    CTRL_R = 117
    CTRL_S = 118
    CTRL_T = 119
    CTRL_U = 120
    CTRL_V = 121
    CTRL_W = 122
    CTRL_X = 123
    CTRL_Y = 124
    CTRL_Z = 125


KEY_NAMES = {key.name: key for key in KeyCode}
