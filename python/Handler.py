#!/usr/bin/env python

import random
from Event import Event

DEBUG = True

def initEvents (full_dataset):
    keys = full_dataset [0]
    events= []
    index = 1
    for e in full_dataset:
        if (index%1000) == 0: print 'Event %d / %d' % (index, len(full_dataset))
        if e == keys: continue
        events.append (Event (keys, e))
        index = index+1
        if DEBUG and index == 10000: break 
            
    if DEBUG:
        print 'DEBUG: initEvents(), pick random'
        for i in range (0,1):
            e = random.choice (events)
            print '* Event %s ' % (e.PID)
            for k in [ a for a in dir(e) if not a.startswith('__')]:
                print '\t %s = %s' % (k, getattr(e, k))


    return events


def decodeSelection (selection):
    
    if selection == 'tmp':
        return 'int (self.STANZE) == 4'
    if selection == 'breath_system':
        return 'self.CD1A == "1" OR self.CD1A1 == "1" OR self.CD1B == "1" OR self.CD1B1 == "1"'
    elif selection == 'circ_system':
        return 'self.CD1C== "1" OR self.CD1C1 == "1" OR self.CD1D == "1" OR self.CD1D1 == "1" OR self.CD1E == "1" OR self.CD1E1 == "1" OR self.CD1F == "1" OR self.CD1F1 == "1" OR self.CD1G == "1" OR self.CD1G1 == "1" OR self.CUORE == "1" OR self.CUORE1 == "1"'
    elif selection == 'digest_system':
        return 'self.CD1L == "1" OR self.CD1L1 == "1" OR self.CD1M == "1" OR self.CD1M1 == "1" OR self.CD1N == "1" OR self.CD1N1 == "1" OR self.INREN == "1" OR self.INREN1 == "1"'
    elif selection == 'healthy':
        selection_string = str()
        for letter in [chr(i) for i in range(ord('A'),ord('N')+1)]:
            selection_string += 'self.CD1'+letter+' != "1" AND self.CD1'+letter+'1 != "1" AND '
        for section in ['CUORE', 'INREN', 'TUMOR', 'ALZH', 'PARKIN']:
            selection_string += 'self.'+section+' != "1" AND self.'+section+'1 != "1" AND '
        return selection_string [:-4]
    else:
        print 'ERROR Selection %s not found: no selection applied' % selection
        return 'ALL'
    
    
def selectEvents (selection, events):
    condition = decodeSelection (selection)
    sel_events = [x for x in events if x.fulfil (condition)]
    return sel_events
