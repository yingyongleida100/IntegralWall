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
    
5.nginx 配置
    
    1.修改Uwsgi/uwsgiApiWeb.ini
    http = :9091 ->socket = :9091
    
    2.修改/etc/nginx/conf.d/default.conf
    
    server {
        client_max_body_size 4G;
        listen  80;  ## listen for ipv4; this line is default and implied
        server_name test.integralwall.com;

        location /{
        uwsgi_pass  127.0.0.1:9091;
        include /etc/nginx/uwsgi_params;
        }
    }


## 依赖组件

    pip install pymongo
    pip install requests
  
## 启动

    启动Web服务
    sh ./Uwsgi/restartApiWeb.sh
    
    启动回调服务
    python ./Services/CallBackService.py
    
    后台启动回调任务
    
    log.txt 为 记录日志文件
    
    nohup python ./Services/CallBackService.py >>log.txt 2>&1 &

    


## 测试

    点击接口
    curl "http://ip:8081/?t=click&udid=b82c611c-41c8-11e7-a9dc-d017c28c4914&multipleurl=http://www.ann9.com&appid=12312345" |json_pp
    
    Check IDFA 接口
    curl "http://ip:8081/?t=checkidfa&idfa=b82c611c-41c8-11e7-a9dc-d017c28c4914&appid=12312345“ |json_pp
    
    客户端用户激活接口
    curl "http://ip:8081/?t=active&idfa=b82c611c-41c8-11e7-a9dc-d017c28c4914&appid=12312345“ |json_pp
    

    
   