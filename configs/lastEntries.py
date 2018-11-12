import pathlib
try:
    from configparser import ConfigParser as CParser
except ModuleNotFoundError:
    from ConfigParser import ConfigParser as CParser

import cfg.generalCfg as gCfg
import cfg.tkCfg as tkCfg


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


class LastEntryParser (CParser):
    def __init__(self, configPath = None, lastEntryConfigFile = None):
        # ToDo
        self._properties = {'FILE_ENTRY': ['pathName', 'delimiter', 'chunk', 'mixer'],
                      'EQUATION_ENTER': ['funcRead', 'timesRead', 'samples', 'rands']}

        self._valuesToChange = {'delimiter': tkCfg.contDelim, 'chunk': tkCfg.contChunck,
                          'mixer': tkCfg.loMix, 'down': tkCfg.downSampling,
                        'funcRead': tkCfg.equations, 'timesRead': tkCfg.funcSamplTime,
                        'samples': tkCfg.pointNum, 'rands': tkCfg.rands}

        self.configPath = configPath if configPath else gCfg.CONFIG_PATH
        self.lastEntryFile = lastEntryConfigFile if lastEntryConfigFile else gCfg.LAST_ENTRY_NAME


    def createLastEntry (self):
        for section in list(self._properties.items()):
            self.add_section(section)

    def writeLastInsert (self, **propToWrite):
        
        if not self.configPath.exist():
            self.configPath.mkdir()

        if not (self.configPath / self.lastEntryFile).exist():
            self.createLastEntry()
        self.updateLastEntry(self._valuesToChange)

     def updateLastEntry(self, **propToUpdate):
        # ToDO
        # update last entries...
        toChange = propToUpdate
        for propName, propVal in toChange.items():
            section = self._findSectionToChange(propName)
            self.set(section, propName, str(propVal))
        with open(str(self.configPath / self.lastEntryFile), 'w') as lastFile:
            self.write(lastFile)

    def _findSectionToChange (self, propName):
        listOfItems = self._properties.items()
        foundSection = None
        for item in listOfItems:
            if propName in item[1]:
                foundSection = item[0]
        return foundSection

    def readLastEntry(self):
        self.read(self.lastEntryFile)

        for section, prop in self._properties:
            readVal = self.get(section, prop)
            self._valuesToChange[prop].set(readVal)


