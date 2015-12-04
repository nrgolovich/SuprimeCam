I am using ZwCL2120 since it falls partially within the SDSS footprint and of
of the three clusters observed that fall within SDSS it was the one least
affected by the technical guiding issues that plagued several of the clusters
throughout the night.

## Reduce the g, r
Run throught he reduction notes zwcl2120_Reduction_Notes.md with specifying a
zero point of 0 during the "Fix header in final combined image" step near the
end of the reduction.

## Match the SDSS and Subaru catalogs

Using the SExtractor catalogs generated from the final coadd of the reduction I
matched them to the SDSS star catalog, type=6 objects in ZwCL2120_SDSS_Cat.csv,
which includes all SDSS stars withing a 20' radius of the field center and their
magnitdes (u, gu, r, i, z). The matching was done using TopCat spatial matching
based on RA, Dec of each catalog.
## Estimate Zero Point based on median color

Then in the ../python/ZeroPoint Estimate_2015sep.ipynb I determined the median
difference between the SDSS and Subaru bands over a reasonable magnitude range
to estimate the following zero points.
Results:
---------

band |  ZP
-----|------
g    | 27.227
r    | 27.488
