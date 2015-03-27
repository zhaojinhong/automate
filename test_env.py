#!/usr/bin/env python
from fabric.api import *

env.user='huizhong'
env.port='51226'
env.password='PHWuYou!20@15#03$'
env.hosts=['10.10.10.25','10.10.10.26','10.10.10.27','10.10.10.28','10.10.10.29''10.10.10.30','10.10.10.31']

@runs_once
def local_task():
	local("uname -a")

def remote_task():
		run("date")

