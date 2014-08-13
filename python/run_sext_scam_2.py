import astromatic as ast
import sys

if len(sys.argv)<3:
    print ''
    print 'ERROR: run_sext_scam_2.py requires 2 parameters:'
    print '    1. Input science fits filename'
    print '    2. Zero point'
    print ''
    print 'Example:  python run_sext_scam_2.py 0435_scam_mar14_r.fits 27.685'
    print ''
    exit()

infile = sys.argv[1]
zeropoint = float(sys.argv[2])
whtfile = infile.replace('.fits','_wht.fits')
regfile = infile.replace('.fits','.reg')
outcat  = infile.replace('.fits','.cat')
configfile = 'sext_scam_final.config'
print 'Running SExtractor on %s' % infile

ast.make_cat_suprimecam(infile,outcat=outcat,regfile=regfile,
                        configfile=configfile,weight_file=whtfile,
                        zeropt=zeropoint)

