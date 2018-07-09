
import os
from math import ceil
def replace_str(path):
    with open(path,encoding="utf-8") as f:
        arr1=[]
        for line in f:
            str_line = line.replace("|",",").strip()
            arr1.append(str_line)

        arr2=[]
        num=100
        endCount=ceil(len( arr1)/num)
        for item in range(endCount):
            subItem = arr1[num*item:num*item + num]
            arr2.append( ','.join(subItem))

        aa = ",".join(arr2)
        bb = len(aa.split(","))

        sql = "update merchant SET company_id = 200 WHERE id in ({0});"
        subStr = ""
        for item in arr2:
            subStr += "\n\n" + sql.format(item)
        return subStr

if __name__=='__main__':
    path = "E:\\Users\\charles\\Desktop\\aa.txt"
    res = replace_str(path)
    print(res)
