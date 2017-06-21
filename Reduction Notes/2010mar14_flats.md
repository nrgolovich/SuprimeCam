These are the commands used to create the sky flats for the V and i broadband images that I'm using to reduce the archival Subaru/SurpimeCam V and i images of Abell 781 from 2010-03-14 (V and i) and 2010-03-15 (V). I downloaded 500 exposures from the same observing program (including the ones from Abell 781, which we'll exlude)

The following are the list of files that should be used for creating skyflats. Note that I start off by listing all possible files for each band (not including the short 3 and 30 s exposures, since James recommends against using these), then I consider whether there are too many bright stars in each field.


|Cluster	| Use for skyflat? |
|-----------|--------------|
|ABELL0773  | yes |
|ZWCL0857	| yes |
|ABELL0963	| yes |
|ABELL0781	| no  |
|ABELL1423	| yes |

The raw data for the flats are stored in /sandbox/Subaru/flats/2010mar/rawdata, and the sdfred2 pipeline will be run in the directories named according to filter. 

#V band 

Will already made the flats for this filter. Note these are not the same as the raw data, so would need to remake using that data since we don't have the data anywhere.

# i-band

## Run SDFRED flat pipeline
### Link to the raw data

This will give 41 separate exposures for the skyflat which should be sufficient (after excluding the grayed out exposures).

```
cd /sandbox/Subaru/flats/2010mar/i/

ln -s ../rawdata/SUPA011* .
rm SUPA011968* SUPA011970*

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
rm H*
```
