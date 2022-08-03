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


class Foo(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.InterfaceInNamespaceIncludesClasses.Foo",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @builtins.property
    @jsii.member(jsii_name="bar")
    def bar(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bar"))

    @bar.setter
    def bar(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Foo, "bar").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bar", value)


@jsii.data_type(
    jsii_type="jsii-calc.InterfaceInNamespaceIncludesClasses.Hello",
    jsii_struct_bases=[],
    name_mapping={"foo": "foo"},
)
class Hello:
    def __init__(self, *, foo: jsii.Number) -> None:
        '''
        :param foo: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Hello.__init__)
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
        return "Hello(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Foo",
    "Hello",
]

publication.publish()
