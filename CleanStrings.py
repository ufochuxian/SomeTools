import os
from os import path
from xml.etree.ElementTree import ElementTree

# dir_root=path.abspath(os.getcwd())
dir_root = "/Users/chenjianxiang/Documents/opensource/security-master"

modules = ["adsdk", "antitheft", "app", "applock", "business", "camouflage", "keepalive", "libraries", "secret"]

print(dir_root)

valueList = []
keyList = []
strings_data = []

# 使用集合来跟踪已经添加的键
added_keys = set()

for module in modules:
    s = dir_root + "/" + module + "/src/main/res/values/strings.xml"
    
    # 检查文件是否存在
    if not path.exists(s):
        # print(f"File not found: {s}")
        continue
    
    tree = ElementTree()
    
    try:
        # 打开文件并解析
        with open(s, "r", encoding="utf-8") as file:
            element = tree.parse(s)

        # 遍历strings.xml中所有文本
        for e in element:
            key = str(e.attrib.get("name"))
            value = e.text
            
            # 检查key是否已经存在于added_keys中
            if key not in added_keys:
                keyList.append(key)
                valueList.append(value)
                added_keys.add(key)
    
    except Exception as e:
        print(f"Error processing file {s}: {e}")

strings_data = list(zip(keyList, valueList))

# # 打印结果（可选）
# for key, value in strings_data:
#     print(f"Key: {key}, Value: {value}")

#print(strings_data)


#遍历指定目录下的所有文件
def dirlist(path, allfile):
    filelist =  os.listdir(path)  

    for filename in filelist:  
        filepath = os.path.join(path, filename)  
        if os.path.isdir(filepath):  
            dirlist(filepath, allfile)  
        else:  
            allfile.append(filepath)  
    return allfile  

file=[]

# modules=["applock","business"]

for module in modules:
    if(module=='secret'):
        dirlist(dir_root+"/"+module+"/src/main/java", file)
        dirlist(str(dir_root+"/"+module+"/src/main/res/layout"), file)
        dirlist(str(dir_root+"/"+module+"/src/main/res/menu"), file)
    else:
         dirlist(dir_root+"/"+module+"/src/main/java", file)
         dirlist(str(dir_root+"/"+module+"/src/main/res/layout"), file)

#查找java文件中的字符串
def findJavaFileToString(fileList,list):
    for fileitme in fileList:
      if fileitme.endswith(".DS_Store") == False:
            a=open(fileitme,"r",encoding="utf-8")
            sourceText=a.read()
            a.close()
            for item in list:
                if sourceText.find(str("R.string."+item[0])) !=-1:
                    strings_data.remove(item)
                    # print("文件路径:",fileitme,",找到的字符串为:",item[0])
                elif sourceText.find(str("@string/"+item[0])) !=-1:
                    strings_data.remove(item)
                    # print("文件路径:",fileitme,",找到的字符串为:",item[0])
                else:
                    pass
                    # print("文件路径:",fileitme,",未找到的字符串为:",item[0])
                    print(item[0])


findJavaFileToString(file,strings_data)
# print("",strings_data)
