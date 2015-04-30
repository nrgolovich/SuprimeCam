I am using ZwCL1447 since it falls within the SDSS footprint and doesn't suffer from highly variable galactic dust reddening. While there is one bright star in the field it is not as bad as some of the other overlapping SDSS fields.

## Reduce the g, r, z images
Run throught he reduction notes zwcl1447_Reduction_Notes.md with specifying a zero point of 0 during the "Fix header in final combined image" step near the end of the reduction.

## Match the SDSS and Subaru catalogs

Using the SExtractor catalogs generated from the final coadd of the reduction I matched them to the SDSS star catalog ZwCL1447_SDSSstars.csv which includes all SDSS stars withing a 20' radius of the field center and their magnitdes (u, gu, r, i, z). The matching was done using TopCat spatial matching based on RA, Dec of each catalog.

## Estimate Zero Point based on median color

Then in the ZeroPoint Estimate.ipynb I deterined the median difference between the SDSS and Subaru bands over a reasonable magnitude range to estimate the following zero points. (which agree to within ~0.01 mags with Chris' estimates from a few nights later.)



Results:
---------

band |  ZP
-----|------
g    | 27.368
r    | 27.683
i    | 27.573
 