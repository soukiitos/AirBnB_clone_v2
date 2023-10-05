#!/usr/bin/python3
"""
creates and distributes an archive to your web servers,
using the function deploy
"""
from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir

env.hosts = ['100.26.249.88', '100.26.50.67']


def do_pack():
    '''Define do pack'''
    try:
        d = datetime.now.strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        f_name = "versions/web_static_{}.tgz".format(d)
        local("tar -cvzf {} web_static_{}".format(f_name))
        return f_name
    except Exception:
        return None


def do_deploy(archive_path):
    '''Define do deploy()'''
    if exists(archive_path) is False:
        return False
    try:
        n_file = archive_path.split("/")[-1]
        n_ext = n_file.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, n_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(n_file, path, n_ext))
        run('rm /tmp/{}'.format(n_file))
        run('mv {0}{1}/web_static/* {0}{1}'.format(path, n_ext))
        run('rm -rf {}{}/web_static'.format(path, n_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, n_ext))
        return True
    except Exception:
        return False


def deploy():
    '''Define deploy()'''
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
