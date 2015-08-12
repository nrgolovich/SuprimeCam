The reduction process produces a large number of files:
* ~35 Gb per lensing band
* ~18 Gb per photometry band

Many of these can be deleted without much information loss. It is important to
keep the files generated in the final step of the reduction, and if lensing
shapes are going to be measured then it is also important to keep the final
scamp files for the individual chips and exposures (`*.resamp.fits`, and
`*.resamp_wht.fits`).
Of course the raw files should also be kept!

The following commands remove the unnecessary files.

```
rm AgfTo*.fits
rm gfTo*.fits
rm fTo*.fits
rm To*.fits
rm object*.cat
rm object*.reg
rm object*.head
rm object*.texp.fits
rm object*.weight.fits
rm object*wht_init.fits
rm swarp_median.fits
rm swarp_median_wht.fits
rm swarp_wmean_texp.fits
rm texp_wht.fits
rm tmp
```
