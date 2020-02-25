'''
Run this code to get result.
INPUT : 3d cooordinates
OUTPUT : Flight mission in mission.txt
'''
import pandas as pd
import numpy as np
from itertools import accumulate
from matplotlib import pyplot as plt
import classification as clsf


def processing(ds):

    print("Choose categorization axis")
    cat = input('Axis :')

    if cat.lower() in ['lat','latitude']:
        coor_list = clsf.latitude(ds)
        indi = 0
        print('Sorting through latitude...')

    if cat.lower() in ['lon','long','longitude']:
        coor_list = clsf.longitude(ds)
        indi = 1
        print('Sorting through longitude...')

    if cat.lower() in ['alt','altitude']:
        coor_list = clsf.altitude(ds)
        print('Sorting through altitude...')
    '''
    Transform data into half completed matrix
    '''
    length_to_split = clsf.separate(coor_list,ds)

    dz = [ds[x - y: x] for x, y in zip(
             accumulate(length_to_split), length_to_split)]

    '''
    Add zeros to create mxn matrix
    '''
    dz.sort(key=lambda x: x[indi])
    length = max(map(len, dz))
    y=[xi+[0]*(length-len(xi)) for xi in dz]
    row = len(y)
    col = max(len(x) for x in y)

    return row,col,y

'''
zig zag Algorithm
'''
def zigzag(row,col,a):
    evenRow = 0
    oddRow = 1
    index = []
    while evenRow < row:
        for i in range(col):
            x = (a[evenRow][i])
            index.append(x)
        evenRow = evenRow + 2

        if oddRow < row:
            for i in range(col - 1, -1, -1):
                x = (a[oddRow][i])
                index.append(x)
        oddRow = oddRow + 2
    return (index)

'''
Remove zeros from list and waypoint created
'''
def waypoint (wp):
    print('final list')
    nwp=np.array([x for x in wp if x != 0])
    print(nwp)

    return nwp

def visual():
    pass

'''
Write mission in QGC WPL 110
'''
def mission (gps_points,fileName):
    print('Get home location')
    lat = input("Enter Latitude: ")
    long = input("Enter Longitude: ")
    alt = input("Enter Alt:")
    print ('\nGet Mission Parameters')
    hgt = input("Enter Mission Height:")
    spraytime = input('Enter Spray Time:')
    flow = input('Enter flow rate (%): ')

    flow1 = 1100 + (int(flow)*8)

    # Function to write mission file with cooordinates

    def mission_writing():
        x = 3*i+1
        y = 3*i+2
        z = 3*i+3
        file.write ('\n'+str(x)+'\t0\t10\t16\t1\t0\t0\t0\t'+str(gps_points[i, 0])+'\t'+str(gps_points[i, 1])+'\t'+str(hgt)+'\t1\n'+str(y)+'\t0\t10\t184\t9\t'+str(int(flow1))+'\t1\t'+str((int(spraytime)*2))+'	0	0	0	1')
        file.write ('\n'+str(z)+'\t0\t10\t93\t'+str(spraytime)+'\t0\t0\t0\t0\t0\t0\t1')

    # Write
    file = open("dataset/%s/%s_mission.txt"%(fileName,fileName),"w")
    file.write ('QGC WPL 110\n0	1	0	16	0	0	0	0\t'+str(lat)+'\t'+str(long)+'\t'+str(alt)+'\t1')

    nrows = len(gps_points)

    for i in range(nrows):
        mission_writing()
    print('Mission written as dataset/%s/%s_mission.txt'%(fileName,fileName))
    file.close()

def main():
  fileName = input ("File name : ")
  dir = f"dataset/{fileName}/{fileName}_xy.csv"
  ds = pd.read_csv(dir).values.tolist()

  dsp = processing(ds)
  wp = zigzag(dsp[0],dsp[1],dsp[2])
  nwp = waypoint(wp)
  # Mission = mission(nwp,fileName)
  print("Done!")

if __name__ == '__main__':
    main()
