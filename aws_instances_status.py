import subprocess
from collections import defaultdict
from sqlite3 import Timestamp
from pythonjsonlogger import jsonlogger
import json
import boto3
import terminal_output_messages as tm
import datetime
import os.path
from dotenv import load_dotenv, find_dotenv



load_dotenv(find_dotenv())

INSTANCE_NAME = "k8s.io/role/master"
STATE = 'running' # Possible values: running, stopped, pending, stopping
aws_access_key_id_env = os.environ['KEY_ID']
aws_secret_access_key_env = os.environ['ACCESS_KEY']


"""
A tool for retrieving basic information from the running EC2 instances.
"""
session = boto3.Session(
    aws_access_key_id=aws_access_key_id_env,
    aws_secret_access_key=aws_secret_access_key_env,
)


# Connect to EC2
ec2 = session.resource('ec2', 'eu-west-1',

                    )

status_timestamp = datetime.datetime.now()

def get_all_instance_info(instance_name=INSTANCE_NAME, state=STATE, search_by_specific_name= True):

    instance_log = []

    # Get information for all running instances
    running_instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': [f'{state}']}])

    ec2info = defaultdict()
    for instance in running_instances:
        for tag in instance.tags:
            if 'Name'in tag['Key']:
                if search_by_specific_name is True and tag['Value'] in instance_name:
                    name = tag['Value']

                    instance_full_info = ec2info[instance.id] = {
                            'Name': name,
                            'Type': instance.instance_type,
                            'State': instance.state['Name'],
                            'Private IP': instance.private_ip_address,
                            'Public IP': instance.public_ip_address,
                            'Launch Time': str(instance.launch_time),
                            'Request timestamp': status_timestamp.strftime("%Y-%m-%d %H:%M:%S")
                        }


                    attributes = ['Name', 'Type', 'State', 'Private IP', 'Public IP', 'Launch Time', 'Request timestamp']
                    for instance_id, instance in ec2info.items():
                        for key in attributes:
                            print(("\t \t {0}: {1}".format(key, instance[key])))
                        print(f"{tm.ok_message}----------------------------------------------")


                        with open('/usr/src/app/instance_log_file.json', 'w') as f:
                            print(f"{tm.ok_message} The json file is created")
                            json.dump(instance_full_info, f, indent=2)

                        return instance_full_info






print(get_all_instance_info())
# Removing from Image config.json and .env files.
subprocess.check_call(["rm -rf /aws-state-app-helm/config.json"], shell=True)
subprocess.check_call(["rm -rf .env"], shell=True)
subprocess.check_call(["rm -rf .githubtoken"], shell=True)

