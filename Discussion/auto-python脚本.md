## import os

```python
# 获取路径path
path=""
while(True):
    path=input("path: ")
    if path=="1":
        path = os.getcwd()
        break
    elif os.path.exists(path):
        break
    else:
        print("error path.......\n")

# 遍历路径path和筛选文件file
for root, dirs, files in os.walk(path):
    for file in files:
        if <condiions>:
            <operation with os.path.join(root, file)> 

# <condiions>
#文件名和文件后缀
file.endswith(".sth")
fileName,fileEnd=file.split('.')


# <operation>
#系统命令
os.system(sysCommand)
#删除文件
os.remove(fileAddress)

# file文件操作
for line in open("./demo.txt", "r"):
    ...
```







