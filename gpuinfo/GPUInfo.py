import os
import re
__all__=['get_user','gpu_usage','check_empty','get_info']
def get_user(pid):
    '''
    get_user(pid)
    Input a pid number , return its creator by linux command ps
    '''
    ps=os.popen('ps -eo pid,user|grep '+str(pid))
    lines=ps.readlines()
    for line in lines:
        return re.split('[ \n]',line)[-2]
    return None

def gpu_usage():
    '''
    gpu_usage()
    return two lists. The first list contains usage percent of every GPU. The second list contains the memory used of every GPU. The information is obtained by command 'nvidia-smi'
    '''
    pid_current,percent,memory,gpu_used=get_info()
    return percent,memory

def check_empty():
    '''
    check_empty()
    return a list containing all GPU ids that no process is using currently.
    '''
    gpu_unused=list()
    pid_current,percent,memory,gpu_used=get_info()
    for i in range(0,8):
        if not i in gpu_used:
            gpu_unused.append(i)
        
    if len(gpu_unused)==0:
        return None
    else:
        return (gpu_unused)

def get_info():
    '''
    pid_list,percent,memory,gpu_used=get_info()
    return a dict and three lists. pid_list has pids as keys and gpu ids as values, showing which gpu the process is using
    '''
    gpu_used=list()
    pid_current=list()
    ns=os.popen('nvidia-smi')
    lines_ns=ns.readlines()
    percent=list()
    memory=list()
    pid_list=dict()
    for line in lines_ns:
        if line.find('%')!=-1:
            percent.append(int(line.split('%')[0][-3:]))
            memory.append(int(line.split('MiB')[0][-4:]))
        if line.find('%')==-1 and line.find('MiB')!=-1:
            #processes
            arrs=re.split('[ ]+',line)
            gpu_id=arrs[1]
            pid=arrs[2]
            process_name=arrs[4]
            gpu_used.append(int(gpu_id))
            mem=int(arrs[5][:-3])
            if pid in pid_list.keys():
                pid_list[pid].append(gpu_id)
            else:
                pid_list[pid]=list()
                pid_list[pid].append(gpu_id)
    pid_current=pid_list.keys()
    return pid_list,percent,memory,gpu_used

