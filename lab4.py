import boto3
import os

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

# ElastiCache information
print('ElastiCache: \n')

# Elastic LB
print('Elastic LB: \n')

# VPC
print('VPC: \n')

print('\n\n')

print('done!')










