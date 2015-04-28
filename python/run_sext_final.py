'''
A script that runs SExtractor on the final combined images.
'''
import pyfits as pf
import sys
import os
import argparse

parser = argparse.ArgumentParser(description='This script is intended to be run as part of the Subaru SuprimeCam reduction pipeline. It generates a SExtractor catalog for the final stacked image. If two files are specified then SExtractor is run in Dual Image Mode with the first is used as the detection image and the second as the photometry image.')

parser.add_argument('fitsfile', type=str, default='swarp_wmean.fits',
                    help='The name of the weighted mean stacked fits image. If --detectfile None the this image will be used for both detection and photometry, else it will only be use for photometry (Default: swarp_wmean.fits)')
parser.add_argument('-c','--configfile', type=str, default='sext_scam_final.config',
                    help='Name of SExtractor configuration file (Default: sext_scam_final.config).')
parser.add_argument('--detectfile', type=str, default=None,
                    help='The name of the weighted mean stacked fits image that is to be used as the detection image (Default: None).')

args = parser.parse_args()

imgfile = args.fitsfile
whtfile = imgfile.replace('.fits','_wht.fits')
regfile = imgfile.replace('.fits','.reg')
outcat = imgfile.replace('.fits','.cat')

if args.detectfile != None:
    detect_imgfile = args.detectfile
    detect_whtfile = detect_imgfile.replace('.fits','_wht.fits')
else:
    detect_imgfile = None
    detect_whtfile = None    

config = args.configfile

# Check for zeropoint in fits file header
try:
    hdr = pf.getheader(scifile)
except:
    print ''
    print 'ERROR: Could not open header for fits file %s' % imgfile
    print ''
    exit()
try:
    zeropoint = hdr['magzpt']
except:
    print ''
    print 'ERROR: Could not get zeropoint in header for fits file %s' % imgfile
    print ''
    del hdr
    exit()
del hdr

# Summarize this information
print ''
print 'SExtractor input parameters'
print '-------------------------------------------------------'
print 'Photometry file:        %s' % imgfile
print 'Photometry weight file: %s' % whtfile
print 'Detection file:         %s' % detect_imgfile
print 'Detection weight file:  %s' % detect_whtfile
print 'Output catalog:         %s' % catfile
print 'Regions file:           %s' % regfile
print 'Config file:            %s' % configfile
print 'Zeropoint:              %6.3f' % zeropoint
print ''

def make_sexcat(imgfile, outcat='tmp.cat', configfile='sext_scam.config', 
                whtfile=None, weight_type='MAP_WEIGHT',
                detectfile=None, detect_whtfile=None, 
                detect_weight_type='MAP_WEIGHT', regfile=None,
                ncoadd=1, satur=50000., zeropt=None, catformat='ldac',
                flag_file=None, det_thresh=-1, det_area=-1, seeing=0.0,
                logfile=None, verbose=True):
    # get the gain and exposure time of the photomety image
    hdr = pf.getheader(imgfile)
    try:
        gain = hdr['gain']
    except:
        gain = 1.0
    try:
        texp = hdr['exptime']
    except:
        texp = 1.0
    if verbose:
        print ""
        print "File: %s has gain=%6.3f and t_exp = %7.1f" % (imgfile,gain,texp)
    
    # Set up the gain and format of the output catalog (default is LDAC)
    if catformat.lower() == 'ascii':
        cattype = 'ASCII_HEAD'
    else:
        cattype = 'FITS_LDAC'
    gain_eff = gain * texp * ncoadd
    
    # Prepare other parameters
    satur_eff = satur * ncoadd
    
    # Prepare the optional portions of the call to SExtractor
    sopts = '-GAIN %f -CATALOG_NAME %s -CATALOG_TYPE %s -SATUR_LEVEL %f ' %\
        (gain_eff,outcat,cattype,satur_eff)
    if det_area>0:
        sopts += '-DETECT_MINAREA %d ' % det_area
    if det_thresh>0.:
        sopts += '-DETECT_THRESH %5.2f -ANALYSIS_THRESH %5.2f ' \
            % (det_thresh,det_thresh)
    if zeropt is not None:
        sopts += '-MAG_ZEROPOINT %5.2f ' % zeropt
    if seeing>0.0:
        sopts += '-SEEING_FWHM %6.3f ' % seeing
    # specify weight file and handle correctly for dual band mode
    if whtfile is None and detect_whtfile is None:
        sopts += '-WEIGHT_TYPE NONE '
    elif whtfile is not None and detect_whtfile is None:    
        sopts += '-WEIGHT_TYPE %s -WEIGHT_IMAGE %s ' % (weight_type,whtfile)
    elif whtfile is not None and detect_whtfile is not None:
        sopts += '-WEIGHT_TYPE {0},{1} -WEIGHT_IMAGE {2},{3} '.format(weight_type, detect_weight_type, whtfile, detect_whtfile)
    else:
        print 'Error: specified detect_whtfile without whtfile, exiting.'
        sys.exit()
        
    if weight_thresh is not None:
        sopts += '-WEIGHT_THRESH %9.2f ' % weight_thresh
    if flag_file is not None:
        sopts += '-FLAG_IMAGE %s ' % flag_file
    if verbose is False:
        sopts += '-VERBOSE_TYPE QUIET '
    
    # Run SExtractor
    print "length of fitsfile = {0}".format(len(fitsfile))
    if verbose:
        print ""
        if detectfile is None:
            print "Running SExtractor in single band mode on {0}".format(imgfile)
        else:
            print "Running SExtractor in dual band mode with:"
            print "    {0} as the detection band".format(detectfile)
            print "    {0} as the photometry band".format(imgfile)
        print "Configuration file: %s" % configfile
        print "Override variables:"
        print sopts
        print ""    
        
    if detectfile is None:
        # run in single band mode
        if logfile is None:
            try:
                os.system('sex {0} -c {1} {2}'.format(imgfile,
                                                      configfile,sopts))
            except:
                print ""
                print "ERROR.  Could not run SExtractor on %s" % imgfile
                print ""
                return
        else:
            try:
                os.system('sex {0} -c {1} {2} > {3}'.format(imgfile,
                                                            configfile,sopts,
                                                            logfile))
            except:
                print ""
                print "ERROR.  Could not run SExtractor on %s" % fitsfile
                print ""
                return
    elif detectfile is not None:
        # run in dual band mode
        if logfile is None:
            try:
                os.system('sex {0},{1} -c {2} {3}'.format(detectfile,
                                                          imgfile,
                                                          configfile,sopts))
            except:
                print ""
                print "ERROR.  Could not run SExtractor on %s" % fitsfile
                print ""
                return
        else:
            try:
                os.system('sex {0},{1} -c {2} {3} > {4}'.format(detectfile,
                                                                imgfile,
                                                                configfile,
                                                                sopts,
                                                                logfile)) 
            except:
                print ""
                print "ERROR.  Could not run SExtractor on %s" % fitsfile
                print ""
                return

    if verbose:
        print ""
        if detectfile is None:
            print "Ran SExtractor in single band mode on %s to produce output catalog %s" % \
                  (fitsfile,outcat)
        else:
            print "Ran SExtractor in dual band mode with:"
            print "    {0} as the detection band".format(detectfile)
            print "    {0} as the photometry band".format(imgfile)
            print "to produce output catalog {0}".format(outcat)  
    
    if regfile is not None:
        import catfuncs
        if verbose:
            print "Creating ds9 regions file %s from SExtractor catalog." % regfile
        if catformat=='ascii':
            if racol is None:
                racol = 1
                namecol = 0
            if deccol is None:
                deccol = 2
                namecol = 0
            tmpcat = catfuncs.Secat(outcat,catformat,racol=racol,deccol=deccol,
                                    namecol=namecol)
        else:
            tmpcat = catfuncs.Secat(outcat,catformat)
        tmpcat.make_reg_file(regfile,fluxcol,fluxerrcol)
        #make_reg_file(outcat,regfile,catformat)
    if verbose:
        print ""

# call the make_sexcat function with user inputs
make_sexcat(imgfile, outcat=catfile, configfile=configfile, 
            whtfile=whtfile, weight_type='MAP_WEIGHT',
            detectfile=detect_imgfile, detect_whtfile=detect_whtfile, 
            detect_weight_type='MAP_WEIGHT', regfile=regfile,
            ncoadd=1, satur=50000., zeropt=zeropoint, catformat='ldac',
            flag_file=None, det_thresh=-1, det_area=-1, seeing=0.0,
            logfile=None, verbose=True)