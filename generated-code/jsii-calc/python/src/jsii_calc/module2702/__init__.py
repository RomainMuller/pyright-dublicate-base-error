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

import scope.jsii_calc_base


class Class1(
    scope.jsii_calc_base.Base,
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.module2702.Class1",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="base")
    def base(self) -> None:
        return typing.cast(None, jsii.invoke(self, "base", []))


class Class2(
    scope.jsii_calc_base.Base,
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.module2702.Class2",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @builtins.property
    @jsii.member(jsii_name="base")
    def base(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "base"))


@jsii.implements(scope.jsii_calc_base.IBaseInterface)
class Class3(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.module2702.Class3"):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="bar")
    def bar(self) -> None:
        return typing.cast(None, jsii.invoke(self, "bar", []))

    @jsii.member(jsii_name="foo")
    def foo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "foo", []))

    @jsii.member(jsii_name="iBaseInterface")
    def i_base_interface(self) -> None:
        return typing.cast(None, jsii.invoke(self, "iBaseInterface", []))


@jsii.interface(jsii_type="jsii-calc.module2702.IBaz")
class IBaz(scope.jsii_calc_base.IBaseInterface, typing_extensions.Protocol):
    @jsii.member(jsii_name="bazMethod")
    def baz_method(self) -> None:
        ...


class _IBazProxy(
    jsii.proxy_for(scope.jsii_calc_base.IBaseInterface), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.module2702.IBaz"

    @jsii.member(jsii_name="bazMethod")
    def baz_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "bazMethod", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBaz).__jsii_proxy_class__ = lambda : _IBazProxy


@jsii.interface(jsii_type="jsii-calc.module2702.IConstruct")
class IConstruct(typing_extensions.Protocol):
    @jsii.member(jsii_name="constructMethod")
    def construct_method(self) -> None:
        ...


class _IConstructProxy:
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.module2702.IConstruct"

    @jsii.member(jsii_name="constructMethod")
    def construct_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "constructMethod", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConstruct).__jsii_proxy_class__ = lambda : _IConstructProxy


@jsii.interface(jsii_type="jsii-calc.module2702.IFoo")
class IFoo(scope.jsii_calc_base.IBaseInterface, typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="iBaseInterface")
    def i_base_interface(self) -> builtins.str:
        ...


class _IFooProxy(
    jsii.proxy_for(scope.jsii_calc_base.IBaseInterface), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.module2702.IFoo"

    @builtins.property
    @jsii.member(jsii_name="iBaseInterface")
    def i_base_interface(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iBaseInterface"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFoo).__jsii_proxy_class__ = lambda : _IFooProxy


@jsii.interface(jsii_type="jsii-calc.module2702.IResource")
class IResource(IConstruct, typing_extensions.Protocol):
    @jsii.member(jsii_name="resourceMethod")
    def resource_method(self) -> None:
        ...


class _IResourceProxy(
    jsii.proxy_for(IConstruct), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.module2702.IResource"

    @jsii.member(jsii_name="resourceMethod")
    def resource_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resourceMethod", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResource).__jsii_proxy_class__ = lambda : _IResourceProxy


@jsii.interface(jsii_type="jsii-calc.module2702.IVpc")
class IVpc(IResource, typing_extensions.Protocol):
    @jsii.member(jsii_name="vpcMethod")
    def vpc_method(self) -> None:
        ...


class _IVpcProxy(
    jsii.proxy_for(IResource), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.module2702.IVpc"

    @jsii.member(jsii_name="vpcMethod")
    def vpc_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "vpcMethod", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVpc).__jsii_proxy_class__ = lambda : _IVpcProxy


@jsii.implements(IBaz)
class Baz(Class3, metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.module2702.Baz"):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="bazMethod")
    def baz_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "bazMethod", []))


@jsii.implements(IConstruct)
class Construct(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.module2702.Construct"):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="constructMethod")
    def construct_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "constructMethod", []))


@jsii.implements(IResource)
class Resource(
    Construct,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="jsii-calc.module2702.Resource",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="resourceMethod")
    def resource_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resourceMethod", []))


class _ResourceProxy(Resource):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Resource).__jsii_proxy_class__ = lambda : _ResourceProxy


@jsii.implements(IVpc)
class Vpc(Resource, metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.module2702.Vpc"):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="vpcMethod")
    def vpc_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "vpcMethod", []))


__all__ = [
    "Baz",
    "Class1",
    "Class2",
    "Class3",
    "Construct",
    "IBaz",
    "IConstruct",
    "IFoo",
    "IResource",
    "IVpc",
    "Resource",
    "Vpc",
]

publication.publish()
