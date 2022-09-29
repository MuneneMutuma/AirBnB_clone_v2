#!/usr/bin/python3

from fabric.operations import local

def do_pack():
    with lcd ("/tmp"):
        local("git clone https://github.com/MuneneMutuma/AirBnB_clone.git")
        local(f"tar -cfv ~/alx/AirBnB_clone_v2/name.tar ./AirBnB_clone/*")
    
    return "~/alx/AirBnB_clone_v2/name.tar"
