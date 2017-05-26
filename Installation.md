##1.系统工具安装

    yum groupinstall "Development Tools" -y
    yum install epel-release -y
    yum install -y python-pip
    yum install net-tools -y
    yum install vim -y
    yum install wget -y
    yum install zlib-devel -y
    yum install libuuid-devel -y
    yum install python-devel -y
    yum install python-sphinx -y
    yum install psmisc -y
    yum -y install bind-utils
    pip install pymongo
    pip install requests
    pip install uwsgi


##2.安装MongoDB


    echo "[mongodb-org-3.4]
    name=MongoDB Repository
    baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.4/x86_64/
    gpgcheck=1
    enabled=1
    gpgkey=https://www.mongodb.org/static/pgp/server-3.4.asc" >/etc/yum.repos.d/mongodb-org-3.4.repo
    
    sudo yum install -y mongodb-org
    sudo service mongod start
    
    
    

