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
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_f_path = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(archived_f_path))
    if t_gzip_archive.succeeded:
        return archived_f_path
    else:
        return None


def do_deploy(archive_path):
    '''Define do_deploy()'''
    if os.path.exists(archive_path):
        archived__file = archive_path[9:]
