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


class ClassWithSelf(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.PythonSelf.ClassWithSelf",
):
    def __init__(self_, self: builtins.str) -> None:
        '''
        :param self: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClassWithSelf.__init__)
            check_type(argname="argument self", value=self, expected_type=type_hints["self"])
        jsii.create(self_.__class__, self_, [self])

    @jsii.member(jsii_name="method")
    def method(self_, self: jsii.Number) -> builtins.str:
        '''
        :param self: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClassWithSelf.method)
            check_type(argname="argument self", value=self, expected_type=type_hints["self"])
        return typing.cast(builtins.str, jsii.invoke(self_, "method", [self]))

    @builtins.property
    @jsii.member(jsii_name="self")
    def self(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "self"))


class ClassWithSelfKwarg(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.PythonSelf.ClassWithSelfKwarg",
):
    def __init__(self_, *, self: builtins.str) -> None:
        '''
        :param self: 
        '''
        props = StructWithSelf(self=self)

        jsii.create(self_.__class__, self_, [props])

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "StructWithSelf":
        return typing.cast("StructWithSelf", jsii.get(self, "props"))


@jsii.interface(jsii_type="jsii-calc.PythonSelf.IInterfaceWithSelf")
class IInterfaceWithSelf(typing_extensions.Protocol):
    @jsii.member(jsii_name="method")
    def method(self_, self: jsii.Number) -> builtins.str:
        '''
        :param self: -
        '''
        ...


class _IInterfaceWithSelfProxy:
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.PythonSelf.IInterfaceWithSelf"

    @jsii.member(jsii_name="method")
    def method(self_, self: jsii.Number) -> builtins.str:
        '''
        :param self: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IInterfaceWithSelf.method)
            check_type(argname="argument self", value=self, expected_type=type_hints["self"])
        return typing.cast(builtins.str, jsii.invoke(self_, "method", [self]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInterfaceWithSelf).__jsii_proxy_class__ = lambda : _IInterfaceWithSelfProxy


@jsii.data_type(
    jsii_type="jsii-calc.PythonSelf.StructWithSelf",
    jsii_struct_bases=[],
    name_mapping={"self": "self"},
)
class StructWithSelf:
    def __init__(self_, *, self: builtins.str) -> None:
        '''
        :param self: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StructWithSelf.__init__)
            check_type(argname="argument self", value=self, expected_type=type_hints["self"])
        self_._values: typing.Dict[str, typing.Any] = {
            "self": self,
        }

    @builtins.property
    def self(self) -> builtins.str:
        result = self._values.get("self")
        assert result is not None, "Required property 'self' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StructWithSelf(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ClassWithSelf",
    "ClassWithSelfKwarg",
    "IInterfaceWithSelf",
    "StructWithSelf",
]

publication.publish()
