#! /bin/bash

cd src
uvicorn main:app --port 666 --reload