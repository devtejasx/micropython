# Calling a function whose state does not fit on the heap, and is too large
# for the C stack as well, must raise instead of overflowing the stack.

try:
    import micropython

    micropython.heap_lock
except (ImportError, AttributeError):
    print("SKIP")
    raise SystemExit

# A list display pushes every element onto the VM stack before building the
# list, so this function needs about 20000 words of state.
try:
    exec("def f():\n return [" + "0," * 20000 + "]")
except MemoryError:
    print("SKIP")
    raise SystemExit

# With the heap locked the state cannot come from the heap.
result = None
micropython.heap_lock()
try:
    f()
    result = "returned"
except RuntimeError:
    result = "RuntimeError"
except MemoryError:
    result = "MemoryError"
micropython.heap_unlock()
print(result)
