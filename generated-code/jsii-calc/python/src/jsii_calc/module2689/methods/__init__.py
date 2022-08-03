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

import scope.jsii_calc_base
import scope.jsii_calc_lib


class MyClass(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.module2689.methods.MyClass",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="bar")
    def bar(
        self,
        _bar: typing.Mapping[builtins.str, typing.Union[scope.jsii_calc_base.BaseProps, typing.Dict[str, typing.Any]]],
    ) -> None:
        '''
        :param _bar: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MyClass.bar)
            check_type(argname="argument _bar", value=_bar, expected_type=type_hints["_bar"])
        return typing.cast(None, jsii.invoke(self, "bar", [_bar]))

    @jsii.member(jsii_name="foo")
    def foo(self, _values: typing.Sequence[scope.jsii_calc_lib.Number]) -> None:
        '''
        :param _values: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MyClass.foo)
            check_type(argname="argument _values", value=_values, expected_type=type_hints["_values"])
        return typing.cast(None, jsii.invoke(self, "foo", [_values]))


__all__ = [
    "MyClass",
]

publication.publish()
