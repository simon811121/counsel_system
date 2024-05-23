#!/bin/bash

# Change directory to the location of the script
cd "$(dirname "$0")"
pwd

# test main page
chmod +x test_main.sh
./test_main.sh

# test api page
chmod +x test_api.sh
./test_api.sh