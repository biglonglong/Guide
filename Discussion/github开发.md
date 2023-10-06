# 零、配置

> 本地Git仓库和GitHub仓库间**通过SSH加密传输**，==使用前需先配置ssh key建立连接==

- 安装git

- git bash设置机器标识

  ```
  git config --global user.name "GitHub_ID"
  git config --global user.email "GitHub_Email"
  ```

- 创建[私钥](.\User \.ssh\id_rsa) 

  ```
  ssh-keygen -t rsa -C "GitHub_Email"
  ```

- Github连接：github -> Account settings -> SSH and GPG keys->New SSH key；[write key_title and paste Private Key just now]

- git bash 验证

  ```
  ssh -T git@github.com
  ```

- 设置偏好config，具体自行搜索攻略

  ```
  git config --system  <property> “selection”
  git config --global  <property> “selection”
  //手动操作C:\Users\Administrator\.gitconfig或.\.git\config
  export property=selection
  ```

  



# 一、项目发布

## New in Github

![image-20230527180714642](img/image-20230527180714642.png)

- Repository name: 仓库名称
- Description: 仓库描述介绍(可选)
- Public, Private : 仓库权限（公开共享，私有或指定合作者）
- Initialize this repository with a README: 基于Description添加一个README.md 
- gitignore: 不需要进行版本管理的仓库类型，对应生成文件.gitignore
- license: 证书类型，对应生成文件LICENSE

![image-20230527180935801](img/image-20230527180935801.png)

选择一个远程仓库地址（三选一、待会要用）



## New Located

- 创建一个项目文件夹（名字无所谓，不影响后续内容）

```
cd Desktoop
mkdir demo
cd demo
...
```

- 在项目文件夹中开发…..(一些你想要上传的内容)
- 要建立==本地项目（分支）与github项目（分支）的连接==（git remote）



## Up to Github

### 寻常路

克隆远程的仓库，将项目**内**文件加入克隆的文件夹中，这种方法本身就建立好了与远程仓库分支的连接，方便简单。

```
git clone <仓库地址>
git add .
git commit -m ""
git push
```

### 不走寻常路

- 项目文件夹中右键可打开git bash

- 创建本地版本库(此时项目受git版本管控)

  ```
  git init
  git add .
  git commit -m ""
  ```

- 建立本地项目（分支）与github项目（分支）的连接

  - 将远程称为origin（你可以改）
  
    ```
    git remote add origin git@github.com:biglonglong/SpaceHunt.git
    ```
  
  - 建立分支的upstream（只在第一次需要这么做，之后直接push即可）
  
    ```
    git push -u origin master
    ```





> 多数情况下，项目为多人开发，远端与本地会形成不一致从而造成各种问题
>
> *除了仓库的owner外，要想让团队的其他成员也可以拥有该仓库的上传权限，需要将其他人添加到项目成员中*

# 二、合作开发

## 关于分支

- 开发者在本地仓库创建新分支开发，提交后在远端也形成新分支；远程仓库分支名与本地仓库分支名是**统一**的

- git push可认为是远程仓库分支合并本地仓库对应的分支；如果远程仓库没有对应分支，则创建一个新的空分支进行合并；对应的git pull可认为是本地仓库对应的分支合并远程仓库分支
- Github上默认分支为main，git上默认分支为master；由于历史原因，某些情况下本地仓库master分支与远程仓库main分支不冲突时，两者会合并为远程仓库main分支



## 关于冲突

> 不同开发者在本地仓库相同分支开发，后提交者分支与远端仓库分支产生冲突，假设冲突分支是master

1. 下拉并合并远端仓库master分支到本地仓库

   ```
   git pull origin master
   git pull --rebase origin master //不建议
   ```

   有可能：`refusing to merge unrelated histories`，这是因为文件版本没有及时更新，两个分支是两个不同的版本，，具有不同的提交历史，则

   ```
   git pull origin master --allow-unrelated-histories
   ```

   有可能：`Your local changes to the following files would be overwritten by merge`，这里就是存在文件冲突，自主修改在：

   ```
   git add .
   git commit -m "changes"
   ```
   
2.  此时本地仓库已更新为远端最新版本了，在提交即可

   ```
   git push -u origin master
   ```



> 不同开发者在本地仓库不同分支同步开发v1.0、v1.1、v1.2，最终项目需要1.0已经增加的功能先合并到1.2

1. 检出项目

   ```
   git clone ...
   ```

2. 检出项目为默认分支

   ```
   git branch -a
   ```

3. 检出分支

   ```
   git checkout v1.0
   git checkout v1.2
   ```

4. 合并分支

   ```
   git checkout v1.2
   git merge v1.0
   ```

5. 解决冲突，提交冲突

   ```
   vim ...
   git add .
   git commmit -m "conflict"
   ```

6. 提交分支

   ```
   git push origin v1.2
   ```

7. 删除多余分支

   ```
   git push origin --delete v1.0
   // 删除远程分支
   git checkout v1.2
   git branch -d v1.0或者git branch -D v1.0
   // 删除本地分支或者强制删除本地分支
   ```





# 三、开发模板

```
==================< 1.创建本地工作分支work，修改目标文件并提交到本地work分支 >===================
$ git branch work     #创建工作分支work
$ git checkout work   #切换到工作分支work
$ vi 1.txt   #修改1.txt内容
$ git add 1.txt 
$ git commit -m "modify in branch work"  #提交到本地work分支


===========================< 2.切换到master分支，拉取最新代码>===============================
$ git checkout master    #重新切换到master分支
$ git pull origin master   #拉取服务器maser分支代码


======================< 3.切换到work分支进行rebase/merge并进行冲突解决 >======================
$ git checkout work   #再次切换到work分支
$ git rebase master  #将work分支rebase到master分支上

手工解决所有冲突
执行 "git add/rm <冲突的文件>" 标记冲突已解决，然后执行 "git rebase --continue"。
您也可以执行"git rebase --skip" 命令跳过这个提交。
如果想要终止执行并回到"git rebase" 执行之前的状态，执行 "git rebase --abort"。

$ vi 1.txt     #上一步合并有冲突，所以手动修改(merge)文件
$ git add 1.txt   #变基的临时分支，直接git add将修改加进暂存区
$ git rebase --continue    #使用continue选项继续前面的rebase


======================< 4.切换到master分支进行merge并提交到远程服务器 >========================
$ git checkout master #切换到分支 'master'，您的分支与上游分支 'origin/master' 一致。
$ git merge work 
$ git push origin master 
```





# 四、版本回退

```
git hist  # 寻找历史版本<hash>（及时git tag <hash>）
git checkout <hash>  # 版本切换进行查看
git reset --hard <hash>  # 还原到任意一次提交
git push -f origin master  # 强制覆盖远程仓库
```



```
#撤回added
git checkout <file>、.

#重置暂存区added <file>
git reset HEAD <file>    

#还原最后一次提交 commited
git revert HEAD [--no-edit]
```





# 五、Pull Request

> 非原作者开发成员没有对项目发布新版本的权限，但可以进行fork并request原作者pull自己的版本

- Fork：从原作者仓库fork，建一个自己的分支仓库
- Clone：将自己的分支仓库clone到本地开发并push
- Pull request：Github服务端显示修改并产生Pull request链接，Pull request并注明修改内容（注意是否冲突），可与原作者在该Pull request下进行Comment
- Merge request：等待原仓库的作者查看和决定是否接受修改，原作者与fork成员Comment后点击Merge request即可

