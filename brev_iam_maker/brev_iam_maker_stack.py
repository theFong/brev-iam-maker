import typing
import json

from aws_cdk import core
import aws_cdk.aws_iam as Iam

class BrevIamMakerStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        user = Iam.User(self, "brev-user")

        policy_json = get_role_policy_json()
        policy_document = Iam.PolicyDocument.from_json(policy_json)

        role = Iam.Role(self, "brev-role", inline_policies={"brev-policy": policy_document}, assumed_by=Iam.ServicePrincipal("sagemaker.amazonaws.com"))

        policy_statements = get_user_policy_statements()
        allow_role_statement = Iam.PolicyStatement(actions=["iam:GetRole", "iam:PassRole"], effect=Iam.Effect.ALLOW, resources=[role.role_arn])
        policy_statements.append(allow_role_statement)

        policy = Iam.Policy(self, "brev-policy", statements=policy_statements)
        policy.attach_to_user(user)

        access_key = Iam.CfnAccessKey(self, 'brev_access_key', user_name=user.user_name)

        core.CfnOutput(self, "access_key_id", value=access_key.ref)
        core.CfnOutput(self, "secret_access_key", value=access_key.attr_secret_access_key)
        core.CfnOutput(self, "iam_role", value=role.role_name)


def get_user_policy_statements() -> typing.List[Iam.PolicyStatement]:
    policy_obj = get_user_policy_json()
    return [Iam.PolicyStatement.from_json(statement_obj) for statement_obj in policy_obj["Statement"]]
    
def get_user_policy_json() -> typing.Any:
    with open("policies/sagemaker/user.json", mode="r") as f:
        return json.load(f)

def get_role_policy_json() -> typing.Any:
    with open("policies/sagemaker/role.json", mode="r") as f:
        return json.load(f)

