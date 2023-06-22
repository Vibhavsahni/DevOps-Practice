'''This program schedules the Ec2 status checks
 to run automatically every 5 minutes. We've used the Schedule 1.2.0 library'''

import boto3
import schedule
ec2_client = boto3.client('ec2', region_name= "us-east-1")
ec2_resource = boto3. resource ('ec2', region_name="us-east-1")

def check_ins_status():
    statuses=ec2_client.describe_instance_status(IncludeAllInstances=True)

    for status in statuses['InstanceStatuses']:
        ins_status = status['InstanceStatus']['Status']
        sys_status = status['SystemStatus']['Status']
        state = status['InstanceState']
        print(f"Instance {status['InstanceId']} is {state['Name']} , "
              f"status is {ins_status} and system status of this "
              f"instance is {sys_status}")
    print("____________________________________________________\n")


schedule.every(5).minutes.do(check_ins_status)

while True:
    schedule.run_pending()