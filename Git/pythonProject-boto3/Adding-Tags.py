''' This program will add "Production" tags to all instances
in the region "us-east-1" and "Development" to all instances
in "ca-central-1" '''

import boto3
ec2_client_usa = boto3.client('ec2', region_name="us-east-1")
instances_info_usa = ec2_client_usa.describe_instances()
ec2_client_canada = boto3.client('ec2', region_name="ca-central-1")
instances_info_canada = ec2_client_usa.describe_instances()
instance_ids_usa = []
instance_ids_canada = []
reservations_usa = instances_info_usa['Reservations']
for res in reservations_usa:
    instances = res['Instances']
    for instance in instances:
        instance_ids_usa.append(instance['InstanceId'])
        response = ec2_client_usa.create_tags(

            Resources=instance_ids_usa
            ,
            Tags=[
                {
                    'Key': 'env',
                    'Value': 'Production'
                },
            ]
        )

reservations_canada = instances_info_canada['Reservations']
for res in reservations_canada:
    instances = res['Instances']
    for instance in instances:
        instances_info_canada.append(instance['InstanceId'])
        response = instances_info_canada.create_tags(
            
            Resources=instances_info_canada
            ,
            Tags=[
                {
                    'Key': 'env',
                    'Value': 'Development'
                },
            ]
        )