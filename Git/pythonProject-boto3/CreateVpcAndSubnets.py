'''This program creates a custom VPC and custom
Subnets associated with'''


import boto3
ec2_client = boto3.client('ec2',region_name= "us-east-1")
ec2_resource = boto3. resource ('ec2', region_name="us-east-1")

#Grabbing values from existing VPC:
all_available_vpcs = ec2_client.describe_vpcs()
vpcs_dic = all_available_vpcs["Vpcs"]
number_of_vpcs = str(len(vpcs_dic))
print(f"Total Vpcs found: {number_of_vpcs}")
for vpc in vpcs_dic:
    print("VPC Found:" + vpc["VpcId"])
    vpc_cidr_block = vpc["CidrBlockAssociationSet"]
    for cidr_block_element in vpc_cidr_block:
        print("The IP CIDR of my default VPC is: " + cidr_block_element["CidrBlock"])


#Creating a custom VPC :
new_vpc = ec2_resource. create_vpc(
    CidrBlock="10.0.0.0/16"
)
new_vpc.create_subnet (
    CidrBlock="10.0.1.0/24"
)
new_vpc.create_subnet (
    CidrBlock="10.0.2.0/24"
)
new_vpc.create_tags(
    Tags= [
        {
            'Key': 'Name',
            'Value': 'my-vpc'
        }
    ]
)
