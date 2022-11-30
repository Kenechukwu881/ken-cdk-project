from aws_cdk import (
    # Duration,
    aws_s3 as _s3,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

class KenCdkProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        _s3.Bucket(
            self,
            "myBucketid",
            bucket_name="myfirstcdkprojectbucket1001",
            versioned=True,
            # encryption=_s3.BucketEncryption.KMS

        )

        # example resource
        # queue = sqs.Queue(
        #     self, "KenCdkProjectQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
