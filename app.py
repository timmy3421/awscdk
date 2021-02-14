#!/usr/bin/env python3

from aws_cdk import core
from aws_cdk.core import Aws

from awscdk.awscdk_stack import AwscdkStack

'''
    Aws.accontId & Aws.region are derived from the account and region that this stack is being deployed into
'''
# env = core.Environment(account=Aws.accountId, region=Aws.region)
'''
    The line below can be used to `cdk synth` and output the correct 'APP_ENV' as a test. Above is the prod code
    that will derive the accountid and region from where this cdk is deployed to/in
'''
env = core.Environment(account='1234567', region='us-west-2')

app = core.App()
AwscdkStack(app, "awscdk-parameterstore-build", env=env)

app.synth()
