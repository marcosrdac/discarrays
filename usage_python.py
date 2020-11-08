from discarrays import discarray
import numpy as np

# create memory-mapped array (full of zeros)
arr = discarray("test.bin", "w+", dtype=np.int32, shape=(2, 2))

# write first index of array to 2
arr[0, 0] = 2

# delete variable to close file and free memory
del arr

# open memory-mapped array in read-only mode
arr = discarray("test.bin", "r", dtype=np.int32)

print(arr)
print(type(arr))
