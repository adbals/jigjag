'''
Read file from csv in list
'''
import pandas as pd

# Define read file
def read(fileName):
    dirName = "datasetTSP/%s/%s_xy.csv" % (fileName, fileName)
    df = pd.read_csv(dirName, sep=",", usecols =["no","x","y","z"]).values.tolist()
    clist = []
    for item in df:
        clist.append(item)

    return clist
