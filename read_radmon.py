#!/usr/bin/env python

import sys
import os.path
import numpy as np
from scipy.io import FortranFile
from datetime import datetime, timedelta

def read_radmon_ctl(file_path=None, file_name='time.mhs_metop-b.ctl'):

    if file_path:
        filename = os.path.join( file_path, file_name )
    else:
        filename = file_name
    if not os.path.isfile(filename):
        print ('no file:', filename)
        channo = None
        nchan = None
        nregion = None
        return channo, nregion

    print ('Opening ', filename)
    f = open(filename, 'r')
   
    f.readline()  # Three
    f.readline()  # header
    f.readline()  # lines

    line = f.readline()
  
    try:
       title,ins,sat,nchan = line.split()
    except ValueError:
       title,ins,sat,nchan, _ = line.split()

    nchan = int(nchan)
    channo = np.zeros(nchan,dtype=np.int8)

    f.readline()  # lines

    ichan=0
    while ichan < nchan:
       #Reading file
       line = f.readline()
       x2=line[20:25]
       channo[ichan]=(int(x2))
       ichan += 1

    while line[0]=='*':
       line = f.readline()

    nregion = int(line[7:9])
 
    f.close()
    return channo, nchan, nregion
  
def read_radmon_ieee(file_name, nchan, nregion, file_path=None):

    if file_path:
        filename = os.path.join( file_path, file_name )
    else:
        filename = file_name
    if not os.path.isfile(filename):
        print ('no file:', filename)
        channo = None
        nchan = None
        nregion = None
        return channo, nregion

    print ('Opening ', filename)
   
    f=FortranFile(filename,'r','>u4')

    count=f.read_reals(dtype=np.dtype('>f4')).reshape(nchan,nregion)
    penalty=f.read_reals(dtype=np.dtype('>f4')).reshape(nchan,nregion)
    omgnbc_sum=f.read_reals(dtype=np.dtype('>f4')).reshape(nchan,nregion)
    totcorg_sum=f.read_reals(dtype=np.dtype('>f4')).reshape(nchan,nregion)
    omgbc_sum=f.read_reals(dtype=np.dtype('>f4')).reshape(nchan,nregion)
    omgnbc_sum2=f.read_reals(dtype=np.dtype('>f4')).reshape(nchan,nregion)
    omgbc_sum2=f.read_reals(dtype=np.dtype('>f4')).reshape(nchan,nregion)

    f.close()

    return count, penalty, omgnbc_sum, omgnbc_sum, totcorg_sum, \
       omgbc_sum, omgnbc_sum2, omgbc_sum2

instr='mhs_metop-b'
sdate=datetime(2015,8,1,6)
edate=datetime(2015,8,1,6)
index=pd.date_range(sdate, edate, freq='6H')

date_string=d.strftime("%Y%m%d%H")

print('Running read_radmon')
channo, nchan, nregion = read_radmon_ctl(file_name='time.'+instr+'.ctl')
print(channo, nregion)
count, penalty, omgnbc_sum, omgnbc_sum, totcorg_sum, \
       omgbc_sum, omgnbc_sum2, omgbc_sum2 = \
       read_radmon_ieee('time.'+instr+'.'+datei_string+'.ieee_d',\
          nchan, nregion, file_path=None)
