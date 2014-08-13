import astromatic as ast
import sys

infile = sys.argv[1]
regfile = infile.replace('.fits','.reg')
outcat = infile.replace('.fits','.cat')
print 'Running SExtractor on %s' % infile

ast.make_cat_suprimecam(infile,outcat=outcat,regfile=regfile,
                        configfile='sext_scam_astrom.config',satur=60000.)

