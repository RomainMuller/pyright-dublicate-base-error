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


class OnlyStatics(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.module2617.OnlyStatics",
):
    @jsii.member(jsii_name="bar")
    @builtins.classmethod
    def bar(cls) -> None:
        return typing.cast(None, jsii.sinvoke(cls, "bar", []))

    @jsii.member(jsii_name="foo")
    @builtins.classmethod
    def foo(cls) -> None:
        return typing.cast(None, jsii.sinvoke(cls, "foo", []))


__all__ = [
    "OnlyStatics",
]

publication.publish()
