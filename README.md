# How to reproduce

The bug does not manifest consistently, so good luck...

In order to have the right prerequisites for type checking to succeed, you need
to:

1. Run `./prepare-venv.sh` so the right Python virtual environment is populated
1. Either `./run-test.sh`, or open the `generated-code` folder in VS Code with
   Pylance or PyRight extensions enabled (type checking set to `basic`)

## Error information

The unexpected "Duplicate base class not allowed" error show up on this line:

https://github.com/RomainMuller/pyright-dublicate-base-error/blob/9f0067283b44fae09b5b3a513efa12b411513135/generated-code/jsii-calc/python/src/jsii_calc/module2692/submodule2/__init__.py#L58

The "first" base is declared on this line:

https://github.com/RomainMuller/pyright-dublicate-base-error/blob/9f0067283b44fae09b5b3a513efa12b411513135/generated-code/jsii-calc/python/src/jsii_calc/module2692/submodule2/__init__.py#L23

And the "second" base (which is different from the first one) is imported at:

https://github.com/RomainMuller/pyright-dublicate-base-error/blob/9f0067283b44fae09b5b3a513efa12b411513135/generated-code/jsii-calc/python/src/jsii_calc/module2692/submodule2/__init__.py#L15

## Note

The bulk of this is generated code, which explains the odd naming... This is
part of the test suite of [aws/jsii](https://github.com/aws/jsii)'s code
generation tools.
