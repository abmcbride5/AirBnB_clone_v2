#!/usr/bin/python3
import os
from fabric.api import *

def do_deploy(archive_path):

    if not os.path.exist(archive_path):
        return False
    put(archive_path, "/tmp/")
    list1 = archive_path.split('.')
    print(list1)
