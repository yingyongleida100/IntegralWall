# IntegralWall
Ann9 IntegralWall Interface Demo

## Config

1.配置数据连接

    文件路径：Mongodb/Utilitys.py 
    修改变量mongodbServerIp 设置IP
    修改变量mongodbPort 设置端口号
2.配置uWsgi路径

    文件路径:Uwsgi/uwsgiApiWeb.ini
    将文件中的{Path}替换为项目的绝对目录  

3.配置启动路径

    文件路径:Uwsgi/restartApiWeb.sh
    将文件中的{Path}替换为项目的绝对目录 
    
4.数据库增加索引

    db.usersagent.createIndex({"isAcitve": 1, "iscallback": 1},{"background":true})
    db.usersagent.createIndex({"udid": 1, "dateCreated"：1},{"background":true})

## 依赖组件

    pip install pymongo
    pip install requests
  
## 启动

    启动Web服务
    sh ./Uwsgi/restartApiWeb.sh
    
    启动回调服务
    python ./Services/CallBackService.py
    


## 测试

    点击接口
    curl "http://ip:8081/?t=click&udid=b82c611c-41c8-11e7-a9dc-d017c28c4914&multipleurl=http://www.ann9.com&appid=12312345" |json_pp
    
    Check IDFA 接口
    curl "http://ip:8081/?t=checkidfa&idfa=b82c611c-41c8-11e7-a9dc-d017c28c4914&appid=12312345“ |json_pp
    
    客户端用户激活接口
    curl "http://ip:8081/?t=active&idfa=b82c611c-41c8-11e7-a9dc-d017c28c4914&appid=12312345“ |json_pp
    

    
   