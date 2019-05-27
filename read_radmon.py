#!/usr/bin/env python

import sys
import os.path
import numpy as np
from scipy.io import FortranFile
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt

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
        return channo, nchan, nregion

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
    line = f.readline()

    nregion = int(line[5:7])
    print(nchan,nregion) 
    f.close()
    return channo, nchan, nregion
  
def read_radmon_ieee(file_name, nchan, nregion, file_path=None):

    if file_path:
        filename = os.path.join( file_path, file_name )
    else:
        filename = file_name
    if not os.path.isfile(filename):
        print ('no file:', filename)
        count = None
        penalty = None
	omgnbc_sum = None
        omgnbc_sum = None
        totcorg_sum = None
        omgbc_sum = None
        omgnbc_sum2 = None
        omgbc_sum2 = None
        totcorg_sum2 = None
        return count, penalty, omgnbc_sum, omgnbc_sum, totcorg_sum, \
             omgbc_sum, omgnbc_sum2, omgbc_sum2

    print ('Opening ', filename)
   
    f=FortranFile(filename,'r','>u4')

    count=f.read_reals(dtype=np.dtype('>f4')).reshape(nchan,nregion)
    penalty=f.read_reals(dtype=np.dtype('>f4')).reshape(nchan,nregion)
    omgnbc_sum=f.read_reals(dtype=np.dtype('>f4')).reshape(nchan,nregion)
    totcorg_sum=f.read_reals(dtype=np.dtype('>f4')).reshape(nchan,nregion)
    omgbc_sum=f.read_reals(dtype=np.dtype('>f4')).reshape(nchan,nregion)
    omgnbc_sum2=f.read_reals(dtype=np.dtype('>f4')).reshape(nchan,nregion)
    totcorg_sum2=f.read_reals(dtype=np.dtype('>f4')).reshape(nchan,nregion)
    omgbc_sum2=f.read_reals(dtype=np.dtype('>f4')).reshape(nchan,nregion)

    f.close()

    return count, penalty, omgnbc_sum, totcorg_sum, \
       omgbc_sum, omgnbc_sum2, totcorg_sum2, omgbc_sum2

path_0='/scratch4/NCEPDEV/da/noscrub/Andrew.Collard/radmon/stats/Ctl'

instr='hirs4_metop-a'
sdate=datetime(2015,5,14,18)
edate=datetime(2015,5,21,00)
index=pd.date_range(sdate, edate, freq='6H')

# Get instrument info from "ctl" file
date_string=sdate.strftime("%Y%m%d")
channo, nchan, nregion = read_radmon_ctl(file_name='time.'+instr+'.ctl', \
    file_path=path_0+'/radmon.'+date_string)

# Initialise Pandas dataframes
count = pd.DataFrame(index=index, columns=channo)
omgnbc_sum = pd.DataFrame(index=index, columns=channo)
omgbc_sum = pd.DataFrame(index=index, columns=channo)
omgnbc_sum2 = pd.DataFrame(index=index, columns=channo)
omgbc_sum2 = pd.DataFrame(index=index, columns=channo)
totcorg_sum = pd.DataFrame(index=index, columns=channo)
totcorg_sum2 = pd.DataFrame(index=index, columns=channo)

hour_string=sdate.strftime("%H")

for ix, row in count.iterrows():
   date_string=ix.strftime("%Y%m%d")
   hour_string=ix.strftime("%H")
   print(ix)
   path=path_0+'/radmon.'+date_string
   count_tmp, penalty_tmp, omgnbc_sum_tmp, totcorg_sum_tmp, \
       omgbc_sum_tmp, omgnbc_sum2_tmp, totcorg_sum2_tmp, omgbc_sum2_tmp = \
       read_radmon_ieee('time.'+instr+'.'+date_string+hour_string+'.ieee_d',\
       nchan, nregion, file_path=path)
   count.loc[ix]=count_tmp[:,0]
   omgnbc_sum.loc[ix]=omgnbc_sum_tmp[:,0]
   omgbc_sum.loc[ix]=omgbc_sum_tmp[:,0]
   omgnbc_sum2.loc[ix]=omgnbc_sum2_tmp[:,0]
   omgbc_sum2.loc[ix]=omgbc_sum2_tmp[:,0]
   totcorg_sum.loc[ix]=totcorg_sum_tmp[:,0]
   totcorg_sum2.loc[ix]=totcorg_sum2_tmp[:,0]

count.reset_index().plot(x='index')
plt.show()







