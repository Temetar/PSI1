#!/usr/bin/env python3
from lxml import etree #To edit xml
from tidylib import tidy_document #To tidy up (prettyprint) xml
from pathlib import Path #To read and write text (used in combination with tidylib)
from copy import deepcopy #To add the same subtree multiple times to one root
import shutil #To copy the config .txt files
import os #To run shell commands
import re #To find variable in string
import numpy as np #Better arrays
from time import sleep

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
    RD53.set("configfile", "CMSIT_RD53_chip"+str(chip_ids[i])+".txt")
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

#Voltagetuning, Replaces string in .xml, modify carefully.
"""run_number = Path('../RunNumber.txt').read_text()

os.system('cd ..; CMSITminiDAQ -f ' + output_path + 'CMSIT_autogenerated.xml -c voltagetuning')
logfile = open('../logs/CMSITminiDAQ' + run_number[:-1] + '_voltagetuning.log')
logfile = logfile.readlines()
for i in chip_ids:
    for line in logfile:
        if (str(i) + '[0m[32m] are: VDDD') in line:
            #print(line)
            VDDs = re.match(r'(.*)VDDD = \[1m\[33m(.*)\[0m\[32m, VDDA = \[1m\[33m(.*)\[0m', line)
            #VDDD = re.match('(.*)\[(.*)', 'abc[3')
            VDDD = VDDs.group(2)
            VDDA = VDDs.group(3)
            #print(VDDD)
            #print(VDDA)
    document = document.replace('VOLTAGE_TRIM_DIG="16"', 'VOLTAGE_TRIM_DIG="'+str(VDDD)+'"', 1)
    document = document.replace('VOLTAGE_TRIM_ANA="16"', 'VOLTAGE_TRIM_ANA="'+str(VDDA)+'"', 1)
Path(output_path+"CMSIT_autogenerated.xml").write_text(document)
print("Successfully set VDDD and VDDA")

print("To apply the voltage tuning, please do a power cycle. Continuing in")
for i in range(10,0,-1):
    print(i)
    sleep(1)"""
os.system('cd ..; CMSITminiDAQ -f ' + output_path + 'CMSIT_autogenerated.xml -c voltagetuning')
for i in chip_ids:
    logfile = open(output_path + "CMSIT_RD53_chip"+str(i)+".txt")
    logfile = logfile.readlines()
    for line in logfile:
        if "VOLTAGE_TRIM_DIG" in line:
            VDD = int(re.match('VOLTAGE_TRIM_DIG          0xA2          0x0010                  0x(.*)                             05', line).group(1),16)
            document = document.replace('VOLTAGE_TRIM_DIG="16"','VOLTAGE_TRIM_DIG="'+str(VDD)+'"',1)
        elif "VOLTAGE_TRIM_ANA" in line:
            VDA = int(re.match('VOLTAGE_TRIM_ANA          0xA3          0x0010                  0x(.*)                             05', line).group(1),16)
            document = document.replace('VOLTAGE_TRIM_ANA="16"','VOLTAGE_TRIM_DIG="'+str(VDA)+'"',1)
Path(output_path+"CMSIT_autogenerated.xml").write_text(document)

#Latency tuning

#Coarse latency
document = document.replace('"DoFast">0','"DoFast">1')
Path(output_path+"CMSIT_autogenerated.xml").write_text(document)
os.system('cd ..; CMSITminiDAQ -f ' + output_path + 'CMSIT_autogenerated.xml -c latency')
latency_max = 0
latency_min = 511
for i in chip_ids:
    logfile = open(output_path + "CMSIT_RD53_chip"+str(i)+".txt")
    logfile = logfile.readlines()
    for line in logfile:
        if "LATENCY_CONFIG" in line:
            #print(line)
            latency_max_temp = int(re.match('LATENCY_CONFIG            0x25          0x01F4                  0x(.*)                             09', line).group(1),16)
            latency_max = max(latency_max, latency_max_temp)
            latency_min = min(latency_min, latency_max_temp - 10)
document = document.replace('"LatencyStart">0','"LatencyStart">'+str(latency_min))
document = document.replace('"LatencyStop">511','"LatencyStop">'+str(latency_max))
Path(output_path+"CMSIT_autogenerated.xml").write_text(document)
sleep(2)

#Fine Latency
document = document.replace('"DoFast">1','"DoFast">0')
document = document.replace('nTRIGxEvent">10','nTRIGxEvent">1')
Path(output_path+"CMSIT_autogenerated.xml").write_text(document)
os.system('cd ..; CMSITminiDAQ -f ' + output_path + 'CMSIT_autogenerated.xml -c latency')
for i in chip_ids:
    logfile = open(output_path + "CMSIT_RD53_chip"+str(i)+".txt")
    logfile = logfile.readlines()
    for line in logfile:
        if "LATENCY_CONFIG" in line:
            #print(line)
            latency = int(re.match('LATENCY_CONFIG            0x25          0x01F4                  0x(.*)                             09', line).group(1),16)
            document = document.replace('LATENCY_CONFIG="136"','LATENCY_CONFIG="'+str(latency)+'"',1)
Path(output_path+"CMSIT_autogenerated.xml").write_text(document)
sleep(2)

#Threshold equalization
os.system('cd ..; CMSITminiDAQ -f ' + output_path + 'CMSIT_autogenerated.xml -c threqu')
sleep(2)
#Threshold adjustment
os.system('cd ..; CMSITminiDAQ -f ' + output_path + 'CMSIT_autogenerated.xml -c thradj')