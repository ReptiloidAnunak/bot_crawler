#!/bin/bash


docker build -t bot_cool_crawler .
docker run -it --env-file .env bot_cool_crawler


