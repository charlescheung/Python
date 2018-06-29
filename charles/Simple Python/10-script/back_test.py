#!/usr/bin/env python
# Filename: backup_ver1.py
import os
import time
import subprocess

# 1. The files and directories to be backed up are specified in a list.
#source=['/home/swaroop/byte','/home/swaroop/bin']
# source=['D:\\FileCopier\\*.*','D:\\jeecms_doc\\*.*']
source = ['E:\\tmp\\a.txt', 'E:\\tmp\\b.txt']
# If you are using Windows, use source=[r'C:\Documents',r'D:\Work'] or something like that

# 2. The backup must be stored in a main backup directory
#target_dir='/mnt/e/backup/' #Remember to change this to what you will be using
target_dir='E:\\tmp\\' #Remember to change this to what you will be using

# 3. The files are backed up into a zip file
# 4. The name of the zip archive is the current date and time
target=target_dir+time.strftime('%Y%m%d%H%M%S')+'.zip'

# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
#zip_command="zip -qr '%s' %s" %(target,' '.join(source))
zip_command="rar a -p10086 " + target + ' ' + ' '.join(source)
# zip_command = "rar a '%s' %s" % (target, ' '.join(source))
# Run the backup

# output = os.popen(zip_command,'w',1)
# print (output)

fd = subprocess.Popen(zip_command, executable=r'rar.exe', stdout=subprocess.PIPE)
print (fd.stdout.read())

# if os.popen(zip_command).read() == 0:
#     print ('Successful backup to',target)
# else:
#     print ('Backup FAILED')


# zipFileName = "test";
# rarPath = r"D:\" + zipFileName + ".rar"
# filePath = r"D:\test"
# # cmd = "rar a -p10086 " + rarPath + " " + filePath
# cmd = ['rar', 'a', '-p10086', 'rarPath', 'filePath]
# 根据winrar的安装路径来开启子进程，我这里用绝对路径，环境变量不可靠；
# 如果希望子进程阻塞主线程就用call，否则用Popen
# fd = subprocess.Popen(cmd, executable=r'C:\Program Files\WinRAR\rar.exe', stdout=subprocess.PIPE)
# # fd = subprocess.call(cmd,executable=r'C:\Program Files\WinRAR\rar.exe')
# # 如果不需要知道子进程的输出，参数stdout=subprocess.PIPE可以不写
# print fd.stdout.read()