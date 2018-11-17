try:
    import queue
except ModuleNotFoundError:
    import Queue as queue
import pathlib

sharedQueue = queue.Queue()
ROOT_PATH = pathlib.Path.cwd()
IMG_PATH = ROOT_PATH / 'img'
CONFIG_PATH = ROOT_PATH / 'configFiles'
LAST_ENTRY_NAME = 'lastEntry.ini'

loadedData = None

