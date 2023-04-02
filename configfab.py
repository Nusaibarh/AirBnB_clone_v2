#!/usr/bin/python3
"""
    Fabric script that distributes an archive to my web servers
"""
from fabric.api import *
from fabric.operations import run, put, sudo
import os
env.hosts = ['44.192.72.216', '44.192.52.223']


def do_deploy(archive_path):
    """
        using fabric to distribute archive
    """
    if os.path.isfile(archive_path) is False:
        return False
    try:
        put("{}".format(archive_path), "/{}".format(archive))
        return True
    except:
        return False
