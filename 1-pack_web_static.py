#!/usr/bin/python3
"""
Generate a .tgz archive from the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local, runs_once
from datetime import datetime
import os


@runs_once
def do_pack():
    '''Define do_pack()'''
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    curr_time = datetime.now()
    result = "version/web_static_{}{}{}{}{}{}.tgz".format(
            curr_time.year,
            curr_time.month,
            curr_time.day,
            curr_time.hour,
            curr_time.minute,
            curr_time.second
            )
    try:
        print("The Package web_staic to {}".format(result))
        local("tar -cvzf {} web_static".format(result))
        s = os.stat(result).st_s
        print("web_static packed: {} -> {} Bytes".format(result, s))
    except Exception:
        result = None
    return result
