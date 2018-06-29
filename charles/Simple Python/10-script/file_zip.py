import os
import zipfile

def zip_dir(dirname,zipfilename):
    filelist = []
    if os.path.isfile(dirname): #判断压缩目录是否是文件，是则添加到文件列表filelist中
        filelist.append(dirname)
    else:
        for root,dirs,files in os.walk(dirname): #root是根目录,dirs存放的是子目录，files存放的是根目录下边的文件
            for name in files:
                filelist.append(os.path.join(root,name))
                print('joined:',os.path.join(root,name),dirs)
    zf = zipfile.ZipFile(zipfilename,"w",zipfile.ZIP_DEFLATED,allowZip64=True)
    for tar in filelist:
        arcname = tar[len(dirname):] #文件名
        print(arcname,tar)
        zf.write(tar,arcname)  #将tar源文件的内容写到arcname文件中
    zf.close()


if __name__=='__main__':
    dirname = "E:\\tmp\\test"
    zipname = "E:\\tmp\\2017-9-1.zip"
    zip_dir(dirname,zipname)

def unzip_dir(zipfilename):
    fullzipfilepath = os.path.abspath(zipfilename)  #压缩文件的绝对路径C:\Users\Administrator\Desktop\apk数据\2017-9-1.zip
    print(fullzipfilepath)
    unzipdir = fullzipfilepath.split('.zip')[0][0:] #解压文件的根目录C:\Users\Administrator\Desktop\apk数据\2017-9-1
    if not os.path.exists(fullzipfilepath):
        print("Dir %s is not exists,input fullzipfilepaht")
        fullzipfilepath = input()
    if not os.path.exists(unzipdir):
        os.mkdir(unzipdir)
    zf = zipfile.ZipFile(fullzipfilepath,'r')  #读方式打开压缩
    for filename in zf.namelist():  #zf.namelist() 获取压缩包文件中的文件列表
        eachfilepath = os.path.normpath(os.path.join(unzipdir,filename))  #将文件路径转化为正常路径，
                                                             # 从压缩文件获取的文件列表中，获取的文件格式是test1/2017-9-1.txt,
                                                             #无法创建目录或文件
        eachfiledir = os.path.dirname(eachfilepath)
        if not os.path.exists(eachfiledir):
            os.mkdir(eachfiledir) #递归创建目录,如果子目录创建失败或者已经存在，会抛出一个OSError的异常，
            # os.makedirs(eachfiledir)  #创建目录，如果目录是多级，则创建最后一级，如果最后一级的上级目录不存在，则会报出异常
        fp = open(eachfilepath,'w')
        fp.write(str(zf.read(filename)))
        fp.close()
    zf.close()


if __name__=='__main__':
    zipfilename = "E:\\tmp\\2017-9-1.zip"
    unzip_dir(zipfilename)

from zipfile import ZipFile
def print_file(inputfile_path):
    myzip  = ZipFile(inputfile_path,'r')
    for file_name in myzip.namelist():
        for  data in myzip.open(file_name,'r'):
            print(data)
    myzip.close()

if __name__=='__main__':
    inputfile_path = "E:\\tmp\\2017-9-1.zip"
    print_file(inputfile_path)

def unzip_file(zfile_path, unzip_dir):
    '''
    function:解压
    params:
        zfile_path:压缩文件路径
        unzip_dir:解压缩路径
    description:
    '''
    try:
        with zipfile.ZipFile(zfile_path) as zfile:
            zfile.extractall(path=unzip_dir)
    except zipfile.BadZipFile as e:
        print (zfile_path+" is a bad zip file ,please check!")

if __name__ == '__main__':
    #zip_dir(r'/tmp/xungou',r'/tmp/xungou.zip')
    unzip_file(r'E:\\tmp\\2017-9-1.zip',r'E:\\tmp\\2017-9-1')
