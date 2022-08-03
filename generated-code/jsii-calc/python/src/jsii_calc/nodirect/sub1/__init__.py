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


class TypeFromSub1(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.nodirect.sub1.TypeFromSub1",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="sub1")
    def sub1(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "sub1", []))


__all__ = [
    "TypeFromSub1",
]

publication.publish()
