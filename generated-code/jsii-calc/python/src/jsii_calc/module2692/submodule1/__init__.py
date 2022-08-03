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


@jsii.data_type(
    jsii_type="jsii-calc.module2692.submodule1.Bar",
    jsii_struct_bases=[],
    name_mapping={"bar1": "bar1"},
)
class Bar:
    def __init__(self, *, bar1: builtins.str) -> None:
        '''
        :param bar1: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Bar.__init__)
            check_type(argname="argument bar1", value=bar1, expected_type=type_hints["bar1"])
        self._values: typing.Dict[str, typing.Any] = {
            "bar1": bar1,
        }

    @builtins.property
    def bar1(self) -> builtins.str:
        result = self._values.get("bar1")
        assert result is not None, "Required property 'bar1' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Bar(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Bar",
]

publication.publish()
