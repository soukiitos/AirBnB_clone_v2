#!/usr/bin/python3
"""
Distribute an archive to our web servers,
using the function do_deploy
"""
from datetime import datetime
import os
from fabric.api import task, local, env, put, run

env.hosts = ['100.26.249.88', '100.26.50.67']


def do_pack():
    '''Define do_pack()'''
    d = datetime.now().strftime("%Y%m%d%H%M%S")
    mkdir = "mkdir -p versions"
    path = "versions/web_static_{}.tgz".format(d)
    print("Packing web_static to {}".format(path))
    if local("{} && tar -cvzf {} web_static".format(mkdir, path)).succeeded:
        return path
    return None


def do_deploy(archive_path):
    '''Define do_deploy()'''
    try:
        if not os.path.exists(archive_path):
            return False
        f_with_ext = os.path.basename(archive_path)
        f_with_no_ext, ext = os.path.splitext(f_with_ext)
        d_path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("rm -rf {}{}/".format(d_path, f_with_no_ext))
        run("mkdir -p {}{}/".format(d_path, f_with_no_ext))
        run("tar -xzf /tmp/{} -C {}{}/".format(
            f_with_ext, d_path, f_with_no_ext
            ))
        run("rm /tmp/{}".format(f_with_ext))
        run("mv {0}{1}/web_static/* {0}{1}/".format(d_path, f_with_no_ext))
        run("rm -rf {}{}/web_static".format(d_path,  f_with_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(
            d_path, f_with_no_ext
            ))
        print("New version deployed!")
        return True
    except Exception:
        return False
