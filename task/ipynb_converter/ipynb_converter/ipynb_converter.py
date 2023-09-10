'''
time:2022-09-06
author:biglonglng
environment:nbconvert & pandoc & TeX & pyppeteer &
function:ipynb converter TTML、LaTeX、PDF、Markdown、notebook、Ascii ...
'''

import os

#information collection
target=input("请输入目标文件后缀(1默认为markdown!!!):")
if target=="1":
	target="markdown"
flag=input("自动删除原文件？ 1\\0:")
path=0
while(path==0 or os.path.exists(path)==False):
	if(path!=0):
		print("路径错误!")
	path = input("请输入正确路径(1默认为当前路径!!!):")
	if path=="1":
		path=os.getcwd()
		break

for root,dirs,files in os.walk(path): 
	for file in files:
		if file.endswith(".ipynb"):
			os.system("jupyter nbconvert --to "+ target +" "+ os.path.join(root,file))
			if flag=="1":
				os.remove(os.path.join(root,file))
print("任务完成！！！")

