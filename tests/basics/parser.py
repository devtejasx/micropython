# parser tests

try:
    compile
except NameError:
    print("SKIP")
    raise SystemExit

# completely empty string
# MPy and CPy differ for this case
#try:
#    compile("", "stdin", "single")
#except SyntaxError:
#    print("SyntaxError")
try:
    compile("", "stdin", "eval")
except SyntaxError:
    print("SyntaxError")
compile("", "stdin", "exec")

# empty continued line
try:
    compile("\\\n", "stdin", "single")
except SyntaxError:
    print("SyntaxError")
try:
    compile("\\\n", "stdin", "eval")
except SyntaxError:
    print("SyntaxError")
try:
    compile("\\\n", "stdin", "exec")
except SyntaxError:
    print("SyntaxError")

# a line continuation at the end of the input has nothing to continue onto
for mode in ("single", "eval", "exec"):
    try:
        compile("123\\", "stdin", mode)
    except SyntaxError:
        print("SyntaxError")
    try:
        compile("123\\\n", "stdin", mode)
    except SyntaxError:
        print("SyntaxError")
