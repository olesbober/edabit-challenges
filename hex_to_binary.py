## Hex to Binary
# Create a function that will take a HEX number and returns the binary equivalent (as a string).

## Examples
# to_binary(0xFF) ➞ "11111111"
# to_binary(0xAA) ➞ "10101010"
# to_binary(0xFA) ➞ "11111010"

## Notes
# The number will be always an 8-bit number.

def to_binary(num):
    s = ""
    while num > 0:
        s = str(num%2)+s
        num = num>>1
    return s

print(to_binary(0xDAB))