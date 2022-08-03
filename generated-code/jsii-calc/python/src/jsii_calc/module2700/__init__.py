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


@jsii.interface(jsii_type="jsii-calc.module2700.IFoo")
class IFoo(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="baz")
    def baz(self) -> jsii.Number:
        ...

    @jsii.member(jsii_name="bar")
    def bar(self) -> builtins.str:
        ...


class _IFooProxy:
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.module2700.IFoo"

    @builtins.property
    @jsii.member(jsii_name="baz")
    def baz(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "baz"))

    @jsii.member(jsii_name="bar")
    def bar(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "bar", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFoo).__jsii_proxy_class__ = lambda : _IFooProxy


@jsii.implements(IFoo)
class Base(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.module2700.Base"):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="bar")
    def bar(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "bar", []))

    @builtins.property
    @jsii.member(jsii_name="baz")
    def baz(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "baz"))


@jsii.implements(IFoo)
class Derived(Base, metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.module2700.Derived"):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="zoo")
    def zoo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "zoo", []))


__all__ = [
    "Base",
    "Derived",
    "IFoo",
]

publication.publish()
