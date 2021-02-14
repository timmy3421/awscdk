from aws_cdk import core as _core
import jmespath
from pprint import pprint

'''
    This is an app level config that will use the Aws.accountId & Aws.region as verification to map other
    AWS required static values. In this specific case the VPC ID.
'''
APP_ENVS = {
    "app_envs": [
        {
            "aws_account": 1234567,
            "stage": 'production',
            "regions": {
                "us-west-2": {
                    "vpc_id": "vpc-1234"
                }
            }
        },
        {
            "aws_account": 7890123,
            "stage": 'staging',
            "regions": {
                "us-west-2": {
                    "vpc_id": "vpc-1234"
                }
            }
        },
        {
            "aws_account": 4567890,
            "stage": 'development',
            "regions": {
                "us-west-2": {
                    "vpc_id": "vpc-1234"
                }
            }
        }
    ]
}


class AwscdkStack(_core.Stack):

    def __init__(self, scope: _core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        '''
            With the super() constructor above the following are already set due to passing them in during class creation 
        '''
        print(self.account)
        print(self.region)

        '''
            The jmespath search below will take the 'env' passed from app.py and use it to derive the 
            application environment mapping from the global var 'APP_ENVS'
            
            Note that this search can be enhanced to filter both the accountid and region to just retrun the 
            exact items you need. Now it just returns everything for the accountid.
            
            
        '''
        app_env_dict = jmespath.search(f"app_envs[?aws_account == `{self.account}`]|[0]", APP_ENVS)
        '''
            RUN: `cdk synth` to see what the output of the code below
        '''
        pprint(app_env_dict)

        # The code that defines your stack goes here
