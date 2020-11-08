include("discarrays.jl")
using .Discarrays

# create memory-mapped array (full of zeros)
arr = discarray("test.bin", "w+", Int32, (2, 2))

# write first index of array to 2
arr[1, 1] = 2

# reasign variable to close file and free memory
arr = 0

# open memory-mapped array in read-only mode
arr = discarray("test.bin", "r", Int32)

display(arr)
