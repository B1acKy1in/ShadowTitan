#!/bin/bash

cd ../src
workon data
pip freeze > requestments.txt
