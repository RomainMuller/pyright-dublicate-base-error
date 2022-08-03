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

from .. import MyClass as _MyClass_a2fdc0b6


@jsii.data_type(
    jsii_type="jsii-calc.submodule.back_references.MyClassReference",
    jsii_struct_bases=[],
    name_mapping={"reference": "reference"},
)
class MyClassReference:
    def __init__(self, *, reference: _MyClass_a2fdc0b6) -> None:
        '''
        :param reference: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MyClassReference.__init__)
            check_type(argname="argument reference", value=reference, expected_type=type_hints["reference"])
        self._values: typing.Dict[str, typing.Any] = {
            "reference": reference,
        }

    @builtins.property
    def reference(self) -> _MyClass_a2fdc0b6:
        result = self._values.get("reference")
        assert result is not None, "Required property 'reference' is missing"
        return typing.cast(_MyClass_a2fdc0b6, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MyClassReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "MyClassReference",
]

publication.publish()
