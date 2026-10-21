# test that parsing an integer string too big for 64 bits either gives the
# right value (arbitrary precision) or raises OverflowError, but never wraps

for s in (
    "9223372036854775808",
    "18446744073709551615",
    "18446744073709551616",
    "18446744073709551617",
    "18446744073709551625",
    "-18446744073709551616",
    "184467440737095516160",
    "0x10000000000000000",
):
    try:
        v = int(s, 0)
        ok = ("%#x" % v if s.startswith("0x") else str(v)) == s
    except OverflowError:
        ok = True
    print(s, ok)
