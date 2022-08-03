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


class TypeFromSub2(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.nodirect.sub2.TypeFromSub2",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="sub2")
    def sub2(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "sub2", []))


__all__ = [
    "TypeFromSub2",
]

publication.publish()
