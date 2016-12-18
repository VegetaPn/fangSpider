# fangSpider  

## 房天下——北京——住宅&别墅&商铺&写字楼 Spider项目  

### 需求  
抓取北京住宅&别墅&商铺&写字楼的以下信息存于数据库中：   

- 住宅&别墅：

1. 建筑面积
2. 当前户数
3. 容积率
4. 绿化率
5. 所属区域（1期新增）
6. 环线位置（1期新增） 


- 商铺&写字楼：

1. 物业类别
2. 建筑面积
3. 停车位信息   

### 说明  
本项目为Python项目，用到了Django框架。所以机器要满足运行Python、Django以及MySQL的基本条件。并且要装有pip（Python的包管理，用来安装和管理类库）

### 主要运行环境  
1. Python 2.7
2. MySQL 没有严格版本要求
3. Django 版本为1.9

### 安装和配置  
安装：  

1. 装好Python2.7和MySQL
1. 执行pip --version，若报错则安装pip
2. 满足2之后，进入项目目录，执行pip install -r requirements.txt  

配置：  

1. 修改fangSpider/settings.py文件中的DATABASES部分，改为自己数据库的配置（NAME-数据库名称，USER-数据库用户名，PASSWORD-密码）
2. 修改main.py和grab\_urls.py文件的PATH\_TO\_PROJECT变量值为当前项目的绝对路径

### 第一次运行  
注意：第一次运行时需要做以下步骤： 

1. 安装和配置
2. 进入项目目录
2. 执行python manage.py makemigrations
3. 执行python manage.py migrate
3. 执行python grab_urls.py 抓取列表和url到数据库
4. 执行python main.py 开始爬取数据

以后再运行时直接执行第2、6步即可。  

### 运行结果  
爬取得到的数据经过解析会保存到数据库中以fspider_开头的表中。

### 项目架构  
本项目采用了Django提供的目录结构，并且采用Django提供的ORM作为数据库操作工具。  

- fangSpider/settings.py 为配置文件
- fspider中的models.py为数据模型，和数据库表对应
- fspider中的views.py为业务逻辑，包含所有的数据抓取、解析模块
