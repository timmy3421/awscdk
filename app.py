#!/usr/bin/env python3

from aws_cdk import core
from aws_cdk.core import Aws

from awscdk.awscdk_stack import AwscdkStack

#accounts
#account personal
#aws_account_id = "393365708829"
#account sandbox
#aws_account_id = "974851384123"
#account non-prod
aws_account_id = "935961962045"
#account prod
#aws_account_id = "000000000000"

#regions, uncomment region needed
#Oregon
aws_region = "us-west-2"
#North California
#aws_region = "us-west-1"
#N. Virginia
#aws_region = "us-east-1"
'''
    Aws.accontId & Aws.region are derived from the account and region that this stack is being deployed into
'''
env = core.Environment(account=aws_account_id, region=aws_region)
'''
    The line below can be used to `cdk synth` and output the correct 'APP_ENV' as a test. Above is the prod code
    that will derive the accountid and region from where this cdk is deployed to/in
'''
#env = core.Environment(account='1234567', region='us-west-2')

app = core.App()
AwscdkStack(app, "awscdk-parameterstore-build", env=env)

app.synth()
