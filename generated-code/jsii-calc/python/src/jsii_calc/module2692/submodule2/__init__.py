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

from ..submodule1 import Bar as _Bar_ec7eccad


@jsii.data_type(
    jsii_type="jsii-calc.module2692.submodule2.Bar",
    jsii_struct_bases=[],
    name_mapping={"bar2": "bar2"},
)
class Bar:
    def __init__(self, *, bar2: builtins.str) -> None:
        '''
        :param bar2: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Bar.__init__)
            check_type(argname="argument bar2", value=bar2, expected_type=type_hints["bar2"])
        self._values: typing.Dict[str, typing.Any] = {
            "bar2": bar2,
        }

    @builtins.property
    def bar2(self) -> builtins.str:
        result = self._values.get("bar2")
        assert result is not None, "Required property 'bar2' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Bar(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="jsii-calc.module2692.submodule2.Foo",
    jsii_struct_bases=[Bar, _Bar_ec7eccad],
    name_mapping={"bar2": "bar2", "bar1": "bar1", "foo2": "foo2"},
)
class Foo(Bar, _Bar_ec7eccad):
    def __init__(
        self,
        *,
        bar2: builtins.str,
        bar1: builtins.str,
        foo2: builtins.str,
    ) -> None:
        '''
        :param bar2: 
        :param bar1: 
        :param foo2: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Foo.__init__)
            check_type(argname="argument bar2", value=bar2, expected_type=type_hints["bar2"])
            check_type(argname="argument bar1", value=bar1, expected_type=type_hints["bar1"])
            check_type(argname="argument foo2", value=foo2, expected_type=type_hints["foo2"])
        self._values: typing.Dict[str, typing.Any] = {
            "bar2": bar2,
            "bar1": bar1,
            "foo2": foo2,
        }

    @builtins.property
    def bar2(self) -> builtins.str:
        result = self._values.get("bar2")
        assert result is not None, "Required property 'bar2' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bar1(self) -> builtins.str:
        result = self._values.get("bar1")
        assert result is not None, "Required property 'bar1' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def foo2(self) -> builtins.str:
        result = self._values.get("foo2")
        assert result is not None, "Required property 'foo2' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Foo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Bar",
    "Foo",
]

publication.publish()
