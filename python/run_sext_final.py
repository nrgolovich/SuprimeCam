"""

Script to run SExtractor on the final combined image

Usage: python run_sext_final.py [scifile] ([config_file])

Example for the observations of the 1608+656 field in the r-band

   python run_sext_final.py 1608_scam_mar14_r.fits

"""

import sys
import pyfits as pf
import astromatic as astrom

if len(sys.argv)<2:
    print ""
    print "ERROR: run_sext_final.py requires at least one input parameter"
    print "  1. Filename for final coadded data, e.g., 1608_scam_mar14_r.fits"
    print "  2. [OPTIONAL] name of configuration file.  This is only needed"
    print "     if the file is something other than sext_scam_final.config"
    print ""
    print "For example, for observations of the 1608+656 field in the r-band"
    print ""
    print "   python run_sext_final.py 1608_scam_mar14_r.fits"
    print ""
    exit()

""" Set up the filenames """
scifile = sys.argv[1]
catfile = scifile.replace('fits','cat')
regfile = scifile.replace('fits','reg')
whtfile = scifile.replace('.fits','_wht.fits')
if len(sys.argv) > 2:
    configfile = sys.argv[2]
else:
    configfile = 'sext_scam_final.config'

""" Check for zeropoint in fits file header """
try:
    hdr = pf.getheader(scifile)
except:
    print ''
    print 'ERROR: Could not open header for fits file %s' % scifile
    print ''
    exit()
try:
    zeropoint = hdr['magzpt']
except:
    print ''
    print 'ERROR: Could not get zeropoint in header for fits file %s' % scifile
    print ''
    del hdr
    exit()
del hdr

""" Summarize input information """
print ''
print 'SExtractor input parameters'
print '-------------------------------------------------------'
print 'Science file:   %s' % scifile
print 'Weight file:    %s' % whtfile
print 'Output catalog: %s' % catfile
print 'Regions file:   %s' % regfile
print 'Config file:    %s' % configfile
print 'Zeropoint       %6.3f' % zeropoint
print ''

""" Actually run SExtractor """
astrom.make_cat_suprimecam(scifile,catfile,regfile,configfile=configfile,whtfile=whtfile,zeropt=zeropoint)
