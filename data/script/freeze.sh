#!/bin/bash

cd ../src
workon data
pip freeze > requirements.txt
