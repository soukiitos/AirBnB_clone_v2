#!/usr/bin/python3
"""
Generate a .tgz archive from the contents of the web_static folder
of our AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local, runs_once
from datetime import datetime
import os


@runs_once
def do_pack():
    '''Define do_pack()'''
    if not os.path.exists("versions"):
        os.mkdir("versions")
    timest = datetime.now()
    res = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            timest.year,
            timest.month,
            timest.day,
            timest.hour,
            timest.minute,
            timest.second
            }
    try:
        c.local("tar -czvf versions/{} web_static".format(res))
        res_path = os.path.join("versions", res)
        return res_path
    except Exception:
        return None
