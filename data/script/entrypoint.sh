#! /bin/bash

cd app
nohup uvicorn main:app --reload --host 0.0.0.0 --port 9999 &