'''
Classification by latitude,longitude and altitude
2D - latitude, Longitude
3D - latitude, longitude, altitude
Sorting every class according to situation

'''
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

# IMPORT FILE FROM .csv
# fileName = input("File name : ")
# dir = f"dataset/{fileName}/{fileName}_xy.csv"
# ds = pd.read_csv(dir).values.tolist()
# print(ds)


def latitude(dataset):
    N = len(dataset)
    coor_list = []
    for i in range(N):
        x = (dataset[i][0])
        coor_list.append(x)
    return coor_list


def longitude(dataset):
    N = len(dataset)
    coor_list = []
    for i in range(N):
        y = (dataset[i][1])
        coor_list.append(y)
    return coor_list


def altitude(dataset):
    N = len(dataset)
    coor_list = []
    for i in range(N):
        z = (dataset[i][2])
        coor_list.append(z)
    return coor_list


def separate(coor_list,ds):
    low_coor = min(coor_list)
    high_coor = max(coor_list)

    dCoor = round(high_coor - low_coor, 5)

    NL = round((dCoor / 6), 5)

    # Classify by lat layer
    layerlist = []
    for j in range(6):
        layer = [k for k in coor_list if low_coor + (j * NL) <= k <= \
                 (low_coor + ((j + 1) * NL))]
        layerlist.append(layer)

    corrected_list = {}
    for a in range(len(layerlist)):
        item = []
        for b in range(len(ds)):
            if coor_list[b] in (layerlist[a]):
                item.append(ds[b])
        corrected_list[a] = item
    lengths = [len(corrected_list[x]) for x in corrected_list if isinstance(corrected_list[x], list)]
    return lengths
    # check list(should be separate into rows)


#
# print("Choose categorization axis")
# cat = input('Axis :')
#
# if cat.lower() in ['lat', 'latitude']:
#     print('Sorting through latitude...')
#     coor_list = latitude(ds)
#
# if cat.lower() in ['lon', 'long', 'longitude']:
#     print('Sorting through longitude...')
#     coor_list = longitude(ds)
#
# if cat.lower() in ['alt', 'altitude']:
#     print('Sorting through altitude...')
#     coor_list = altitude(ds)
#
# finallist = separate(coor_list)
# print(finallist)
