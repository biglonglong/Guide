![img](img/1090617-20181008211557402-232838726.png)



# 零、配置

1. 安装git

```bash
...
Git Bash Here
```

2. 设置机器标识

```bash
git config --global user.name "GitHub_ID"
git config --global user.email "GitHub_Email"
```

> 本地Git仓库和GitHub仓库间**通过SSH加密传输**，使用前需先配置**ssh key**建立连接

1. 建立密钥连接

```bash
ssh-keygen -t rsa -C "GitHub_Email"      		# C:\Users\<Administrator>\.ssh\id_rsa
//copy id_rsa to https://github.com/settings/keys -> New SSH key
ssh -T git@github.com
```

2. 设置property，具体内容自行搜索攻略

```bash
git config --system <property> "selection"	  	# ...\Git\etc\gitconfig
git config --global <property> "selection"    	# C:\Users\<Administrator>\.gitconfig
git config --local <property> "selection"    	# ...\<project>\.git\config
```



# 一、项目发布

1. 项目启动

```bash
cd Desktoop
mkdir <project>
cd <project>
```

2. 创建本地版本库，默认分支为master，对项目内容进行更新并提交

```bash
git init
git branch -m master main
git status
vim README.md
...
git add .
git commit -m "changes"
```

3. 建立远程裸仓库，默认分支为main，记录远程仓库地址

```bash
//https://github.com/ -> New 
//copy Code -> Clone
```

4. 本地仓库分支与远程保持一致，建立远程仓库origin连接

```bash
git branch -m master main
git remote add origin git@github.com:biglonglong/<project>.git
```

5. 建立分支的upstream（只在第一次需要这么做，之后直接push即可）

```bash
git push -u origin main
```



# 二、合作开发

> 关于权限：
>
> Authority：除仓库owner，要想让其他成员拥有仓库上传权限，需将其添加到项目成员目录中，否则只能进行**Pull Request**：
>
> - Fork：从原作者仓库fork，建一个自己的分支仓库
> - Clone：将fork的仓库clone到本地dev分支开发并push
> - Pull request：Github服务端显示修改并产生Pull request链接，Pull request并注明修改内容与冲突关系，与原作者在该Pull request下进行Comment
> - Merge request：等待原仓库的作者查看和决定是否接受修改，原作者与fork成员Comment后点击Merge request即可
>
> 关于分支：
>
> - 开发者在本地仓库创建新分支开发，提交后在远端也形成新分支；远程仓库分支名与本地仓库分支名是**统一**的，除了master与main
> - git push可认为是远程仓库分支**合并**本地仓库对应的分支；如果远程仓库没有对应分支，则创建一个新的空分支进行合并；对应的git pull可认为是本地仓库对应的分支合并远程仓库分支

1. 克隆远程仓库

```bash
 git clone [url]						# 默认只克隆远程主分支
```

```bash
git remote								
git remote show <name>		  	 		 # 查看现有远程仓库及其地址
git branch -a							# 查看当前远程仓库所有分支
```

```bash
git remote <name> [url]					 # 跟踪远程仓库
git branch --track dev origin/dev		  # 跟踪远程其他分支
```

2. 本地开发与整合

```bash
===========================< 1.创建本地工作分支work，在work分支上进行开发>===========================
git checkout -b work								# 创建work分支
git checkout work									# 切换到work分支
vim ...											   # 开发
git add .
git commit -m "changes"

=================================< 2.切换到main分支，拉取最新代码>==================================
git checkout main									# 切换回main分支
git pull origin main								# 拉取远程main分支最新代码 
//Error：`refusing to merge unrelated histories`		  # 解决冲突
//git pull origin main --allow-unrelated-histories	   # 允许冲突下拉
//vim ...										   # 解决冲突
//git add .
//git commit -m "conflicts"
//git push -u origin main

=========================< 3.切换到work分支进行rebase/merge并解决冲突>==============================
git checkout work									# 再次切换到work分支
git merge main/git rebase main						 # 合并main分支到work分支
vim ...											   # 解决冲突
git add .
git commit -m "conflicts"
git rebase --continue								# 变基合并继续 | git rebase --skip | git rebase --abort

===========================< 4.切换到main分支进行merge并提交到远程服务器>===========================
git checkout main									# 再次切换回main分支
git merge work										# 合并work分支到main分支
git push origin main 								# 提交
```

3. 删除多余分支

```bash
git checkout main
git branch -D work								   # 删除本地分支
git push origin --delete dev						# 删除远程分支
```



# 三、版本回退

```bash
git log								# 寻找历史版本<hash>（及时git tag <hash-tag-name>）
git checkout <hash>[^]				 # 版本切换进行查看
git checkout main					 # 返回main最新版本
```

```bash
git checkout <filename>				 # 回退<filename>未暂存的更改
```

```bash
git reset HEAD <filename>			 # 回退<filename>更改的已暂存
```

```bash
git revert HEAD --no-edit			 # 回退已提交的
```

```bash
git tag current						# 标记重置前记录 
git reset --hard v1					# 重置已提交记录至v1
git log --all					    # 显示所有操作记录
git tag --d current					# 删除重置前记录
```

```bash
git commit --amend -m <changes>		 # 合并上次提交
```

```bash
git push -f origin main				# 强制覆盖远程仓库
```



# 五、其他问题

## 1.CRLF换行符

> 现象：（跨平台）工作空间commit项目时**Warning:LF will be replaced by CRLF**，再次clone后文件乱码
>
> 原因：换行主要与CR回车`\r`、LF换行`\n`相关，文件行尾的换行符在不同编辑器和不同平台下具有不同的表示：Linux和macOS使用LF换行，而Dos和Windows使用CR LF换行，在编辑器中体现为KEY `Enter`

- 更改`git config --global|system|local`

单独开发的程序员：

```bash
#提交检出均不转换
$ git config --global core.autocrlf false
```

多人协作跨平台开发的window程序员：

```bash
#提交时转换为LF，检出时转换为CRLF
$ git config --global core.autocrlf true
```

多人协作跨平台开发的Linux程序员：

```bash
#提交时转换为LF，检出时不转换
$ git config --global core.autocrlf input
```

为了防止文换行符杂糅，设置检查：

```bash
#拒绝提交包含混合换行符的文件
git config --global core.safecrlf true   
#允许提交包含混合换行符的文件
git config --global core.safecrlf false
#提交包含混合换行符的文件时给出警告
git config --global core.safecrlf warn
```

- 项目文件`.gitattributes`（最高优先级），文件内容格式为`支持*的文件作用域 属性...`，常用属性：

1. text：标记为文本文件
2. -text：标记为非文本文件
3. text=auto：标记为文本文件并行尾规范化，默认将为新加入项目文件行尾设置为LF
4. eol=crlf：行尾规范化，出库时转为CRLF，入库转为LF
5. eol=lf：行尾规范化，入库转为LF，出库时不操作
