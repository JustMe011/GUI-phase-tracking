import pathlib
try:
    import configparser as cp
except ModuleNotFoundError:
    import ConfigParser as cp
try:
    import tkinter as tk
except:
    import Tkinter as tk
import cfg.generalCfg as gCfg
import cfg.tkCfg as tkCfg
import io

'''
accepted fields:
[] delimiter ""
[] chunck ""
[] mixer ""
[] down ""
[] funcRead ["","",""]
[] timesRead  ""
[] samples ""
[] rands ["","",""]
'''


class LastEntryParser (cp.ConfigParser):

    # ***** INTERFACE *****


    def __init__(self, configPath = None, lastEntryConfigFile = None):
        cp.ConfigParser.__init__(self)

        self.tkDT = [tk.StringVar, tk.IntVar, tk.BooleanVar]
        self.configPath = gCfg.CONFIG_PATH if not configPath else configPath
        self.lastEntryFile = gCfg.LAST_ENTRY_NAME if not lastEntryConfigFile else lastEntryConfigFile

        self.readLastEntry()


    def writeLastInsert (self, **propToWrite):
        self._updateDefVars()

        if not self.configPath.exists():
            self.configPath.mkdir()

        if not (self.configPath / self.lastEntryFile).exists():
            # It shouldn't be necessary
            self._createLastEntry()
        self._updateLastEntry()


    def readLastEntry(self):
        self._updateDefVars()
        try:
            if not self.read(self.configPath / self.lastEntryFile):
                raise ValueError
            for elName, elVal in list(self._lastEntryVal.items()):
                try:
                    readVal = self.get(elVal[0], elName)
                except cp.NoSectionError:
                    print('Cannot find a section\nIgnoring...')
                except cp.NoOptionError:
                    print('Cannot find the property\nIgnoring...')
                else:
                    elVal[1].set(readVal)
            print('file {} readed'.format(self.lastEntryFile))
        except (io.UnsupportedOperation, ValueError):
            print("Can't read {} file".format(self.lastEntryFile))
            # No file
            self._createLastEntry()

     # ***** PRIVATE METHODS *****
    def _updateDefVars(self):
        # syntax {OBJ_NAME: [SECTION, VARIABLE]}
        self._lastEntryVal = {'pathName': ['FILE_ENTRY', tkCfg.opFileName],
                              'delimiter': ['FILE_ENTRY', tkCfg.contDelim],
                              'chunk': ['FILE_ENTRY', tkCfg.contChunk],
                              'mixer': ['FILE_ENTRY', tkCfg.loMix],
                              'funcRead': ['EQ_ENTRY', tkCfg.equations],
                              'timesRead': ['EQ_ENTRY', tkCfg.funcSamplTime],
                              'samples': ['EQ_ENTRY', tkCfg.samples],
                              'rands': ['EQ_ENTRY', tkCfg.rands]
                              }

        #{'FILE_ENTRY': ['pathName', 'delimiter', 'chunk', 'mixer'], 'EQUATION_ENTER': ['funcRead', 'timesRead', 'samples', 'rands']}
    def _createLastEntry (self):
        for elName, elVal in list(self._lastEntryVal.items()):
            self.add_section(elVal[0])
        return



     def _updateLastEntry(self):
        # update last entries...
        # for propName, propVal in self._valuesToChange.items():
        #     section = self._findSectionToChange(propName)
        #     self.set(section, propName, str(propVal.get()))

        for elName, elVal in self._lastEntryVal.items():
            tmpVal = elVal[1].get() if type(elVal[1]) in self.tkDT else elVal[1]
            self.set(elVal[0], elName, tmpVal)
            
        with open(self.configPath / self.lastEntryFile, 'w') as writeFile:
            self.write(writeFile)