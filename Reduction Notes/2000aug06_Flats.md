These are the commands used to create the sky flats for the V broadband images during the reduction of MACS J2243.3-0935 W-C-RC and W-C-IC
archival images.

I downloaded 100 exposures of the W-C-RC W-C-IC bands taken during the nights between:
2000-06-01..2000-10-01
from SMOKA.
 /sandbox/Subaru/rawdata/2003aug25/flats/ R or I

Since all of this data is archival data taken before 2008 we will need to use sdfred1 by prepending its bin to the PATH.

```
export PATH="/usr/local/sdfred20100528_mf1/bin:$PATH"
```

Setup the flat folder architecture.

```
cd /sandbox/Subaru/flats
mkdir 2000aug
cd 2000aug
mkdir R I
```

# R-band

## Run SDFRED flat pipeline
### Link to the raw data
There are 99 separate exposures for the skyflat which should be sufficient.

```
cd R
ln -s ../../../rawdata/2000aug06/flats/R/SUPA*.fits .
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
### Skyflat option:
```
ls -1 To_RH*.fits > mkflat.lis
mask_mkflat_HA.csh mkflat.lis skyflat_R 0.5 1.3
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

# I-band

## Run SDFRED flat pipeline
### Link to the raw data
There are 99 separate exposures for the skyflat which should be sufficient.

```
cd I
ln -s ../../../rawdata/2000aug06/flats/I/SUPA*.fits .
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
### Skyflat option:
```
ls -1 To_RH*.fits > mkflat.lis
mask_mkflat_HA.csh mkflat.lis skyflat_I 0.5 1.3
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
