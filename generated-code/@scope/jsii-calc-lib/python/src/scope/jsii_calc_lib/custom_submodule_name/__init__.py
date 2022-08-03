'''
# Submodule Readme

This is a submodule readme.
'''
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


@jsii.interface(jsii_type="@scope/jsii-calc-lib.submodule.IReflectable")
class IReflectable(typing_extensions.Protocol):
    '''
    :stability: deprecated
    '''

    @builtins.property
    @jsii.member(jsii_name="entries")
    def entries(self) -> typing.List["ReflectableEntry"]:
        '''
        :stability: deprecated
        '''
        ...


class _IReflectableProxy:
    '''
    :stability: deprecated
    '''

    __jsii_type__: typing.ClassVar[str] = "@scope/jsii-calc-lib.submodule.IReflectable"

    @builtins.property
    @jsii.member(jsii_name="entries")
    def entries(self) -> typing.List["ReflectableEntry"]:
        '''
        :stability: deprecated
        '''
        return typing.cast(typing.List["ReflectableEntry"], jsii.get(self, "entries"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReflectable).__jsii_proxy_class__ = lambda : _IReflectableProxy


class NestingClass(
    metaclass=jsii.JSIIMeta,
    jsii_type="@scope/jsii-calc-lib.submodule.NestingClass",
):
    '''(deprecated) This class is here to show we can use nested classes across module boundaries.

    :stability: deprecated
    '''

    class NestedClass(
        metaclass=jsii.JSIIMeta,
        jsii_type="@scope/jsii-calc-lib.submodule.NestingClass.NestedClass",
    ):
        '''(deprecated) This class is here to show we can use nested classes across module boundaries.

        :stability: deprecated
        '''

        def __init__(self) -> None:
            '''
            :stability: deprecated
            '''
            jsii.create(self.__class__, self, [])

        @builtins.property
        @jsii.member(jsii_name="property")
        def property(self) -> builtins.str:
            '''
            :stability: deprecated
            '''
            return typing.cast(builtins.str, jsii.get(self, "property"))

    @jsii.data_type(
        jsii_type="@scope/jsii-calc-lib.submodule.NestingClass.NestedStruct",
        jsii_struct_bases=[],
        name_mapping={"name": "name"},
    )
    class NestedStruct:
        def __init__(self, *, name: builtins.str) -> None:
            '''(deprecated) This is a struct, nested within a class.

            Normal.

            :param name: 

            :stability: deprecated
            '''
            if __debug__:
                type_hints = typing.get_type_hints(NestingClass.NestedStruct.__init__)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''
            :stability: deprecated
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NestedStruct(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@scope/jsii-calc-lib.submodule.ReflectableEntry",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class ReflectableEntry:
    def __init__(self, *, key: builtins.str, value: typing.Any) -> None:
        '''
        :param key: 
        :param value: 

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ReflectableEntry.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''
        :stability: deprecated
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> typing.Any:
        '''
        :stability: deprecated
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReflectableEntry(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Reflector(
    metaclass=jsii.JSIIMeta,
    jsii_type="@scope/jsii-calc-lib.submodule.Reflector",
):
    '''
    :stability: deprecated
    '''

    def __init__(self) -> None:
        '''
        :stability: deprecated
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="asMap")
    def as_map(
        self,
        reflectable: IReflectable,
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param reflectable: -

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Reflector.as_map)
            check_type(argname="argument reflectable", value=reflectable, expected_type=type_hints["reflectable"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "asMap", [reflectable]))


__all__ = [
    "IReflectable",
    "NestingClass",
    "ReflectableEntry",
    "Reflector",
]

publication.publish()
