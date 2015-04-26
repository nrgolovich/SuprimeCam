These are the commands used to create the sky flats for the g, r, i broadband images. For the N-B-L816 band images we only observed one cluster and with just 4 exposures so we used dome flats for this band.

The following are the list of files that should be used for creating skyflats. Note that I start off by listing all possible files for each band (not including the short 3 and 30 s exposures, since James recommends against using these), then I consider whether there are too many bright stars in each field. 


|Cluster	| Use for skyflat? |
|----------	|------------------|
|A3365		| yes |
|1RXS J0603	| No. There is a very bright star (V=8.62 1RXS J0603.3) in the center of the field, plus there is a very high stellar density. Plus we have enough alternative exposures. |
|A3411		| yes |
|A1240		| yes |
|RXCJ 1314	| yes |
|A1612		| yes |
|A523		| yes |
|A746		| No. There is a very bright star (V=4.5 Abell 746) in the field. Plus we have enough alternative exposures. |
|RXC J1053	| yes |
|A1300		| yes |
|PLCK G287	| yes |
|ZwCL 1447	| yes | 
|A2034		| yes |
|A2061		| Yes |
|MACS J1752	| Yes. There are some bright (V~10) stars in the field but not too bad. |

Setup the flat folder architecture. 

```
cd /sandbox/Subaru/flats
mkdir 2014feb
cd 2014feb
mkdir g r i N-B-L816
```

# g-band
The ~~strike through~~ lines are not used in the flat fields for the reasons commented in the table above.
## Exposures
### Night 1
- 20:33:05  object031  SUPE01438680        Abell3365    W-S-G+   180.0  194.43   47.00  1.370  6.920  116.75    786
- 20:36:51  object032  SUPE01438690        Abell3365    W-S-G+   180.0  195.62   46.77  1.376  6.920  116.48    789
- 20:40:36  object033  SUPE01438700        Abell3365    W-S-G+   180.0  196.92   46.52  1.382  6.920   97.52    798
- 20:44:21  object034  SUPE01438710        Abell3365    W-S-G+   180.0  198.08   46.23  1.389  6.920  100.96    806
- ~~23:12:28  object060  SUPE01438970  1RXSJ0603.2+4212    W-S-G+   180.0  310.48   44.88  1.429  7.030  102.69   1100~~
- ~~23:16:12  object061  SUPE01438980  1RXSJ0603.2+4212    W-S-G+   180.0  310.24   44.24  1.446  7.030   98.58   1117~~
- ~~23:19:57  object062  SUPE01438990  1RXSJ0603.2+4212    W-S-G+   180.0  310.00   43.51  1.466  7.030  108.97   1146~~
- ~~23:23:42  object063  SUPE01439000  1RXSJ0603.2+4212    W-S-G+   180.0  309.75   42.86  1.484  7.030  100.60   1123~~
- 01:40:48  object091  SUPE01439280        Abell3411    W-S-G+   180.0  232.28   32.63  1.879  7.050   95.98   1118
- 01:44:34  object092  SUPE01439290        Abell3411    W-S-G+   180.0  232.92   31.94  1.916  7.050   95.68   1125
- 01:48:18  object093  SUPE01439300        Abell3411    W-S-G+   180.0  233.61   31.20  1.958  7.050   98.72   1126
- 01:52:02  object094  SUPE01439310        Abell3411    W-S-G+   180.0  234.18   30.49  1.999  7.050  110.72   1168
- 02:14:18  object097  SUPE01439340        Abell1240    W-S-G+   180.0  338.73   64.62  1.109  7.050  110.87    930
- 02:17:59  object098  SUPE01439350        Abell1240    W-S-G+   180.0  337.42   64.31  1.112  7.050  112.78    940
- 02:21:42  object099  SUPE01439360        Abell1240    W-S-G+   180.0  335.96   63.94  1.116  7.050   94.75    938
- 02:25:24  object100  SUPE01439370        Abell1240    W-S-G+   180.0  334.70   63.61  1.119  7.050   97.34    940
- 05:26:01  object129  SUPE01439660  RXCJ1314.4-2515    W-S-G+   180.0  216.42   34.81  1.767  7.050  108.32   1839
- 05:29:45  object130  SUPE01439670  RXCJ1314.4-2515    W-S-G+   180.0  217.19   34.30  1.791  7.050  121.01   1904
- 05:33:29  object131  SUPE01439680  RXCJ1314.4-2515    W-S-G+   180.0  218.04   33.73  1.818  7.050  106.93   2022
- 05:37:12  object132  SUPE01439690  RXCJ1314.4-2515    W-S-G+   180.0  218.77   33.18  1.845  7.050   99.45   2294
- 05:43:30  object135  SUPE01439720        Abell1612    W-S-G+   180.0  247.06   41.47  1.528  7.050  108.51   3517
- 05:47:13  object136  SUPE01439730        Abell1612    W-S-G+   180.0  247.65   40.68  1.553  7.050  113.83   5948
- ~~05:50:57  object137  SUPE01439740        Abell1612    W-S-G+   180.0  248.29   39.82  1.581  7.050  101.76  11506~~
- ~~05:54:42  object138  SUPE01439750        Abell1612    W-S-G+   180.0  248.82   39.00  1.609  7.050  114.61  23877~~
### Night 2
- 19:25:50  object004  SUPE01440090         Abell523    W-S-G+   180.0  212.52   77.04  1.028  7.000  104.22   1636
- 19:29:35  object005  SUPE01440100         Abell523    W-S-G+   180.0  215.88   76.56  1.030  7.000   99.57   1303
- 19:33:20  object006  SUPE01440110         Abell523    W-S-G+   180.0  219.05   76.02  1.033  7.000  112.57   1150
- 19:37:05  object007  SUPE01440120         Abell523    W-S-G+   180.0  222.18   75.40  1.036  7.000   96.84   1100
- ~~23:25:05  object045  SUPE01440500         Abell746    W-S-G+   180.0  354.95   58.16  1.177  7.050  102.40    940~~
- ~~23:28:50  object046  SUPE01440510         Abell746    W-S-G+   180.0  353.90   58.08  1.179  7.050   98.89    953~~
- ~~23:32:35  object047  SUPE01440520         Abell746    W-S-G+   180.0  352.81   57.99  1.180  7.050   97.01    989~~
- ~~23:36:21  object048  SUPE01440530         Abell746    W-S-G+   180.0  351.62   57.85  1.182  7.050  110.71   1812~~
- 23:43:10  object051  SUPE01440560  RXCJ1053.7+5452    W-S-G+   180.0   16.36   52.68  1.254  7.050   97.79    822
- 23:46:53  object052  SUPE01440570  RXCJ1053.7+5452    W-S-G+   180.0   15.61   52.90  1.250  7.050  112.44    834
- 23:50:37  object053  SUPE01440580  RXCJ1053.7+5452    W-S-G+   180.0   14.80   53.14  1.246  7.050  114.94    845
- 23:54:22  object054  SUPE01440590  RXCJ1053.7+5452    W-S-G+   180.0   13.89   53.38  1.243  7.050  111.48    823
- 00:16:16  object058  SUPE01440630        Abell1300    W-S-G+   180.0  154.60   46.28  1.376  7.030  120.00    916
- 00:19:56  object059  SUPE01440640        Abell1300    W-S-G+   180.0  155.70   46.64  1.368  7.030  120.00    920
- 00:23:36  object060  SUPE01440650        Abell1300    W-S-G+   180.0  156.86   46.98  1.361  7.030  120.00    919
- 00:27:17  object061  SUPE01440660        Abell1300    W-S-G+   180.0  158.11   47.33  1.353  7.030  120.00    923
- 00:34:00  object064  SUPE01440690  PLCKG287.0+32.9    W-S-G+   180.0  158.78   38.70  1.588  7.030  120.00    949
- 00:37:41  object065  SUPE01440700  PLCKG287.0+32.9    W-S-G+   180.0  159.71   39.00  1.579  7.030  120.00    946
- 00:41:20  object066  SUPE01440710  PLCKG287.0+32.9    W-S-G+   180.0  160.68   39.28  1.569  7.030  120.00    953
- 00:44:59  object067  SUPE01440720  PLCKG287.0+32.9    W-S-G+   180.0  161.73   39.58  1.560  7.030  120.00    960
- 04:26:53  object104  SUPE01441090  ZwCl1447.2+2619    W-S-G+   180.0   35.08   82.30  1.008  7.000  102.78    932
- 04:30:38  object105  SUPE01441100  ZwCl1447.2+2619    W-S-G+   180.0   29.86   82.75  1.007  7.000  104.56    914
- 04:34:23  object106  SUPE01441110  ZwCl1447.2+2619    W-S-G+   180.0   23.84   83.16  1.007  7.000  108.51    915
- 04:38:07  object107  SUPE01441120  ZwCl1447.2+2619    W-S-G+   180.0   16.65   83.49  1.006  7.000   99.10    939

## Run SDFRED flat pipeline
### Link to the raw data
There are 36 separate exposures for the skyflat which should be sufficient (after excluding the grayed out exposures).

```
cd g
ln -s ../../../rawdata/2014feb24/SUPA014386[8-9]?.fits .
ln -s ../../../rawdata/2014feb24/SUPA014387[0-1]?.fits .
ln -s ../../../rawdata/2014feb24/SUPA014392[8-9]?.fits .
ln -s ../../../rawdata/2014feb24/SUPA014393[0-1]?.fits .
ln -s ../../../rawdata/2014feb24/SUPA014393[4-7]?.fits .
ln -s ../../../rawdata/2014feb24/SUPA014396[6-9]?.fits .
ln -s ../../../rawdata/2014feb24/SUPA014397[2-3]?.fits .
ln -s ../../../rawdata/2014feb25/SUPA0144009?.fits .
ln -s ../../../rawdata/2014feb25/SUPA014401[0-2]?.fits .
ln -s ../../../rawdata/2014feb25/SUPA014405[6-9]?.fits .
ln -s ../../../rawdata/2014feb25/SUPA014406[3-6]?.fits .
ln -s ../../../rawdata/2014feb25/SUPA0144069?.fits .
ln -s ../../../rawdata/2014feb25/SUPA014407[0-2]?.fits .
ln -s ../../../rawdata/2014feb25/SUPA0144090?.fits .
ln -s ../../../rawdata/2014feb25/SUPA014411[0-2]?.fits .
```
### rename the data files in each band folder
```
ls -1 SUPA*.fits > namechange.lis
namechange.csh namechange.lis
```
### perform subtraction of overscan and bias in each band folder
```
ls -1 H*.fits > ovserscansub.lis
overscansub.csh ovserscansub.lis
```
### Skyflat option (for g, r, i):
```
ls -1 To_RH*.fits > mkflat.lis
mask_mkflat_HA.csh mkflat.lis skyflat_g 0.4 1.3
```
### Check that the flats look reasonable
e.g. with:

```
ds9 -mosaic wcs skyflat*.fits
```
### Clean up working files to save disk space
```
rm To_*
rm tmp*
rm ssbtmp*
rm mnah*
rm blank*
```

# r-band
## Exposures
### Night 1
- 21:01:44  object038  SUPE01438750        Abell3365    W-S-R+   360.0  203.47   44.80  1.433  6.950   99.42   8742
- 21:08:26  object039  SUPE01438760        Abell3365    W-S-R+   360.0  205.42   44.16  1.450  6.950   97.30   8919
- 21:15:11  object040  SUPE01438770        Abell3365    W-S-R+   360.0  207.35   43.44  1.471  6.950  106.90   9105
- 21:21:47  object041  SUPE01438780        Abell3365    W-S-R+   360.0  209.26   42.68  1.494  6.950  106.27   9341
- 21:28:32  object042  SUPE01438790        Abell3365    W-S-R+   360.0  211.09   41.89  1.518  6.950   94.95   9472
- 21:35:16  object043  SUPE01438800        Abell3365    W-S-R+   360.0  212.80   41.04  1.546  6.950  102.70   9650
- 21:42:00  object044  SUPE01438810        Abell3365    W-S-R+   360.0  214.51   40.15  1.575  6.950  124.42   9930
- 21:48:45  object045  SUPE01438820        Abell3365    W-S-R+   360.0  216.21   39.27  1.607  6.950  103.39  10212
- ~~22:01:27  object048  SUPE01438850  1RXSJ0603.2+4212    W-S-R+   360.0  319.04   56.91  1.206  6.950  104.85   7383~~
- ~~22:08:07  object049  SUPE01438860  1RXSJ0603.2+4212    W-S-R+   360.0  317.87   55.89  1.221  6.950  100.80   7438~~
- ~~22:14:47  object050  SUPE01438870  1RXSJ0603.2+4212    W-S-R+   360.0  316.75   54.83  1.238  6.950   96.84   7479~~
- ~~22:21:30  object051  SUPE01438880  1RXSJ0603.2+4212    W-S-R+   360.0  315.69   53.68  1.257  6.950  111.66   7474~~
- ~~22:28:12  object052  SUPE01438890  1RXSJ0603.2+4212    W-S-R+   360.0  314.78   52.56  1.276  6.950   97.02   7467~~
- ~~22:34:56  object053  SUPE01438900  1RXSJ0603.2+4212    W-S-R+   360.0  313.90   51.47  1.296  6.950  101.64   7254~~
- ~~22:41:41  object054  SUPE01438910  1RXSJ0603.2+4212    W-S-R+   360.0  313.12   50.30  1.319  6.950  103.64   7170~~
- ~~22:48:26  object055  SUPE01438920  1RXSJ0603.2+4212    W-S-R+   360.0  312.50   49.12  1.343  6.950  105.94   7231~~
- 00:31:33  object080  SUPE01439170        Abell3411    W-S-R+   360.0  217.08   44.18  1.456  7.000  103.56   7116
- 00:38:19  object081  SUPE01439180        Abell3411    W-S-R+   360.0  218.83   43.22  1.484  7.000  101.44   7200
- 00:45:03  object082  SUPE01439190        Abell3411    W-S-R+   360.0  220.52   42.20  1.514  7.000  104.13   7223
- 00:51:48  object083  SUPE01439200        Abell3411    W-S-R+   360.0  222.22   41.11  1.549  7.000  101.42   7404
- 00:58:33  object084  SUPE01439210        Abell3411    W-S-R+   360.0  223.80   40.03  1.585  7.000  113.05   7644
- 01:05:18  object085  SUPE01439220        Abell3411    W-S-R+   360.0  225.24   38.92  1.625  7.000   98.88   7688
- 01:11:59  object086  SUPE01439230        Abell3411    W-S-R+   360.0  226.69   37.78  1.669  7.000  101.29   7815
- 01:18:39  object087  SUPE01439240        Abell3411    W-S-R+   360.0  228.11   36.66  1.715  7.000   97.11   7894
- 02:40:56  object104  SUPE01439410        Abell1240    W-S-R+   360.0  329.75   61.88  1.141  7.000   92.96   5960
- 02:47:43  object105  SUPE01439420        Abell1240    W-S-R+   360.0  327.86   61.06  1.151  7.000  120.37   5946
- 02:54:21  object106  SUPE01439430        Abell1240    W-S-R+   360.0  326.08   60.22  1.161  7.000  113.59   5927
- 03:01:07  object107  SUPE01439440        Abell1240    W-S-R+   360.0  324.33   59.27  1.173  7.000   94.88   5918
- 03:07:53  object108  SUPE01439450        Abell1240    W-S-R+   360.0  322.81   58.31  1.186  7.000  105.92   6032
- 03:14:34  object109  SUPE01439460        Abell1240    W-S-R+   360.0  321.38   57.39  1.199  7.000  108.95   6021
- 03:21:17  object110  SUPE01439470        Abell1240    W-S-R+   360.0  320.06   56.38  1.214  7.000  103.94   6193
- 03:28:03  object111  SUPE01439480        Abell1240    W-S-R+   360.0  318.93   55.31  1.230  7.000  118.66   6434
- 03:47:40  object115  SUPE01439520  RXCJ1314.4-2515    W-S-R+   360.0  190.08   44.18  1.440  7.080  108.33   7621
- 03:54:25  object116  SUPE01439530  RXCJ1314.4-2515    W-S-R+   360.0  192.13   43.88  1.450  7.080  106.24   7630
- 04:01:08  object117  SUPE01439540  RXCJ1314.4-2515    W-S-R+   360.0  194.17   43.51  1.461  7.080  121.03   7654
- 04:07:49  object118  SUPE01439550  RXCJ1314.4-2515    W-S-R+   360.0  196.25   43.08  1.474  7.080  109.42   7721
- 04:14:32  object119  SUPE01439560  RXCJ1314.4-2515    W-S-R+   360.0  198.23   42.62  1.488  7.080  106.93   7829
- 04:21:15  object120  SUPE01439570  RXCJ1314.4-2515    W-S-R+   360.0  200.10   42.08  1.505  7.080  113.41   7937
- 04:28:00  object121  SUPE01439580  RXCJ1314.4-2515    W-S-R+   360.0  202.02   41.51  1.524  7.080   99.44   8050
- 04:34:38  object122  SUPE01439590  RXCJ1314.4-2515    W-S-R+   360.0  203.87   40.95  1.542  7.080   95.63   8145
### Night 2
- 19:52:55  object011  SUPE01440160         Abell523    W-S-R+   360.0  232.34   72.68  1.054  6.900   96.30   8001
- 19:59:36  object012  SUPE01440170         Abell523    W-S-R+   360.0  235.72   71.43  1.062  6.900   96.22   7989
- 20:06:21  object013  SUPE01440180         Abell523    W-S-R+   360.0  238.74   70.08  1.072  6.900  113.02   8032
- 20:13:05  object014  SUPE01440190         Abell523    W-S-R+   360.0  241.50   68.66  1.083  6.900  100.09   8145
- 20:19:47  object015  SUPE01440200         Abell523    W-S-R+   360.0  243.89   67.26  1.095  6.900  101.95   8197
- 20:26:23  object016  SUPE01440210         Abell523    W-S-R+   360.0  245.86   65.86  1.107  6.900  109.59   8264
- 20:33:06  object017  SUPE01440220         Abell523    W-S-R+   360.0  247.79   64.40  1.121  6.900  102.19   8379
- 20:39:47  object018  SUPE01440230         Abell523    W-S-R+   360.0  249.62   62.95  1.136  6.900   97.58   8407
- ~~20:58:28  object022  SUPE01440270         Abell746    W-S-R+   360.0   30.94   49.43  1.302  7.000  102.40   7317~~
- ~~21:05:09  object023  SUPE01440280         Abell746    W-S-R+   360.0   29.92   50.20  1.288  7.000   94.47   7014~~
- ~~21:12:15  object024  SUPE01440290         Abell746    W-S-R+   360.0   28.75   51.03  1.274  7.000   97.36   7012~~
- ~~21:18:55  object025  SUPE01440300         Abell746    W-S-R+   360.0   27.52   51.81  1.261  7.000  108.67   7828~~
- ~~21:25:38  object026  SUPE01440310         Abell746    W-S-R+   360.0   26.26   52.52  1.249  7.000   97.02   8352~~
- ~~21:32:18  object027  SUPE01440320         Abell746    W-S-R+   360.0   25.03   53.20  1.239  7.000   98.43   7062~~
- ~~21:39:03  object028  SUPE01440330         Abell746    W-S-R+   360.0   23.63   53.87  1.229  7.000   98.16   7243~~
- ~~21:45:45  object029  SUPE01440340         Abell746    W-S-R+   360.0   22.13   54.44  1.221  7.000   96.24   7498~~
- 22:04:36  object034  SUPE01440390  RXCJ1053.7+5452    W-S-R+   360.0   31.74   42.89  1.448  7.050  111.68   7196
- 22:11:23  object035  SUPE01440400  RXCJ1053.7+5452    W-S-R+   360.0   31.04   43.70  1.427  7.050   99.34   7137
- 22:21:05  object036  SUPE01440410  RXCJ1053.7+5452    W-S-R+   360.0   29.96   44.87  1.399  7.050   94.77   6889
- 22:27:46  object037  SUPE01440420  RXCJ1053.7+5452    W-S-R+   360.0   29.10   45.69  1.381  7.050   98.85   6681
- 22:34:30  object038  SUPE01440430  RXCJ1053.7+5452    W-S-R+   360.0   28.21   46.44  1.364  7.050  122.59   6469
- 22:41:11  object039  SUPE01440440  RXCJ1053.7+5452    W-S-R+   360.0   27.36   47.17  1.349  7.050  117.19   6425
- 22:47:55  object040  SUPE01440450  RXCJ1053.7+5452    W-S-R+   360.0   26.37   47.90  1.334  7.050   94.02   6214
- 22:54:37  object041  SUPE01440460  RXCJ1053.7+5452    W-S-R+   360.0   25.29   48.55  1.321  7.050  105.29   6310
- 01:08:20  object071  SUPE01440760  PLCKG287.0+32.9    W-S-R+   360.0  168.20   41.01  1.514  7.100  104.17   8553
- 01:15:05  object072  SUPE01440770  PLCKG287.0+32.9    W-S-R+   360.0  170.10   41.31  1.506  7.100  109.02   8358
- 01:21:49  object073  SUPE01440780  PLCKG287.0+32.9    W-S-R+   360.0  172.06   41.55  1.501  7.100  104.57   8292
- 01:28:35  object074  SUPE01440790  PLCKG287.0+32.9    W-S-R+   360.0  174.12   41.74  1.497  7.100   94.98   8348
- 01:35:19  object075  SUPE01440800  PLCKG287.0+32.9    W-S-R+   360.0  176.10   41.89  1.494  7.100   98.43   8443
- 01:42:00  object076  SUPE01440810  PLCKG287.0+32.9    W-S-R+   360.0  178.04   41.94  1.494  7.100  106.74   8588
- 01:48:45  object077  SUPE01440820  PLCKG287.0+32.9    W-S-R+   360.0  180.06   41.96  1.494  7.100  103.83   8709
- 01:55:30  object078  SUPE01440830  PLCKG287.0+32.9    W-S-R+   360.0  182.07   41.99  1.495  7.100  105.06   8597
- 02:08:03  object082  SUPE01440870        Abell1300    W-S-R+   360.0  193.88   49.06  1.330  7.050  102.81   7749
- 02:14:46  object083  SUPE01440880        Abell1300    W-S-R+   360.0  196.17   48.66  1.339  7.050   96.27   7690
- 02:21:30  object084  SUPE01440890        Abell1300    W-S-R+   360.0  198.44   48.18  1.351  7.050   98.43   7633
- 02:29:56  object085  SUPE01440900        Abell1300    W-S-R+   360.0  201.31   47.49  1.367  7.050   95.15   7460
- 02:36:39  object086  SUPE01440910        Abell1300    W-S-R+   360.0  203.47   46.89  1.382  7.050  105.07   7375
- 02:43:21  object087  SUPE01440920        Abell1300    W-S-R+   360.0  205.49   46.22  1.399  7.050  102.41   7403
- 02:50:02  object088  SUPE01440930        Abell1300    W-S-R+   360.0  207.52   45.52  1.417  7.050  100.06   7346
- 02:56:45  object089  SUPE01440940        Abell1300    W-S-R+   360.0  209.53   44.81  1.436  7.050  122.80   7307
- 03:14:09  object093  SUPE01440980  ZwCl1447.2+2619    W-S-R+   360.0   69.35   67.82  1.070  7.070  103.23   5308
- 03:26:28  object094  SUPE01440990  ZwCl1447.2+2619    W-S-R+   360.0   67.60   70.50  1.053  7.070   96.02   5161
- 03:33:01  object095  SUPE01441000  ZwCl1447.2+2619    W-S-R+   360.0   66.42   71.92  1.044  7.070  100.11   5093
- 03:39:44  object096  SUPE01441010  ZwCl1447.2+2619    W-S-R+   360.0   64.84   73.42  1.037  7.070  116.42   5137
- 03:46:24  object097  SUPE01441020  ZwCl1447.2+2619    W-S-R+   360.0   62.93   74.83  1.030  7.070  118.03   5037
- 03:53:08  object098  SUPE01441030  ZwCl1447.2+2619    W-S-R+   360.0   60.78   76.21  1.024  7.070   97.35   4939
- 03:59:53  object099  SUPE01441040  ZwCl1447.2+2619    W-S-R+   360.0   57.84   77.59  1.020  7.070  118.41   5027
- 04:06:29  object100  SUPE01441050  ZwCl1447.2+2619    W-S-R+   360.0   53.98   78.85  1.016  7.070  113.22   4870

## Run SDFRED flat pipeline
### Link to the raw data
This will give 72 separate exposures for the skyflat which should be sufficient (after excluding the grayed out exposures).

```
cd ../r
ln -s ../../../rawdata/2014feb24/SUPA014387[5-9]?.fits .
ln -s ../../../rawdata/2014feb24/SUPA014388[0-2]?.fits .
ln -s ../../../rawdata/2014feb24/SUPA014391[7-9]?.fits .
ln -s ../../../rawdata/2014feb24/SUPA014392[0-4]?.fits .
ln -s ../../../rawdata/2014feb24/SUPA014394[1-8]?.fits .
ln -s ../../../rawdata/2014feb24/SUPA014395[2-9]?.fits .
ln -s ../../../rawdata/2014feb25/SUPA014401[6-9]?.fits .
ln -s ../../../rawdata/2014feb25/SUPA014402[0-3]?.fits .
ln -s ../../../rawdata/2014feb25/SUPA0144039?.fits .
ln -s ../../../rawdata/2014feb25/SUPA014404[0-6]?.fits .
ln -s ../../../rawdata/2014feb25/SUPA014407[6-9]?.fits .
ln -s ../../../rawdata/2014feb25/SUPA014408[0-3]?.fits .
~~ln -s ../../../rawdata/2014feb25/SUPA014408[7-9]?.fits .~~
ln -s ../../../rawdata/2014feb25/SUPA014409[0-4]?.fits .
ln -s ../../../rawdata/2014feb25/SUPA014409[8-9]?.fits .
ln -s ../../../rawdata/2014feb25/SUPA014410[0-5]?.fits .
```

Note that the ~~line~~ above was not executed by accident. This excludes three exposures from the flat, but given that they are such a small fraction it is not worth remaking the flat.

### rename the data files in each band folder
```
ls -1 SUPA*.fits > namechange.lis
namechange.csh namechange.lis
```
### perform subtraction of overscan and bias in each band folder
```
ls -1 H*.fits > ovserscansub.lis
overscansub.csh ovserscansub.lis
```
### Skyflat option (for g, r, i):
```
ls -1 To_RH*.fits > mkflat.lis
mask_mkflat_HA.csh mkflat.lis skyflat_r 0.4 1.3
```
### Check that the flats look reasonable
e.g. with:

```
ds9 -mosaic wcs skyflat*.fits
```
### Clean up working files to save disk space
```
rm To_*
rm tmp*
rm ssbtmp*
rm mnah*
rm blank*
```

# i-band
## Exposures
### Night 1
- 19:57:40  object023  SUPE01438600        Abell3365    W-S-I+   180.0  182.33   48.22  1.341  6.900   99.42   7575
- 20:01:25  object024  SUPE01438610        Abell3365    W-S-I+   180.0  183.60   48.18  1.342  6.900  105.35   7527
- 20:05:57  object025  SUPE01438620        Abell3365    W-S-I+   180.0  185.17   48.09  1.344  6.900  116.48   7462
- 20:09:42  object026  SUPE01438630        Abell3365    W-S-I+   180.0  186.55   47.99  1.347  6.900  118.29   7451
- ~~23:41:39  object067  SUPE01439040  1RXSJ0603.2+4212    W-S-I+   180.0  308.96   39.58  1.586  7.050  102.34   7173~~
- ~~23:45:23  object068  SUPE01439050  1RXSJ0603.2+4212    W-S-I+   180.0  308.84   38.92  1.608  7.050  101.24   7218~~
- ~~23:49:08  object069  SUPE01439060  1RXSJ0603.2+4212    W-S-I+   180.0  308.70   38.24  1.633  7.050   98.58   7346~~
- ~~23:52:53  object070  SUPE01439070  1RXSJ0603.2+4212    W-S-I+   180.0  308.59   37.49  1.661  7.050  110.44   7446~~
- 00:03:15  object073  SUPE01439100        Abell3411    W-S-I+   180.0  208.86   47.82  1.356  7.050   96.00   6066
- 00:06:58  object074  SUPE01439110        Abell3411    W-S-I+   180.0  209.98   47.41  1.365  7.050  108.36   6218
- 00:10:42  object075  SUPE01439120        Abell3411    W-S-I+   180.0  211.11   46.95  1.376  7.050  103.80   6315
- 00:14:28  object076  SUPE01439130        Abell3411    W-S-I+   180.0  212.30   46.46  1.387  7.050  104.51   6374
### Night 2
- 04:52:23  object111  SUPE01441160  ZwCl1447.2+2619    W-S-I+   180.0  348.01   83.62  1.007  6.970  102.78   4304
- 04:56:08  object112  SUPE01441170  ZwCl1447.2+2619    W-S-I+   180.0  341.10   83.39  1.007  6.970  104.56   4269
- 04:59:50  object113  SUPE01441180  ZwCl1447.2+2619    W-S-I+   180.0  334.55   83.07  1.008  6.970  108.50   4263
- 05:03:34  object114  SUPE01441190  ZwCl1447.2+2619    W-S-I+   180.0  328.33   82.62  1.009  6.970   99.10   4290
- 05:08:52  object115  SUPE01441200        Abell2061    W-S-I+   180.0   10.63   79.02  1.018  6.970  112.99   4316
- 05:12:35  object116  SUPE01441210        Abell2061    W-S-I+   180.0    6.58   79.14  1.018  6.970  107.28   4450
- 05:16:19  object117  SUPE01441220        Abell2061    W-S-I+   180.0    2.31   79.22  1.018  6.970   99.25   4363
- 05:20:05  object118  SUPE01441230        Abell2061    W-S-I+   180.0  357.67   79.22  1.018  6.970  103.75   4378
- 05:26:55  object119  SUPE01441240  MACSJ1752.0+4440    W-S-I+   180.0   41.59   51.56  1.268  6.970  120.00   5642
- 05:30:34  object120  SUPE01441250  MACSJ1752.0+4440    W-S-I+   180.0   41.09   52.10  1.259  6.970  120.00   5547
- 05:34:12  object121  SUPE01441260  MACSJ1752.0+4440    W-S-I+   180.0   40.57   52.67  1.250  6.970  120.00   5712
- 05:37:49  object122  SUPE01441270  MACSJ1752.0+4440    W-S-I+   180.0   39.97   53.26  1.240  6.970  120.00   6037
- 05:42:08  object123  SUPE01441280  MACSJ1752.0+4440    W-S-I+   180.0   39.27   53.91  1.230  6.970  120.00   7333
- 05:45:46  object124  SUPE01441290  MACSJ1752.0+4440    W-S-I+   180.0   38.68   54.43  1.222  6.970  120.00  10214

## Run SDFRED flat pipeline
### Link to the raw data
This will give 22 separate exposures for the skyflat which should be sufficient (after excluding the grayed out exposures).

```
cd i
ln -s ../../../rawdata/2014feb24/SUPA014386[0-3]?.fits .
ln -s ../../../rawdata/2014feb24/SUPA014391[0-3]?.fits .
ln -s ../../../rawdata/2014feb25/SUPA014411[6-9]?.fits .
ln -s ../../../rawdata/2014feb25/SUPA014412[0-9]?.fits .
```
### rename the data files in each band folder
```
ls -1 SUPA*.fits > namechange.lis
namechange.csh namechange.lis
```
### perform subtraction of overscan and bias in each band folder
```
ls -1 H*.fits > ovserscansub.lis
overscansub.csh ovserscansub.lis
```
### Skyflat option (for g, r, i):
```
ls -1 To_RH*.fits > mkflat.lis
mask_mkflat_HA.csh mkflat.lis skyflat_i 0.4 1.3
```
### Check that the flats look reasonable
e.g. with:

```
ds9 -mosaic wcs skyflat*.fits
```
### Clean up working files to save disk space
```
rm To_*
rm tmp*
rm ssbtmp*
rm mnah*
rm blank*
```

# N-B-L816
## Exposures
- 04:54:09  object124  SUPE01439610  RXCJ1314.4-2515  N-B-L816   250.0  208.96   38.88  1.608  7.050  101.25    389
- 04:59:03  object125  SUPE01439620  RXCJ1314.4-2515  N-B-L816   250.0  210.16   38.33  1.628  7.050   96.16    395
- 05:03:57  object126  SUPE01439630  RXCJ1314.4-2515  N-B-L816   250.0  211.34   37.73  1.651  7.050  121.03    398
- 05:08:51  object127  SUPE01439640  RXCJ1314.4-2515  N-B-L816   250.0  212.57   37.08  1.676  7.050  116.05    405

I am concerned that these are not enough to do a proper sky flat so I recommend using the dome flat for the NB filter:

- 06:29:38  object149  SUPE01439860         DOMEFLAT  N-B-L816    20.0  249.81   89.97  1.000  7.050  163.00  26877
- 06:31:03  object150  SUPE01439870         DOMEFLAT  N-B-L816    20.0  249.81   89.97  1.000  7.050  163.00  27042
- 06:31:53  object151  SUPE01439880         DOMEFLAT  N-B-L816    20.0  249.81   89.97  1.000  7.050  163.00  27054
- 06:32:43  object152  SUPE01439890         DOMEFLAT  N-B-L816    20.0  249.81   89.97  1.000  7.050  163.00  27026
- 06:33:39  object153  SUPE01439900         DOMEFLAT  N-B-L816    20.0  249.81   89.97  1.000  7.050  163.00  27050
- 06:34:35  object154  SUPE01439910         DOMEFLAT  N-B-L816    20.0  249.81   89.97  1.000  7.050  163.00  27043
- 06:35:30  object155  SUPE01439920         DOMEFLAT  N-B-L816    20.0  249.81   89.97  1.000  7.050  163.00  27120
- 06:36:27  object156  SUPE01439930         DOMEFLAT  N-B-L816    20.0  249.81   89.97  1.000  7.050  163.00  27204
- 06:37:16  object157  SUPE01439940         DOMEFLAT  N-B-L816    20.0  249.81   89.97  1.000  7.050  163.00  27085

## Run SDFRED flat pipeline
### Link to the raw data
```
cd N-B-L816
ln -s ../../../rawdata/2014feb24/SUPA014398[6-9]?.fits .
ln -s ../../../rawdata/2014feb24/SUPA014399[0-4]?.fits .
```
### rename the data files in each band folder
```
ls -1 SUPA*.fits > namechange.lis
namechange.csh namechange.lis
```
### perform subtraction of overscan and bias in each band folder
```
ls -1 H*.fits > ovserscansub.lis
overscansub.csh ovserscansub.lis
```
### Dome flat option (for N-B-L816):
```
ls -1 To_RH*.fits > mkflat.lis
mask_mkflat_HA.csh mkflat.lis dome 0.4 1.3
```

### Check that the flats look reasonable
e.g. with:

```
ds9 -mosaic wcs dome*.fits
```
### Clean up working files to save disk space
```
rm To_*
rm tmp*
rm ssbtmp*
rm mnah*
rm blank*
```