#!/bin/bash

docker build -t flask . && docker run -d -p 1337:80 flask

