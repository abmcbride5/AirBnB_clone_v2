#!/usr/bin/python3
""" generates .tgz archive"""
from fabric.api import local
import datetime


def do_pack():
    """ method that generates .tgz file"""
    local("mkdir -p versions")
    created_at = datetime.datetime.now()
    result = local("tar -zcvf versions/web_static_{}.tgz web_static".
                   format(created_at.strftime("%Y%m%d%H%M%S")))
    if results.failed:
        return None
    return results
