import numpy as np

# will create 1D array
a = np.array([1,2,3])

#print(a)

# will create an array of type float
a = np.array([1,2,3],dtype=float)

#print(a)

# size method will tell you how many elements are there in an array

#print('Size of the array is = ',a.size)

# ndim method will tell you dimension of the array
#print('Dimension of the array is = ',a.ndim)

# will give you 2 D array
b = np.ones((3,4))

#print('Array of 3*4 with all values as 1 = \n',b)

# will give you 3D array
c = np.zeros((2,3,4))

#print(c)

# will create 2D  array with random values

d = np.random.random((2,2))
#print('dimension of the array and number of elements in array and array = \n',d.ndim,d.size,'\n',d)

# will create an array with evenly spaced values
e = np.arange(10,25,5)

#print(e)

# will create an array of evenly spaced values
f = np.linspace(0,2,9)
#print(f)

# statistical function, Axes are like directions along the NumPy array.
# In a 2-dimensional array, axis 0 is the axis that points down the
# rows and axis 1 is the axis that points horizontally across the columns.

g = np.array([[3,7,5],[8,4,3],[2,4,9]])
#print(g)
#print('minimum in array g is =',np.amin(g,axis=1))
#print('maximum in array g is = ', np.amax(g,axis=1))

#print('mean of the array is = ' , np.mean(g,axis=0)) # to take mean of each col

#print('mean of the array is = ' , np.mean(g,axis=1)) # to take mean of each row

#print('median of the array is = ' , np.median(g,axis=0)) # to take mean of each col

#print('median of the array is = ' , np.median(g,axis=1)) # to take mean of each row

#print('standard deviation of the array is = ', np.std(g,axis=0))

# Array indexing

h = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

#print(h)

row_1 = h[1,:]
row_2 = h[1:2,:]

#print(row_1,'\n',row_1.shape,'\n',row_2,'\n',row_2.shape)

col_1 = h[:,1]
col_2 = h[:,1:2]

#print(col_1,'\n',col_2)

# Array Methods
# ndarray.shape
# ndarray.ndim
# ndarray.data
# ndarray.size
# ndarray.nbytes
# ndarray.tolist    Return the array as a (possibly nested) list.
# ndarray.tostring  Construct Python bytes containing the raw data bytes in the array.
# ndarray.copy      Return a copy of the array.
# ndarray.view      New view of array with the same data


