import pathlib
from configparser import ConfigParser as CParser
from cfg import CONFIG_PATH

confParserObj = cParser()

class lastEntryParser (CParser):
    def __init__(self):
        # ToDo
        pass
    def writeLa
    stInsert (self,**writeToFile):
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
        if not CONFIG_PATH.exist():
            CONFIG_PATH.mkdir()

        if not (CONFIG_PATH / LAST_ENTRY_NAME).exist():
            createLastEntry(confParserObj)
        updateLastEntry(confParserObj, delimiter,chunck, mixer,down,func_read,times_read,samples,rands)

    def createLastEntry(self, confParserObj):
        confParserObj.add_section('PATH_NAME')
        confParserObj.add_section('DELIMITER')
        confParserObj.add_section('CHUNCK')
        confParserObj.add_section('MIXER')
        confParserObj.add_section('DOWN')
        confParserObj.add_section('EQUATIONS')
        confParserObj.add_section('RANDWALK_VALS')
        confParserObj.add_section('SAMPLING_TIMES')
        confParserObj.add_section('N_SAMPLING')

     
