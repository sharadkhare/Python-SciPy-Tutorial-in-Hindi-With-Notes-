# Scipy matlab Arrays: Exporting the data in Matlab format
# for converting or export data we use savemat(). here we have 3 parameters: filename, mdict, do_compression.
# example : here now we will export the below array as variable name "vec" to mat file.
from scipy import io 
import numpy as np
sharad = np.arange(10)
io.savemat('sharad.mat', {"vec": sharad})

# here now we will import the existing mat file. it have only 1 parameter that is filename:

from scipy import io 
import numpy as np
sharad = np.array([0,1,2,3,4,5,6,7,8,9])
#Export
io.savemat('sharad.mat', {"vec": sharad})
#import
sharadnew = io.loadmat('sharad.mat', squeeze_me = True)
print(sharadnew['vec'])
