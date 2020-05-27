import pandas

import const
import config

def readData():
    data = pandas.read_csv(config.FILE_PATH, names=const.DATA_FIELDS, encoding='latin-1')
    return data