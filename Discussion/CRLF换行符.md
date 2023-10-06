> （跨平台）工作空间commit项目时，警告：**LF will be replaced by CRLF**，再次git clone后文件乱码





## 一、原理

> 文件行尾的换行符在不同编辑器和不同平台下具有不同的表示

在文本处理中，换行主要与CR、LF相关：

- CR（CarriageReturn）：回车，即回到一行的开头，用字符\r表示，十进制ASCII码为13
- LF（LineFeed）：换行，即另起一行，用字符\n表示，十进制ASCII码为10



然而不同操作系统使用的换行符不同：

- Linux：使用**换行（LF）**，即“\n”；
- Mac：早期使用回车（CR），即'\r'；后mac os x使用**换行（LF）**，即“\n”；
- Dos、Windows： 使用**回车+换行(CR+LF)**，即“\r\n”；

许多 Windows 上的编辑器会悄悄把行尾的换行（LF）字符转换成回车（CR）和换行（LF），或在用户按下 Enter 键时，插入回车（CR）和换行（LF）两个字符





## 二、解决问题

> 更改git 全局config 使得换行符与检出系统匹配

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



> 为了防止文换行符杂糅，设置检查

```php
#拒绝提交包含混合换行符的文件
git config --global core.safecrlf true   
#允许提交包含混合换行符的文件
git config --global core.safecrlf false
#提交包含混合换行符的文件时给出警告
git config --global core.safecrlf warn
```





## 三、终极方案

> 通过设置 core.autocrlf 并不能跟随远程仓库进行设置，落到具体的开发者身上，还是会存在换行符不一致的问题。所以最终的处理方案应该是跟随项目提供一个配置文件（ **.gitattributes**），并且给以最高的优先级

### .gitattributes文件格式

```
要匹配的文件后缀 属性1 属性2 ...
```

属性：

- text：用于控制（本地和远程)行尾的规范性，与库内文件有关，默认为LF。
- eol
  - eol=lf，入库时将行尾规范为LF，检出时行尾保持为LF
  - eol=crlf，入库时将行尾规范为LF，检出时将行尾转换为CRLF
- diff？



###  .gitattributes文件示例

```txt
*           text=auto  
# 文件的行尾自动转换。如果是文本文件，则在文件入Git库时，行尾自动转换为LF。如果已经在入Git库中的文件的行尾是GRLF，则文件在入Git库时，不再转换为LF。

*.txt       text  
# 对于.txt文件，标记为文本文件，并进行行尾规范化。

*.jpg       -text  
# 对于`.jpg`文件，标记为非文本文件

*.vcproj    text eol=crlf 
# 对于.vcproj文件，标记为文本文件，在文件入Git库时进行规范化，行尾转换为LF。在检测到出工作目录时，行尾自动转换为GRLF。

*.sh        text eol=lf  
# 对于sh文件，标记为文本文件，在文件入Git库时进行规范化，即行尾为LF。在检出到工作目录时，行尾也不会转换为CRLF（即保持LF）。

*.py        eol=lf  
# 对于py文件，只针对工作目录中的文件，行尾为LF。

*.bat       text eol=crlf 
# 无格式的文本文件,保证 Windows 的批处理文件在 checkout 至工作区时，始终被转换为 CRLF 风格的换行符；
```



### 据.gitattributes重置本地仓库行尾符

```
git rm --cached -r
git reset --hard
```



### 为所有本地仓库设置行尾符

```
git config --get core.attributesFile
git config --global --get core.attributesFile
```

