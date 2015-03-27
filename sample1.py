#!/usr/bin/env python
from fabric import *

env.user='root'
env.password='111111'
env.hosts=['192.168.10.236','192.168.10.239']

@runs_once
def local_task():
	local("uname -a")

def remote_task():
		run("date")

