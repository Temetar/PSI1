#!/usr/bin/env python3
from lxml import etree
from tidylib import tidy_document
from pathlib import Path

hybrid_id = 1
num_chips = 3

parser = etree.XMLParser(remove_blank_text=True)
tag = etree.parse("base.xml",parser)
Hybrid = tag.find(".//Hybrid")
chip = etree.parse("chip.xml",parser)
chip_element = chip.find("RD53")
Hybrid.insert(1,chip_element)

tag.write("result.xml",pretty_print=True)

Result = Path("result.xml").read_text()
document, errors = tidy_document(Result, options={'indent':'auto','indent-attributes':'yes', 'input-xml':'yes'})
Path("result.xml").write_text(document)