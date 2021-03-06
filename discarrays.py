import numpy as np


def discarray(filename, mode='r', dtype=float, shape=None, order='C'):
    '''
    This function is an interface to a memory-mapped array creation. This
    interface has a header of Int64 values, the first one of them being the 
    number of dimensions present in the array, (ndim), and then its dimensions
    (shape). After the header comes the body: a flattened version of that array.
    WARNING: This interface will not save the data types, so you must inform it
    everytime you read a file.
    '''
    file_mode = f'{mode[0]}b{mode[1:]}'
    with open(filename, file_mode) as io:
        if mode.startswith('w'):
            assert shape is not None
            shape = tuple(np.asarray(shape).flatten())
            ndims_shape = np.asarray([len(shape), *shape], dtype=np.int64)
            ndims_shape.tofile(io)
        if mode.startswith('r'):
            ndims = np.fromfile(io, dtype=np.int64, count=1)[0]
            shape = tuple(np.fromfile(io, dtype=np.int64, count=ndims))
        offset = io.tell()
        arr = np.memmap(io, mode=mode, dtype=dtype, shape=shape, 
                        offset=offset, order=order)
    return(arr)
