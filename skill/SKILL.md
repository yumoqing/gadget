---
name: gadget-repo
version: 1.0.0
description: gadget 仓库：30 个文件，主语言Python 8，Shell 3，JSON 1
trigger_conditions:
  - 需要理解、修改或排障 gadget 的代码
  - 在 gadget 里定位入口、数据表、对外契约或构建方式
---

# gadget 仓库技能

> 由仓库实际内容生成的骨架（README/目录/模型定义/契约/构建脚本逐项取证）。新增判断与坑位请直接在下面对应小节补充。

## 定位

**gadget**

a light wight web server base on aiohttp please look [ahserver](https://github.com/yumoqing/ahserver) to learn how to configure under "website" in the conf/config.json file, identify ssl with "crtfile" and "keyfile" like this. In the conf/config.json, need to config log, you need to identify "name",

- 远端：`https://github.com/yumoqing/gadget.git`
- 默认分支：`main`（共 36 个提交）
- 最近提交：2023-10-27 `aa05fba` bugfix
- 规模：30 个文件；Python 8，Shell 3，JSON 1

## 目录结构

- `src/` — 源码（9 个文件）
- `docs/` — 文档（6 个文件）
- `test/` — 测试（6 个文件）
- `ubuntu/` — 3 个文件
- `macos/` — 2 个文件
- `windows/` — 2 个文件
- 根文件：`README.md`、`requirements.txt`

## 构建与运行

- `requirements.txt`：10 项（ahserver、sqlor、apppublic、aiohttp、aiohttp-auth-autz、openpyxl）

## README 要点与注意（摘自 `README.md`）

- 章节：Documentation、Dependent、Download、Configuration、Test

## 建议阅读顺序

1. `README.md`
2. `docs/`

