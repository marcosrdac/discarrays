# Discarrays (MMAP interfaces for Julia and Python)

This repository has modules for using the MMAP syscall with arrays.

I wrote these modules so that using MMAP with Python and Julia becomes extremely easy (see the "usage_<language>.<ext>" files).


## *I'm sorry, what is MMAP?*

You have probably used the "read" command for reading files before in any programming language. This function is actually calling the operational system to get data from your ROM via the "READ" SYSCALL. The fact is that there are other SYSCALLs, as MMAP. MMAP is used for mapping files between ROM an RAM. It is useful for many purposes (i.e. reading and writing files, IPC, etc.). When using MMAP, the system automatically handles allocation, syncronization and deallocation of memory between RAM and ROM as your code asks.

When dealing with arrays, this SYSCALL becomes very useful: you can map an array inside a file to your memory, even if this arrays is too big. The system will keep part of the file cached so that you can use it, but if you ask for memory that is not cached, MMAP will deallocate old cached data and alocate a new part of the array for your code to work on.

What happens in practice is that you don't bother for array sizes or allocations for the rest of your program.


## Array compatibility between Python/C and Julia/Fortran programs

If you are using Python along with Julia or Fortran, make sure to use:
```
discarray(..., order="F")
```
so that Python interface will read and save column-major order (a.k.a. Fortran-contiguous) arrays.
