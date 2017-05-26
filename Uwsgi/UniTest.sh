#!/usr/bin/env bash

#processUserClick

curl "http://127.0.0.1:8081?t=click&udid=3b9961e640fa11e7a9dcd017c28c4914&multipleurl=http://www.ann9.com&appid=12312345"|pjson
curl "http://127.0.0.1:8081?t=checkidfa&idfa=b82c611c-41c8-11e7-a9dc-d017c28c4914&appid=12312345" |pjson
curl "http://127.0.0.1:8081?t=active&idfa=b82c611c-41c8-11e7-a9dc-d017c28c4914&appid=12312345" |pjson
