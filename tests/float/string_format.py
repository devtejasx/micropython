def test(fmt, *args):
    print("{:8s}".format(fmt) + ">" + fmt.format(*args) + "<")


test("{:10.4}", 123.456)
test("{:10.4e}", 123.456)
test("{:10.4e}", -123.456)
test("{:10.4f}", 123.456)
test("{:10.4f}", -123.456)
test("{:10.4g}", 123.456)
test("{:10.4g}", -123.456)
test("{:10.4n}", 123.456)
test("{:e}", 100)
test("{:f}", 200)
test("{:g}", 300)

test("{:10.4E}", 123.456)
test("{:10.4E}", -123.456)
test("{:10.4F}", 123.456)
test("{:10.4F}", -123.456)
test("{:10.4G}", 123.456)
test("{:10.4G}", -123.456)

test("{:06e}", float("inf"))
test("{:06e}", float("-inf"))
test("{:06e}", float("nan"))

test("{:f}", False)
test("{:f}", True)

# The following fails right now
# test("{:10.1}", 0.0)

print("%.0f" % (1.750000 % 0.08333333333))
# Below isn't compatible with single-precision float
# print("%.1f" % (1.750000 % 0.08333333333))
# print("%.2f" % (1.750000 % 0.08333333333))
# print("%.12f" % (1.750000 % 0.08333333333))

# tests for errors in format string

try:
    "{:10.1b}".format(0.0)
except ValueError:
    print("ValueError")

# Digit separators in a float format spec. These were parsed and then dropped,
# so the number came out ungrouped.
print("{:,.1f}".format(1234.5))
print("{:,.2f}".format(1234.56789))
print("{:,.1f}".format(1234567.5))
print("{:,.2f}".format(-1234567.25))
print("{:,.3f}".format(1234567890.125))
print("{:_.1f}".format(1234.5))
print("{:,.1f}".format(123.5))
print("{:,.1f}".format(0.5))
print("{:,.1f}".format(-0.5))
print("{:,.1f}".format(1e20))
print("{:,.1%}".format(1234.5))

# Nothing to group, and nothing that looks like an integer part to mangle.
print("{:,e}".format(1234.5))
print("{:,}".format(float("inf")))
print("{:,}".format(float("-inf")))
print("{:,}".format(float("nan")))

# Grouping composes with sign and alignment.
print("{:+,.1f}".format(1234.5))
print("{:>15,.1f}".format(1234.5))
print("{:<15,.1f}".format(1234.5))
print("{:^15,.1f}".format(1234.5))
