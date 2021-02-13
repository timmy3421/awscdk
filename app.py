#!/usr/bin/env python3

from aws_cdk import core

from awscdk.awscdk_stack import AwscdkStack

#accounts
#account personal
#aws_account_id = "00000000000"
#account sandbox
aws_account_id = "00000000000"
#account non-prod
#aws_account_id = "000000000000"
#account prod
#aws_account_id = "000000000000"

#regions, uncomment region needed
#Oregon
aws_region = "us-west-2"
#North California
#aws_region = "us-west-1"
#N. Virginia
#aws_region = "us-east-1"

#vpcs, uncomment vpc needed. 
#Personal N. Virginia
#available_vpc_id = "vpc-random23223"
#Sandbox Oregon
available_vpc_id = "vpc-random23223"

#N. Virginia
#aws_region = "us-east-1"

globalenv = core.Environment(account=aws_account_id, region=aws_region)

app = core.App()
AwscdkStack(app, "awscdk-parameterstore-build",env=globalenv)

app.synth()
