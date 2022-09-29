#!/usr/bin/python3
"""module for compressing web_static folder"""


from fabric.api import local, lcd
import datetime


def do_pack():
    """packs web_static folder into a tar.gz archive"""

    now = datetime.datetime.now()
    file_name = "web_static_{:02d}{:02d}{:02d}{:02d}{:02d}{:02d}".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second)
    local("mkdir -p versions")
    with lcd("/tmp"):
        local("git clone https://github.com/MuneneMutuma/AirBnB_clone.git")
        local(f"tar czfv ~/alx/AirBnB_clone_v2/versions/{file_name}\
                ./AirBnB_clone/web_static")
        return f"~/alx/AirBnB_clone_v2/versions/{file_name}"

    return None


def reset():
    """resets, and removes the clone"""
    with lcd("/tmp"):
        local("rm -rf AirBnB_clone")
