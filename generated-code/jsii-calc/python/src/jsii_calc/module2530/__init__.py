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


class MyClass(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.module2530.MyClass"):
    '''Verifies a method with parameters "_" can be generated.

    :see: https://github.com/aws/jsii/issues/2530
    '''

    def __init__(self, _: jsii.Number) -> None:
        '''
        :param _: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MyClass.__init__)
            check_type(argname="argument _", value=_, expected_type=type_hints["_"])
        jsii.create(self.__class__, self, [_])

    @jsii.member(jsii_name="bar")
    @builtins.classmethod
    def bar(cls, _: builtins.bool) -> None:
        '''
        :param _: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MyClass.bar)
            check_type(argname="argument _", value=_, expected_type=type_hints["_"])
        return typing.cast(None, jsii.sinvoke(cls, "bar", [_]))

    @jsii.member(jsii_name="foo")
    def foo(self, _: builtins.str) -> None:
        '''
        :param _: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MyClass.foo)
            check_type(argname="argument _", value=_, expected_type=type_hints["_"])
        return typing.cast(None, jsii.invoke(self, "foo", [_]))


__all__ = [
    "MyClass",
]

publication.publish()
