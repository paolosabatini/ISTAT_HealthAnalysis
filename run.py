#!/usr/bin/env python

import os, sys
sys.path.insert(0, './python')
from Handler import initEvents
from Handler import selectEvents

MAIN_PATH = os.getcwd()
DATA_PATH = MAIN_PATH + "/data/MICRODATI/"
DATA_FILE = "EHIS_Microdati_Anno_2015.txt"


if __name__ == "__main__":

    f = open(DATA_PATH+DATA_FILE, "r")
    full_dataset = f.readlines()
    f.close()

    print 'Reading dataset "'+(DATA_PATH+DATA_FILE)+'"'
    events = initEvents (full_dataset)
    # breath_events = selectEvents ('breath_system', events)
    # circ_events = selectEvents ('circ_system', events)
    # digest_events = selectEvents ('digest_system', events)
    # healthy_events = selectEvents ('healthy', events)
    tmp_events = selectEvents ('tmp', events)

    print 'Selected events:'
    # print '\t* Breath system issues: %d / %d' % (len (breath_events), len (events))
    # print '\t* Circulation system issues: %d / %d' % (len (circ_events), len (events))
    # print '\t* Digestive system issues: %d / %d' % (len (digest_events), len (events))
    # print '\t* Healthy: %d / %d' % (len (healthy_events), len (events))
    print '\t* tmp: %d / %d' % (len (tmp_events), len (events))
 
