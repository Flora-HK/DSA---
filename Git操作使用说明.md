# Git 操作使用说明

## 一、Git 简介

### 1.1 什么是 Git？

Git 是一个**分布式版本控制系统**（Distributed Version Control System，简称 DVCS），由 Linus Torvalds 于 2005 年创建，最初用于管理 Linux 内核源代码。

它能够记录文件内容的变更，并支持多人协同开发，是当今软件开发中最广泛使用的版本管理工具。

### 1.2 Git 的核心特点

| 特点 | 说明 |
| --- | --- |
| 分布式 | 每个开发者本地都拥有完整的版本库，不依赖中央服务器 |
| 速度快 | 大部分操作在本地完成，无需网络通信 |
| 分支轻量 | 创建、切换、合并分支成本极低 |
| 数据完整性 | 通过 SHA-1 哈希值校验，确保数据不被篡改 |
| 支持离线工作 | 提交、分支、日志等操作均可在本地完成 |

### 1.3 Git 与 GitHub 的区别

- **Git**：版本控制工具（软件）
- **GitHub**：基于 Git 的代码托管平台（网站服务）
- 类似的托管平台还有：GitLab、Gitee、Bitbucket 等

---

## 二、Git 核心概念

### 2.1 三个工作区域

```
┌──────────────┐  git add   ┌──────────────┐  git commit  ┌──────────────┐
│  工作区       │ ─────────► │  暂存区       │ ──────────►  │  版本库       │
│ Working Dir   │            │ Staging Area │              │ Repository   │
└──────────────┘            └──────────────┘              └──────────────┘
```

| 区域 | 说明 |
| --- | --- |
| **工作区（Working Directory）** | 你能直接看到和编辑的文件目录 |
| **暂存区（Staging Area / Index）** | 临时存放待提交的改动 |
| **版本库（Repository）** | Git 正式记录的所有提交历史 |

### 2.2 文件的四种状态

```
Untracked ──git add──► Staged ──git commit──► Unmodified ──修改文件──► Modified
                          ▲                                                    │
                          └──────────────────── git add ──────────────────────┘
```

- **Untracked**：未被 Git 跟踪的新文件
- **Staged**：已加入暂存区，等待提交
- **Unmodified**：已提交且未修改
- **Modified**：已跟踪但内容有变更

### 2.3 分支（Branch）

分支是 Git 的灵魂功能，它允许你从主线上分离出来，独立开发新功能或修复 bug，最后再合并回主线。

```
main:     A ── B ─────────────── E (merge)
                   \             /
feature:            C ────────── D
```

---

## 三、Git 安装与配置

### 3.1 安装

- **Windows**：从 [git-scm.com](https://git-scm.com/download/win) 下载安装包，按默认选项安装即可
- **macOS**：`brew install git` 或安装 Xcode Command Line Tools
- **Linux（Debian/Ubuntu）**：`sudo apt-get install git`

### 3.2 全局配置

首次使用需设置用户名和邮箱（提交记录会使用这些信息）：

```bash
# 设置全局用户名和邮箱
git config --global user.name "你的名字"
git config --global user.email "your_email@example.com"

# 查看所有配置
git config --list

# 设置默认分支名为 main
git config --global init.defaultBranch main

# 设置默认编辑器（可选）
git config --global core.editor "code --wait"

# 设置命令别名（可选，提升效率）
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.lg "log --oneline --graph --all"
```

> 配置文件存放位置：
> - 全局配置：`~/.gitconfig`（Windows 为 `C:\Users\用户名\.gitconfig`）
> - 仓库配置：`项目目录/.git/config`

---

## 四、常见 Git 操作汇总

### 4.1 仓库初始化与克隆

```bash
# 在当前目录初始化一个新仓库
git init

# 克隆远程仓库到本地
git clone <仓库URL>

# 克隆到指定目录
git clone <仓库URL> <目录名>

# 克隆指定分支
git clone -b <分支名> <仓库URL>

# 只克隆最近一次提交（浅克隆，节省时间和空间）
git clone --depth 1 <仓库URL>
```

### 4.2 查看状态与差异

```bash
# 查看工作区状态（最常用命令之一）
git status

# 以简洁方式查看状态
git status -s

# 查看工作区与暂存区的差异
git diff

# 查看暂存区与最新提交的差异（已暂存但未提交）
git diff --cached

# 查看工作区与最新提交的差异
git diff HEAD

# 查看某文件的修改历史
git log -p <文件名>
```

### 4.3 添加与提交

```bash
# 添加单个文件到暂存区
git add <文件名>

# 添加所有修改到暂存区（包括新增、修改、删除）
git add .

# 添加某目录下所有改动
git add <目录名>/

# 交互式选择添加（按 hunk 选择）
git add -p

# 提交暂存区的改动
git commit -m "提交说明"

# 提交所有已跟踪文件的修改（跳过 add 步骤）
git commit -am "提交说明"

# 修改上一次提交（追加文件或修改说明）
git commit --amend -m "新的提交说明"

# 修改上一次提交但不修改说明
git commit --amend --no-edit
```

> **提交信息规范建议**：
> - `feat: 新功能`
> - `fix: 修复 bug`
> - `docs: 文档更新`
> - `style: 代码格式调整`
> - `refactor: 重构`
> - `test: 测试相关`
> - `chore: 构建/工具变动`

### 4.4 查看历史记录

```bash
# 查看完整提交历史
git log

# 单行简洁显示
git log --oneline

# 图形化显示分支结构
git log --oneline --graph --all

# 显示每次提交的改动内容
git log -p

# 显示最近 N 条提交
git log -5

# 查看某文件的修改历史
git log -- <文件名>

# 按作者筛选
git log --author="作者名"

# 按日期筛选
git log --since="2025-01-01" --until="2025-12-31"

# 查看每一行代码最后修改的提交
git blame <文件名>
```

### 4.5 分支操作

```bash
# 列出所有本地分支
git branch

# 列出所有分支（含远程）
git branch -a

# 列出远程分支
git branch -r

# 创建新分支（不切换）
git branch <分支名>

# 创建并切换到新分支
git checkout -b <分支名>
# 或使用新命令
git switch -c <分支名>

# 切换分支
git checkout <分支名>
# 或
git switch <分支名>

# 切换到上一个分支
git checkout -

# 删除本地分支（需已合并）
git branch -d <分支名>

# 强制删除本地分支
git branch -D <分支名>

# 删除远程分支
git push origin --delete <分支名>

# 重命名分支
git branch -m <旧名> <新名>

# 合并分支（将指定分支合并到当前分支）
git merge <分支名>

# 变基（将当前分支的提交移到指定分支顶端）
git rebase <分支名>
```

> **merge 与 rebase 的区别**：
> - `merge`：保留完整历史，生成合并提交，历史记录是网状的
> - `rebase`：使历史线性整洁，但会重写提交哈希，**不要对已推送的公共分支做 rebase**

### 4.6 远程仓库操作

```bash
# 查看远程仓库
git remote -v

# 添加远程仓库
git remote add origin <仓库URL>

# 修改远程仓库地址
git remote set-url origin <新URL>

# 重命名远程仓库
git remote rename origin upstream

# 删除远程仓库
git remote remove origin

# 拉取远程更新（不合并）
git fetch

# 拉取远程分支并合并到当前分支
git pull

# 拉取并使用 rebase 方式合并（推荐，保持历史整洁）
git pull --rebase

# 推送本地分支到远程
git push origin <分支名>

# 推送并设置上游关联（首次推送）
git push -u origin <分支名>

# 推送所有分支
git push --all

# 推送所有标签
git push --tags

# 强制推送（危险！会覆盖远程历史，慎用）
git push --force
# 更安全的方式：使用 force-with-lease
git push --force-with-lease
```

### 4.7 撤销与回退

```bash
# 撤销工作区某文件的修改（恢复到暂存区或最新提交的状态）
git checkout -- <文件名>
# 新命令
git restore <文件名>

# 撤销所有工作区修改
git checkout -- .

# 将文件从暂存区移回工作区（取消暂存，不丢失修改）
git reset HEAD <文件名>
# 新命令
git restore --staged <文件名>

# 回退到指定提交（保留修改在工作区）
git reset --soft <commit-hash>

# 回退到指定提交（保留修改在暂存区）
git reset --mixed <commit-hash>   # 默认模式

# 回退到指定提交（完全丢弃修改）
git reset --hard <commit-hash>

# 通过新提交撤销指定提交（不改写历史，安全用于公共分支）
git revert <commit-hash>

# 撤销最近一次提交但保留改动
git reset --soft HEAD~1
```

| 方式 | 是否保留改动 | 是否改写历史 | 适用场景 |
| --- | --- | --- | --- |
| `reset --soft` | 保留到暂存区 | 是 | 本地调整提交 |
| `reset --mixed` | 保留到工作区 | 是 | 本地重新组织提交 |
| `reset --hard` | **丢弃** | 是 | 彻底放弃改动 |
| `revert` | 生成撤销提交 | 否 | 撤销已推送的提交 |

### 4.8 标签（Tag）操作

```bash
# 列出所有标签
git tag

# 创建轻量标签
git tag <标签名>

# 创建附注标签（推荐，包含信息）
git tag -a <标签名> -m "标签说明"

# 给历史提交打标签
git tag -a <标签名> <commit-hash>

# 查看标签信息
git show <标签名>

# 推送单个标签到远程
git push origin <标签名>

# 推送所有标签到远程
git push --tags

# 删除本地标签
git tag -d <标签名>

# 删除远程标签
git push origin --delete <标签名>
```

### 4.9 储藏（Stash）

当工作未完成但需要切换分支时，可临时保存改动：

```bash
# 保存当前工作区和暂存区的改动
git stash

# 保存并添加说明
git stash save "说明信息"
# 新版语法
git stash push -m "说明信息"

# 查看储藏列表
git stash list

# 恢复最近一次储藏（并删除记录）
git stash pop

# 恢复最近一次储藏（保留记录）
git stash apply

# 恢复指定储藏
git stash apply stash@{2}

# 删除储藏
git stash drop stash@{0}

# 清空所有储藏
git stash clear
```

### 4.10 其他实用操作

```bash
# 查看某次提交的详细信息
git show <commit-hash>

# 比较两个分支的差异
git diff <分支1> <分支2>

# 查看某个文件在指定提交时的内容
git show <commit-hash>:<文件路径>

# 将指定提交应用到当前分支
git cherry-pick <commit-hash>

# 二分查找定位引入 bug 的提交
git bisect start
git bisect bad              # 标记当前版本有 bug
git bisect good <commit>    # 标记已知正常版本
# Git 会自动切换，测试后继续标记
git bisect reset            # 结束查找

# 合并其他分支的某次提交
git cherry-pick <commit-hash>

# 清理未跟踪文件
git clean -n        # 预览将删除的文件
git clean -fd        # 删除未跟踪的文件和目录

# 交互式暂存
git add -i

# 归档当前 HEAD（导出干净代码包）
git archive --format=zip --output=project.zip HEAD
```

---

## 五、.gitignore 文件

用于指定 Git 应忽略的文件或目录，避免将编译产物、依赖包、密钥等纳入版本控制。

### 5.1 常见示例

```gitignore
# 依赖目录
node_modules/
__pycache__/
venv/
.venv/

# 编译产物
dist/
build/
*.class
*.o
*.exe

# IDE 配置
.vscode/
.idea/
*.swp

# 操作系统文件
.DS_Store
Thumbs.db

# 环境变量与密钥
.env
*.pem
*.key

# 日志文件
*.log
logs/
```

### 5.2 语法说明

| 语法 | 含义 |
| --- | --- |
| `#` | 注释 |
| `*.log` | 匹配所有 `.log` 文件 |
| `/build/` | 只忽略根目录下的 build 目录 |
| `node_modules/` | 忽略任意层级的 node_modules 目录 |
| `!file.txt` | 不忽略该文件（取反） |
| `temp/*.tmp` | 忽略 temp 下的 tmp 文件 |

> 已被跟踪的文件即使加入 `.gitignore` 也不会被忽略，需先执行：
> ```bash
> git rm --cached <文件名>
> ```

---

## 六、常见问题与解决方案

### 6.1 提交了不该提交的文件

```bash
# 从版本库移除但保留本地文件
git rm --cached <文件名>
git commit -m "移除误提交的文件"
```

### 6.2 提交信息写错了

```bash
# 修改最近一次提交信息
git commit --amend -m "正确的提交信息"
```

### 6.3 想撤销已推送的提交

```bash
# 使用 revert（推荐，安全）
git revert <commit-hash>
git push origin <分支名>
```

### 6.4 合并冲突解决

当 `git merge` 出现冲突时：

```bash
# 1. Git 会提示冲突文件，手动编辑文件解决 <<<< ==== >>>> 标记
# 2. 标记冲突已解决
git add <文件名>

# 3. 完成合并
git commit -m "解决合并冲突"

# 放弃合并
git merge --abort
```

### 6.5 不小心执行了 reset --hard

```bash
# 使用 reflog 找回之前的提交
git reflog

# 找到要恢复的 commit-hash，然后
git reset --hard <commit-hash>
```

### 6.6 修改了最近几次提交

```bash
# 交互式 rebase，压缩/修改/删除最近 N 次提交
git rebase -i HEAD~3
```

---

## 七、Git 工作流（常见协作模型）

### 7.1 Git Flow（经典分支模型）

| 分支 | 用途 |
| --- | --- |
| `main` / `master` | 生产环境代码 |
| `develop` | 开发集成 |
| `feature/*` | 新功能开发 |
| `release/*` | 发布准备 |
| `hotfix/*` | 紧急修复 |

### 7.2 GitHub Flow（简化模型，适合小型项目）

1. 从 `main` 创建分支
2. 在分支上开发并提交
3. 创建 Pull Request
4. 代码评审通过后合并回 `main`
5. 删除分支

### 7.3 日常开发推荐流程

```bash
# 1. 同步远程最新代码
git checkout main
git pull

# 2. 创建功能分支
git checkout -b feature/login

# 3. 开发并提交
git add .
git commit -m "feat: 实现登录功能"

# 4. 推送分支到远程
git push -u origin feature/login

# 5. 在远程平台创建 Pull Request

# 6. 评审通过后合并，删除分支
git branch -d feature/login
git push origin --delete feature/login
```

---

## 八、命令速查表

| 操作 | 命令 |
| --- | --- |
| 初始化仓库 | `git init` |
| 克隆仓库 | `git clone <url>` |
| 查看状态 | `git status` |
| 查看差异 | `git diff` |
| 添加到暂存区 | `git add .` |
| 提交 | `git commit -m "msg"` |
| 查看日志 | `git log --oneline --graph` |
| 创建分支 | `git branch <name>` |
| 切换分支 | `git checkout <name>` |
| 合并分支 | `git merge <name>` |
| 拉取远程 | `git pull` |
| 推送远程 | `git push` |
| 暂存改动 | `git stash` |
| 恢复改动 | `git stash pop` |
| 撤销提交 | `git revert <hash>` |
| 回退版本 | `git reset --hard <hash>` |
| 查看远程 | `git remote -v` |
| 打标签 | `git tag -a v1.0 -m "msg"` |

---

## 九、参考资源

- **官方文档**：[https://git-scm.com/doc](https://git-scm.com/doc)
- **Pro Git 中文版**：[https://git-scm.com/book/zh/v2](https://git-scm.com/book/zh/v2)
- **GitHub 官方文档**：[https://docs.github.com](https://docs.github.com)
- **交互式 Git 学习**：[https://learngitbranching.js.org](https://learngitbranching.js.org)
- **Git 命令速查（图）**：[https://ndpsoftware.com/git-cheatsheet.html](https://ndpsoftware.com/git-cheatsheet.html)

---

> 本文档持续更新中，如有错误或建议欢迎指正。
