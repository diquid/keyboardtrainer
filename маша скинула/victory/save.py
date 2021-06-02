import shelve
from typewindow import *
from recordtable import *
from textread import *
from aftertype import *

class Save(object):
    def __init__(self):
        self.file = shelve.open('data')
        self.info = {
            'errors' : 1,
            'typespeed': 15,
            'totaltime': 40}

    def save(self):
        self.file['info'] = self.info

    def get(self):
        print (self.file['Info'])

    def __del__(self):
        self.file.close()
        





