# Git

*安装的第一步，首先设置了git的用户名和email

```
git config --global user.name "hihongboyang"
git config --global user.name "245035255@qq.com"
```

*第二步，初始化git仓库

```
git init  #创建仓库
```

当然现在这是一个空仓库。

*试着添加一个文件进入git仓库（缓冲区）

```git
git add readme.txt
```

*添加进仓库后还得将文件提交到仓库保存

```
git commit -m "lala" #提交修改 -m 提交的说明，干了啥
```

分两步走是为了能够一次提交多个文件

*上传了文件之后就可以查看仓库的状态了

```
git status  #查看状态
```

*当然也可以查看某个文件的修改记录

```
git diff readme.txt  #查看修改记录
```

*如果想回退到一个指定版本的修改该怎么办呢？

`HEAD`指的是当前最新的版本。

上一个版本就是`HEAD^`。

上上一个版本就是`HEAD^^`。

上一百个版本就是`HEAD`+一百个^。。no 是  `HEAD~100`

```
git reset --hard HEAD^
```

*可以回退回去，那可以刻穿越到未来版本

```
git reset --hard ****  #版本号，指定版本号就好
```

当然你可以去命令日志中寻找之前输入的命令。

```
git reflog
```

*缓存区，git有一个缓存区用于临时存储修改的文件，最后这些文件是要被存储在版本库中的

*如果发现提交的内容错了就可使用命令撤回缓冲区的内容。

````
git checkout -- readme.text  #将文件回到最近一次git commit 或者git add 时的状态。//丢掉工作区的修改。  用版本库中的版本替换工作区的版本。
````

分为两种情况，有没有推送到缓冲区，

```
git reset HEAD readme.txt  #把缓存区的修改撤销掉，重新放回工作区。
```

### 删除文件

```
git rm readme.txt  #删除文件，但是还得跟 git commit 提交。
```







### 关联远程仓库

使用git生成秘钥

```
ssh-keygen -t rsa -C "245035255@qq.com"
```

本地目录会生成一个.ssh文件夹`id_rsa`是私钥，`id_rsa.pub`是公钥。

第二步，添加公钥到GitHub

关联远程仓库

```
git remote add origin git@github.com:Hihongboyang/nightgit.git
```

关联好了以后就是推送服务了。第一次推送所有的内容。

```
git push -u origin master
```

之后再做本地提交的话可以使用

```
git push origin master
```



### 克隆远程仓库到本地

```
git clone git@github.com:Hihongboyang/nightgit.git
```

也可以使用ssh协议和HTTPS协议。HTTPS比较慢。





### 分支管理

分支管理的核心就是”指针“的使用。

*创建分支

```
git checkout -b dev
```

-b 表示创建和切换，相当于

```
git branch dev
git checkout dev
```

*现在就可以在分支上做自己的修改*

之后

可以提交

```
git add readme.txt
git commit -m "branch test"
```

回到master分支

```
git checkout master
```

合并分支

```
git merge dev  #合并指定分支到当前分支
```

删除分支,删除创建的分支

```
git branch -d dev
```



查看分支，查看当前工作中所有的分支，*代表当前所在分支。

```
git branch
```























