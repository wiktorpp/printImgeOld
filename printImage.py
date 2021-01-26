import os
import sys
esc = chr(0x1B)

from heart import heart as bitmap
#from pebble import pebble as bitmap
size = [len(bitmap), len(bitmap[0])]
for row in range(size[0]):
    if row%2 != 0:
        print(f"{esc}[0m")
        continue
    for col in range(size[1]):
        pixelUpper =bitmap[row][col]
        try: pixelLower = bitmap[row + 1][col]
        except: pixelLower = [0, 0, 0]
        sys.stdout.write(f"{esc}[38;2;{pixelUpper[0]};{pixelUpper[1]};{pixelUpper[2]}m")
        sys.stdout.write(f"{esc}[48;2;{pixelLower[0]};{pixelLower[1]};{pixelLower[2]}m")
        sys.stdout.write("▀")
