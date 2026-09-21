# A list display pushes every element onto the VM stack before building the
# list, so a large enough one needs more stack than a function can record.
# The compiler must reject it rather than truncate the stack size, which
# would let the VM write past the end of the function's state.

results = []
for n in (1000, 70000):
    try:
        x = eval("[" + "0," * n + "]")
        results.append(len(x))
    except MemoryError:
        print("SKIP")
        raise SystemExit
    except RuntimeError as er:
        results.append("RuntimeError('{}')".format(er))
print(results)
