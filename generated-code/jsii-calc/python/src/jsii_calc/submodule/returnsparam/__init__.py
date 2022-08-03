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

from ..param import SpecialParameter as _SpecialParameter_5bbf34a2


class ReturnsSpecialParameter(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.submodule.returnsparam.ReturnsSpecialParameter",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="returnsSpecialParam")
    def returns_special_param(self) -> _SpecialParameter_5bbf34a2:
        return typing.cast(_SpecialParameter_5bbf34a2, jsii.invoke(self, "returnsSpecialParam", []))


__all__ = [
    "ReturnsSpecialParameter",
]

publication.publish()
