'''
# Read you, read me

This is the readme of the `jsii-calc.submodule` module.
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

from .. import AllTypes as _AllTypes_b08307c5
from .child import (
    Awesomeness as _Awesomeness_d37a24df,
    Goodness as _Goodness_2df26737,
    SomeEnum as _SomeEnum_b2e41d92,
    SomeStruct as _SomeStruct_91627123,
)
from .nested_submodule.deeply_nested import INamespaced as _INamespaced_e2f386ad
from .param import SpecialParameter as _SpecialParameter_5bbf34a2


@jsii.data_type(
    jsii_type="jsii-calc.submodule.Default",
    jsii_struct_bases=[],
    name_mapping={"foo": "foo"},
)
class Default:
    def __init__(self, *, foo: jsii.Number) -> None:
        '''A struct named "Default".

        :param foo: 

        :see: https://github.com/aws/jsii/issues/2637
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Default.__init__)
            check_type(argname="argument foo", value=foo, expected_type=type_hints["foo"])
        self._values: typing.Dict[str, typing.Any] = {
            "foo": foo,
        }

    @builtins.property
    def foo(self) -> jsii.Number:
        result = self._values.get("foo")
        assert result is not None, "Required property 'foo' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Default(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_INamespaced_e2f386ad)
class MyClass(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.submodule.MyClass"):
    def __init__(self, *, prop: _SomeEnum_b2e41d92) -> None:
        '''
        :param prop: 
        '''
        props = _SomeStruct_91627123(prop=prop)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="methodWithSpecialParam")
    def method_with_special_param(self, *, value: builtins.str) -> builtins.str:
        '''
        :param value: 
        '''
        param = _SpecialParameter_5bbf34a2(value=value)

        return typing.cast(builtins.str, jsii.invoke(self, "methodWithSpecialParam", [param]))

    @builtins.property
    @jsii.member(jsii_name="awesomeness")
    def awesomeness(self) -> _Awesomeness_d37a24df:
        return typing.cast(_Awesomeness_d37a24df, jsii.get(self, "awesomeness"))

    @builtins.property
    @jsii.member(jsii_name="definedAt")
    def defined_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "definedAt"))

    @builtins.property
    @jsii.member(jsii_name="goodness")
    def goodness(self) -> _Goodness_2df26737:
        return typing.cast(_Goodness_2df26737, jsii.get(self, "goodness"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> _SomeStruct_91627123:
        return typing.cast(_SomeStruct_91627123, jsii.get(self, "props"))

    @builtins.property
    @jsii.member(jsii_name="allTypes")
    def all_types(self) -> typing.Optional[_AllTypes_b08307c5]:
        return typing.cast(typing.Optional[_AllTypes_b08307c5], jsii.get(self, "allTypes"))

    @all_types.setter
    def all_types(self, value: typing.Optional[_AllTypes_b08307c5]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MyClass, "all_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allTypes", value)


__all__ = [
    "Default",
    "MyClass",
    "back_references",
    "child",
    "isolated",
    "nested_submodule",
    "param",
    "returnsparam",
]

publication.publish()

# Loading modules to ensure their types are registered with the jsii runtime library
from . import back_references
from . import child
from . import isolated
from . import nested_submodule
from . import param
from . import returnsparam
