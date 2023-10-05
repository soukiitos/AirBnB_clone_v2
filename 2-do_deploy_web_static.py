#!/usr/bin/python3
"""
Distribute an archive to our web servers,
using the function do_deploy
"""
from datetime import datetime
import os
from fabric.api import *

env.hosts = ["100.26.249.88", "100.26.50.67"]
env.user = "ubuntu"


def do_pack():
    '''Define do_pack()'''
    local("mkdir -p versions")
    curr_time = datetime.now().strftime("%Y%m%d%H%M%S")
    path_archived = "versions/web_static_{}.tgz".format(curr_time)
    tgz_archive = local("tar -cvzf {} web-static".format(path_archived))
    if not tgz_archive.succeeded:
        return None
    else:
        return path_archived


def do_deploy(archive_path):
    '''Define do_deploy()'''
    if os.path.exists(archive_path):
        archived__file = archive_path[9:]
