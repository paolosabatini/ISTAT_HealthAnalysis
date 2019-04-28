#!/usr/bin/env python

class Event:
    def __init__ (self, keys, values):
        n_keys = len (keys.split ('\t'))
        for i in range (0,n_keys):
            self.__dict__[keys.split('\t')[i].replace ('\n','')] = values.split('\t')[i].replace ('\n','')


    def fulfil (self, selection):

        selection = selection.replace(' AND ', ' and ')
        selection = selection.replace(' OR ', ' or ')
        if selection == 'ALL': return True
        elif (eval (selection)): return True
        else: return False
