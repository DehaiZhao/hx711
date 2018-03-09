#!/bin/sh
nohup python weight_server.py >/dev/null 2>&1 &
echo weight_server.py start done!!!
nohup python mp3_play_api.py >/dev/null 2>&1 & 
echo mp3_server.py start done!!!

