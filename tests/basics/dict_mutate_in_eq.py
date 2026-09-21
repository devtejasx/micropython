# A key's __eq__ may modify the dict it is being looked up in.
# The lookup must not use the old table afterwards.


class ClearOnEq(str):
    def __eq__(self, other):
        target.clear()
        return False

    def __hash__(self):
        return hash("test")


class GrowOnEq(str):
    grown = False

    def __eq__(self, other):
        # Grow the dict (forcing a resize) the first time only; the inserts
        # themselves may compare against this key again.
        if not GrowOnEq.grown:
            GrowOnEq.grown = True
            for i in range(20):
                target["filler%d" % i] = i
        return False

    def __hash__(self):
        return hash("test")


def run(make):
    global target

    target = make()
    target[ClearOnEq("a")] = 1
    print("test" in target, len(target))

    target = make()
    target[ClearOnEq("a")] = 1
    print(target.get("test", "missing"), len(target))

    target = make()
    target[ClearOnEq("a")] = 1
    target["test"] = 2
    print(sorted(target.items()))

    target = make()
    target[ClearOnEq("a")] = 1
    try:
        del target["test"]
    except KeyError:
        print("KeyError")
    print(len(target))

    GrowOnEq.grown = False
    target = make()
    target[GrowOnEq("a")] = 1
    print("test" in target, len(target))


run(dict)
