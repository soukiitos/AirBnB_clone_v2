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
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    d_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            d_time.year,
            d_time.month,
            d_time.day,
            d_time.hour,
            d_time.minute,
            d_time.second
            )
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, size))
    except Exception:
        output = None
    return output
