#!/usr/bin/python3
# a Fabric script that generates a .tgz archive from the contents
# of the web_static folder of your AirBnB Clone repo,
# using the function do_pack.

from datetime import datetime
from fabric.api import local


def do_pack():
    """ a function that generates a .tgz archive """

    try:
        now = datetime.now()
        local("mkdir -p versions")
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
                now.year, now.month, now.day, now.hour,
                now.minute, now.second)
        local("tar -czvf versions/{} web_static".format(archive_name))
        return archive_name
    except Exception:
        return None

#    time_format = "%Y%m%d%H%M%S"
#    time = datetime.now().strftime("time_format")
#    archive_name = "web_static_" + time +  ".tgz"
#    local("tar -czvf versions/{} web_static".format(archive_name))
