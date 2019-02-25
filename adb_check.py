#-*- coding:utf-8 -*-

import os
import logging
import _winreg as winreg
import ctypes
import re

if __name__ == "__main__":
    
    old_path_list = []
    old_path = ""
    new_path_list = []
    new_path = ""
    adbexe_path_list = []
    
    logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='path_change.log',
                    filemode='w',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s  %(levelname)s: %(message)s'
                    #日志格式
                    )
    
    #在系统环境变量下查找adb.exe文件
    for k,v in os.environ.items():
        if k == "PATH":
            old_path = v
            old_path_list = v.split(";")
            logging.info("[old path is]" + old_path) 
        
    if old_path_list:
        for path_item in old_path_list:
            find_flag = False
            #在每个路径下面找adb.exe
            if path_item:
                for root,dirs,firs in os.walk(path_item):
                    for name in firs:
                        if name == "adb.exe":
                            adbexe_path = os.path.join(root,name)
                            adbexe_path_list.append(adbexe_path)
                            find_flag = True
            #如果没有adb.exe文件，则保留
            if not find_flag:
                new_path_list.append(path_item)
    
    if adbexe_path_list:
        logging.info("[delete adb path]需去除系统变量中包含adb.exe的路径")
        for adbexe_path_item in adbexe_path_list:
            logging.info("[find adb exe]"+adbexe_path_item)
    else:
        logging.info("[no adb in path]系统变量所在路径下，没有找到adb.exe文件")
         
        
    if new_path_list:
        new_path = ";".join(new_path_list)
        logging.info("[new path is]" + new_path)
        
        
    #------------------------------------
    
    #在system32下查看adb.exe
    
    system_adbexe_path = ""
    system_adbexe_path_list = [] 
    
    system_path = r"C:\Windows\System32"
    for root,dirs,firs in os.walk(system_path):
        for name in firs:
            if name == "adb.exe":
                system_adbexe_path = os.path.join(root,name)
                system_adbexe_path_list.append(system_adbexe_path)
    
    if system_adbexe_path_list:
        for system_adbexe_path_item in system_adbexe_path_list:
            logging.info("[system find adb exe]"+system_adbexe_path_item)
    else:
        logging.info("[no adb in path]System32所在路径下，没有找到adb.exe文件") 
        
    
    logging.info("[find adb end !]")
    
    
    #------------------------------
    #设置环境变量
    #修改注册表后，更新生效
    def refresh():
        HWND_BROADCAST = 0xFFFF
        WM_SETTINGCHANGE = 0x1A
        SMTO_ABORTIFHUNG = 0x0002
        result = ctypes.c_long()
        SendMessageTimeoutW = ctypes.windll.user32.SendMessageTimeoutW
        SendMessageTimeoutW(HWND_BROADCAST, WM_SETTINGCHANGE, 0, u'Environment', SMTO_ABORTIFHUNG, 5000, ctypes.byref(result))
          
    #设置环境变量   
    if new_path:
        path_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',0, winreg.KEY_ALL_ACCESS)
        path_value = winreg.QueryValueEx(path_key, 'Path')
        winreg.SetValueEx(path_key,"Path",0,winreg.REG_EXPAND_SZ, new_path)
        refresh()
        logging.info("[set new path]设置新的path为%s"%new_path)
    
        logging.info("[set adb end !]")


            