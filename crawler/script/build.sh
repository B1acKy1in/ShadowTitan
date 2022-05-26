#! /bin/bash

pip freeze > static/requirements.txt

docker build -t titan/crawler:1.0 .