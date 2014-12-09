#!/bin/tcsh
#
# Runs the final swarp to combine the files
#

# Check the command line
if ( $# < 2) then
    echo ""
    echo "run_final_swarp.sh"
    echo ""
    echo " Usage: run_final_swarp.sh [lens_root] [band]"
    echo ""
    echo "run_final_swarp requires 2 inputs:"
    echo "  1. the lens root, e.g., 0435"
    echo "  2. the observing band, e.g., r"
    echo ""
    echo "For example, if lens_root=0435 and band=r then the script will"
    echo "  * look for input config file swarp_0435_2.config" 
    echo "  * create two output files:"
    echo "      0435_scam_mar14_r.fits "
    echo "      0435_scam_mar14_r_wht.fits"
    echo ""
    exit
endif

# Set up the files needed to run swarp
set sconfig = swarp_$1_2.config
set outname = $1_scam_mar14_$2.fits
set whtname = $1_scam_mar14_$2_wht.fits

# Check for the existence of the input files
echo ""
echo "Checking for existence of input file for run_final_swarp.sh"
echo "-----------------------------------------------------------"
set existerr = 0
foreach i ($sconfig)
   if(! -e $i) then
      echo " ERROR: $i does not exist."
      set existerr = 1
   else
      echo " Found $i"
   endif
end
if ($existerr) then
   echo ""
   echo "Exiting script"
   echo ""
   exit
endif

# Actually run swarp
swarp *resamp.fits -c $sconfig -IMAGEOUT_NAME $outname -WEIGHTOUT_NAME $whtname

echo ""
