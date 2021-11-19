dset ^seviri_m11.%y4%m2%d2%h2.ieee_d
options template big_endian sequential
undef -999.
title seviri     m11           8
*XDEF is scan position
*YDEF is channel number
*  y=    1, channel=    4 , iuse= -1 , error=    0.750 , wlth=      3.89 , freq=  77136.90
*  y=    2, channel=    5 , iuse=  1 , error=    2.500 , wlth=      6.27 , freq=  47807.18
*  y=    3, channel=    6 , iuse=  1 , error=    2.250 , wlth=      7.35 , freq=  40806.62
*  y=    4, channel=    7 , iuse= -1 , error=    1.250 , wlth=      8.72 , freq=  34390.54
*  y=    5, channel=    8 , iuse= -1 , error=    1.250 , wlth=      9.66 , freq=  31020.89
*  y=    6, channel=    9 , iuse= -1 , error=    0.750 , wlth=     10.75 , freq=  27879.96
*  y=    7, channel=   10 , iuse= -1 , error=    0.800 , wlth=     11.93 , freq=  25133.08
*  y=    8, channel=   11 , iuse= -1 , error=    1.250 , wlth=     13.38 , freq=  22409.77
*ZDEF is geographic region
*  region= 1 global (180W-180E, 90S-90N)
*  region= 2 land (180W-180E, 90S-90N)
*  region= 3 water (180W-180E, 90S-90N)
*  region= 4 ice/snow (180W-180E, 90S-90N)
*  region= 5 mixed (180W-180E, 90S-90N)
xdef  90 linear   0.0   1.0
ydef    8 linear 1.0 1.0
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
