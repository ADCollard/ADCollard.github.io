dset ^ahi_himawari8.%y4%m2%d2%h2.ieee_d
options template big_endian sequential
undef -999.
title ahi        himawari8    10
*XDEF is scan position
*YDEF is channel number
*  y=    1, channel=    7 , iuse= -1 , error=    2.200 , wlth=      3.88 , freq=  77219.56
*  y=    2, channel=    8 , iuse=  1 , error=    3.000 , wlth=      6.21 , freq=  48243.84
*  y=    3, channel=    9 , iuse=  1 , error=    2.500 , wlth=      6.93 , freq=  43232.45
*  y=    4, channel=   10 , iuse=  1 , error=    2.200 , wlth=      7.35 , freq=  40813.35
*  y=    5, channel=   11 , iuse= -1 , error=    2.200 , wlth=      8.59 , freq=  34909.13
*  y=    6, channel=   12 , iuse= -1 , error=    2.200 , wlth=      9.63 , freq=  31121.71
*  y=    7, channel=   13 , iuse= -1 , error=    2.200 , wlth=     10.40 , freq=  28820.03
*  y=    8, channel=   14 , iuse= -1 , error=    2.200 , wlth=     11.23 , freq=  26703.74
*  y=    9, channel=   15 , iuse= -1 , error=    2.200 , wlth=     12.36 , freq=  24260.46
*  y=   10, channel=   16 , iuse= -1 , error=    2.200 , wlth=     13.27 , freq=  22585.44
*ZDEF is geographic region
*  region= 1 global (180W-180E, 90S-90N)
*  region= 2 land (180W-180E, 90S-90N)
*  region= 3 water (180W-180E, 90S-90N)
*  region= 4 ice/snow (180W-180E, 90S-90N)
*  region= 5 mixed (180W-180E, 90S-90N)
xdef  90 linear   0.0   1.0
ydef   10 linear 1.0 1.0
zdef  5 linear 1.0 1.0
tdef 121 linear 18Z20aug2020 06hr
vars      35
satang      1 0     satang
count       5 0      count
penalty     5 0    penalty
omgnbc      5 0     omgnbc
total       5 0      total
omgbc       5 0      omgbc
fixang      5 0     fixang
lapse       5 0      lapse
lapse2      5 0     lapse2
const       5 0      const
scangl      5 0     scangl
clw         5 0        clw
cos         5 0        cos
sin         5 0        sin
emiss       5 0      emiss
ordang4     5 0    ordang4
ordang3     5 0    ordang3
ordang2     5 0    ordang2
ordang1     5 0    ordang1
omgnbc_2    5 0   omgnbc_2
total_2     5 0    total_2
omgbc_2     5 0    omgbc_2
fixang_2    5 0   fixang_2
lapse_2     5 0    lapse_2
lapse2_2    5 0   lapse2_2
const_2     5 0    const_2
scangl_2    5 0   scangl_2
clw_2       5 0      clw_2
cos_2       5 0      cos_2
sin_2       5 0      sin_2
emiss_2     5 0    emiss_2
ordang4_2   5 0  ordang4_2
ordang3_2   5 0  ordang3_2
ordang2_2   5 0  ordang2_2
ordang1_2   5 0  ordang1_2
endvars
