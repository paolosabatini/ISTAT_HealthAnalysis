#!/usr/bin/env python

import os, sys
sys.path.insert(0, './python')
from Handler import initEvents

MAIN_PATH = os.getcwd()
DATA_PATH = MAIN_PATH + "/data/MICRODATI/"
DATA_FILE = "EHIS_Microdati_Anno_2015.txt"


if __name__ == "__main__":

    f = open(DATA_PATH+DATA_FILE, "r")
    full_dataset = f.readlines()
    f.close()

    print 'Reading dataset "'+(DATA_PATH+DATA_FILE)+'"'
    events = initEvents (full_dataset)
    
