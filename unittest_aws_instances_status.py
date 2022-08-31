import unittest
from wsgiref import validate
import aws_instances_status as ais
import pathlib as pl
import os



class TestStringMethods(unittest.TestCase):


    def test_existing_output(self):
        instance_log = ais.get_all_instance_info()
        self.assertIsNotNone(instance_log, True)

    def test_existing_keys(self):
        instance_log_dict = ais.get_all_instance_info()
        for key, value in instance_log_dict.items():
            attributes = ['Name', 'Type', 'State', 'Private IP', 'Public IP', 'Launch Time']
            if key in attributes:
                validation = True
            else:
                validation = False
            self.assertIsNotNone(validation, True)


        



if __name__ == '__main__':
    unittest.main()