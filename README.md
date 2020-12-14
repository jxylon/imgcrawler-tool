# imgcrawler-爬虫工具

#### 1. 环境安装

+ Python 3

+ 库

  + pip install -r requirements.txt

+ 运行

  + python imagecrawler/main.py
  

#### 2. 功能列表

+ 更改存储路径
  + 选择文件夹作为存储图片的目录。

+ 模式
  + 模式一：爬取百度图片
    + 该模式下网址固定为百度图片，**关键词必须**。
  + 模式二：爬取任意网址的图片
    + 该模式下**网址必须**，无需关键词。
+ 审核
  + 选择文件夹，浏览目录下的图片，可用的留下，不可用的删去。
+ 图片重命名
  + 该功能涉及到“重命名图片后缀”和“重命名起始数字”两个参数。
  + **若“重命名图片后缀为"all"**，图片重命名为后缀保持不变，文件名从“重命名起始数字“开始递增。
  + 若"重命名图片后缀"不为“all”，图片重命名后的后缀为该指定的后缀，文件名从“重命名起始数字“开始递增。
+ 标注
  + 该功能为labelimg的代码。
+ 设置：与imgcralwer/settings.txt参数保持一致
  + time_step：爬取间隔
  + start_page：起始爬取页面（仅模式一可用）
  + page_num：爬取页面数（仅模式一可用）
  + file_suffix：重命名图片后缀
  + start_num：重命名起始数字
  + 待补充
+ 停止爬虫
  + 如果你不想运行爬虫了，可以停止爬虫。

#### 3. 使用方法

+ 爬取图片

  1. 选择图片存储路径

  2. 选择模式
  3. 设置 - 修改参数
  4. 输入网址/关键词
  5. 点击开始爬取（过程中可以停止爬虫）

+ 审核
  1. 待爬取完毕，点击审核
  2. 选择文件夹 - 打开
  3. 审核图片，通过 - 下一张（快捷键D），不通过 - 删除（快捷键S），上一张的快捷键是A

+ 图片重命名
  1. 设置 - 重命名后缀修改为all
  2. 选择文件夹 - 重命名
  3. 打标签
  4. 打完标签后，设置 - 重命名后缀修改为jpg
  5. 选择文件夹 - 重命名

#### 4. 提交记录

- 2020.7.14
  - 修改了设置后缀名为空出错的bug。
  - 修改了“删除”之后“上一页”和“下一页”不可用的bug。
  - 添加了“上一页”、“删除”、“下一页”的快捷键。
  - 修改了“审核”时窗口一直为全屏（但是不能按缩小键）。
  - 增加了参数“爬取起始页面”。
- 2020.7.15
  - 修改了模式一关键词不能为空。
  - 优化了”设置“选项。
- 2020.7.21
  - 修改了重命名后缀不为all时，重命名乱序的问题。

#### 5. 问题

+ 如果遇到问题

  ```
  	assert(stringId in self.idToMessage), "Missing string id : " + stringId
  AssertionError: Missing string id : useDefaultLabel
  ```
  
  请进入“x:\xxx\imgcrawler-tool\imgcrawler\labelImg”文件夹，运行命令
  
  ```
  pyrcc5 -o resources.py resources.qrc
  ```