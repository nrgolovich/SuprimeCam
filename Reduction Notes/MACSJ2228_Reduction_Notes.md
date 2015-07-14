These are the Subaru SuprimeCam reduction notes. The

```
code blocks
```
are meant to be copied in to the terminal commandline.

It is recommended that you start with your deepest band first, as some of reduction outputs can help with the reduction of the other bands (e.g. using the stacked catalog as input to scamp).

This reduction is run with the following versions:

* sdfred20100528
* scamp 1.3.11 (note that 2.0.4 has a bug that causes poor solutions at the periphery of the field)
* swarp 2.38.0
* https://github.com/MCTwo/SuprimeCam commit:ef0a506
* https://github.com/MCTwo/CodeCDF commit:8b5c009

### Prepend the PATH with the old version of SDFRED
Since all of this data is archival data taken before 2008 we will need to use sdfred1 by prepending its bin to the PATH.

```
export PATH="/usr/local/sdfred20100528_mf1/bin:$PATH"
```

### Setup the folder architecture and cluster specific inputs
```
cd /sandbox/Subaru/
mkdir macsj2228
cd macsj2228
mkdir R B V I z
```

Define the base name for result reduced files (e.g. short name of the cluster).

```
basename=macsj2228
```

Define the deepest band. Reduction should start with this band as some of it files may be used in the reduction of the other bands.

```
deepband=R
```

Define the ra,dec of the center of the field (degrees). This will ensure similar image properties for all bands.

```
fieldcenter=337.140,20.62
```

# R
Go to the VR directory and specify band name.

```
cd R
band=R
```

Define the exposure time for the individual exposures in seconds.

```
EXPTIME=240
```

Define the zero point for this band.

```
zp=0
```
## SDFRED Reduction Portion
This portion of the pipeline uses SDFRED and the proceedure documented in its [manual](http://www.naoj.org/Observing/Instruments/SCam/sdfred/v2.0/sdfred2_2p1ae.pdf).

### Link to the raw data
Range from SUPA00232340 to SUPA00232429
2003-July-27
```
ln -s ../../rawdata/2003jul27/SUPA002323[4-9]?.fits .
ln -s ../../rawdata/2003jul27/SUPA002324[0-2]?.fits .
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
The flat field images were download from JVO.

```
ln -s ../../flats/2003jul/$band'/skyflat'*.fits .
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
One bad exposure:
object020_w9c2.cat A9  P1  -3.50 deg  0.2024"   1.07     -39."    -28."  0.819
removed from good_frames_pass1.txt
I tried matching against SDSS since A115 is within the survey but the old version of scamp doesn't give the option of DR > 5 and I guess A115 hadn't been observed yet.

*If there are any objects for which scamp fails to find an astrometric solution there are two options:*

1. Try running with a different astrometric reference catalog (e.g. SDSS-R5 instead of the default 2MASS)

	```
	scamp object*cat -c scamp_scam.config -ASTREF_CATALOG SDSS-R5
	```

2. Edit out any objects in the good_frames_pass1.txt file that had redlines in the scamp output. Then run through the following steps up to and through running SExtractor on the second swarp coadd, use this catalog as ASTREFCAT_NAME input in the scamp.config file, and repeat all of the following steps a second time.

	```
	ln -s $gitdir/SuprimeCam/Astromatic/scamp_scam_pass2.config .
	scamp object*cat -c scamp_scam_pass2.config -ASTREFCAT_NAME ../$basename'_'$deepband'.cat'
	ls object*fits | grep -v wht | grep -v resamp > good_frames_pass2.txt
	```
	*Remove any objects with redlines from the good_frames_pass2.txt file.*
	after second pass everyting worked

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
ds9 -tile swarp_median.fits -scale log -scale limits 0 50 -zoom to fit swarp_median_wht.fits -scale linear -scale minmax -zoom to fit
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
ds9 -tile swarp_wmean.fits -scale log -scale limits 0 50 -zoom to fit swarp_wmean_wht.fits -scale linear -scale mode minmax -zoom to fit
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

# B (2007Aug13)
Note that there were V-band observations take on 2003sep25 (18 minutes total) and on 2005oct03 (7.5 minutes total).

Go to the B directory and specify band name.

```
cd ../B
band=B
```

Define the exposure time for the individual exposures in seconds.

```
EXPTIME=180
```

Define the zero point for this band.

```
zp=0
```

## SDFRED Reduction Portion
This portion of the pipeline uses SDFRED and the proceedure documented in its [manual](http://www.naoj.org/Observing/Instruments/SCam/sdfred/v2.0/sdfred2_2p1ae.pdf).

### Link to the raw data
Thesefile range from SUPA00562030 to SUPA00562109.


```
ln -s ../../rawdata/2007aug13/SUPA005620[3-9]?.fits .
ln -s ../../rawdata/2007aug13/SUPA0056210?.fits .
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
The flat field images were created using the proceedure outlined in [2014A_Flats.md](https://github.com/MCTwo/SuprimeCam/blob/master/Reduction%20Notes/2014A_Flats.md).

_make sure to change path to correct filter_

```
ln -s ../../flats/2007aug/$band'/skyflat'*.fits .
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
This actually failed three frames so I tried:

```
scamp object*cat -c scamp_scam.config
ls object*fits | grep -v wht > good_frames_pass1.txt
```
and all frames passed.

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

# V (2006Jun25)

Go to the V directory and specify band name.

```
cd ../V
band=V
```

Define the exposure time for the individual exposures in seconds.

```
EXPTIME=240
```

Define the zero point for this band.

```
zp=0
```

## SDFRED Reduction Portion
This portion of the pipeline uses SDFRED and the proceedure documented in its [manual](http://www.naoj.org/Observing/Instruments/SCam/sdfred/v2.0/sdfred2_2p1ae.pdf).

### Link to the raw data
Thesefile range from SUPA00487380 to SUPA00487459.


```
ln -s ../../rawdata/2006jun25/SUPA004873[8-9]?.fits .
ln -s ../../rawdata/2006jun25/SUPA004874[0-5]?.fits .
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
The flat field images were created using the proceedure outlined in [2014A_Flats.md](https://github.com/MCTwo/SuprimeCam/blob/master/Reduction%20Notes/2014A_Flats.md).

_make sure to change path to correct filter_

```
ln -s ../../flats/2006jun/$band'/skyflat'*.fits .
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
This actually failed three frames so I tried:

```
scamp object*cat -c scamp_scam.config
ls object*fits | grep -v wht > good_frames_pass1.txt
```
and all frames passed.

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

# I (2004Jul19)

Go to the I directory and specify band name.

```
cd ../I
band=I
```

Define the exposure time for the individual exposures in seconds.

```
EXPTIME=180
```

Define the zero point for this band.

```
zp=0
```

## SDFRED Reduction Portion
This portion of the pipeline uses SDFRED and the proceedure documented in its [manual](http://www.naoj.org/Observing/Instruments/SCam/sdfred/v2.0/sdfred2_2p1ae.pdf).

### Link to the raw data
Thesefile range from SUPA00330440 to SUPA00330529.

```
ln -s ../../rawdata/2004jul19/SUPA003304[4-9]?.fits .
ln -s ../../rawdata/2004jul19/SUPA003305[0-2]?.fits .
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
The flat field images were created using the proceedure outlined in [2014A_Flats.md](https://github.com/MCTwo/SuprimeCam/blob/master/Reduction%20Notes/2014A_Flats.md).

_make sure to change path to correct filter_

```
ln -s ../../flats/2004jul/$band'/skyflat'*.fits .
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
This actually failed three frames so I tried:

```
scamp object*cat -c scamp_scam.config
ls object*fits | grep -v wht > good_frames_pass1.txt
```
and all frames passed.

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

# z (2007Jul18)

Go to the I directory and specify band name.

```
cd ../z
band=z
```

Define the exposure time for the individual exposures in seconds.

```
EXPTIME=180
```

Define the zero point for this band.

```
zp=0
```

## SDFRED Reduction Portion
This portion of the pipeline uses SDFRED and the proceedure documented in its [manual](http://www.naoj.org/Observing/Instruments/SCam/sdfred/v2.0/sdfred2_2p1ae.pdf).

### Link to the raw data
Thesefile range from SUPA00557410 to SUPA00557509.


```
ln -s ../../rawdata/2007jul18/SUPA005574[1-9]?.fits .
ln -s ../../rawdata/2007jul18/SUPA0055750?.fits .
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
The flat field images were created using the proceedure outlined in [2014A_Flats.md](https://github.com/MCTwo/SuprimeCam/blob/master/Reduction%20Notes/2014A_Flats.md).

_make sure to change path to correct filter_

```
ln -s ../../flats/2007jul/$band'/skyflat'*.fits .
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
This actually failed three frames so I tried:

```
scamp object*cat -c scamp_scam.config
ls object*fits | grep -v wht > good_frames_pass1.txt
```
and all frames passed.

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
