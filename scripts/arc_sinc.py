# arc_sinc.py
# Tracy Whelen, Microwave Remote Sensing Lab, University of Massachusetts
# June 4, 2015

# This is the python version of arc_sinc.m, which calculates the inverse sinc function.

#!/usr/bin/python
from numpy import *
from math import *
from scipy import interpolate
import numpy as np

# define arc_sinc function
def arc_sinc(x, c_param):
    # Get rid of extreme values by set all values where x > 1 equal to 1, and x < 0 equal to 0 
    x[(x > 1)] = 1
    x[(x < 0)] = 0

    # Create array of increments between 0 and pi of size pi/100
    XX = linspace(0, math.pi, num=100, endpoint=True)

    # Set the first value of XX to eps to avoid division by zero issues -> Paul's suggestion
    XX[0] = spacing(1)

    # Calculate sinc for XX and save it to YY
    ## YY = sinc(XX / math.pi)
    YY = np.sin(XX) / XX

    # Reset the first value of XX to zero and the first value of YY to the corresponding output
    XX[0] = 0
    YY[0] = 1
    
    # Set the last value of YY to 0 to avoid NaN issues
    YY[-1] = 0

    # Flip XX and YY left to right
    XX = XX[::-1]
    YY = YY[::-1]
    
#    XX = array([ 3.14159265,  3.10985939,  3.07812614,  3.04639288,  3.01465962, 2.98292636,  2.9511931 ,  2.91945984,  2.88772658,  2.85599332, 2.82426006,  2.7925268 ,  2.76079354,  2.72906028,  2.69732703, 2.66559377,  2.63386051,  2.60212725,  2.57039399,  2.53866073, 2.50692747,  2.47519421,  2.44346095,  2.41172769,  2.37999443, 2.34826118,  2.31652792,  2.28479466,  2.2530614 ,  2.22132814, 2.18959488,  2.15786162,  2.12612836,  2.0943951 ,  2.06266184, 2.03092858,  1.99919533,  1.96746207,  1.93572881,  1.90399555, 1.87226229,  1.84052903,  1.80879577,  1.77706251,  1.74532925, 1.71359599,  1.68186273,  1.65012947,  1.61839622,  1.58666296, 1.5549297 ,  1.52319644,  1.49146318,  1.45972992,  1.42799666, 1.3962634 ,  1.36453014,  1.33279688,  1.30106362,  1.26933037, 1.23759711,  1.20586385,  1.17413059,  1.14239733,  1.11066407, 1.07893081,  1.04719755,  1.01546429,  0.98373103,  0.95199777, 0.92026451,  0.88853126,  0.856798  ,  0.82506474,  0.79333148, 0.76159822,  0.72986496,  0.6981317 ,  0.66639844,  0.63466518, 0.60293192,  0.57119866,  0.53946541,  0.50773215,  0.47599889, 0.44426563,  0.41253237,  0.38079911,  0.34906585,  0.31733259, 0.28559933,  0.25386607,  0.22213281,  0.19039955,  0.1586663 , 0.12693304,  0.09519978,  0.06346652,  0.03173326,  0.        ])
#    YY = array([ 0.        ,  0.01020237,  0.02060472,  0.03120282,  0.04199229, 0.05296859,  0.06412703,  0.07546277,  0.08697083,  0.09864608, 0.11048326,  0.12247694,  0.1346216 ,  0.14691157,  0.15934105, 0.17190411,  0.18459472,  0.19740671,  0.21033383,  0.22336969, 0.23650781,  0.24974161,  0.26306441,  0.27646944,  0.28994984, 0.30349868,  0.31710894,  0.33077352,  0.34448527,  0.35823696, 0.37202131,  0.38583098,  0.39965857,  0.41349667,  0.42733779, 0.44117444,  0.45499906,  0.46880411,  0.48258199,  0.49632512, 0.51002589,  0.52367669,  0.53726993,  0.55079798,  0.56425328, 0.57762824,  0.59091533,  0.60410701,  0.6171958 ,  0.63017424, 0.64303494,  0.65577053,  0.66837371,  0.68083722,  0.69315389, 0.7053166 ,  0.7173183 ,  0.72915204,  0.74081093,  0.75228819, 0.76357711,  0.77467109,  0.78556364,  0.79624836,  0.80671897, 0.81696931,  0.82699334,  0.83678514,  0.84633891,  0.85564901, 0.8647099 ,  0.87351622,  0.88206272,  0.89034433,  0.8983561 , 0.90609326,  0.91355119,  0.92072543,  0.92761169,  0.93420585, 0.94050396,  0.94650224,  0.95219709,  0.9575851 ,  0.96266301, 0.96742778,  0.97187655,  0.97600663,  0.97981554,  0.98330097, 0.98646084,  0.98929323,  0.99179643,  0.99396894,  0.99580945, 0.99731683,  0.99849018,  0.9993288 ,  0.99983218,  1.        ])
    
    # Run interpolation
    # XX and YY are your original values, x is the query values, and y is the interpolated values that correspond to x
    interp_func = interpolate.interp1d(YY, XX * c_param, kind='slinear') 
    y = interp_func(x)

    # Set all values in y less than 0 equal to 0
    y[(y < 0)] = 0
    # return y
    return y
