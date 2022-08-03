#!/usr/bin/env bash

python3 -m venv python-venvs/venv

source python-venvs/venv/bin/activate

python3 -m pip install                                    \
  jsii-0.0.0-py3-none-any.whl                             \
  -e generated-code/@scope/jsii-calc-base-of-base/python  \
  -e generated-code/@scope/jsii-calc-base/python          \
  -e generated-code/@scope/jsii-calc-lib/python           \
  -e generated-code/jsii-calc/python
