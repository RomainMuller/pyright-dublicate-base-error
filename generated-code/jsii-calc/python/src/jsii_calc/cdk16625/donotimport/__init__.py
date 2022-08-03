import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ..._jsii import *

from ... import IRandomNumberGenerator as _IRandomNumberGenerator_9643a8b9


@jsii.implements(_IRandomNumberGenerator_9643a8b9)
class UnimportedSubmoduleType(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.cdk16625.donotimport.UnimportedSubmoduleType",
):
    '''This type demonstrates the ability to receive a callback argument that has a type from a submodule not explicitly imported in the user's code.

    This checks
    that all types available in the assembly can be resolved by the runtime
    library, regardless of whether they were explicitly referenced or not.

    :see: https://github.com/aws/aws-cdk/issues/16625
    '''

    def __init__(self, value: jsii.Number) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UnimportedSubmoduleType.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.create(self.__class__, self, [value])

    @jsii.member(jsii_name="next")
    def next(self) -> jsii.Number:
        '''Not quite random, but it'll do.

        :return: 1337
        '''
        return typing.cast(jsii.Number, jsii.invoke(self, "next", []))


__all__ = [
    "UnimportedSubmoduleType",
]

publication.publish()
