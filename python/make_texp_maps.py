"""
Script to call the make_texp_map method in suprimecam_redux.py for all of
the resampled weight files

Usage: python make_texp_maps.py [texp]

Example:  python make_texp_maps.py 300
 for a series of 300 sec exposures
"""

import glob
import suprimecam_redux as scam
import sys

if len(sys.argv)<2:
    print ""
    print "ERROR: make_texp_maps.py requires one input parameter"
    print "  1. Exposure time in seconds for each of the input files"
    print ""
    return

infiles = glob.glob('object*resamp_wht.fits')
texp = float(argv[1])

scam.make_texp_map(infiles,texp)

