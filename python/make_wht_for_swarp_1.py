"""
Makes the input _wht files for running pass 1 of swarp, in which the
median-stacked image is created.
"""

import suprimecam_redux as sc
import glob

infiles = glob.glob('object*.fits')

sc.make_wht_for_swarp(infiles, mingood=510)
