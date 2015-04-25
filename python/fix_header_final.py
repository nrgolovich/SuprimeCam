import suprimecam_redux as scam
import sys
'''
Corrects the header information regarding zeropoint and exposure time.
'''
scifile = sys.arg[1]
zeropt = float(sys.argv[2])
texpfile = scifile.replace('.fits','_texp.fits')
scam.fix_final_headers(scifile,texpfile,zeropt)