import aws_cdk as core
import aws_cdk.assertions as assertions

from ken_cdk_project.ken_cdk_project_stack import KenCdkProjectStack

# example tests. To run these tests, uncomment this file along with the example
# resource in ken_cdk_project/ken_cdk_project_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = KenCdkProjectStack(app, "ken-cdk-project")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
