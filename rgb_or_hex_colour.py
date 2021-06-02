## RGB or Hex Colour
# RGB is a color model that defines color by the combination of Red, Green, and Blue.
# An RGB tuple is composed of three numbers that specify the intensity of each color.
# Because it uses 8 bits (0s or 1s) for each color, each intensity can be transformed
# into a hexadecimal number with two digits at most. There are 256 possible shades for
# each color, since "11111111" (or hex "ff") corresponds to decimal 255, plus the number
# 000. The combination of all 256 possible shades for the three primary colors gives 256
# cubed, or over 16 million possible colors. Write a function that takes a color in RGB
# or hex and returns the opposite. If it takes in the three integers in an RGB tuple, it
# should return a string with the equivalent hexadecimal notation, plus a hash sign (#)
# at the front. If it takes in a string in hex, it should return a tuple with the three
# integers corresponding to RGB.

## Examples
# rgb_or_hex(150, 50, 76) ➞ "#96324c"
# 150 is hex 96, 50 is hex 32 and 76 is hex 4c.
# rgb_or_hex("#303749") ➞ (48, 55, 73)
# 30 is dec 48, 37 is dec 55 and 49 is dec 73.
# rgb_or_hex(170, 14, 0) ➞ "#aa0e00"
# 170 is hex aa, 14 is hex e and 0 is hex 0.

## Notes
# Remember that all three colors should be two-digit hex numbers, so for Green value 14,
# the hex value should be 0e rather than just e.
# Try using formatting or filling methods to minimize if statements.

def rgb_or_hex(*args):
    if len(args) == 3:  # colors in RGB
        if any(i > 255 or i < 0 for i in args):
            raise Exception("Invalid input.")
        str = "#"
        for h in args:
            str += hex(h)[2:].zfill(2)
        return str
    elif len(args) == 1:  # colors in hex
        if args[0][0] != '#' or any(not c.isalnum() for c in args[0][1:]):
            raise Exception("Invalid input.")
        return (int(args[0][1:3], 16), int(args[0][3:5], 16), int(args[0][5:], 16))
    else:
        raise Exception("Invalid input.")

print(rgb_or_hex(150, 50, 76))
print(rgb_or_hex("#3037FF"))
print(rgb_or_hex(170, 14, 0))