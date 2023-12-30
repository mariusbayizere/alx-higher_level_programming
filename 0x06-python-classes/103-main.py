#!/usr/bin/python3

import dis
MagicClass = __import__('103-magic_class').MagicClass

print("\nDisassembly of __init__:")
dis.dis(MagicClass.__init__)
print("\nDisassembly of area:")
dis.dis(MagicClass.area)
print("\nDisassembly of circumference:")
dis.dis(MagicClass.circumference)
