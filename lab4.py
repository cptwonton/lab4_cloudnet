import boto3
import os
import json
import datetime

# used to instantiate a client. one needed per service (RDS, S3, etc)
def makeclient(awstype):
    client = boto3.client(
                awstype,
                aws_access_key_id='AKIAJEGKZKCFU5TZ7WCQ',
                aws_secret_access_key='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',
                region_name='us-west-2'
            )
    return client

# RDS instance information
print('RDS: \n')
rds = makeclient('rds')
print(rds.describe_account_attributes())
print(rds.describe_db_instances())
print(rds.describe_db_log_files(DBInstanceIdentifier='cs436-dbs-oregon'))
print('\n\n')

# EB instance information
print('ElasticBeanStalk: \n')
ebs = makeclient('elasticbeanstalk')
response = ebs.describe_applications()
print('Elastic BeanStalk:', response['Applications'])
response = ebs.describe_environments()
print('Environments:', response['Environments'])
print('\n\n')

# ElastiCache information
print('ElastiCache: \n')
elasticache = makeclient('elasticache')
response = elasticache.describe_cache_clusters()
print('Elasticache Clusters:', response['CacheClusters'])
response = elasticache.describe_events(StartTime=datetime.datetime(2018,10,25), EndTime=datetime.datetime(2018,10,28))
print('Elasticache Events:', response['Events'])
print('\n\n')

# Elastic LB
print('Elastic LB: \n')
elb = makeclient('elb')
response = elb.describe_load_balancers()
print('Load Balancers:', response['LoadBalancerDescriptions'])
print('\n\n')

# VPC
print('VPC: \n')
#ec2_resource = boto3.resource('ec2', region_name='us-west-2')
ec2 = makeclient('ec2')
response = ec2.describe_regions()
print('Regions:', response['Regions'])
response = ec2.describe_availability_zones()
print('Availability Zones:', response['AvailabilityZones'])
response = ec2.describe_route_tables()
print('Route Tables:', response['RouteTables'])

#filters = [{'Name':'tag:Name', 'Values':['VPN*']}]
#vpcs = list(ec2_resource.vpcs.filter(Filters=filters))
#for vpc in vpcs:
#	response = ec2_client.describe_vpcs(
#		VpcIds=[
#			vpc.id,
#		]
#	)
#	print(json.dumps(response, sort_keys=True, indent=4))
print('\n\n')

os.system("pause")










