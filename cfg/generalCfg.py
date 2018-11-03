try:
    import queue
except:
    import Queue as queue
import pathlib

sharedQueue = queue.Queue()
ROOT_PATH = pathlib.Path.cwd()
IMG_PATH = ROOT_PATH / 'img'

