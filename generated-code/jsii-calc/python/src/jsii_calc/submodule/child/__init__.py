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


@jsii.enum(jsii_type="jsii-calc.submodule.child.Awesomeness")
class Awesomeness(enum.Enum):
    AWESOME = "AWESOME"
    '''It was awesome!'''


@jsii.enum(jsii_type="jsii-calc.submodule.child.Goodness")
class Goodness(enum.Enum):
    PRETTY_GOOD = "PRETTY_GOOD"
    '''It's pretty good.'''
    REALLY_GOOD = "REALLY_GOOD"
    '''It's really good.'''
    AMAZINGLY_GOOD = "AMAZINGLY_GOOD"
    '''It's amazingly good.'''


class InnerClass(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.submodule.child.InnerClass",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.python.classproperty
    @jsii.member(jsii_name="staticProp")
    def STATIC_PROP(cls) -> "SomeStruct":
        return typing.cast("SomeStruct", jsii.sget(cls, "staticProp"))


class OuterClass(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.submodule.child.OuterClass",
):
    '''Checks that classes can self-reference during initialization.

    :see: : https://github.com/aws/jsii/pull/1706
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @builtins.property
    @jsii.member(jsii_name="innerClass")
    def inner_class(self) -> InnerClass:
        return typing.cast(InnerClass, jsii.get(self, "innerClass"))


@jsii.enum(jsii_type="jsii-calc.submodule.child.SomeEnum")
class SomeEnum(enum.Enum):
    SOME = "SOME"


@jsii.data_type(
    jsii_type="jsii-calc.submodule.child.SomeStruct",
    jsii_struct_bases=[],
    name_mapping={"prop": "prop"},
)
class SomeStruct:
    def __init__(self, *, prop: SomeEnum) -> None:
        '''
        :param prop: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SomeStruct.__init__)
            check_type(argname="argument prop", value=prop, expected_type=type_hints["prop"])
        self._values: typing.Dict[str, typing.Any] = {
            "prop": prop,
        }

    @builtins.property
    def prop(self) -> SomeEnum:
        result = self._values.get("prop")
        assert result is not None, "Required property 'prop' is missing"
        return typing.cast(SomeEnum, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SomeStruct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="jsii-calc.submodule.child.Structure",
    jsii_struct_bases=[],
    name_mapping={"bool": "bool"},
)
class Structure:
    def __init__(self, *, bool: builtins.bool) -> None:
        '''
        :param bool: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Structure.__init__)
            check_type(argname="argument bool", value=bool, expected_type=type_hints["bool"])
        self._values: typing.Dict[str, typing.Any] = {
            "bool": bool,
        }

    @builtins.property
    def bool(self) -> builtins.bool:
        result = self._values.get("bool")
        assert result is not None, "Required property 'bool' is missing"
        return typing.cast(builtins.bool, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Structure(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="jsii-calc.submodule.child.KwargsProps",
    jsii_struct_bases=[SomeStruct],
    name_mapping={"prop": "prop", "extra": "extra"},
)
class KwargsProps(SomeStruct):
    def __init__(
        self,
        *,
        prop: SomeEnum,
        extra: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param prop: 
        :param extra: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KwargsProps.__init__)
            check_type(argname="argument prop", value=prop, expected_type=type_hints["prop"])
            check_type(argname="argument extra", value=extra, expected_type=type_hints["extra"])
        self._values: typing.Dict[str, typing.Any] = {
            "prop": prop,
        }
        if extra is not None:
            self._values["extra"] = extra

    @builtins.property
    def prop(self) -> SomeEnum:
        result = self._values.get("prop")
        assert result is not None, "Required property 'prop' is missing"
        return typing.cast(SomeEnum, result)

    @builtins.property
    def extra(self) -> typing.Optional[builtins.str]:
        result = self._values.get("extra")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KwargsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Awesomeness",
    "Goodness",
    "InnerClass",
    "KwargsProps",
    "OuterClass",
    "SomeEnum",
    "SomeStruct",
    "Structure",
]

publication.publish()
