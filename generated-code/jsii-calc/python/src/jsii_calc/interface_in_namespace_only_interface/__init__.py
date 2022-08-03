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


@jsii.data_type(
    jsii_type="jsii-calc.InterfaceInNamespaceOnlyInterface.Hello",
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
    "Hello",
]

publication.publish()
