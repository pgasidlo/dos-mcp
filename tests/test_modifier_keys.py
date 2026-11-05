from dos_mcp.protocol.constants import KeyCode
from dos_mcp.protocol.messages import KeyRequest


def test_modifier_key_codes_are_unique_bytes() -> None:
    values = [key.value for key in KeyCode]
    assert len(values) == len(set(values))
    assert all(0 < value < 256 for value in values)
    assert KeyCode.CTRL_C == 26 and KeyCode.CTRL_D == 27
    assert KeyCode.ALT_A == 28 and KeyCode.ALT_Z == 53
    assert KeyCode.ALT_0 == 54 and KeyCode.ALT_F1 == 64
    assert KeyCode.SHIFT_F1 == 76 and KeyCode.CTRL_F1 == 88
    assert KeyCode.CTRL_A == 100 and KeyCode.CTRL_Z == 125


def test_modifier_keys_round_trip_through_key_request() -> None:
    keys = (KeyCode.ALT_X, KeyCode.ALT_F1, KeyCode.SHIFT_F4, KeyCode.CTRL_F12, KeyCode.CTRL_A)
    request = KeyRequest(text=b"", keys=keys, inter_key_delay_ms=0)
    decoded = KeyRequest.decode(request.encode())
    assert decoded.keys == keys
