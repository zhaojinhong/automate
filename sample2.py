#!/usr/bin/env python
from fabric.api import *

env.user='root'
env.password='111111'
env.hosts=['192.168.10.236','192.168.10.239']

@runs_once
def input_raw():
	return prompt("please input directory name:",default="/home")
def worktask(dirname):
		run("ls -l "+dirname)
@task

def go():
	getdirname = input_raw()
	worktask(getdirname)

