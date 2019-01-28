scrapy 爬虫学习
spider_learn 目录下的每个目录都是一个单独的项目

### 命令 创建一个项目
scrapy startproject tutorial

这将创建一个包含以下内容的tutorial目录：
tutorial/
    scrapy.cfg            # 部署配置文件

    tutorial/             # 项目的Python模块,你将在这里输入你的代码
        __init__.py

        items.py          # 项目的items定义文件

        middlewares.py    # 项目中间件文件

        pipelines.py      # 项目管道文件

        settings.py       # 项目设置文件

        spiders/          # 稍后放置spider的文件夹
            __init__.py

cd tutorial
scrapy genspider taptap taptap.com