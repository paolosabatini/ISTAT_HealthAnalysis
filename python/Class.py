import os
from Converter import *

class Interview:
    def __init__(self, dic):
        self.id = dic['PID']
        self.geo = geoConverter(dic['RIP'])
        self.smokeflag = smokeConverter(dic['SK1'])
