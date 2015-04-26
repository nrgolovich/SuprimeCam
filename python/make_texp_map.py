"""

Script to call the make_texp_map method in suprimecam_redux.py for all of
the resampled weight files and then swarp them all together into a
final exposure time map.

Usage: python make_texp_map.py [root] [band] [texp]

Example for the observations of the 1608+656 field in the r-band where each
 input exposure is 300 seconds:

   python make_texp_map.py 1608 r 300

"""

import glob
import suprimecam_redux as scam
import ccdredux
import sys
import os

print len(sys.argv)

if len(sys.argv)<2:
    print ""
    print "ERROR: make_texp_map.py requires one input parameters"
    print "  1. Exposure time in seconds for each of the input files"
    print ""
    print "For example, "
    print "   python make_texp_map.py 300"
    print ""
    exit()

infiles = glob.glob('object*resamp_wht.fits')
texp = float(sys.argv[1])

print ""
print "Making the exposure maps for the individual input files"
print "-------------------------------------------------------"
ccdredux.make_texp_map(infiles,texp)

print ""
print "Using swarp to combine the individual files into the final exposure map"
print "-----------------------------------------------------------------------"
configfile = 'swarp_texp.config'
if os.path.isfile(configfile) is False:
    print ""
    print 'ERROR: Missing the expected swarp configuration file: %s' % configfile
    print ''
    exit()
else:
    outfile = 'swarp_wmean_texp.fits'
    os.system('swarp *texp.fits -c %s -IMAGEOUT_NAME %s' % (configfile,outfile))
    print ''
    print 'Created output exposure time map: %s' % outfile
    print ''



