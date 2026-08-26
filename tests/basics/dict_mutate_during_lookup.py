# Mutating a dict from __hash__ or __eq__ while that same dict is being looked
# up must not crash the interpreter.

# __eq__ clears the dict part-way through the probe
class ClearOnEq:
    def __hash__(self):
        return 1

    def __eq__(self, other):
        d.clear()
        return False


d = {}
d[ClearOnEq()] = "value"
print(ClearOnEq() in d)
print(len(d))


# __hash__ clears the dict before the probe even starts
class ClearOnHash:
    def __hash__(self):
        e.clear()
        return 1

    def __eq__(self, other):
        return False


e = {1: "a", 2: "b"}
print(e.get(ClearOnHash()))
print(len(e))


# __eq__ deletes the key that is being looked up
class DeleteOnEq:
    def __hash__(self):
        return 2

    def __eq__(self, other):
        f.pop(stored, None)
        return False


f = {}
stored = DeleteOnEq()
f[stored] = "value"
print(DeleteOnEq() in f)
print(len(f))
