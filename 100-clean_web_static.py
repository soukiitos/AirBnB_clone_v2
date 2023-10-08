#!/usr/bin/python3
'''Delete out-of-date archives, using the function do_clean'''
from fabric.api import task, local, env, put, run, runs_once
import os

env.hosts = ['100.26.249.88', '100.26.50.67']


def do_pack():
    '''Define do pack'''
    d = datetime.now().strftime("%Y%m%d%H%M%S")
    mkdir = "mkdir -p versions"
    path = "versions/web_static_{}.tgz".format(d)
    print("Packing web_static to {}".format(path))
    if local("{} && tar -cvzf {} web_static".format(mkdir, path)).succeeded:
        return path
    return None


@task
def do_deploy(archive_path):
    '''Define do deploy()'''
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


@task
def deploy():
    '''define deploy()'''
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)


@runs_once
def local_remove(number):
    '''define local_remove()'''
    local("ls -dt versions/* | tail -n +{} | sudo xargs rm -fr".format(number))


@task
def do_clean(number=0):
    '''define do_clean()'''
    if int(number) == 0:
        number = 1
    number = int(number) + 1
    local_remove(number)
    m_path = "/data/web_static/releases/*"
    run("ls -dt {} | tail -n +{} | sudo xargs rm -fr".format(m_path, number))
