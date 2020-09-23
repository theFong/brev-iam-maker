#!/usr/bin/env python3

from aws_cdk import core

from brev_iam_maker.brev_iam_maker_stack import BrevIamMakerStack


app = core.App()
BrevIamMakerStack(app, "brev-iam-maker")

app.synth()
