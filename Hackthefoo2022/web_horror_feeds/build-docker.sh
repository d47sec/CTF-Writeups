#!/bin/bash
docker rm -f web_horror_feeds
docker build --tag=web_horror_feeds .
docker run -p 1337:1337 -p 5678:5678 --rm --name=web_horror_feeds web_horror_feeds