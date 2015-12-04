These are the commands used to create the sky flats for the g, and r broadband images.

The following are the list of files that should be used for creating skyflats. Note that I start off by listing all possible files for each band (not including the short 3 and 30 s exposures, since James recommends against using these), then I consider whether there are too many bright stars in each field.


|Cluster	| Use for skyflat? |
|----------	|------------------|
|ZwCL1856+6616		| yes |
|ZwCL2120+2256  | yes |
|Abell2355	| yes |
|MACSJ2135.2-0102		| yes |
|PSZ1G108.18-11.53		| yes |
|CIZAJ0638.1+4747	| yes |

Setup the flat folder architecture.

```
cd /sandbox/Subaru/flats
mkdir 2015sep
cd 2015sep
mkdir g r
```

# g-band
The ~~strike through~~ lines are not used in the flat fields for the reasons commented in the table above.
## Exposures
### Night 1
- ~~20:20:20  object000  SUPE01538720         FOCUSING    W-S-G+    70.0  356.46   43.23  1.459  6.650  120.01      0~~
- ~~20:25:36  object001  SUPE01538730    ZwCL1856+6616    W-S-G+    30.0  355.74   43.15  1.461  6.750  111.79    124~~
- 20:27:02  object002  SUPE01538740    ZwCL1856+6616    W-S-G+   180.0  355.55   43.12  1.463  6.750  111.79    741
- 20:30:57  object003  SUPE01538750    ZwCL1856+6616    W-S-G+   180.0  355.06   43.04  1.465  6.750  117.30    753
- 20:34:43  object004  SUPE01538760    ZwCL1856+6616    W-S-G+   180.0  354.55   42.97  1.467  6.750   98.17    765
- 20:38:27  object005  SUPE01538770    ZwCL1856+6616    W-S-G+   180.0  353.98   42.87  1.470  6.750  114.57    777
- ~~20:44:33  object006  SUPE01538780    ZwCL2120+2256    W-S-G+    30.0   76.91   67.31  1.083  6.750  104.95    139~~
- 20:45:37  object007  SUPE01538790    ZwCL2120+2256    W-S-G+   180.0   76.86   67.56  1.077  6.750  104.95    824
- 20:55:05  object008  SUPE01538800    ZwCL2120+2256    W-S-G+   180.0   76.34   69.71  1.061  6.750  120.00    849
- 20:59:11  object009  SUPE01538810    ZwCL2120+2256    W-S-G+   180.0   76.08   70.65  1.055  6.750  120.00    828
- 21:02:50  object010  SUPE01538820    ZwCL2120+2256    W-S-G+   180.0   75.76   71.54  1.050  6.750  120.00    786
- ~~21:07:48  object011  SUPE01538830         FOCUSING    W-S-G+    70.0  128.33   62.05  1.129  6.650  120.00      0~~
- ~~21:12:23  object012  SUPE01538840        Abell2355    W-S-G+    30.0  130.03   62.88  1.122  7.000  120.00    157~~
- 21:13:24  object013  SUPE01538850        Abell2355    W-S-G+   180.0  130.41   63.07  1.116  7.000  120.00    934
- 21:16:55  object014  SUPE01538860        Abell2355    W-S-G+   180.0  131.80   63.69  1.110  6.700  120.00    924
- 21:20:31  object015  SUPE01538870        Abell2355    W-S-G+   180.0  133.23   64.30  1.105  6.700  120.00    904
- 21:24:10  object016  SUPE01538880        Abell2355    W-S-G+   180.0  134.82   64.91  1.100  6.700  120.00    905
- 21:27:45  object017  SUPE01538890        Abell2355    W-S-G+   180.0  136.54   65.54  1.094  6.700  120.00    900
- ~~21:31:23  object018  SUPE01538900  MACSJ2135.2-0102    W-S-G+    30.0  141.79   64.15  1.110  6.700  120.00    154~~
- 21:32:38  object019  SUPE01538910  MACSJ2135.2-0102    W-S-G+   180.0  142.38   64.33  1.105  6.700  102.76    924
- 21:36:54  object020  SUPE01538920  MACSJ2135.2-0102    W-S-G+   180.0  144.39   64.92  1.100  6.700  120.00    916
- 21:40:35  object021  SUPE01538930  MACSJ2135.2-0102    W-S-G+   180.0  146.31   65.43  1.096  6.700  120.00    922
- 21:44:28  object022  SUPE01538940  MACSJ2135.2-0102    W-S-G+   180.0  148.29   65.90  1.092  6.700  120.00    920
- 21:48:08  object023  SUPE01538950  MACSJ2135.2-0102    W-S-G+   180.0  150.40   66.37  1.089  6.700  120.00    918
- ~~21:55:05  object024  SUPE01538960  PSZ1G108.18-11.53    W-S-G+    30.0   36.54   49.31  1.317  6.700  120.00    174~~
- 22:04:02  object025  SUPE01538970  PSZ1G108.18-11.53    W-S-G+   180.0   35.27   50.55  1.287  6.700  121.05   1042
- 22:08:02  object026  SUPE01538980  PSZ1G108.18-11.53    W-S-G+   180.0   34.68   51.06  1.278  6.700  120.76    978
- 22:12:10  object027  SUPE01538990  PSZ1G108.18-11.53    W-S-G+   180.0   34.03   51.62  1.268  6.700  120.00    960
- 22:15:47  object028  SUPE01539000  PSZ1G108.18-11.53    W-S-G+   180.0   33.38   52.14  1.259  6.700  120.00   1011
- ~~04:13:05  object072  SUPE01539440         FOCUSING    W-S-G+    70.0  316.16   35.20  1.743  6.750  120.01      0~~
- ~~04:16:20  object073  SUPE01539450  PSZ1G108.18-11.53    W-S-G+    30.0  316.05   34.67  1.758  6.900  120.01    181~~
- 04:17:23  object074  SUPE01539460  PSZ1G108.18-11.53    W-S-G+   180.0  316.02   34.50  1.784  6.900  121.06   1089
- 04:21:07  object075  SUPE01539470  PSZ1G108.18-11.53    W-S-G+   180.0  315.92   33.91  1.812  6.900  120.76   1055
- 04:24:51  object076  SUPE01539480  PSZ1G108.18-11.53    W-S-G+   180.0  315.80   33.30  1.841  6.900  117.84   1044
- 04:28:35  object077  SUPE01539490  PSZ1G108.18-11.53    W-S-G+   180.0  315.70   32.63  1.875  6.900  123.46   1082
- ~~04:34:38  object078  SUPE01539500  CIZAJ0638.1+4747    W-S-G+    30.0   41.70   44.06  1.434  6.900  123.46    177~~
- 04:35:51  object079  SUPE01539510  CIZAJ0638.1+4747    W-S-G+   180.0   41.60   44.26  1.420  6.900  110.96   1065
- 04:39:35  object080  SUPE01539520  CIZAJ0638.1+4747    W-S-G+   180.0   41.28   44.81  1.406  6.900   97.68   1065
- 04:43:20  object081  SUPE01539530  CIZAJ0638.1+4747    W-S-G+   180.0   40.94   45.40  1.392  6.900  118.25   1094
- 04:47:05  object082  SUPE01539540  CIZAJ0638.1+4747    W-S-G+   180.0   40.54   46.02  1.378  6.900   98.19   1105
- 04:52:54  object083  SUPE01539550  CIZAJ0638.1+4747    W-S-G+   180.0   39.94   46.88  1.359  6.900  103.92   1138
- 04:56:38  object084  SUPE01539560  CIZAJ0638.1+4747    W-S-G+   180.0   39.53   47.45  1.347  6.900  111.01   1220
- 05:00:25  object085  SUPE01539570  CIZAJ0638.1+4747    W-S-G+   180.0   39.10   47.98  1.336  6.900  124.47   1414

## Run SDFRED flat pipeline
### Link to the raw data
There are 33 separate exposures for the skyflat which should be sufficient (after excluding the grayed out exposures).

```
cd g
ln -s ../../../rawdata/2015sep11/SUPA015387[4-7]?.fits .
ln -s ../../../rawdata/2015sep11/SUPA0153879?.fits .
ln -s ../../../rawdata/2015sep11/SUPA015388[0-2]?.fits .
ln -s ../../../rawdata/2015sep11/SUPA015388[5-9]?.fits .
ln -s ../../../rawdata/2015sep11/SUPA015389[1-5]?.fits .
ln -s ../../../rawdata/2015sep11/SUPA015389[7-9]?.fits .
ln -s ../../../rawdata/2015sep11/SUPA0153900?.fits .
ln -s ../../../rawdata/2015sep11/SUPA015394[6-9]?.fits .
ln -s ../../../rawdata/2015sep11/SUPA015395[1-7]?.fits .
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
- ~~22:29:26  object029  SUPE01539010         FOCUSING    W-S-R+    70.0  341.65   37.17  1.657  6.650  120.00      0~~
- ~~22:32:54  object030  SUPE01539020    ZwCL1856+6616    W-S-R+    30.0  341.36   36.91  1.664  6.830  120.00    457~~
- 22:34:56  object031  SUPE01539030    ZwCL1856+6616    W-S-R+   360.0  341.19   36.75  1.687  6.830  120.00   5531
- 22:53:44  object032  SUPE01539040    ZwCL1856+6616    W-S-R+   360.0  339.75   35.27  1.750  6.830  120.54   5784
- 23:08:26  object033  SUPE01539050    ZwCL1856+6616    W-S-R+   360.0  338.79   34.06  1.806  6.830  100.29   6118
- 23:17:22  object034  SUPE01539060    ZwCL1856+6616    W-S-R+   360.0  338.23   33.30  1.843  6.830   80.37   6267
- 23:25:08  object035  SUPE01539070    ZwCL1856+6616    W-S-R+   360.0  337.76   32.56  1.881  6.830   91.71   6390
- 23:32:42  object036  SUPE01539080    ZwCL1856+6616    W-S-R+   360.0  337.37   31.88  1.919  6.830  107.75   6477
- 23:39:29  object037  SUPE01539090    ZwCL1856+6616    W-S-R+   360.0  337.02   31.30  1.951  6.830  102.89   6678
- ~~23:47:28  object038  SUPE01539100         FOCUSING    W-S-R+    70.0  283.60   69.53  1.070  6.750  120.01      0~~
- ~~00:00:50  object039  SUPE01539110  MACSJ2135.2-0102    W-S-R+    30.0  228.32   60.16  1.153  6.840  120.01    480~~
- ~~00:22:58  object042  SUPE01539140        Abell2355    W-S-R+    30.0  238.93   57.59  1.185  6.840  120.00    480~~
- 00:37:10  object044  SUPE01539160        Abell2355    W-S-R+   180.0  242.56   54.69  1.234  6.840  120.00   2855
- 00:43:24  object045  SUPE01539170        Abell2355    W-S-R+   180.0  243.99   53.37  1.256  6.840  120.00   2935
- 00:49:01  object046  SUPE01539180        Abell2355    W-S-R+   180.0  245.26   52.13  1.277  6.840  120.00   3032
- 00:52:30  object047  SUPE01539190        Abell2355    W-S-R+   180.0  246.00   51.38  1.291  6.840  120.00   3039
- ~~00:57:34  object048  SUPE01539200    ZwCL2120+2256    W-S-R+    30.0  282.65   53.40  1.247  6.840  120.00    463~~
- ~~01:53:09  object049  SUPE01539210         FOCUSING    W-S-R+    70.0  284.12   40.64  1.545  6.750  120.01      0~~
- 01:56:48  object050  SUPE01539220    ZwCL2120+2256    W-S-R+   180.0  284.25   39.84  1.582  6.860  116.95   2879
- 02:00:32  object051  SUPE01539230    ZwCL2120+2256    W-S-R+   180.0  284.39   38.93  1.613  6.860   99.89   2957
- 02:04:19  object052  SUPE01539240    ZwCL2120+2256    W-S-R+   180.0  284.55   38.07  1.644  6.860   98.04   2996
- 02:08:02  object053  SUPE01539250    ZwCL2120+2256    W-S-R+   180.0  284.65   37.25  1.676  6.860  113.18   3128
- ~~02:15:42  object054  SUPE01539260  PSZ1G108.18-11.53    W-S-R+    30.0  327.51   52.80  1.256  6.860  120.00    446~~
- 02:16:56  object055  SUPE01539270  PSZ1G108.18-11.53    W-S-R+   360.0  327.30   52.64  1.271  6.860  121.95   5417
- 02:23:42  object056  SUPE01539280  PSZ1G108.18-11.53    W-S-R+   360.0  326.19   51.78  1.286  6.860  111.42   5493
- 02:30:24  object057  SUPE01539290  PSZ1G108.18-11.53    W-S-R+   360.0  325.11   50.90  1.303  6.860  108.85   5371
- 02:37:07  object058  SUPE01539300  PSZ1G108.18-11.53    W-S-R+   360.0  324.07   49.93  1.322  6.860   93.39   5433
- 02:43:48  object059  SUPE01539310  PSZ1G108.18-11.53    W-S-R+   360.0  323.17   48.99  1.342  6.860  101.04   5521
- 02:50:32  object060  SUPE01539320  PSZ1G108.18-11.53    W-S-R+   360.0  322.30   48.08  1.362  6.860   99.05   5466
- 02:57:16  object061  SUPE01539330  PSZ1G108.18-11.53    W-S-R+   360.0  321.49   47.09  1.384  6.860  112.18   5589
- ~~03:06:12  object062  SUPE01539340         FOCUSING    W-S-R+    70.0   45.53   29.54  2.006  6.750  120.00      0~~
- ~~03:10:02  object063  SUPE01539350  CIZAJ0638.1+4747    W-S-R+    30.0   45.49   30.18  1.979  6.950  120.00    557~~
- 03:11:17  object064  SUPE01539360  CIZAJ0638.1+4747    W-S-R+   360.0   45.48   30.39  1.915  6.950  103.69   6500
- 03:18:02  object065  SUPE01539370  CIZAJ0638.1+4747    W-S-R+   360.0   45.38   31.50  1.857  6.900   96.12   6457
- 03:24:46  object066  SUPE01539380  CIZAJ0638.1+4747    W-S-R+   360.0   45.27   32.62  1.802  6.900  118.25   6445
- 03:31:32  object067  SUPE01539390  CIZAJ0638.1+4747    W-S-R+   360.0   45.10   33.81  1.748  6.900  108.48   6459
- 03:38:16  object068  SUPE01539400  CIZAJ0638.1+4747    W-S-R+   360.0   44.89   34.93  1.701  6.900  105.44   6413
- 03:44:58  object069  SUPE01539410  CIZAJ0638.1+4747    W-S-R+   360.0   44.71   36.02  1.659  6.900   95.04   6465
- 03:51:41  object070  SUPE01539420  CIZAJ0638.1+4747    W-S-R+   360.0   44.44   37.14  1.617  6.900  118.67   6429
- 03:58:25  object071  SUPE01539430  CIZAJ0638.1+4747    W-S-R+   360.0   44.06   38.24  1.579  6.900   96.03   6348

## Run SDFRED flat pipeline
### Link to the raw data
This will give 30 separate exposures for the skyflat which should be sufficient (after excluding the grayed out exposures).

```
cd ../r
ln -s ../../../rawdata/2015sep11/SUPA015390[3-9]?.fits .
ln -s ../../../rawdata/2015sep11/SUPA015391[6-9]?.fits .
ln -s ../../../rawdata/2015sep11/SUPA015392[2-5]?.fits .
ln -s ../../../rawdata/2015sep11/SUPA015392[7-9]?.fits .
ln -s ../../../rawdata/2015sep11/SUPA015393[0-3]?.fits .
ln -s ../../../rawdata/2015sep11/SUPA015393[6-9]?.fits .
ln -s ../../../rawdata/2015sep11/SUPA015394[0-3]?.fits .
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
