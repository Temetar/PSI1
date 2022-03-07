#!/usr/bin/env python3
from lxml import etree #To edit xml
from tidylib import tidy_document #To tidy up (prettyprint) xml
from pathlib import Path #To read and write text (used in combination with tidylib)
from copy import deepcopy #To add the same subtree multiple times to one root
import shutil #To copy the config .txt files
import os #To run shell commands

##### Settings #####
hybrid_id = 1 #Port on the fc7, starting at 0
num_chips = 3 #Number of chips
chip_ids = range(num_chips) #Ids of the chips, default is range(num_chips)
uri = "chtcp-2.0://localhost:10203?target=192.168.1.80:50001" #check if ip is correct
output_path = "/home/l_tester/work/pixel_phase2/Ph2_ACF_runs/tamar2/PythonScript/test/" #Path where the output files are saved. Should end in '/'.
####################

#Open Base tree and find insertion point
parser = etree.XMLParser(remove_blank_text=True)
tag = etree.parse("base.xml",parser)
Hybrid = tag.find(".//Hybrid")
Hybrid.set("Id", str(hybrid_id))
connection = tag.find(".//connection")
connection.set("uri", str(uri))
#Change configuration file path
RD53_Files = tag.find(".//RD53_Files")
RD53_Files.set("path", str(output_path))

#Insert child trees
chip = etree.parse("chip.xml",parser)
RD53 = chip.find("RD53")
for i in range(num_chips):
    RD53.set("Id", str(chip_ids[i]))
    RD53.set("Lane", str(chip_ids[i]))
    RD53.set("configfile", "CMSIT_RD53_chip"+str(i)+".txt")
    Hybrid.insert(i+1,deepcopy(RD53))
    #Copy init files
    try:
        shutil.copyfile(r'/home/l_tester/work/pixel_phase2/Ph2_ACF_runs/tamar2/configs/init/CMSIT_RD53.txt', output_path+"CMSIT_RD53_chip"+str(i)+".txt")
    except FileNotFoundError:
        print("Directory not found, creating directory")
        shutil.os.mkdir(output_path)
        shutil.copyfile(r'/home/l_tester/work/pixel_phase2/Ph2_ACF_runs/tamar2/configs/init/CMSIT_RD53.txt', output_path+"CMSIT_RD53_chip"+str(i)+".txt")

#Write to xml
tag.write(output_path+"CMSIT_autogenerated.xml",pretty_print=True)

#Format xml
Result = Path(output_path+"CMSIT_autogenerated.xml").read_text()
document, errors = tidy_document(Result, options={'indent':'auto','indent-attributes':'yes', 'input-xml':'yes'})
Path(output_path+"CMSIT_autogenerated.xml").write_text(document)


#Auto-config starts here

#Voltagetuning
#os.system('cd ..; CMSITminiDAQ -f ' + output_path + 'CMSIT_autogenerated.xml -c voltagetuning')
