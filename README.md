# gpuinfo

I implement some functions that can help users to obtain nvidia gpu information.

To use gpuinfo, you need to be able to run 'ps' and 'nvidia-smi' in your terminal. 

# Install with pip
```
pip install gpuinfo
```  
I only tested on linux system with python3.
https://pypi.org/project/gpuinfo/

# Usage

```python
from gpuinfo import GPUInfo
```

GPUInfo has the following functions:
    
    get_users(gpu_id)
        return a dict. show every user and memory on a certain gpu 

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

# Example

```python
from gpuinfo import GPUInfo

available_device=GPUInfo.check_empty()
#available_device就是一个含有所有没有任务的gpu编号的列表
percent,memory=GPUInfo.gpu_usage()
#获得所有gpu的使用百分比和显存占用量
min_percent=percent.index(min([percent[i] for i in available_device]))
#未被使用的gpu里percent最小的
min_memory=memory.index(min([memory[i] for i in available_device]))
#未被使用的gpu里显存占用量最少的

#如果你使用pytorch
torch.cuda.set_device(min_percent) 或者(min_memory)
```
