#!/usr/bin/env python3
import math
import lxml.etree as ET

base_case = ET.parse("base.xml")
base_case_root = base_case.getroot()
chip_case = ET.parse("chip.xml")
chip_case_root = chip_case.getroot()

hybrid_id = 1
num_chips = 3


print(base_case_root[0][1][0])
for i in range(num_chips):
    print(chip_case_root.tag)
    base_case_root[0][1][0].extend(chip_case_root)

base_case.write("result.xml")