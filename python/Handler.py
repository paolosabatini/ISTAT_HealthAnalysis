#!/usr/bin/env python

import random
from Event import Event

DEBUG = True

def initEvents (full_dataset):
    keys = full_dataset [0]
    events= []
    index = 1
    for e in full_dataset:
        if (index%1000) == 0: print 'Event %d / %d' % (index, n_keys)
        if e == keys: continue
        events.append (Event (keys, e))
        index = index+1
        if DEBUG and index == 100: break 
            
    if DEBUG:
        print 'DEBUG: initEvents(), pick random'
        for i in range (0,1):
            e = random.choice (events)
            print '* Event %s ' % (e.PID)
            for k in [ a for a in dir(e) if not a.startswith('__')]:
                print '\t %s = %s' % (k, getattr(e, k))


    return events


    
