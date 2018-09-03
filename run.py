#!/usr/bin/env python

import os
import sys
sys.path.insert(0, './python')
from Class import Interview
from Plot import *
from Filler import *
import argparse

parser = argparse.ArgumentParser(description='Parser for the Health analysis.')
parser.add_argument('--smoke', action='store_true', help='Perform analysis on smoking')
args = parser.parse_args()

MAIN_PATH = os.getcwd()
DATA_PATH = MAIN_PATH + "/data/MICRODATI/"
DATA_FILE = "EHIS_Microdati_Anno_2015.txt"

firstLine = True
labels = []
geo_weights = {'NordWest':0.0,'NordEast':0.0,'Center':0.0,'South':0.0}
geo_smoke = {'NordWest':0.0,'NordEast':0.0,'Center':0.0,'South':0.0}

for line in open(DATA_PATH+DATA_FILE).readlines():
    if firstLine:
        labels = line.split("\t")
        firstLine = False
        continue
    current = {}
    entry = line.split("\t")
    for lab,item in zip(labels,entry):
        current[lab] = item 
    intvw = Interview(current)
    geo_weights[str(intvw.geo)] = geo_weights[str(intvw.geo)] + 1
    if str(intvw.smokeflag) != "UNKNOWN":
        geo_smoke[str(intvw.geo)] += smokeFiller(intvw.smokeflag)
    
    

norm_geo = sum(geo_weights.itervalues())
avg_geo = norm_geo/len(geo_weights)
for g in geo_weights:
     geo_weights[g] /= avg_geo

norm_smoke = sum(geo_smoke.itervalues())
for g in geo_smoke:
     geo_smoke[g] /= norm_smoke
     geo_smoke[g] = geo_smoke[g]*geo_weights[g]
     



if args.smoke:
    print "Running analysis on smokers .."
    plotGeoWeights(geo_weights)
    plotGeoSmoke(geo_smoke)
