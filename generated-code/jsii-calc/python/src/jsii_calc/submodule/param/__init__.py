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
    jsii_type="jsii-calc.submodule.param.SpecialParameter",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class SpecialParameter:
    def __init__(self, *, value: builtins.str) -> None:
        '''
        :param value: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpecialParameter.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "value": value,
        }

    @builtins.property
    def value(self) -> builtins.str:
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpecialParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "SpecialParameter",
]

publication.publish()
