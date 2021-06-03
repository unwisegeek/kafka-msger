#!/bin/sh
session="chat"
tmux start-server
tmux new-session -d -s $session
tmux selectp -t 1
tmux send-keys "python chat.py --msg" C-m
tmux splitw -v -p 2
tmux send-keys "python chat.py --input" C-m
tmux attach-session -t $session