"""
Simple code to just call the add_exptime function for a list of files
"""

import suprimecam_redux as scam
import glob
import sys

if len(sys.argv) < 2:
    print ''
    print 'ERROR: add_exptime.py requires one input parameter: the desired'
    print '  exposure time to add to the fits files.'
    print ''
    print 'Example: to add EXPTIME 120 to the files, type'
    print '   python add_exptime.py 120'
    print ''
    exit()

exptime = float(argv[1])
inlist = glob.glob('*resamp.fits')

scam.add_exptime(inlist,exptime)

