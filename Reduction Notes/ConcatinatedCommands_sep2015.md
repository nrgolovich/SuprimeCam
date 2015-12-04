This file lists the commands for reducing the Subaru data in chuncks that can be copy and pasted. Breaks are at locations where user input/action is require.

Define the correct `$` parameters, e.g. `$basename` and `$deepband`.

## After linking to the raw data

```
ls -1 SUPA*.fits > namechange.lis
namechange.csh namechange.lis
ls -1 H*.fits > ovserscansub.lis
overscansub.csh ovserscansub.lis
ln -s ../../flats/2015sep/$band'/skyflat'*.fits .
ls -1 skyflat*.fits > ffield_mf.lis
ls -1 To_RH*.fits > ffield_im.lis
ffield.csh ffield_mf.lis ffield_im.lis
ls -1 fTo_RH*.fits > distcorr.lis
distcorr.csh distcorr.lis
ls -1 gfTo_RH*.fits > mask_AGX.lis
mask_AGX.csh mask_AGX.lis
ln -s $gitdir/SuprimeCam/Astromatic/sext_astfile.param .
ln -s $gitdir/SuprimeCam/Astromatic/sext_astfile_final.param .
ln -s $gitdir/SuprimeCam/Astromatic/sext_scam_astrom.config .
ln -s $gitdir/SuprimeCam/Astromatic/scamp_scam.config .
python $gitdir/SuprimeCam/python/rename_before_swarp.py
python $gitdir/SuprimeCam/python/make_wht_for_swarp_1.py
ls object*.fits | grep -v wht | xargs -I {} -P 20 python $gitdir/SuprimeCam/python/run_sext_scam_1.py {}
```

## if deep band

```
scamp object*cat -c scamp_scam.config
ls object*fits | grep -v wht > good_frames_pass1.txt
```

## else if shallow band

```
ln -s $gitdir/SuprimeCam/Astromatic/scamp_scam_pass2.config .
scamp object*cat -c scamp_scam_pass2.config -ASTREFCAT_NAME ../$basename'_'$deepband'.cat'
ls object*fits | grep -v wht > good_frames_pass1.txt
```


## Check if any of the exposures failed during scamp and edit good_frame_pass1.txt

```
ln -s $gitdir/Suprimecam/Astromatic/swarp_scam_1.config .
swarp @good_frames_pass1.txt -c swarp_scam_1.config -CENTER_TYPE MANUAL -CENTER $fieldcenter
ds9 -tile swarp_median.fits -scale log -scale limits 0 100 -zoom to fit swarp_median_wht.fits -scale linear -scale minmax -zoom to fit
```

## look at swarp images

```
python $gitdir/SuprimeCam/python/make_wht_for_swarp_2.py swarp_median.fits 2.
python $gitdir/SuprimeCam/python/add_exptime.py $EXPTIME
ln -s $gitdir/Suprimecam/Astromatic/swarp_scam_2.config .
swarp *resamp.fits -c swarp_scam_2.config -CENTER_TYPE MANUAL -CENTER $fieldcenter
ds9 -tile swarp_wmean.fits -scale log -scale limits 0 100 -zoom to fit swarp_wmean_wht.fits -scale linear -scale mode minmax -zoom to fit
```

## look at swarp images

## If deep detection band:

```
ln -s $gitdir/SuprimeCam/Astromatic/swarp_texp.config .
python $gitdir/SuprimeCam/python/make_texp_map.py $EXPTIME $fieldcenter
python $gitdir/SuprimeCam/python/fix_header_final.py swarp_wmean.fits $zp
ln -s $gitdir/SuprimeCam/Astromatic/sext_scam_final.config .
python $gitdir/SuprimeCam/python/run_sext_final.py swarp_wmean.fits
mv swarp_wmean.fits ../$basename'_'$band'.fits'
mv swarp_wmean_wht.fits ../$basename'_'$band'_wht.fits'
mv swarp_wmean.cat ../$basename'_'$band'.cat'
mv swarp_wmean.reg ../$basename'_'$band'.reg'
```

## If shallow photometry band

```
ln -s $gitdir/SuprimeCam/Astromatic/swarp_texp.config .
python $gitdir/SuprimeCam/python/make_texp_map.py $EXPTIME $fieldcenter
python $gitdir/SuprimeCam/python/fix_header_final.py swarp_wmean.fits $zp
ln -s $gitdir/SuprimeCam/Astromatic/sext_scam_final.config .
python $gitdir/SuprimeCam/python/run_sext_final.py swarp_wmean.fits --detectfile ../$basename'_'$deepband'.fits'
mv swarp_wmean.fits ../$basename'_'$band'.fits'
mv swarp_wmean_wht.fits ../$basename'_'$band'_wht.fits'
mv swarp_wmean.cat ../$basename'_'$band'.cat'
mv swarp_wmean.reg ../$basename'_'$band'.reg'
```
