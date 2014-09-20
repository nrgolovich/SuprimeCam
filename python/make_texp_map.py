"""

Script to call the make_texp_map method in suprimecam_redux.py for all of
the resampled weight files and then swarp them all together into a
final exposure time map.

Usage: python make_texp_maps.py [root] [band] [texp]

Example for the observations of the 1608+656 field in the r-band where each
 input exposure is 300 seconds:

   python make_texp_maps.py 1608 r 300

"""

import glob
import suprimecam_redux as scam
import sys
import os

print len(sys.argv)

if len(sys.argv)<4:
    print ""
    print "ERROR: make_texp_maps.py requires three input parameters"
    print "  1. Root name for field"
    print "  2. Filter used for observations"
    print "  3. Exposure time in seconds for each of the input files"
    print ""
    print "For example, for observations of the 1608+656 field in the r-band"
    print "  where each input exposure is 300 seconds, type"
    print ""
    print "   python make_texp_map.py 1608 r 300"
    print ""
    exit()

infiles = glob.glob('object*resamp_wht.fits')
rootname = sys.argv[1]
obsband = sys.argv[2]
texp = float(sys.argv[3])

print ""
print "Making the exposure maps for the individual input files"
print "-------------------------------------------------------"
scam.make_texp_map(infiles,texp)

print ""
print "Using swarp to combine the individual files into the final exposure map"
print "-----------------------------------------------------------------------"
configfile = 'swarp_%s_texp.config' % rootname
if os.path.isfile(configfile) is False:
    print ""
    print 'ERROR: Missing the expected swarp configuration file: %s' % configfile
    print ''
    exit()
else:
    outfile = '%s_scam_mar14_%s_texp.fits' % (rootname,obsband)
    os.system('swarp *texp.fits -c %s -IMAGEOUT_NAME %s' % (configfile,outfile))
    print ''
    print 'Created output exposure time map: %s' % outfile
    print ''



