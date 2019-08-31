#!/usr/bin/python3
""" distributes archive """

from fabric.api import put, run, env
import os


env.hosts = ["35.231.48.168", "35.190.138.82"]


def do_deploy(archive_path):
    """ method to distribute archive """
    if not os.path.exists(archive_path):
        return False
    al = archive_path.split(".")
    cn = al[0].split("/")
    load = put(archive_path, "/tmp/{}.tgz".format(cn[1]))
    if load.failed:
        return False
    download = run("mkdir -p /data/web_static/releases/{}/".format(cn[1]))
    if download.failed:
        return False
    compress = run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".
                   format(cn[1], cn[1]))
    if compress.failed:
        return False
    remove = run("rm /tmp/{}.tgz".format(cn[1]))
    if remove.failed:
        return False
    move = run("mv /data/web_static/releases/{}/web_static/*\
               /data/web_static/releases/{}".format((cn[1]), (cn[1])))
    if move.failed:
        return False
    dir_remove = run("rm -rf /data/web_static/releases/{}/web_static".
                     format(cn[1]))
    if dir_remove.failed:
        return False
    dir_remove2 = run("rm -rf /data/web_static/current")
    if dir_remove2.failed:
        return False
    link = run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
               format(cn[1]))
    if link.failed:
        return False
    return True
