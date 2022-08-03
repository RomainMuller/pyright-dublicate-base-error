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


class Base(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.DerivedClassHasNoProperties.Base",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @builtins.property
    @jsii.member(jsii_name="prop")
    def prop(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prop"))

    @prop.setter
    def prop(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Base, "prop").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prop", value)


class Derived(
    Base,
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.DerivedClassHasNoProperties.Derived",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])


__all__ = [
    "Base",
    "Derived",
]

publication.publish()
