import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import scope.jsii_calc_base
import scope.jsii_calc_base_of_base


class BaseFor2647(
    metaclass=jsii.JSIIMeta,
    jsii_type="@scope/jsii-calc-lib.BaseFor2647",
):
    '''(deprecated) A base class for testing #2647.

    The method ``foo`` has a parameter that uses a type
    from a dependent module. Since Go "reimplments" this method, it will also need
    to include an "import" statement for the calc-base module.

    :see: https://github.com/aws/jsii/issues/2647
    :stability: deprecated
    '''

    def __init__(self, very: scope.jsii_calc_base_of_base.Very) -> None:
        '''
        :param very: -

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BaseFor2647.__init__)
            check_type(argname="argument very", value=very, expected_type=type_hints["very"])
        jsii.create(self.__class__, self, [very])

    @jsii.member(jsii_name="foo")
    def foo(self, obj: scope.jsii_calc_base.IBaseInterface) -> None:
        '''
        :param obj: -

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BaseFor2647.foo)
            check_type(argname="argument obj", value=obj, expected_type=type_hints["obj"])
        return typing.cast(None, jsii.invoke(self, "foo", [obj]))


@jsii.data_type(
    jsii_type="@scope/jsii-calc-lib.DiamondLeft",
    jsii_struct_bases=[],
    name_mapping={"hoisted_top": "hoistedTop", "left": "left"},
)
class DiamondLeft:
    def __init__(
        self,
        *,
        hoisted_top: typing.Optional[builtins.str] = None,
        left: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param hoisted_top: 
        :param left: 

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DiamondLeft.__init__)
            check_type(argname="argument hoisted_top", value=hoisted_top, expected_type=type_hints["hoisted_top"])
            check_type(argname="argument left", value=left, expected_type=type_hints["left"])
        self._values: typing.Dict[str, typing.Any] = {}
        if hoisted_top is not None:
            self._values["hoisted_top"] = hoisted_top
        if left is not None:
            self._values["left"] = left

    @builtins.property
    def hoisted_top(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        '''
        result = self._values.get("hoisted_top")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def left(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: deprecated
        '''
        result = self._values.get("left")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DiamondLeft(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@scope/jsii-calc-lib.DiamondRight",
    jsii_struct_bases=[],
    name_mapping={"hoisted_top": "hoistedTop", "right": "right"},
)
class DiamondRight:
    def __init__(
        self,
        *,
        hoisted_top: typing.Optional[builtins.str] = None,
        right: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param hoisted_top: 
        :param right: 

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DiamondRight.__init__)
            check_type(argname="argument hoisted_top", value=hoisted_top, expected_type=type_hints["hoisted_top"])
            check_type(argname="argument right", value=right, expected_type=type_hints["right"])
        self._values: typing.Dict[str, typing.Any] = {}
        if hoisted_top is not None:
            self._values["hoisted_top"] = hoisted_top
        if right is not None:
            self._values["right"] = right

    @builtins.property
    def hoisted_top(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        '''
        result = self._values.get("hoisted_top")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def right(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: deprecated
        '''
        result = self._values.get("right")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DiamondRight(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@scope/jsii-calc-lib.EnumFromScopedModule")
class EnumFromScopedModule(enum.Enum):
    '''(deprecated) Check that enums from @scoped packages can be references.

    See awslabs/jsii#138

    :stability: deprecated
    '''

    VALUE1 = "VALUE1"
    '''
    :stability: deprecated
    '''
    VALUE2 = "VALUE2"
    '''
    :stability: deprecated
    '''


@jsii.interface(jsii_type="@scope/jsii-calc-lib.IDoublable")
class IDoublable(typing_extensions.Protocol):
    '''(deprecated) The general contract for a concrete number.

    :stability: deprecated
    '''

    @builtins.property
    @jsii.member(jsii_name="doubleValue")
    def double_value(self) -> jsii.Number:
        '''
        :stability: deprecated
        '''
        ...


class _IDoublableProxy:
    '''(deprecated) The general contract for a concrete number.

    :stability: deprecated
    '''

    __jsii_type__: typing.ClassVar[str] = "@scope/jsii-calc-lib.IDoublable"

    @builtins.property
    @jsii.member(jsii_name="doubleValue")
    def double_value(self) -> jsii.Number:
        '''
        :stability: deprecated
        '''
        return typing.cast(jsii.Number, jsii.get(self, "doubleValue"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDoublable).__jsii_proxy_class__ = lambda : _IDoublableProxy


@jsii.interface(jsii_type="@scope/jsii-calc-lib.IFriendly")
class IFriendly(typing_extensions.Protocol):
    '''(deprecated) Applies to classes that are considered friendly.

    These classes can be greeted with
    a "hello" or "goodbye" blessing and they will respond back in a fun and friendly manner.

    :stability: deprecated
    '''

    @jsii.member(jsii_name="hello")
    def hello(self) -> builtins.str:
        '''(deprecated) Say hello!

        :stability: deprecated
        '''
        ...


class _IFriendlyProxy:
    '''(deprecated) Applies to classes that are considered friendly.

    These classes can be greeted with
    a "hello" or "goodbye" blessing and they will respond back in a fun and friendly manner.

    :stability: deprecated
    '''

    __jsii_type__: typing.ClassVar[str] = "@scope/jsii-calc-lib.IFriendly"

    @jsii.member(jsii_name="hello")
    def hello(self) -> builtins.str:
        '''(deprecated) Say hello!

        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "hello", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFriendly).__jsii_proxy_class__ = lambda : _IFriendlyProxy


@jsii.interface(jsii_type="@scope/jsii-calc-lib.IThreeLevelsInterface")
class IThreeLevelsInterface(
    scope.jsii_calc_base.IBaseInterface,
    typing_extensions.Protocol,
):
    '''(deprecated) Interface that inherits from packages 2 levels up the tree.

    Their presence validates that .NET/Java/jsii-reflect can track all fields
    far enough up the tree.

    :stability: deprecated
    '''

    @jsii.member(jsii_name="baz")
    def baz(self) -> None:
        '''
        :stability: deprecated
        '''
        ...


class _IThreeLevelsInterfaceProxy(
    jsii.proxy_for(scope.jsii_calc_base.IBaseInterface), # type: ignore[misc]
):
    '''(deprecated) Interface that inherits from packages 2 levels up the tree.

    Their presence validates that .NET/Java/jsii-reflect can track all fields
    far enough up the tree.

    :stability: deprecated
    '''

    __jsii_type__: typing.ClassVar[str] = "@scope/jsii-calc-lib.IThreeLevelsInterface"

    @jsii.member(jsii_name="baz")
    def baz(self) -> None:
        '''
        :stability: deprecated
        '''
        return typing.cast(None, jsii.invoke(self, "baz", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IThreeLevelsInterface).__jsii_proxy_class__ = lambda : _IThreeLevelsInterfaceProxy


@jsii.data_type(
    jsii_type="@scope/jsii-calc-lib.MyFirstStruct",
    jsii_struct_bases=[],
    name_mapping={
        "anumber": "anumber",
        "astring": "astring",
        "first_optional": "firstOptional",
    },
)
class MyFirstStruct:
    def __init__(
        self,
        *,
        anumber: jsii.Number,
        astring: builtins.str,
        first_optional: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''(deprecated) This is the first struct we have created in jsii.

        :param anumber: (deprecated) An awesome number value.
        :param astring: (deprecated) A string value.
        :param first_optional: 

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MyFirstStruct.__init__)
            check_type(argname="argument anumber", value=anumber, expected_type=type_hints["anumber"])
            check_type(argname="argument astring", value=astring, expected_type=type_hints["astring"])
            check_type(argname="argument first_optional", value=first_optional, expected_type=type_hints["first_optional"])
        self._values: typing.Dict[str, typing.Any] = {
            "anumber": anumber,
            "astring": astring,
        }
        if first_optional is not None:
            self._values["first_optional"] = first_optional

    @builtins.property
    def anumber(self) -> jsii.Number:
        '''(deprecated) An awesome number value.

        :stability: deprecated
        '''
        result = self._values.get("anumber")
        assert result is not None, "Required property 'anumber' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def astring(self) -> builtins.str:
        '''(deprecated) A string value.

        :stability: deprecated
        '''
        result = self._values.get("astring")
        assert result is not None, "Required property 'astring' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def first_optional(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :stability: deprecated
        '''
        result = self._values.get("first_optional")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MyFirstStruct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NumericValue(
    scope.jsii_calc_base.Base,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@scope/jsii-calc-lib.NumericValue",
):
    '''(deprecated) Abstract class which represents a numeric value.

    :stability: deprecated
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''(deprecated) String representation of the value.

        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @builtins.property
    @jsii.member(jsii_name="value")
    @abc.abstractmethod
    def value(self) -> jsii.Number:
        '''(deprecated) The value.

        :stability: deprecated
        '''
        ...


class _NumericValueProxy(
    NumericValue,
    jsii.proxy_for(scope.jsii_calc_base.Base), # type: ignore[misc]
):
    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        '''(deprecated) The value.

        :stability: deprecated
        '''
        return typing.cast(jsii.Number, jsii.get(self, "value"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, NumericValue).__jsii_proxy_class__ = lambda : _NumericValueProxy


class Operation(
    NumericValue,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@scope/jsii-calc-lib.Operation",
):
    '''(deprecated) Represents an operation on values.

    :stability: deprecated
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="toString")
    @abc.abstractmethod
    def to_string(self) -> builtins.str:
        '''(deprecated) String representation of the value.

        :stability: deprecated
        '''
        ...


class _OperationProxy(
    Operation,
    jsii.proxy_for(NumericValue), # type: ignore[misc]
):
    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''(deprecated) String representation of the value.

        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Operation).__jsii_proxy_class__ = lambda : _OperationProxy


@jsii.data_type(
    jsii_type="@scope/jsii-calc-lib.StructWithOnlyOptionals",
    jsii_struct_bases=[],
    name_mapping={
        "optional1": "optional1",
        "optional2": "optional2",
        "optional3": "optional3",
    },
)
class StructWithOnlyOptionals:
    def __init__(
        self,
        *,
        optional1: typing.Optional[builtins.str] = None,
        optional2: typing.Optional[jsii.Number] = None,
        optional3: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(deprecated) This is a struct with only optional properties.

        :param optional1: (deprecated) The first optional!
        :param optional2: 
        :param optional3: 

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StructWithOnlyOptionals.__init__)
            check_type(argname="argument optional1", value=optional1, expected_type=type_hints["optional1"])
            check_type(argname="argument optional2", value=optional2, expected_type=type_hints["optional2"])
            check_type(argname="argument optional3", value=optional3, expected_type=type_hints["optional3"])
        self._values: typing.Dict[str, typing.Any] = {}
        if optional1 is not None:
            self._values["optional1"] = optional1
        if optional2 is not None:
            self._values["optional2"] = optional2
        if optional3 is not None:
            self._values["optional3"] = optional3

    @builtins.property
    def optional1(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The first optional!

        :stability: deprecated
        '''
        result = self._values.get("optional1")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optional2(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: deprecated
        '''
        result = self._values.get("optional2")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def optional3(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: deprecated
        '''
        result = self._values.get("optional3")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StructWithOnlyOptionals(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IDoublable)
class Number(
    NumericValue,
    metaclass=jsii.JSIIMeta,
    jsii_type="@scope/jsii-calc-lib.Number",
):
    '''(deprecated) Represents a concrete number.

    :stability: deprecated
    '''

    def __init__(self, value: jsii.Number) -> None:
        '''(deprecated) Creates a Number object.

        :param value: The number.

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Number.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.create(self.__class__, self, [value])

    @builtins.property
    @jsii.member(jsii_name="doubleValue")
    def double_value(self) -> jsii.Number:
        '''(deprecated) The number multiplied by 2.

        :stability: deprecated
        '''
        return typing.cast(jsii.Number, jsii.get(self, "doubleValue"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        '''(deprecated) The number.

        :stability: deprecated
        '''
        return typing.cast(jsii.Number, jsii.get(self, "value"))


__all__ = [
    "BaseFor2647",
    "DiamondLeft",
    "DiamondRight",
    "EnumFromScopedModule",
    "IDoublable",
    "IFriendly",
    "IThreeLevelsInterface",
    "MyFirstStruct",
    "Number",
    "NumericValue",
    "Operation",
    "StructWithOnlyOptionals",
    "custom_submodule_name",
]

publication.publish()

# Loading modules to ensure their types are registered with the jsii runtime library
from . import custom_submodule_name
