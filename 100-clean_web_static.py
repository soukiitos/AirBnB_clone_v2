#!/usr/bin/python3
'''Delete out-of-date archives, using the function do_clean'''
from fabric.api import *
import os

env.hosts = ['100.26.249.88', '100.26.50.67']


def do_clean(number=0):
    num = 1 if int(num) == 0 else int(num)
    archive = sorted(os.listdir("versions"))
    [archive.pop() for i in range(num)]
    with lcd("versions"):
        [local("rm ./{}".format(j)) for j in archive]
    with cd("/data/web_static/releases"):
        archive = run("ls -tr").split()
        archive = [j for j in archive if "web_static"_" in j]
        [archive.pop() for i in range(num)]
        [run("rm -rf ./{}".format(j)) for j in archive]
