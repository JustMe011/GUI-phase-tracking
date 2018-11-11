# import pathlib
from configparser import ConfigParser as cParser
# from cfg.generalCfg import CONFIG_PATH
# import pathlib

confParserObj = cParser()


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

'''
class lastEntryParser (CParser):
    def __init__(self):
        # ToDo
        self._sections = ['PATH_NAME', 'DELIMITER', 'CHUNCK',
                            'MIXER', 'DOWN', 'EQUATIONS', 'RANDWALK_VALS',
                            'SAMPLING_TIMES', 'N_SAMPLING']
        pass

    def createLastEntry (self):
        for section in self._sections:
            self.add_section(section)

    def writeLastInsert (self,**writeToFile):
        
        if not CONFIG_PATH.exist():
            CONFIG_PATH.mkdir()

        if not (CONFIG_PATH / LAST_ENTRY_NAME).exist():
            createLastEntry(confParserObj)
        updateLastEntry(confParserObj, delimiter,chunck, mixer,down,func_read,times_read,samples,rands)

     def updateLastEntry(self):
        # ToDO
        # update last entries...
        pass
'''
