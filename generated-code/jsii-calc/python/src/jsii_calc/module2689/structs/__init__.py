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

import scope.jsii_calc_base
import scope.jsii_calc_lib


@jsii.data_type(
    jsii_type="jsii-calc.module2689.structs.MyStruct",
    jsii_struct_bases=[],
    name_mapping={"base_map": "baseMap", "numbers": "numbers"},
)
class MyStruct:
    def __init__(
        self,
        *,
        base_map: typing.Mapping[builtins.str, typing.Union[scope.jsii_calc_base.BaseProps, typing.Dict[str, typing.Any]]],
        numbers: typing.Sequence[scope.jsii_calc_lib.Number],
    ) -> None:
        '''
        :param base_map: 
        :param numbers: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MyStruct.__init__)
            check_type(argname="argument base_map", value=base_map, expected_type=type_hints["base_map"])
            check_type(argname="argument numbers", value=numbers, expected_type=type_hints["numbers"])
        self._values: typing.Dict[str, typing.Any] = {
            "base_map": base_map,
            "numbers": numbers,
        }

    @builtins.property
    def base_map(self) -> typing.Mapping[builtins.str, scope.jsii_calc_base.BaseProps]:
        result = self._values.get("base_map")
        assert result is not None, "Required property 'base_map' is missing"
        return typing.cast(typing.Mapping[builtins.str, scope.jsii_calc_base.BaseProps], result)

    @builtins.property
    def numbers(self) -> typing.List[scope.jsii_calc_lib.Number]:
        result = self._values.get("numbers")
        assert result is not None, "Required property 'numbers' is missing"
        return typing.cast(typing.List[scope.jsii_calc_lib.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MyStruct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "MyStruct",
]

publication.publish()
