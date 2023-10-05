#!/usr/bin/python3
"""
Distribute an archive to our web servers,
using the function do_deploy
"""
from datetime import datetime
import os
from fabric.api import local, runs_once

env.host = ["100.26.249.88", "100.26.50.67"]
env.usr = "ubuntu"


@runs_once
def do_pack():
    '''Define do_pack()'''
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    curr_time = datetime.now()
    result = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            curr_time.year,
            curr_time.month,
            curr_time.day,
            curr_time.hour,
            curr_time.minute,
            curr_time.second
            )
    try:
        print("Packing web_static to {}".format(result))
        local("tar -cvzf {} web_static".format(result))
        size = os.stat(result).st_size
        print("web_static packed: {} -> {} Bytes".format(result, size))
    except Exception:
        result = None
    return result


@runs_once
def do_deploy(archive_path):
    '''Define do_deploy()'''
    if not os.path.exists(archive_path):
        return False
    fn_ext = os.path.basename(archive_path)
    fn_ext_not = os.path.splitext(fn_ext)
