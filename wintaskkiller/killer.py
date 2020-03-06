# kill all task
# -*- coding: utf-8 -*-

import psutil
import wmi

def killProcess_ByAll(PROCNAME): 
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROCNAME:
            proc.kill()

def killProcess_ByPid(pid):
    p = psutil.Process(pid)
    p.terminate() 

# kill_process("firefox.exe")

def list_process(sort='name'):
    # sort - name/pid
    processes = []

    c = wmi.WMI ()
    
    #print(process.ProcessId, process.Name)
    
    if sort == 'pid':
        processes_pid = {}
        for process in c.Win32_Process():
            processes_pid[process.ProcessId] = process

        for pid in sorted(processes_pid.keys()):
            processes.append(  processes_pid[pid] )

    elif sort == 'name':
        processes_name = {}
        process_strings = []

        for process in c.Win32_Process():
            processes_name[process.Name] = process
            process_strings.append( process.Name )

        process_strings.sort()
        processes = [processes_name[process_name] for process_name in process_strings]

        
    file_ = open('running_list.txt','w+')
    for process in processes:
        print(process.ProcessId, process.Name)
        file_.write(f'{process.ProcessId} {process.Name}\n')

        #process.__dict__
        """

        instance of Win32_Process
        {
            Caption = "System Idle Process";
            CreationClassName = "Win32_Process";
            CreationDate = "20200206235942.060650+360";
            CSCreationClassName = "Win32_ComputerSystem";
            CSName = "DESKTOP-LC92I9N";
            Description = "System Idle Process";
            Handle = "0";
            HandleCount = 0;
            KernelModeTime = "2248239062500";
            Name = "System Idle Process";
            OSCreationClassName = "Win32_OperatingSystem";
            OSName = "Microsoft Windows 10 Pro|C:\\Windows|\\Device\\Harddisk0\\Partition4";
            OtherOperationCount = "0";
            OtherTransferCount = "0";
            PageFaults = 2;
            PageFileUsage = 0;
            ParentProcessId = 0;
            PeakPageFileUsage = 0;
            PeakVirtualSize = "65536";
            PeakWorkingSetSize = 4;
            Priority = 0;
            PrivatePageCount = "0";
            ProcessId = 0;
            QuotaNonPagedPoolUsage = 0;
            QuotaPagedPoolUsage = 0;
            QuotaPeakNonPagedPoolUsage = 0;
            QuotaPeakPagedPoolUsage = 0;
            ReadOperationCount = "0";
            ReadTransferCount = "0";
            SessionId = 0;
            ThreadCount = 4;
            UserModeTime = "0";
            VirtualSize = "65536";
            WindowsVersion = "10.0.14393";
            WorkingSetSize = "4096";
            WriteOperationCount = "0";
            WriteTransferCount = "0";
        };
        """
    file_.close()

def dump(obj):
    for attr in dir(obj):
        print("obj.%s = %r" % (attr, getattr(obj, attr)))

def idle_mode():
    kill_running_app_list = ['kited.exe','sublime_text.exe','AoE2DE_s.exe','BattleServer.exe','conhost.exe','python.exe']

list_process()
killProcess_ByAll("chromedriver.exe")