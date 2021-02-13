from aws_cdk import core as _core
from aws_cdk import aws_ssm as _ssm


class AwscdkStack(_core.Stack):

    def __init__(self, scope: _core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        # Blake the example variable is available_vpc_id, it is supposed to transfer to this file. 
        vpc = _ssm.StringParameter(self,"sparklepony_vpc",parameter_name="sparklepony_vpc",string_value=available_vpc_id)
