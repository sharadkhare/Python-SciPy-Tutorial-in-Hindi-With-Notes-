# What is sparse data: Sparse data is the data that has mostly unused elements. like the elements that dont carry any info. [1,0,2,0,4,5,6,9,2,4]
# sparse data example [1,0,2,0,0,3,0,0,0,0,0,4]
# Dense Array: [2,5,6,8,9,7,1,2,3,6]
# How to work with Sparse Data.
# scipy has a module scipy.sparse function. there are 2 matrics in this sparse: CSC(Compressed sparse Column) and CSR(Commpresses Sparse Row)

# CSR Matrics: here we will create a CSR matrics from an array:

import numpy as np
from scipy.sparse import csr_matrix
sharad = np.array([0,0,0,0,0,1,1,0,2])
print(csr_matrix(sharad))

# Sparse matrix Methods
import numpy as np
from scipy.sparse import csr_matrix
sharad = np.array([[0,0,0,],[0,0,1],[1,0,2]])
print(csr_matrix(sharad).data)

# what if we want to count nonzeros, we can do this via count_nonzero() method.
import numpy as np
from scipy.sparse import csr_matrix
sharad = np.array([[0,0,0,],[0,0,1],[1,0,2]])
print(csr_matrix(sharad).count_nonzero())

# For removing the zero elemements from the matrix we will use eliminate_zeros().
import numpy as np
from scipy.sparse import csr_matrix
sharad = np.array([[0,0,0,],[0,0,1],[1,0,2]])
sharadnew = csr_matrix(sharad)
sharadnew.eliminate_zeros()
print(sharadnew)

# eliminating duplicate entries with the sum_duplicates() method:
import numpy as np
from scipy.sparse import csr_matrix
sharad = np.array([[0,0,0,],[0,0,1],[1,0,2]])
sharadnew = csr_matrix(sharad)
sharadnew.sum_duplicates()
print(sharadnew)

# here we will convert csr to csc with the tocsc():
import numpy as np
from scipy.sparse import csr_matrix
sharad = np.array([[0,0,0,],[0,0,1],[1,0,2]])
sharadnew = csr_matrix(sharad).tocsc()
print(sharadnew)