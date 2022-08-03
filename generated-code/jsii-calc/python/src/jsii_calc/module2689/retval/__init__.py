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


class MyClass(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.module2689.retval.MyClass"):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="bar")
    def bar(self) -> typing.Mapping[builtins.str, scope.jsii_calc_base.BaseProps]:
        return typing.cast(typing.Mapping[builtins.str, scope.jsii_calc_base.BaseProps], jsii.invoke(self, "bar", []))

    @jsii.member(jsii_name="foo")
    def foo(self) -> typing.List[scope.jsii_calc_lib.Number]:
        return typing.cast(typing.List[scope.jsii_calc_lib.Number], jsii.invoke(self, "foo", []))


__all__ = [
    "MyClass",
]

publication.publish()
