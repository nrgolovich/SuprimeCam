These are the Subaru SuprimeCam reduction notes. The

```
code blocks
```
are meant to be copied in to the terminal commandline.

It is recommended that you start with your deepest band first, as some of reduction outputs can help with the reduction of the other bands (e.g. using the stacked catalog as input to scamp).

This reduction is run with the following versions:

* SDFRED 20130924_mf2
* scamp 1.3.11 (note that 2.0.4 has a bug that causes poor solutions at the periphery of the field)
* swarp 2.38.0
* https://github.com/MCTwo/SuprimeCam commit:ef0a506
* https://github.com/MCTwo/CodeCDF commit:8b5c009

### Setup the folder architecture ans cluster specific inputs
```
cd /sandbox/Subaru/
mkdir zwcl2120
cd zwcl2120
mkdir g r
```

Define the base name for result reduced files (e.g. short name of the cluster).

```
basename=zwcl2120
```

Define the deepest band. Reduction should start with this band as some of it files may be used in the reduction of the other bands.

```
deepband=r
```

Define the ra,dec of the center of the field (degrees). This will ensure similar image properties for all bands.

```
fieldcenter=320.572,+23.202
```

# r
Go to the r directory and specify band name.

```
cd r
band=r
```

Define the exposure time for the individual exposures in seconds.

```
EXPTIME=180
```

Define the zero point for this band.

```
zp=27.488
```
## SDFRED Reduction Portion
This portion of the pipeline uses SDFRED and the proceedure documented in its [manual](http://www.naoj.org/Observing/Instruments/SCam/sdfred/v2.0/sdfred2_2p1ae.pdf).

### Link to the raw data
From log:
00:57:34  object048  SUPE01539200    ZwCL2120+2256    W-S-R+    30.0  282.65   53.40  1.247  6.840  120.00    463
01:53:09  object049  SUPE01539210         FOCUSING    W-S-R+    70.0  284.12   40.64  1.545  6.750  120.01      0
01:56:48  object050  SUPE01539220    ZwCL2120+2256    W-S-R+   180.0  284.25   39.84  1.582  6.860  116.95   2879
02:00:32  object051  SUPE01539230    ZwCL2120+2256    W-S-R+   180.0  284.39   38.93  1.613  6.860   99.89   2957
02:04:19  object052  SUPE01539240    ZwCL2120+2256    W-S-R+   180.0  284.55   38.07  1.644  6.860   98.04   2996
02:08:02  object053  SUPE01539250    ZwCL2120+2256    W-S-R+   180.0  284.65   37.25  1.676  6.860  113.18   3128

These do not include the short exposures.

```
ln -s ../../rawdata/2015sep11/SUPA015392[2-5]?.fits .
```

### Rename the data files
```
ls -1 SUPA*.fits > namechange.lis
namechange.csh namechange.lis
```
Generates H*.fits files.

### Perform subtraction of ovserscan bias
```
ls -1 H*.fits > ovserscansub.lis
overscansub.csh ovserscansub.lis
```
Generates To_RH*.fits files.

### Apply flat fields to object images
The flat field images were created using the proceedure outlined in [2015sep_Flats.md](https://github.com/MCTwo/SuprimeCam/blob/master/Reduction%20Notes/2015sep_Flats.md).

```
ln -s ../../flats/2014feb/$band'/skyflat'*.fits .
ls -1 skyflat*.fits > ffield_mf.lis
ls -1 To_RH*.fits > ffield_im.lis
ffield.csh ffield_mf.lis ffield_im.lis
```
Generates fTo_RH*.fits files.

### Distortion correction and atmospheric dispersion correction
```
ls -1 fTo_RH*.fits > distcorr.lis
distcorr.csh distcorr.lis
```
Generates gfTo_RH*.fits files.

_Note that we skip the SDFRED 'PSF size measurement', 'PSF size equalization', and 'Sky subtraction' steps._

### Mask the AG shade
```
ls -1 gfTo_RH*.fits > mask_AGX.lis
mask_AGX.csh mask_AGX.lis
```
Generates AgfTo_RH*.fits files.

## Astromatic Reduction Portion

### Link the global Astromatic files
`$gitdir` should be defined in your .bashrc and give the path to your highest level git folder where the SuprimeCam repo has been placed.

```
ln -s $gitdir/SuprimeCam/Astromatic/sext_astfile.param .
ln -s $gitdir/SuprimeCam/Astromatic/sext_astfile_final.param .
ln -s $gitdir/SuprimeCam/Astromatic/sext_scam_astrom.config .
ln -s $gitdir/SuprimeCam/Astromatic/scamp_scam.config .
```

### Shorten object file names
```
python $gitdir/SuprimeCam/python/rename_before_swarp.py
```
Will create `objectnnn_[chipname].fits` files from AgfTo_RH[obsdate]objectnnn_[chipname].fits files.

### Make the initial weight files before running SExtractor
```
python $gitdir/SuprimeCam/python/make_wht_for_swarp_1.py
```
Will create *_wht_init.fits files.

### Run SExtractor on the files
The number following the -P option gives the number of processors to run in parallel.

```
ls object*.fits | grep -v wht | xargs -I {} -P 20 python $gitdir/SuprimeCam/python/run_sext_scam_1.py {}
```

### Run scamp on the files
For this first pass we will use 2MASS as the reference.

```
scamp object*cat -c scamp_scam.config
ls object*fits | grep -v wht > good_frames_pass1.txt
```

**Any objects with redlines in the scamp output?**
No bad exposures.

*If there are any objects for which scamp fails to find an astrometric solution there are two options:*

1. Try running with a different astrometric reference catalog (e.g. SDSS-R5 instead of the default 2MASS)

	```
	scamp object*cat -c scamp_scam.config -ASTREF_CATALOG SDSS-R5
	```

2. Edit out any objects in the good_frames_pass1.txt file that had redlines in the scamp output. Then run through the following steps up to and through running SExtractor on the second swarp coadd, use this catalog as ASTREFCAT_NAME input in the scamp.config file, and repeat all of the following steps a second time.

	```
	ln -s $gitdir/SuprimeCam/Astromatic/scamp_scam_pass2.config .
	scamp object*cat -c scamp_scam_pass2.config -ASTREF_NAME ../$basename'_'$deepband'.cat'
	ls object*fits | grep -v wht | grep -v resamp > good_frames_pass2.txt
	```
	*Remove any objects with redlines from the good_frames_pass2.txt file.*

### Run the initial swarp to create a median-stacked coadd file
This median-stacked coadd will be used to create a mask for pixels in individual exposures that should be excluded from a final mean-stacked coadd (e.g. saturated bleeds, cosmic-ray, etc. pixels). Note we don't want to stop at this stage because the median-stacked image will have lower signal to noise than the mean-stacked image. This step is necessary to have a clean mean-stack.

_If this is the second pass then change good_frames_pass1.txt to good_frames_pass2.txt in the following command_

```
ln -s $gitdir/Suprimecam/Astromatic/swarp_scam_1.config .
swarp @good_frames_pass1.txt -c swarp_scam_1.config -CENTER_TYPE MANUAL -CENTER $fieldcenter
```

Creates swarp_median.fits and swarp_median_wht.fits, as well as a bunch of *resamp.fits images for each chip.

#### look at the images

```
ds9 -tile swarp_median.fits -scale log -scale limits 0 100 -zoom to fit swarp_median_wht.fits -scale linear -scale minmax -zoom to fit
```


### Make the updated weight maps
Compare the individual exposures with the median-stack from the previous step to identify outlier pixels that should be excluded from the mean-stack.

*** NB: The FLXSCAL paramter produced by scamp does the following:

 1. Converts the units of the output swarped file into counts/sec
 2. Adjusts the flux levels by an additional small amount to optimize the flux match between the images.

Note: The sigma clipping level has to be chosen.  For now, go with nsig=2. (the last argument on the line below)

```
python $gitdir/SuprimeCam/python/make_wht_for_swarp_2.py swarp_median.fits 2.
```

### Put the exposure time back into the individual resampled files
The exposure time was not transfered to the *resamp.fits images. We add this back here.

```
python $gitdir/SuprimeCam/python/add_exptime.py $EXPTIME
```

### Do the ultimate coadd
This coadd is slightly different from the previous swarp median-stack coadd; the differences are two fold:

1. COMBINE_TYPE is now WEIGHTED; producing a weighted mean stack.
2. RESAMPLE is now N; since we are building off the *resamp.fits fils from the previous resampling.

These changes are reflected in swarp_scam_2.config

```
ln -s $gitdir/Suprimecam/Astromatic/swarp_scam_2.config .
swarp *resamp.fits -c swarp_scam_2.config -CENTER_TYPE MANUAL -CENTER $fieldcenter
```

Creates swarp_wmean.fits and swarp_wmean_wht.fits.

#### look at the images

```
ds9 -tile swarp_wmean.fits -scale log -scale limits 0 100 -zoom to fit swarp_wmean_wht.fits -scale linear -scale mode minmax -zoom to fit
```

### Create the exposure time map

```
ln -s $gitdir/SuprimeCam/Astromatic/swarp_texp.config .
python $gitdir/SuprimeCam/python/make_texp_map.py $EXPTIME $fieldcenter
```
creates swarp_wmean_texp.fits.

### Fix header in final combined image
Correct the header information regarding exposure time and zero point.

*make sure correct zero point is input as second argument*

```
python $gitdir/SuprimeCam/python/fix_header_final.py swarp_wmean.fits $zp
```

### Run SExtractor on the final coadd, using a filter-specific config file
```
ln -s $gitdir/SuprimeCam/Astromatic/sext_scam_final.config .
python $gitdir/SuprimeCam/python/run_sext_final.py swarp_wmean.fits
```
Creates SExtractor catalog swarp_wmean.cat.

_if previous scamp run had failed chips then you can now go back to that step and run the command with option -ASTREFCAT_NAME swarp_wmean.cat and repeat the subsequent steps_

### Move the final files to the parent cluster folder
```
mv swarp_wmean.fits ../$basename'_'$band'.fits'
mv swarp_wmean_wht.fits ../$basename'_'$band'_wht.fits'
mv swarp_wmean.cat ../$basename'_'$band'.cat'
mv swarp_wmean.reg ../$basename'_'$band'.reg'
```

# g

Go to the g directory and specify band name.

```
cd ../g
band=g
```

Define the exposure time for the individual exposures in seconds.

```
EXPTIME=180
```

Define the zero point for this band.

```
zp=27.227
```

## SDFRED Reduction Portion
This portion of the pipeline uses SDFRED and the proceedure documented in its [manual](http://www.naoj.org/Observing/Instruments/SCam/sdfred/v2.0/sdfred2_2p1ae.pdf).

### Link to the raw data
From log:
20:44:33  object006  SUPE01538780    ZwCL2120+2256    W-S-G+    30.0   76.91   67.31  1.083  6.750  104.95    139
20:45:37  object007  SUPE01538790    ZwCL2120+2256    W-S-G+   180.0   76.86   67.56  1.077  6.750  104.95    824
20:55:05  object008  SUPE01538800    ZwCL2120+2256    W-S-G+   180.0   76.34   69.71  1.061  6.750  120.00    849
20:59:11  object009  SUPE01538810    ZwCL2120+2256    W-S-G+   180.0   76.08   70.65  1.055  6.750  120.00    828
21:02:50  object010  SUPE01538820    ZwCL2120+2256    W-S-G+   180.0   75.76   71.54  1.050  6.750  120.00    786

These do not include the short exposures.

```
ln -s ../../rawdata/2015sep11/SUPA0153879?.fits .
ln -s ../../rawdata/2015sep11/SUPA015388[0-2]?.fits .
```

### Rename the data files
```
ls -1 SUPA*.fits > namechange.lis
namechange.csh namechange.lis
```
Generates H*.fits files.

### Perform subtraction of ovserscan bias
```
ls -1 H*.fits > ovserscansub.lis
overscansub.csh ovserscansub.lis
```
Generates To_RH*.fits files.

### Apply flat fields to object images
The flat field images were created using the proceedure outlined in [2015sep_Flats.md](https://github.com/MCTwo/SuprimeCam/blob/master/Reduction%20Notes/2015sep_Flats.md).

_make sure to change path to correct filter_

```
ln -s ../../flats/2014feb/$band'/skyflat'*.fits .
ls -1 skyflat*.fits > ffield_mf.lis
ls -1 To_RH*.fits > ffield_im.lis
ffield.csh ffield_mf.lis ffield_im.lis
```
Generates fTo_RH*.fits files.

### Distortion correction and atmospheric dispersion correction
```
ls -1 fTo_RH*.fits > distcorr.lis
distcorr.csh distcorr.lis
```
Generates gfTo_RH*.fits files.

_Note that we skip the SDFRED 'PSF size measurement', 'PSF size equalization', and 'Sky subtraction' steps._

### Mask the AG shade
```
ls -1 gfTo_RH*.fits > mask_AGX.lis
mask_AGX.csh mask_AGX.lis
```
Generates AgfTo_RH*.fits files.

## Astromatic Reduction Portion

### Link the global Astromatic files
`$gitdir` should be defined in your .bashrc and give the path to your highest level git folder where the SuprimeCam repo has been placed.

```
ln -s $gitdir/SuprimeCam/Astromatic/sext_astfile.param .
ln -s $gitdir/SuprimeCam/Astromatic/sext_astfile_final.param .
ln -s $gitdir/SuprimeCam/Astromatic/sext_scam_astrom.config .
ln -s $gitdir/SuprimeCam/Astromatic/scamp_scam_pass2.config .
```

### Shorten object file names
```
python $gitdir/SuprimeCam/python/rename_before_swarp.py
```
Will create objectnnn_[chipname].fits files from AgfTo _RH[obsdate]objectnnn _[chipname].fits files.

### Make the initial weight files before running SExtractor
```
python $gitdir/SuprimeCam/python/make_wht_for_swarp_1.py
```
Will create *_wht_init.fits files.

### Run SExtractor on the files
The number following the -P option gives the number of processors to run in parallel.

```
ls object*.fits | grep -v wht | xargs -I {} -P 20 python $gitdir/SuprimeCam/python/run_sext_scam_1.py {}
```

### Run scamp on the files
Use the deep r-band catalog that was generated in the previous reduction steps.

```
scamp object*cat -c scamp_scam_pass2.config -ASTREFCAT_NAME ../$basename'_'$deepband'.cat'
ls object*fits | grep -v wht > good_frames_pass1.txt
```

**Any objects with redlines in the scamp output?**
No bad frames.

*If there are any objects for which scamp fails to find an astrometric solution there are two options:*

1. Try running with a different astrometric reference catalog (e.g. SDSS-R5 instead of the default 2MASS)

	```
	scamp object*cat -c scamp_scam.config -ASTREF_CATALOG SDSS-R5
	```

2. Edit out any objects in the good_frames_pass1.txt file that had redlines in the scamp output and do without them in the final stack of this band.
	*Remove any objects with redlines from the good_frames_pass2.txt file.*

### Run the initial swarp to create a median-stacked coadd file
This median-stacked coadd will be used to create a mask for pixels in individual exposures that should be excluded from a final mean-stacked coadd (e.g. saturated bleeds, cosmic-ray, etc. pixels). Note we don't want to stop at this stage because the median-stacked image will have lower signal to noise than the mean-stacked image. This step is necessary to have a clean mean-stack.

_If this is the second pass then change good_frames_pass1.txt to good_frames_pass2.txt in the following command_

```
ln -s $gitdir/Suprimecam/Astromatic/swarp_scam_1.config .
swarp @good_frames_pass1.txt -c swarp_scam_1.config -CENTER_TYPE MANUAL -CENTER $fieldcenter
```

Creates swarp_median.fits and swarp_median_wht.fits, as well as a bunch of *resamp.fits images for each chip.

#### look at the images

```
ds9 -tile swarp_median.fits -scale log -scale limits 0 100 -zoom to fit swarp_median_wht.fits -scale linear -scale minmax -zoom to fit
```


### Make the updated weight maps
Compare the individual exposures with the median-stack from the previous step to identify outlier pixels that should be excluded from the mean-stack.

*** NB: The FLXSCAL paramter produced by scamp does the following:

 1. Converts the units of the output swarped file into counts/sec
 2. Adjusts the flux levels by an additional small amount to optimize the flux match between the images.

Note: The sigma clipping level has to be chosen.  For now, go with nsig=3. (the last argument on the line below)

```
python $gitdir/SuprimeCam/python/make_wht_for_swarp_2.py swarp_median.fits 2.
```

### Put the exposure time back into the individual resampled files
The exposure time was not transfered to the *resamp.fits images. We add this back here.

```
python $gitdir/SuprimeCam/python/add_exptime.py $EXPTIME
```

### Do the ultimate coadd
This coadd is slightly different from the previous swarp median-stack coadd; the differences are two fold:

1. COMBINE_TYPE is now WEIGHTED; producing a weighted mean stack.
2. RESAMPLE is now N; since we are building off the *resamp.fits fils from the previous resampling.

These changes are reflected in swarp_scam_2.config

```
ln -s $gitdir/Suprimecam/Astromatic/swarp_scam_2.config .
swarp *resamp.fits -c swarp_scam_2.config -CENTER_TYPE MANUAL -CENTER $fieldcenter
```

Creates swarp_wmean.fits and swarp_wmean_wht.fits.

#### look at the images

```
ds9 -tile swarp_wmean.fits -scale log -scale limits 0 100 -zoom to fit swarp_wmean_wht.fits -scale linear -scale mode minmax -zoom to fit
```

### Create the exposure time map

```
ln -s $gitdir/SuprimeCam/Astromatic/swarp_texp.config .
python $gitdir/SuprimeCam/python/make_texp_map.py $EXPTIME $fieldcenter
```
creates swarp_wmean_texp.fits.

### Fix header in final combined image
Correct the header information regarding exposure time and zero point.

*make sure correct zero point is input as second argument*

```
python $gitdir/SuprimeCam/python/fix_header_final.py swarp_wmean.fits $zp
```

### Run SExtractor on the final coadd, using a filter-specific config file
Using the deepest band as the detection band.

```
ln -s $gitdir/SuprimeCam/Astromatic/sext_scam_final.config .
python $gitdir/SuprimeCam/python/run_sext_final.py swarp_wmean.fits --detectfile ../$basename'_'$deepband'.fits'
```

Creates SExtractor catalog swarp_wmean.cat.

### Move the final files to parent folder
```
mv swarp_wmean.fits ../$basename'_'$band'.fits'
mv swarp_wmean_wht.fits ../$basename'_'$band'_wht.fits'
mv swarp_wmean.cat ../$basename'_'$band'.cat'
mv swarp_wmean.reg ../$basename'_'$band'.reg'
```
