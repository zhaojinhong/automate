#!/usr/bin/env python
#-*- coding: UTF-8 -*-
from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

env.user='root'
env.password='111111'
env.hosts=['192.168.10.239']

@task

@runs_once
def tar_task():
	with lcd("/home/python"):
		local("tar -czf python.tar.gz sample*.py")
@task
def put_task():
		run("mkdir -p /home/python")
		with cd("/home/python"):
			with settings(warn_only=True):
				result = put("/home/python/python.tar.gz","/home/python/python")   #第一个参数为（上传文件）本地文件路径，第二个参数为（上传文件）目标服务器路径； 
			if result.failed and not confirm("put file failed,Continue[Y/N]?"):
				abort("Aborting file put task")
@task
def go():
	tar_task()
	put_task()
