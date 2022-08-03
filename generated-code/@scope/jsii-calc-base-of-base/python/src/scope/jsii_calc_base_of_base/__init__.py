import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *


@jsii.interface(jsii_type="@scope/jsii-calc-base-of-base.IVeryBaseInterface")
class IVeryBaseInterface(typing_extensions.Protocol):
    @jsii.member(jsii_name="foo")
    def foo(self) -> None:
        ...


class _IVeryBaseInterfaceProxy:
    __jsii_type__: typing.ClassVar[str] = "@scope/jsii-calc-base-of-base.IVeryBaseInterface"

    @jsii.member(jsii_name="foo")
    def foo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "foo", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVeryBaseInterface).__jsii_proxy_class__ = lambda : _IVeryBaseInterfaceProxy


class StaticConsumer(
    metaclass=jsii.JSIIMeta,
    jsii_type="@scope/jsii-calc-base-of-base.StaticConsumer",
):
    @jsii.member(jsii_name="consume")
    @builtins.classmethod
    def consume(cls, *_args: typing.Any) -> None:
        '''
        :param _args: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StaticConsumer.consume)
            check_type(argname="argument _args", value=_args, expected_type=typing.Tuple[type_hints["_args"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.sinvoke(cls, "consume", [*_args]))


class Very(metaclass=jsii.JSIIMeta, jsii_type="@scope/jsii-calc-base-of-base.Very"):
    '''(experimental) Something here.

    :stability: experimental
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="hey")
    def hey(self) -> jsii.Number:
        '''
        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.invoke(self, "hey", []))


@jsii.data_type(
    jsii_type="@scope/jsii-calc-base-of-base.VeryBaseProps",
    jsii_struct_bases=[],
    name_mapping={"foo": "foo"},
)
class VeryBaseProps:
    def __init__(self, *, foo: Very) -> None:
        '''
        :param foo: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VeryBaseProps.__init__)
            check_type(argname="argument foo", value=foo, expected_type=type_hints["foo"])
        self._values: typing.Dict[str, typing.Any] = {
            "foo": foo,
        }

    @builtins.property
    def foo(self) -> Very:
        result = self._values.get("foo")
        assert result is not None, "Required property 'foo' is missing"
        return typing.cast(Very, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VeryBaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IVeryBaseInterface",
    "StaticConsumer",
    "Very",
    "VeryBaseProps",
]

publication.publish()
