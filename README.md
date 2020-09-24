# Sagemaker Iams creator for Brev

- Creates a _user_ with minimal priviledge to
  - create training jobs
  - create models
  - deploy models as a sagemaker endpoint
  - invoke model endpoints
- Creates a _role_ with minimal priviledge for training jobs to
  - retrieve a dataset from a s3 bucket with "sagemaker" in its name
  - output model artifacts to an s3 bucket with "sagemaker" in its name

To use this,

1. Clone the repo and follow the [setup instrustions for CDK](#aws-cdk-setup).
2. Strengthen the IAM policies as you see fit in `/policies/sagemaker` (will work as is)
3. Run `cdk synth && cdk deploy`
4. The previous command will ouput in the console
   - `brev-iam-maker.accesskeyid` => aws_access_key_id
   - `brev-iam-maker.secretaccesskey` => aws_secret_access_key
   - `brev-iam-maker.iamrole` => training role name

## AWS CDK Setup

Read more about [aws cdk here](https://aws.amazon.com/cdk/)

This project is set up like a standard Python project. The initialization
process also creates a virtualenv within this project, stored under the .env
directory. To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package.

To create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .env
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .env/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .env\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

Next deploy the CloudFormation and show the resulting outputs.

```
$ cdk deploy
```

## Useful CDK commands

- `cdk ls` list all stacks in the app
- `cdk synth` emits the synthesized CloudFormation template
- `cdk deploy` deploy this stack to your default AWS account/region
- `cdk diff` compare deployed stack with current state
- `cdk docs` open CDK documentation

Enjoy!
