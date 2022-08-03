import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import scope.jsii_calc_base_of_base
import scope.jsii_calc_lib


@jsii.implements(scope.jsii_calc_lib.IFriendly)
class ExtendAndImplement(
    scope.jsii_calc_lib.BaseFor2647,
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.module2647.ExtendAndImplement",
):
    '''This class falls into the category of "multiple bases" from a different module from a go code gen perspective.

    :see: https://github.com/aws/jsii/issues/2647
    '''

    def __init__(self, very: scope.jsii_calc_base_of_base.Very) -> None:
        '''
        :param very: -

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ExtendAndImplement.__init__)
            check_type(argname="argument very", value=very, expected_type=type_hints["very"])
        jsii.create(self.__class__, self, [very])

    @jsii.member(jsii_name="hello")
    def hello(self) -> builtins.str:
        '''Say hello!'''
        return typing.cast(builtins.str, jsii.invoke(self, "hello", []))

    @jsii.member(jsii_name="localMethod")
    def local_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "localMethod", []))


__all__ = [
    "ExtendAndImplement",
]

publication.publish()
