#!/bin/bash

# Testing API
API_VER="api/v1"

echo
echo "===Hello page==="
url="http://127.0.0.1:5000/"$API_VER"/hello"
curl $url
echo
#==================================================
echo
echo "===Login page==="
url="http://127.0.0.1:5000/"$API_VER"/login"
curl -X POST -H "Content-Type: application/json" -d "@input/login.json" $url
echo
#==================================================
echo
echo "===Logout page==="
url="http://127.0.0.1:5000/"$API_VER"/logout"
curl $url
echo
#==================================================
echo
echo "===Account page==="
echo "---Post---"
url="http://127.0.0.1:5000/"$API_VER"/account"
curl -X POST -H "Content-Type: application/json" -d "@input/login.json" $url
echo
echo "---Get---"
url="http://127.0.0.1:5000/"$API_VER"/account"
curl -X GET $url
echo
echo "---account id---"
id="123456789"
url="http://127.0.0.1:5000/"$API_VER"/account/"$id
echo "---GET---"
curl -X GET $url
echo "---PUT---"
curl -X PUT $url
echo
#==================================================
echo
echo "===Password page==="
echo "---Forget---"
url="http://127.0.0.1:5000/"$API_VER"/password/forget"
curl -X POST $url
echo "---Setup---"
url="http://127.0.0.1:5000/"$API_VER"/password/setup"
echo "---GET---"
curl -X GET $url
echo "---POST---"
curl -X POST $url
echo
#==================================================