#!/usr/bin/python3
"""Pack and deploy remotely"""


from fabric.api import *
from datetime import datetime
from fabric.operations import run, put, sudo
import os
env.hosts = ['44.192.72.216', '44.192.52.223']


def do_pack():
    """
        generates a .tgz archine from contents of web_static
    """
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_name = "versions/web_static_{}.tgz".format(time)
    try:
        local("mkdir -p ./versions")
        local("tar --create --verbose -z --file={} ./web_static"
              .format(file_name))
        return file_name
    except Exception:
        return None


def do_deploy(archive_path):
    """
        using fabric to distribute archive
    """
    if os.path.isfile(archive_path) is False:
        return False
    try:
        archive = archive_path.split("/")[-1]
        path = "/data/web_static/releases"
        put("{}".format(archive_path), "/tmp/{}".format(archive))
        folder = archive.split(".")
        sudo("mkdir -p {}/{}/".format(path, folder[0]))
        new_archive = '.'.join(folder)
        sudo("tar -xzf /tmp/{} -C {}/{}/"
             .format(new_archive, path, folder[0]))
        sudo("rm /tmp/{}".format(archive))
        sudo("mv {}/{}/web_static/* {}/{}/"
             .format(path, folder[0], path, folder[0]))
        sudo("rm -rf {}/{}/web_static".format(path, folder[0]))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -sf {}/{} /data/web_static/current"
             .format(path, folder[0]))
        return True
    except Exception:
        return False


def deploy():
    """ready to deploy??"""
    path = do_pack()
    if path is not None:
        return (do_deploy(path))
    return (False)
