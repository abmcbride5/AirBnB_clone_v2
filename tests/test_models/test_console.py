#!/usr/bin/python3
""" test console"""
import unittest
import os
import console
import models
import MySQLdb


class TestConsole(unittest.TestCase):
    """ this test that the console is working with update"""

    def Test_create_fs(self):
        """ test do create with classes"""
        state_objects = models.storage.all(State)
        l = len(state_objects)
        os.system('echo create State name=\"California\" | ./console')
        state_after = models.storage.all(State)
        new_l = len(state_after)
        self.assertTrue(new_l > l)

        amenity_objects = models.storage.all(Amenity)
        am_len = len(amenity_objects)
        os.sys('echo create Amenity name=\"Internet\"')
        amenity_ater = models.storage.all(Amenity)
        new_am_len = len(amenity_after)
        self.asserTrue(new_am_len > am_len)

    def Test_create_db(self):
        """ test creation of tables"""
        conn = MySQLdb.connet(host="localhost", user="hbnb_dev",
                              passwd="hbnb_dev_pwd", port=3306,
                              db="hbnb_dev_db", charset="utf8")
        cur = conn.cursor()
        cur.execute("SELECT * FROM states")
        count = cur.fetchall()
        state_count = len(count)
        os.system('echo create State name=\"Arizona\" | ./console')
        cur.execute("SELECT * FROM states")
        counter = cur.fetchall()
        new_state_count = len(counter)
        self.assertTrue(new_state_count > state_count)
