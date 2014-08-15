import astromatic as ast
import sys

infile = sys.argv[1]
whtfile = infile.replace('.fits','_wht_init.fits')
regfile = infile.replace('.fits','.reg')
outcat = infile.replace('.fits','.cat')
print 'Running SExtractor on %s' % infile

ast.make_cat_suprimecam(infile,outcat=outcat,regfile=regfile,weight_file=whtfile,
                        configfile='sext_scam_astrom.config',satur=60000.)

