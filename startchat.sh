#!/bin/sh
host=$1
session="chat"
tmux start-server
tmux new-session -d -s $session
tmux selectp -t 1
tmux send-keys "python chat.py $1 --msg" C-m
tmux splitw -v -p 2
tmux send-keys "python chat.py $1 --input" C-m
tmux attach-session -t $session