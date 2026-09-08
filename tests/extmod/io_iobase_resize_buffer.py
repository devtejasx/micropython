# The buffer handed to IOBase.write/readinto wraps memory owned by the C
# caller, so a stream method must not be able to resize it.
# https://github.com/micropython/micropython/issues/19075

try:
    import io, json
except ImportError:
    print("SKIP")
    raise SystemExit

if not hasattr(io, "IOBase"):
    print("SKIP")
    raise SystemExit


class InPlaceAdd(io.IOBase):
    def write(self, buf):
        buf += buf
        return len(buf)


class GrowingSlice(io.IOBase):
    def write(self, buf):
        buf[0:1] = b"xx"
        return len(buf)


class Sane(io.IOBase):
    def __init__(self):
        self.out = bytearray()

    def write(self, buf):
        self.out += bytes(buf)
        return len(buf)


for cls in (InPlaceAdd, GrowingSlice):
    try:
        json.dump([], cls())
        print(cls.__name__, "no error")
    except ValueError as er:
        print(cls.__name__, "ValueError", er)

# A stream that leaves the buffer alone still works.
s = Sane()
json.dump([1, 2], s)
print(bytes(s.out))
