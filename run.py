#!/usr/bin/env python

import os


MAIN_PATH = os.getcwd()
DATA_PATH = MAIN_PATH + "/data/MICRODATI/"
DATA_FILE = "EHIS_Microdati_Anno_2015.txt"

firstLine = True
labels = []
for line in open(DATA_PATH+DATA_FILE).readlines():
    if firstLine:
        labels = line.split("\t")
        firstLine = False
        continue
    current = {}
    entry = line.split("\t")
    for lab,item in zip(labels,entry):
        current[lab] = item 
    print current
    break

