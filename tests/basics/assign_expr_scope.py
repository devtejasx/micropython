# Test scoping rules for assignment expression :=.

# Test that var is closed over (assigned to in the scope of scope0).
def scope0():
    any((var0 := i) for i in range(2))
    return var0


print("scope0")
print(scope0())
print(globals().get("var0", None))

# Test that var1 gets closed over correctly in the list comprehension.
def scope1():
    var1 = 0
    dummy1 = 1
    dummy2 = 1
    print([var1 := i for i in [0, 1] if i > var1])
    print(var1)


print("scope1")
scope1()
print(globals().get("var1", None))

# Test that var2 in the comprehension honours the global declaration.
def scope2():
    global var2
    print([var2 := i for i in range(2)])
    print(globals().get("var2", None))


print("scope2")
scope2()
print(globals().get("var2", None))

# Test that var1 in the comprehension remains local to inner1.
def scope3():
    global var3

    def inner3():
        print([var3 := i for i in range(2)])

    inner3()
    print(globals().get("var3", None))


print("scope3")
scope3()
print(globals().get("var3", None))

# Test that var4 in the comprehension honours the global declarations.
def scope4():
    global var4

    def inner4():
        global var4
        print([var4 := i for i in range(2)])

    inner4()
    print(var4)


print("scope4")
scope4()
print(globals().get("var4", None))

# Test that var5 in the comprehension honours the nonlocal declaration.
def scope5():
    def inner5():
        nonlocal var5
        print([var5 := i for i in range(2)])

    inner5()
    print(var5)
    var5 = 0  # force var5 to be a local to scope5


print("scope5")
scope5()
print(globals().get("var5", None))

# Test that a target which is also read on the right-hand side still binds in
# the parent scope, at module level.
var6 = 0
print("scope6")
print([(var6 := var6 + 1) for _ in range(3)])
print(var6)

# Same, but where the parent scope declares the name global.
def scope7():
    global var7
    var7 = 0
    print([(var7 := var7 + 1) for _ in range(3)])
    print(var7)

print("scope7")
scope7()
print(globals().get("var7", None))

# Same, but where the target is closed over rather than global.
def scope8():
    var8 = 0
    print([(var8 := var8 + 1) for _ in range(3)])
    print(var8)

print("scope8")
scope8()
print(globals().get("var8", None))
