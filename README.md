# gpuinfo

I implement some functions that can help users to obtain nvidia gpu information.

To use gpuinfo, you need to be able to run 'ps' and 'nvidia-smi' in your terminal. 

# Install with pip:
```
pip install gpuinfo
```  
I only tested on linux system with python3.

# Usage

```python
from gpuinfo import GPUInfo
```

GPUInfo has the following functions:
 
FUNCTIONS
    check_empty()
        check_empty()
        return a list containing all GPU ids that no process is using currently.
    
    get_info()
        pid_list,percent,memory,gpu_used=get_info()
        return a dict and three lists. pid_list has pids as keys and gpu ids as values, showing which gpu the process is using
    
    get_user(pid)
        get_user(pid)
        Input a pid number , return its creator by linux command ps
    
    gpu_usage()
        gpu_usage()
        return two lists. The first list contains usage percent of every GPU. The second list contains the memory used of every GPU. The information is obtained by command 'nvidia-smi'

