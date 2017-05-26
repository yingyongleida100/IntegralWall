#!/usr/bin/env bashs
killall -s INT uwsgi;
sleep 3s
rm -rf /home/lizhenyi/Jobs/Code/Python/IntegralWall/*.log
uwsgi /home/lizhenyi/Jobs/Code/Python/IntegralWall/Uwsgi/uwsgiApiWeb.ini;

sleep 2s

echo $'\n=====ps aux |grep uwsgi======\n'
ps aux |grep uwsgi
echo $'\n=====netstat -ntpl===========\n'
netstat -ntpl
echo $'\n\n'

perl -pe 'eof&&s/$/\n\n===================\n/' /home/lizhenyi/Jobs/Code/Python/IntegralWall/*.log