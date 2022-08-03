'''
# jsii Calculator

This library is used to demonstrate and test the features of JSII

## How to use running sum API:

First, create a calculator:

```python
calculator = calc.Calculator()
```

Then call some operations:

```python
calculator.add(10)
```

## Code Samples

```python
# This is totes a magic comment in here, just you wait!
foo = "bar"
```
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

from ._jsii import *

import scope.jsii_calc_base
import scope.jsii_calc_base_of_base
import scope.jsii_calc_lib
import scope.jsii_calc_lib.custom_submodule_name
from .composition import CompositeOperation as _CompositeOperation_1c4d123b


class AbstractClassBase(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="jsii-calc.AbstractClassBase",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @builtins.property
    @jsii.member(jsii_name="abstractProperty")
    @abc.abstractmethod
    def abstract_property(self) -> builtins.str:
        ...


class _AbstractClassBaseProxy(AbstractClassBase):
    @builtins.property
    @jsii.member(jsii_name="abstractProperty")
    def abstract_property(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "abstractProperty"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, AbstractClassBase).__jsii_proxy_class__ = lambda : _AbstractClassBaseProxy


class AbstractClassReturner(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.AbstractClassReturner",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="giveMeAbstract")
    def give_me_abstract(self) -> "AbstractClass":
        return typing.cast("AbstractClass", jsii.invoke(self, "giveMeAbstract", []))

    @jsii.member(jsii_name="giveMeInterface")
    def give_me_interface(self) -> "IInterfaceImplementedByAbstractClass":
        return typing.cast("IInterfaceImplementedByAbstractClass", jsii.invoke(self, "giveMeInterface", []))

    @builtins.property
    @jsii.member(jsii_name="returnAbstractFromProperty")
    def return_abstract_from_property(self) -> AbstractClassBase:
        return typing.cast(AbstractClassBase, jsii.get(self, "returnAbstractFromProperty"))


class AbstractSuite(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="jsii-calc.AbstractSuite",
):
    '''Ensures abstract members implementations correctly register overrides in various languages.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="someMethod")
    @abc.abstractmethod
    def _some_method(self, str: builtins.str) -> builtins.str:
        '''
        :param str: -
        '''
        ...

    @jsii.member(jsii_name="workItAll")
    def work_it_all(self, seed: builtins.str) -> builtins.str:
        '''Sets ``seed`` to ``this.property``, then calls ``someMethod`` with ``this.property`` and returns the result.

        :param seed: a ``string``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AbstractSuite.work_it_all)
            check_type(argname="argument seed", value=seed, expected_type=type_hints["seed"])
        return typing.cast(builtins.str, jsii.invoke(self, "workItAll", [seed]))

    @builtins.property
    @jsii.member(jsii_name="property")
    @abc.abstractmethod
    def _property(self) -> builtins.str:
        ...

    @_property.setter
    @abc.abstractmethod
    def _property(self, value: builtins.str) -> None:
        ...


class _AbstractSuiteProxy(AbstractSuite):
    @jsii.member(jsii_name="someMethod")
    def _some_method(self, str: builtins.str) -> builtins.str:
        '''
        :param str: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AbstractSuite._some_method)
            check_type(argname="argument str", value=str, expected_type=type_hints["str"])
        return typing.cast(builtins.str, jsii.invoke(self, "someMethod", [str]))

    @builtins.property
    @jsii.member(jsii_name="property")
    def _property(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "property"))

    @_property.setter
    def _property(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AbstractSuite, "_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "property", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, AbstractSuite).__jsii_proxy_class__ = lambda : _AbstractSuiteProxy


class AllTypes(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.AllTypes"):
    '''This class includes property for all types supported by jsii.

    The setters will validate
    that the value set is of the expected type and throw otherwise.
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="anyIn")
    def any_in(self, inp: typing.Any) -> None:
        '''
        :param inp: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AllTypes.any_in)
            check_type(argname="argument inp", value=inp, expected_type=type_hints["inp"])
        return typing.cast(None, jsii.invoke(self, "anyIn", [inp]))

    @jsii.member(jsii_name="anyOut")
    def any_out(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.invoke(self, "anyOut", []))

    @jsii.member(jsii_name="enumMethod")
    def enum_method(self, value: "StringEnum") -> "StringEnum":
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AllTypes.enum_method)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("StringEnum", jsii.invoke(self, "enumMethod", [value]))

    @builtins.property
    @jsii.member(jsii_name="enumPropertyValue")
    def enum_property_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "enumPropertyValue"))

    @builtins.property
    @jsii.member(jsii_name="anyArrayProperty")
    def any_array_property(self) -> typing.List[typing.Any]:
        return typing.cast(typing.List[typing.Any], jsii.get(self, "anyArrayProperty"))

    @any_array_property.setter
    def any_array_property(self, value: typing.List[typing.Any]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AllTypes, "any_array_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "anyArrayProperty", value)

    @builtins.property
    @jsii.member(jsii_name="anyMapProperty")
    def any_map_property(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "anyMapProperty"))

    @any_map_property.setter
    def any_map_property(self, value: typing.Mapping[builtins.str, typing.Any]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AllTypes, "any_map_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "anyMapProperty", value)

    @builtins.property
    @jsii.member(jsii_name="anyProperty")
    def any_property(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "anyProperty"))

    @any_property.setter
    def any_property(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AllTypes, "any_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "anyProperty", value)

    @builtins.property
    @jsii.member(jsii_name="arrayProperty")
    def array_property(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "arrayProperty"))

    @array_property.setter
    def array_property(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AllTypes, "array_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arrayProperty", value)

    @builtins.property
    @jsii.member(jsii_name="booleanProperty")
    def boolean_property(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "booleanProperty"))

    @boolean_property.setter
    def boolean_property(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AllTypes, "boolean_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "booleanProperty", value)

    @builtins.property
    @jsii.member(jsii_name="dateProperty")
    def date_property(self) -> datetime.datetime:
        return typing.cast(datetime.datetime, jsii.get(self, "dateProperty"))

    @date_property.setter
    def date_property(self, value: datetime.datetime) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AllTypes, "date_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dateProperty", value)

    @builtins.property
    @jsii.member(jsii_name="enumProperty")
    def enum_property(self) -> "AllTypesEnum":
        return typing.cast("AllTypesEnum", jsii.get(self, "enumProperty"))

    @enum_property.setter
    def enum_property(self, value: "AllTypesEnum") -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AllTypes, "enum_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enumProperty", value)

    @builtins.property
    @jsii.member(jsii_name="jsonProperty")
    def json_property(self) -> typing.Mapping[typing.Any, typing.Any]:
        return typing.cast(typing.Mapping[typing.Any, typing.Any], jsii.get(self, "jsonProperty"))

    @json_property.setter
    def json_property(self, value: typing.Mapping[typing.Any, typing.Any]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AllTypes, "json_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jsonProperty", value)

    @builtins.property
    @jsii.member(jsii_name="mapProperty")
    def map_property(self) -> typing.Mapping[builtins.str, scope.jsii_calc_lib.Number]:
        return typing.cast(typing.Mapping[builtins.str, scope.jsii_calc_lib.Number], jsii.get(self, "mapProperty"))

    @map_property.setter
    def map_property(
        self,
        value: typing.Mapping[builtins.str, scope.jsii_calc_lib.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AllTypes, "map_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mapProperty", value)

    @builtins.property
    @jsii.member(jsii_name="numberProperty")
    def number_property(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numberProperty"))

    @number_property.setter
    def number_property(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AllTypes, "number_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numberProperty", value)

    @builtins.property
    @jsii.member(jsii_name="stringProperty")
    def string_property(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stringProperty"))

    @string_property.setter
    def string_property(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AllTypes, "string_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stringProperty", value)

    @builtins.property
    @jsii.member(jsii_name="unionArrayProperty")
    def union_array_property(
        self,
    ) -> typing.List[typing.Union[jsii.Number, scope.jsii_calc_lib.NumericValue]]:
        return typing.cast(typing.List[typing.Union[jsii.Number, scope.jsii_calc_lib.NumericValue]], jsii.get(self, "unionArrayProperty"))

    @union_array_property.setter
    def union_array_property(
        self,
        value: typing.List[typing.Union[jsii.Number, scope.jsii_calc_lib.NumericValue]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AllTypes, "union_array_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unionArrayProperty", value)

    @builtins.property
    @jsii.member(jsii_name="unionMapProperty")
    def union_map_property(
        self,
    ) -> typing.Mapping[builtins.str, typing.Union[builtins.str, jsii.Number, scope.jsii_calc_lib.Number]]:
        return typing.cast(typing.Mapping[builtins.str, typing.Union[builtins.str, jsii.Number, scope.jsii_calc_lib.Number]], jsii.get(self, "unionMapProperty"))

    @union_map_property.setter
    def union_map_property(
        self,
        value: typing.Mapping[builtins.str, typing.Union[builtins.str, jsii.Number, scope.jsii_calc_lib.Number]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AllTypes, "union_map_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unionMapProperty", value)

    @builtins.property
    @jsii.member(jsii_name="unionProperty")
    def union_property(
        self,
    ) -> typing.Union[builtins.str, jsii.Number, scope.jsii_calc_lib.Number, "Multiply"]:
        return typing.cast(typing.Union[builtins.str, jsii.Number, scope.jsii_calc_lib.Number, "Multiply"], jsii.get(self, "unionProperty"))

    @union_property.setter
    def union_property(
        self,
        value: typing.Union[builtins.str, jsii.Number, scope.jsii_calc_lib.Number, "Multiply"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AllTypes, "union_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unionProperty", value)

    @builtins.property
    @jsii.member(jsii_name="unknownArrayProperty")
    def unknown_array_property(self) -> typing.List[typing.Any]:
        return typing.cast(typing.List[typing.Any], jsii.get(self, "unknownArrayProperty"))

    @unknown_array_property.setter
    def unknown_array_property(self, value: typing.List[typing.Any]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AllTypes, "unknown_array_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unknownArrayProperty", value)

    @builtins.property
    @jsii.member(jsii_name="unknownMapProperty")
    def unknown_map_property(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "unknownMapProperty"))

    @unknown_map_property.setter
    def unknown_map_property(
        self,
        value: typing.Mapping[builtins.str, typing.Any],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AllTypes, "unknown_map_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unknownMapProperty", value)

    @builtins.property
    @jsii.member(jsii_name="unknownProperty")
    def unknown_property(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "unknownProperty"))

    @unknown_property.setter
    def unknown_property(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AllTypes, "unknown_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unknownProperty", value)

    @builtins.property
    @jsii.member(jsii_name="optionalEnumValue")
    def optional_enum_value(self) -> typing.Optional["StringEnum"]:
        return typing.cast(typing.Optional["StringEnum"], jsii.get(self, "optionalEnumValue"))

    @optional_enum_value.setter
    def optional_enum_value(self, value: typing.Optional["StringEnum"]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AllTypes, "optional_enum_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "optionalEnumValue", value)


@jsii.enum(jsii_type="jsii-calc.AllTypesEnum")
class AllTypesEnum(enum.Enum):
    MY_ENUM_VALUE = "MY_ENUM_VALUE"
    YOUR_ENUM_VALUE = "YOUR_ENUM_VALUE"
    THIS_IS_GREAT = "THIS_IS_GREAT"


class AllowedMethodNames(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.AllowedMethodNames",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="getBar")
    def get_bar(self, _p1: builtins.str, _p2: jsii.Number) -> None:
        '''
        :param _p1: -
        :param _p2: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AllowedMethodNames.get_bar)
            check_type(argname="argument _p1", value=_p1, expected_type=type_hints["_p1"])
            check_type(argname="argument _p2", value=_p2, expected_type=type_hints["_p2"])
        return typing.cast(None, jsii.invoke(self, "getBar", [_p1, _p2]))

    @jsii.member(jsii_name="getFoo")
    def get_foo(self, with_param: builtins.str) -> builtins.str:
        '''getXxx() is not allowed (see negatives), but getXxx(a, ...) is okay.

        :param with_param: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AllowedMethodNames.get_foo)
            check_type(argname="argument with_param", value=with_param, expected_type=type_hints["with_param"])
        return typing.cast(builtins.str, jsii.invoke(self, "getFoo", [with_param]))

    @jsii.member(jsii_name="setBar")
    def set_bar(self, _x: builtins.str, _y: jsii.Number, _z: builtins.bool) -> None:
        '''
        :param _x: -
        :param _y: -
        :param _z: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AllowedMethodNames.set_bar)
            check_type(argname="argument _x", value=_x, expected_type=type_hints["_x"])
            check_type(argname="argument _y", value=_y, expected_type=type_hints["_y"])
            check_type(argname="argument _z", value=_z, expected_type=type_hints["_z"])
        return typing.cast(None, jsii.invoke(self, "setBar", [_x, _y, _z]))

    @jsii.member(jsii_name="setFoo")
    def set_foo(self, _x: builtins.str, _y: jsii.Number) -> None:
        '''setFoo(x) is not allowed (see negatives), but setXxx(a, b, ...) is okay.

        :param _x: -
        :param _y: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AllowedMethodNames.set_foo)
            check_type(argname="argument _x", value=_x, expected_type=type_hints["_x"])
            check_type(argname="argument _y", value=_y, expected_type=type_hints["_y"])
        return typing.cast(None, jsii.invoke(self, "setFoo", [_x, _y]))


class AmbiguousParameters(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.AmbiguousParameters",
):
    def __init__(
        self,
        scope_: "Bell",
        *,
        scope: builtins.str,
        props: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope_: -
        :param scope: 
        :param props: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AmbiguousParameters.__init__)
            check_type(argname="argument scope_", value=scope_, expected_type=type_hints["scope_"])
        props_ = StructParameterType(scope=scope, props=props)

        jsii.create(self.__class__, self, [scope_, props_])

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "StructParameterType":
        return typing.cast("StructParameterType", jsii.get(self, "props"))

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> "Bell":
        return typing.cast("Bell", jsii.get(self, "scope"))


class AsyncVirtualMethods(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.AsyncVirtualMethods",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="callMe")
    def call_me(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.ainvoke(self, "callMe", []))

    @jsii.member(jsii_name="callMe2")
    def call_me2(self) -> jsii.Number:
        '''Just calls "overrideMeToo".'''
        return typing.cast(jsii.Number, jsii.ainvoke(self, "callMe2", []))

    @jsii.member(jsii_name="callMeDoublePromise")
    def call_me_double_promise(self) -> jsii.Number:
        '''This method calls the "callMe" async method indirectly, which will then invoke a virtual method.

        This is a "double promise" situation, which
        means that callbacks are not going to be available immediate, but only
        after an "immediates" cycle.
        '''
        return typing.cast(jsii.Number, jsii.ainvoke(self, "callMeDoublePromise", []))

    @jsii.member(jsii_name="dontOverrideMe")
    def dont_override_me(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.invoke(self, "dontOverrideMe", []))

    @jsii.member(jsii_name="overrideMe")
    def override_me(self, mult: jsii.Number) -> jsii.Number:
        '''
        :param mult: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AsyncVirtualMethods.override_me)
            check_type(argname="argument mult", value=mult, expected_type=type_hints["mult"])
        return typing.cast(jsii.Number, jsii.ainvoke(self, "overrideMe", [mult]))

    @jsii.member(jsii_name="overrideMeToo")
    def override_me_too(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.ainvoke(self, "overrideMeToo", []))


class AugmentableClass(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.AugmentableClass"):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="methodOne")
    def method_one(self) -> None:
        return typing.cast(None, jsii.invoke(self, "methodOne", []))

    @jsii.member(jsii_name="methodTwo")
    def method_two(self) -> None:
        return typing.cast(None, jsii.invoke(self, "methodTwo", []))


class BaseClass(metaclass=jsii.JSIIAbstractClass, jsii_type="jsii-calc.BaseClass"):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="method")
    def method(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.invoke(self, "method", []))

    @builtins.property
    @jsii.member(jsii_name="property")
    def property(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "property"))


class _BaseClassProxy(BaseClass):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, BaseClass).__jsii_proxy_class__ = lambda : _BaseClassProxy


class BaseJsii976(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.BaseJsii976"):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])


@jsii.implements(scope.jsii_calc_lib.IFriendly)
class BinaryOperation(
    scope.jsii_calc_lib.Operation,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="jsii-calc.BinaryOperation",
):
    '''Represents an operation with two operands.'''

    def __init__(
        self,
        lhs: scope.jsii_calc_lib.NumericValue,
        rhs: scope.jsii_calc_lib.NumericValue,
    ) -> None:
        '''Creates a BinaryOperation.

        :param lhs: Left-hand side operand.
        :param rhs: Right-hand side operand.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BinaryOperation.__init__)
            check_type(argname="argument lhs", value=lhs, expected_type=type_hints["lhs"])
            check_type(argname="argument rhs", value=rhs, expected_type=type_hints["rhs"])
        jsii.create(self.__class__, self, [lhs, rhs])

    @jsii.member(jsii_name="hello")
    def hello(self) -> builtins.str:
        '''Say hello!'''
        return typing.cast(builtins.str, jsii.invoke(self, "hello", []))

    @builtins.property
    @jsii.member(jsii_name="lhs")
    def lhs(self) -> scope.jsii_calc_lib.NumericValue:
        '''Left-hand side operand.'''
        return typing.cast(scope.jsii_calc_lib.NumericValue, jsii.get(self, "lhs"))

    @builtins.property
    @jsii.member(jsii_name="rhs")
    def rhs(self) -> scope.jsii_calc_lib.NumericValue:
        '''Right-hand side operand.'''
        return typing.cast(scope.jsii_calc_lib.NumericValue, jsii.get(self, "rhs"))


class _BinaryOperationProxy(
    BinaryOperation,
    jsii.proxy_for(scope.jsii_calc_lib.Operation), # type: ignore[misc]
):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, BinaryOperation).__jsii_proxy_class__ = lambda : _BinaryOperationProxy


class BurriedAnonymousObject(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="jsii-calc.BurriedAnonymousObject",
):
    '''See https://github.com/aws/aws-cdk/issues/7977.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="check")
    def check(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.invoke(self, "check", []))

    @jsii.member(jsii_name="giveItBack")
    @abc.abstractmethod
    def give_it_back(self, value: typing.Any) -> typing.Any:
        '''Implement this method and have it return it's parameter.

        :param value: the value that should be returned.

        :return: ``value``
        '''
        ...


class _BurriedAnonymousObjectProxy(BurriedAnonymousObject):
    @jsii.member(jsii_name="giveItBack")
    def give_it_back(self, value: typing.Any) -> typing.Any:
        '''Implement this method and have it return it's parameter.

        :param value: the value that should be returned.

        :return: ``value``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BurriedAnonymousObject.give_it_back)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(typing.Any, jsii.invoke(self, "giveItBack", [value]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, BurriedAnonymousObject).__jsii_proxy_class__ = lambda : _BurriedAnonymousObjectProxy


class Calculator(
    _CompositeOperation_1c4d123b,
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.Calculator",
):
    '''A calculator which maintains a current value and allows adding operations.

    Here's how you use it::

       calculator = calc.Calculator()
       calculator.add(5)
       calculator.mul(3)
       print(calculator.expression.value)

    I will repeat this example again, but in an @example tag.

    Example::

        calculator = calc.Calculator()
        calculator.add(5)
        calculator.mul(3)
        print(calculator.expression.value)
    '''

    def __init__(
        self,
        *,
        initial_value: typing.Optional[jsii.Number] = None,
        maximum_value: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Creates a Calculator object.

        :param initial_value: The initial value of the calculator. NOTE: Any number works here, it's fine. Default: 0
        :param maximum_value: The maximum value the calculator can store. Default: none
        '''
        props = CalculatorProps(
            initial_value=initial_value, maximum_value=maximum_value
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="add")
    def add(self, value: jsii.Number) -> None:
        '''Adds a number to the current value.

        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Calculator.add)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "add", [value]))

    @jsii.member(jsii_name="mul")
    def mul(self, value: jsii.Number) -> None:
        '''Multiplies the current value by a number.

        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Calculator.mul)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "mul", [value]))

    @jsii.member(jsii_name="neg")
    def neg(self) -> None:
        '''Negates the current value.'''
        return typing.cast(None, jsii.invoke(self, "neg", []))

    @jsii.member(jsii_name="pow")
    def pow(self, value: jsii.Number) -> None:
        '''Raises the current value by a power.

        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Calculator.pow)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "pow", [value]))

    @jsii.member(jsii_name="readUnionValue")
    def read_union_value(self) -> jsii.Number:
        '''Returns teh value of the union property (if defined).'''
        return typing.cast(jsii.Number, jsii.invoke(self, "readUnionValue", []))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> scope.jsii_calc_lib.NumericValue:
        '''Returns the expression.'''
        return typing.cast(scope.jsii_calc_lib.NumericValue, jsii.get(self, "expression"))

    @builtins.property
    @jsii.member(jsii_name="operationsLog")
    def operations_log(self) -> typing.List[scope.jsii_calc_lib.NumericValue]:
        '''A log of all operations.'''
        return typing.cast(typing.List[scope.jsii_calc_lib.NumericValue], jsii.get(self, "operationsLog"))

    @builtins.property
    @jsii.member(jsii_name="operationsMap")
    def operations_map(
        self,
    ) -> typing.Mapping[builtins.str, typing.List[scope.jsii_calc_lib.NumericValue]]:
        '''A map of per operation name of all operations performed.'''
        return typing.cast(typing.Mapping[builtins.str, typing.List[scope.jsii_calc_lib.NumericValue]], jsii.get(self, "operationsMap"))

    @builtins.property
    @jsii.member(jsii_name="curr")
    def curr(self) -> scope.jsii_calc_lib.NumericValue:
        '''The current value.'''
        return typing.cast(scope.jsii_calc_lib.NumericValue, jsii.get(self, "curr"))

    @curr.setter
    def curr(self, value: scope.jsii_calc_lib.NumericValue) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Calculator, "curr").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "curr", value)

    @builtins.property
    @jsii.member(jsii_name="maxValue")
    def max_value(self) -> typing.Optional[jsii.Number]:
        '''The maximum value allows in this calculator.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxValue"))

    @max_value.setter
    def max_value(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Calculator, "max_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxValue", value)

    @builtins.property
    @jsii.member(jsii_name="unionProperty")
    def union_property(
        self,
    ) -> typing.Optional[typing.Union["Add", "Multiply", "Power"]]:
        '''Example of a property that accepts a union of types.'''
        return typing.cast(typing.Optional[typing.Union["Add", "Multiply", "Power"]], jsii.get(self, "unionProperty"))

    @union_property.setter
    def union_property(
        self,
        value: typing.Optional[typing.Union["Add", "Multiply", "Power"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Calculator, "union_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unionProperty", value)


@jsii.data_type(
    jsii_type="jsii-calc.CalculatorProps",
    jsii_struct_bases=[],
    name_mapping={"initial_value": "initialValue", "maximum_value": "maximumValue"},
)
class CalculatorProps:
    def __init__(
        self,
        *,
        initial_value: typing.Optional[jsii.Number] = None,
        maximum_value: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for Calculator.

        :param initial_value: The initial value of the calculator. NOTE: Any number works here, it's fine. Default: 0
        :param maximum_value: The maximum value the calculator can store. Default: none
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CalculatorProps.__init__)
            check_type(argname="argument initial_value", value=initial_value, expected_type=type_hints["initial_value"])
            check_type(argname="argument maximum_value", value=maximum_value, expected_type=type_hints["maximum_value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if initial_value is not None:
            self._values["initial_value"] = initial_value
        if maximum_value is not None:
            self._values["maximum_value"] = maximum_value

    @builtins.property
    def initial_value(self) -> typing.Optional[jsii.Number]:
        '''The initial value of the calculator.

        NOTE: Any number works here, it's fine.

        :default: 0
        '''
        result = self._values.get("initial_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def maximum_value(self) -> typing.Optional[jsii.Number]:
        '''The maximum value the calculator can store.

        :default: none
        '''
        result = self._values.get("maximum_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CalculatorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClassWithCollections(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.ClassWithCollections",
):
    def __init__(
        self,
        map: typing.Mapping[builtins.str, builtins.str],
        array: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param map: -
        :param array: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClassWithCollections.__init__)
            check_type(argname="argument map", value=map, expected_type=type_hints["map"])
            check_type(argname="argument array", value=array, expected_type=type_hints["array"])
        jsii.create(self.__class__, self, [map, array])

    @jsii.member(jsii_name="createAList")
    @builtins.classmethod
    def create_a_list(cls) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.sinvoke(cls, "createAList", []))

    @jsii.member(jsii_name="createAMap")
    @builtins.classmethod
    def create_a_map(cls) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.sinvoke(cls, "createAMap", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="staticArray")
    def static_array(cls) -> typing.List[builtins.str]:  # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(typing.List[builtins.str], jsii.sget(cls, "staticArray"))

    @static_array.setter # type: ignore[no-redef]
    def static_array(cls, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClassWithCollections, "static_array").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.sset(cls, "staticArray", value)

    @jsii.python.classproperty
    @jsii.member(jsii_name="staticMap")
    def static_map(cls) -> typing.Mapping[builtins.str, builtins.str]:  # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.sget(cls, "staticMap"))

    @static_map.setter # type: ignore[no-redef]
    def static_map(cls, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClassWithCollections, "static_map").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.sset(cls, "staticMap", value)

    @builtins.property
    @jsii.member(jsii_name="array")
    def array(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "array"))

    @array.setter
    def array(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClassWithCollections, "array").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "array", value)

    @builtins.property
    @jsii.member(jsii_name="map")
    def map(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "map"))

    @map.setter
    def map(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClassWithCollections, "map").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "map", value)


class ClassWithContainerTypes(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.ClassWithContainerTypes",
):
    def __init__(
        self,
        array: typing.Sequence[typing.Union["DummyObj", typing.Dict[str, typing.Any]]],
        record: typing.Mapping[builtins.str, typing.Union["DummyObj", typing.Dict[str, typing.Any]]],
        obj: typing.Mapping[builtins.str, typing.Union["DummyObj", typing.Dict[str, typing.Any]]],
        *,
        array_prop: typing.Sequence[typing.Union["DummyObj", typing.Dict[str, typing.Any]]],
        obj_prop: typing.Mapping[builtins.str, typing.Union["DummyObj", typing.Dict[str, typing.Any]]],
        record_prop: typing.Mapping[builtins.str, typing.Union["DummyObj", typing.Dict[str, typing.Any]]],
    ) -> None:
        '''
        :param array: -
        :param record: -
        :param obj: -
        :param array_prop: 
        :param obj_prop: 
        :param record_prop: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClassWithContainerTypes.__init__)
            check_type(argname="argument array", value=array, expected_type=type_hints["array"])
            check_type(argname="argument record", value=record, expected_type=type_hints["record"])
            check_type(argname="argument obj", value=obj, expected_type=type_hints["obj"])
        props = ContainerProps(
            array_prop=array_prop, obj_prop=obj_prop, record_prop=record_prop
        )

        jsii.create(self.__class__, self, [array, record, obj, props])

    @builtins.property
    @jsii.member(jsii_name="array")
    def array(self) -> typing.List["DummyObj"]:
        return typing.cast(typing.List["DummyObj"], jsii.get(self, "array"))

    @builtins.property
    @jsii.member(jsii_name="obj")
    def obj(self) -> typing.Mapping[builtins.str, "DummyObj"]:
        return typing.cast(typing.Mapping[builtins.str, "DummyObj"], jsii.get(self, "obj"))

    @builtins.property
    @jsii.member(jsii_name="record")
    def record(self) -> typing.Mapping[builtins.str, "DummyObj"]:
        return typing.cast(typing.Mapping[builtins.str, "DummyObj"], jsii.get(self, "record"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> typing.Optional["ContainerProps"]:
        return typing.cast(typing.Optional["ContainerProps"], jsii.get(self, "props"))


class ClassWithDocs(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.ClassWithDocs"):
    '''This class has docs.

    The docs are great. They're a bunch of tags.

    :see: https://aws.amazon.com/
    :customAttribute: hasAValue

    Example::

        def an_example():
            pass
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])


class ClassWithJavaReservedWords(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.ClassWithJavaReservedWords",
):
    def __init__(self, int: builtins.str) -> None:
        '''
        :param int: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClassWithJavaReservedWords.__init__)
            check_type(argname="argument int", value=int, expected_type=type_hints["int"])
        jsii.create(self.__class__, self, [int])

    @jsii.member(jsii_name="import")
    def import_(self, assert_: builtins.str) -> builtins.str:
        '''
        :param assert_: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClassWithJavaReservedWords.import_)
            check_type(argname="argument assert_", value=assert_, expected_type=type_hints["assert_"])
        return typing.cast(builtins.str, jsii.invoke(self, "import", [assert_]))

    @builtins.property
    @jsii.member(jsii_name="int")
    def int(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "int"))


class ClassWithMutableObjectLiteralProperty(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.ClassWithMutableObjectLiteralProperty",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @builtins.property
    @jsii.member(jsii_name="mutableObject")
    def mutable_object(self) -> "IMutableObjectLiteral":
        return typing.cast("IMutableObjectLiteral", jsii.get(self, "mutableObject"))

    @mutable_object.setter
    def mutable_object(self, value: "IMutableObjectLiteral") -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClassWithMutableObjectLiteralProperty, "mutable_object").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mutableObject", value)


class ConfusingToJackson(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.ConfusingToJackson",
):
    '''This tries to confuse Jackson by having overloaded property setters.

    :see: https://github.com/aws/aws-cdk/issues/4080
    '''

    @jsii.member(jsii_name="makeInstance")
    @builtins.classmethod
    def make_instance(cls) -> "ConfusingToJackson":
        return typing.cast("ConfusingToJackson", jsii.sinvoke(cls, "makeInstance", []))

    @jsii.member(jsii_name="makeStructInstance")
    @builtins.classmethod
    def make_struct_instance(cls) -> "ConfusingToJacksonStruct":
        return typing.cast("ConfusingToJacksonStruct", jsii.sinvoke(cls, "makeStructInstance", []))

    @builtins.property
    @jsii.member(jsii_name="unionProperty")
    def union_property(
        self,
    ) -> typing.Optional[typing.Union[scope.jsii_calc_lib.IFriendly, typing.List[typing.Union[scope.jsii_calc_lib.IFriendly, "AbstractClass"]]]]:
        return typing.cast(typing.Optional[typing.Union[scope.jsii_calc_lib.IFriendly, typing.List[typing.Union[scope.jsii_calc_lib.IFriendly, "AbstractClass"]]]], jsii.get(self, "unionProperty"))

    @union_property.setter
    def union_property(
        self,
        value: typing.Optional[typing.Union[scope.jsii_calc_lib.IFriendly, typing.List[typing.Union[scope.jsii_calc_lib.IFriendly, "AbstractClass"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConfusingToJackson, "union_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unionProperty", value)


@jsii.data_type(
    jsii_type="jsii-calc.ConfusingToJacksonStruct",
    jsii_struct_bases=[],
    name_mapping={"union_property": "unionProperty"},
)
class ConfusingToJacksonStruct:
    def __init__(
        self,
        *,
        union_property: typing.Optional[typing.Union[scope.jsii_calc_lib.IFriendly, typing.Sequence[typing.Union[scope.jsii_calc_lib.IFriendly, "AbstractClass"]]]] = None,
    ) -> None:
        '''
        :param union_property: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConfusingToJacksonStruct.__init__)
            check_type(argname="argument union_property", value=union_property, expected_type=type_hints["union_property"])
        self._values: typing.Dict[str, typing.Any] = {}
        if union_property is not None:
            self._values["union_property"] = union_property

    @builtins.property
    def union_property(
        self,
    ) -> typing.Optional[typing.Union[scope.jsii_calc_lib.IFriendly, typing.List[typing.Union[scope.jsii_calc_lib.IFriendly, "AbstractClass"]]]]:
        result = self._values.get("union_property")
        return typing.cast(typing.Optional[typing.Union[scope.jsii_calc_lib.IFriendly, typing.List[typing.Union[scope.jsii_calc_lib.IFriendly, "AbstractClass"]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfusingToJacksonStruct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConstructorPassesThisOut(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.ConstructorPassesThisOut",
):
    def __init__(self, consumer: "PartiallyInitializedThisConsumer") -> None:
        '''
        :param consumer: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConstructorPassesThisOut.__init__)
            check_type(argname="argument consumer", value=consumer, expected_type=type_hints["consumer"])
        jsii.create(self.__class__, self, [consumer])


class Constructors(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.Constructors"):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="hiddenInterface")
    @builtins.classmethod
    def hidden_interface(cls) -> "IPublicInterface":
        return typing.cast("IPublicInterface", jsii.sinvoke(cls, "hiddenInterface", []))

    @jsii.member(jsii_name="hiddenInterfaces")
    @builtins.classmethod
    def hidden_interfaces(cls) -> typing.List["IPublicInterface"]:
        return typing.cast(typing.List["IPublicInterface"], jsii.sinvoke(cls, "hiddenInterfaces", []))

    @jsii.member(jsii_name="hiddenSubInterfaces")
    @builtins.classmethod
    def hidden_sub_interfaces(cls) -> typing.List["IPublicInterface"]:
        return typing.cast(typing.List["IPublicInterface"], jsii.sinvoke(cls, "hiddenSubInterfaces", []))

    @jsii.member(jsii_name="makeClass")
    @builtins.classmethod
    def make_class(cls) -> "PublicClass":
        return typing.cast("PublicClass", jsii.sinvoke(cls, "makeClass", []))

    @jsii.member(jsii_name="makeInterface")
    @builtins.classmethod
    def make_interface(cls) -> "IPublicInterface":
        return typing.cast("IPublicInterface", jsii.sinvoke(cls, "makeInterface", []))

    @jsii.member(jsii_name="makeInterface2")
    @builtins.classmethod
    def make_interface2(cls) -> "IPublicInterface2":
        return typing.cast("IPublicInterface2", jsii.sinvoke(cls, "makeInterface2", []))

    @jsii.member(jsii_name="makeInterfaces")
    @builtins.classmethod
    def make_interfaces(cls) -> typing.List["IPublicInterface"]:
        return typing.cast(typing.List["IPublicInterface"], jsii.sinvoke(cls, "makeInterfaces", []))


class ConsumePureInterface(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.ConsumePureInterface",
):
    def __init__(self, delegate: "IStructReturningDelegate") -> None:
        '''
        :param delegate: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumePureInterface.__init__)
            check_type(argname="argument delegate", value=delegate, expected_type=type_hints["delegate"])
        jsii.create(self.__class__, self, [delegate])

    @jsii.member(jsii_name="workItBaby")
    def work_it_baby(self) -> "StructB":
        return typing.cast("StructB", jsii.invoke(self, "workItBaby", []))


class ConsumerCanRingBell(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.ConsumerCanRingBell",
):
    '''Test calling back to consumers that implement interfaces.

    Check that if a JSII consumer implements IConsumerWithInterfaceParam, they can call
    the method on the argument that they're passed...
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="staticImplementedByObjectLiteral")
    @builtins.classmethod
    def static_implemented_by_object_literal(
        cls,
        ringer: "IBellRinger",
    ) -> builtins.bool:
        '''...if the interface is implemented using an object literal.

        Returns whether the bell was rung.

        :param ringer: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumerCanRingBell.static_implemented_by_object_literal)
            check_type(argname="argument ringer", value=ringer, expected_type=type_hints["ringer"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "staticImplementedByObjectLiteral", [ringer]))

    @jsii.member(jsii_name="staticImplementedByPrivateClass")
    @builtins.classmethod
    def static_implemented_by_private_class(
        cls,
        ringer: "IBellRinger",
    ) -> builtins.bool:
        '''...if the interface is implemented using a private class.

        Return whether the bell was rung.

        :param ringer: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumerCanRingBell.static_implemented_by_private_class)
            check_type(argname="argument ringer", value=ringer, expected_type=type_hints["ringer"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "staticImplementedByPrivateClass", [ringer]))

    @jsii.member(jsii_name="staticImplementedByPublicClass")
    @builtins.classmethod
    def static_implemented_by_public_class(cls, ringer: "IBellRinger") -> builtins.bool:
        '''...if the interface is implemented using a public class.

        Return whether the bell was rung.

        :param ringer: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumerCanRingBell.static_implemented_by_public_class)
            check_type(argname="argument ringer", value=ringer, expected_type=type_hints["ringer"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "staticImplementedByPublicClass", [ringer]))

    @jsii.member(jsii_name="staticWhenTypedAsClass")
    @builtins.classmethod
    def static_when_typed_as_class(cls, ringer: "IConcreteBellRinger") -> builtins.bool:
        '''If the parameter is a concrete class instead of an interface.

        Return whether the bell was rung.

        :param ringer: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumerCanRingBell.static_when_typed_as_class)
            check_type(argname="argument ringer", value=ringer, expected_type=type_hints["ringer"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "staticWhenTypedAsClass", [ringer]))

    @jsii.member(jsii_name="implementedByObjectLiteral")
    def implemented_by_object_literal(self, ringer: "IBellRinger") -> builtins.bool:
        '''...if the interface is implemented using an object literal.

        Returns whether the bell was rung.

        :param ringer: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumerCanRingBell.implemented_by_object_literal)
            check_type(argname="argument ringer", value=ringer, expected_type=type_hints["ringer"])
        return typing.cast(builtins.bool, jsii.invoke(self, "implementedByObjectLiteral", [ringer]))

    @jsii.member(jsii_name="implementedByPrivateClass")
    def implemented_by_private_class(self, ringer: "IBellRinger") -> builtins.bool:
        '''...if the interface is implemented using a private class.

        Return whether the bell was rung.

        :param ringer: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumerCanRingBell.implemented_by_private_class)
            check_type(argname="argument ringer", value=ringer, expected_type=type_hints["ringer"])
        return typing.cast(builtins.bool, jsii.invoke(self, "implementedByPrivateClass", [ringer]))

    @jsii.member(jsii_name="implementedByPublicClass")
    def implemented_by_public_class(self, ringer: "IBellRinger") -> builtins.bool:
        '''...if the interface is implemented using a public class.

        Return whether the bell was rung.

        :param ringer: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumerCanRingBell.implemented_by_public_class)
            check_type(argname="argument ringer", value=ringer, expected_type=type_hints["ringer"])
        return typing.cast(builtins.bool, jsii.invoke(self, "implementedByPublicClass", [ringer]))

    @jsii.member(jsii_name="whenTypedAsClass")
    def when_typed_as_class(self, ringer: "IConcreteBellRinger") -> builtins.bool:
        '''If the parameter is a concrete class instead of an interface.

        Return whether the bell was rung.

        :param ringer: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumerCanRingBell.when_typed_as_class)
            check_type(argname="argument ringer", value=ringer, expected_type=type_hints["ringer"])
        return typing.cast(builtins.bool, jsii.invoke(self, "whenTypedAsClass", [ringer]))


class ConsumersOfThisCrazyTypeSystem(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.ConsumersOfThisCrazyTypeSystem",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="consumeAnotherPublicInterface")
    def consume_another_public_interface(
        self,
        obj: "IAnotherPublicInterface",
    ) -> builtins.str:
        '''
        :param obj: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumersOfThisCrazyTypeSystem.consume_another_public_interface)
            check_type(argname="argument obj", value=obj, expected_type=type_hints["obj"])
        return typing.cast(builtins.str, jsii.invoke(self, "consumeAnotherPublicInterface", [obj]))

    @jsii.member(jsii_name="consumeNonInternalInterface")
    def consume_non_internal_interface(
        self,
        obj: "INonInternalInterface",
    ) -> typing.Any:
        '''
        :param obj: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsumersOfThisCrazyTypeSystem.consume_non_internal_interface)
            check_type(argname="argument obj", value=obj, expected_type=type_hints["obj"])
        return typing.cast(typing.Any, jsii.invoke(self, "consumeNonInternalInterface", [obj]))


@jsii.data_type(
    jsii_type="jsii-calc.ContainerProps",
    jsii_struct_bases=[],
    name_mapping={
        "array_prop": "arrayProp",
        "obj_prop": "objProp",
        "record_prop": "recordProp",
    },
)
class ContainerProps:
    def __init__(
        self,
        *,
        array_prop: typing.Sequence[typing.Union["DummyObj", typing.Dict[str, typing.Any]]],
        obj_prop: typing.Mapping[builtins.str, typing.Union["DummyObj", typing.Dict[str, typing.Any]]],
        record_prop: typing.Mapping[builtins.str, typing.Union["DummyObj", typing.Dict[str, typing.Any]]],
    ) -> None:
        '''
        :param array_prop: 
        :param obj_prop: 
        :param record_prop: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerProps.__init__)
            check_type(argname="argument array_prop", value=array_prop, expected_type=type_hints["array_prop"])
            check_type(argname="argument obj_prop", value=obj_prop, expected_type=type_hints["obj_prop"])
            check_type(argname="argument record_prop", value=record_prop, expected_type=type_hints["record_prop"])
        self._values: typing.Dict[str, typing.Any] = {
            "array_prop": array_prop,
            "obj_prop": obj_prop,
            "record_prop": record_prop,
        }

    @builtins.property
    def array_prop(self) -> typing.List["DummyObj"]:
        result = self._values.get("array_prop")
        assert result is not None, "Required property 'array_prop' is missing"
        return typing.cast(typing.List["DummyObj"], result)

    @builtins.property
    def obj_prop(self) -> typing.Mapping[builtins.str, "DummyObj"]:
        result = self._values.get("obj_prop")
        assert result is not None, "Required property 'obj_prop' is missing"
        return typing.cast(typing.Mapping[builtins.str, "DummyObj"], result)

    @builtins.property
    def record_prop(self) -> typing.Mapping[builtins.str, "DummyObj"]:
        result = self._values.get("record_prop")
        assert result is not None, "Required property 'record_prop' is missing"
        return typing.cast(typing.Mapping[builtins.str, "DummyObj"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataRenderer(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.DataRenderer"):
    '''Verifies proper type handling through dynamic overrides.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="render")
    def render(
        self,
        *,
        anumber: jsii.Number,
        astring: builtins.str,
        first_optional: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> builtins.str:
        '''
        :param anumber: (deprecated) An awesome number value.
        :param astring: (deprecated) A string value.
        :param first_optional: 
        '''
        data = scope.jsii_calc_lib.MyFirstStruct(
            anumber=anumber, astring=astring, first_optional=first_optional
        )

        return typing.cast(builtins.str, jsii.invoke(self, "render", [data]))

    @jsii.member(jsii_name="renderArbitrary")
    def render_arbitrary(
        self,
        data: typing.Mapping[builtins.str, typing.Any],
    ) -> builtins.str:
        '''
        :param data: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataRenderer.render_arbitrary)
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
        return typing.cast(builtins.str, jsii.invoke(self, "renderArbitrary", [data]))

    @jsii.member(jsii_name="renderMap")
    def render_map(self, map: typing.Mapping[builtins.str, typing.Any]) -> builtins.str:
        '''
        :param map: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataRenderer.render_map)
            check_type(argname="argument map", value=map, expected_type=type_hints["map"])
        return typing.cast(builtins.str, jsii.invoke(self, "renderMap", [map]))


class Default(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.Default"):
    '''A class named "Default".

    :see: https://github.com/aws/jsii/issues/2637
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="pleaseCompile")
    def please_compile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "pleaseCompile", []))


class DefaultedConstructorArgument(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.DefaultedConstructorArgument",
):
    def __init__(
        self,
        arg1: typing.Optional[jsii.Number] = None,
        arg2: typing.Optional[builtins.str] = None,
        arg3: typing.Optional[datetime.datetime] = None,
    ) -> None:
        '''
        :param arg1: -
        :param arg2: -
        :param arg3: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DefaultedConstructorArgument.__init__)
            check_type(argname="argument arg1", value=arg1, expected_type=type_hints["arg1"])
            check_type(argname="argument arg2", value=arg2, expected_type=type_hints["arg2"])
            check_type(argname="argument arg3", value=arg3, expected_type=type_hints["arg3"])
        jsii.create(self.__class__, self, [arg1, arg2, arg3])

    @builtins.property
    @jsii.member(jsii_name="arg1")
    def arg1(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "arg1"))

    @builtins.property
    @jsii.member(jsii_name="arg3")
    def arg3(self) -> datetime.datetime:
        return typing.cast(datetime.datetime, jsii.get(self, "arg3"))

    @builtins.property
    @jsii.member(jsii_name="arg2")
    def arg2(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arg2"))


class Demonstrate982(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.Demonstrate982"):
    '''1.

    call #takeThis() -> An ObjectRef will be provisioned for the value (it'll be re-used!)
    2. call #takeThisToo() -> The ObjectRef from before will need to be down-cased to the ParentStruct982 type
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="takeThis")
    @builtins.classmethod
    def take_this(cls) -> "ChildStruct982":
        '''It's dangerous to go alone!'''
        return typing.cast("ChildStruct982", jsii.sinvoke(cls, "takeThis", []))

    @jsii.member(jsii_name="takeThisToo")
    @builtins.classmethod
    def take_this_too(cls) -> "ParentStruct982":
        '''It's dangerous to go alone!'''
        return typing.cast("ParentStruct982", jsii.sinvoke(cls, "takeThisToo", []))


class DeprecatedClass(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.DeprecatedClass"):
    '''
    :deprecated: a pretty boring class

    :stability: deprecated
    '''

    def __init__(
        self,
        readonly_string: builtins.str,
        mutable_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param readonly_string: -
        :param mutable_number: -

        :deprecated: this constructor is "just" okay

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DeprecatedClass.__init__)
            check_type(argname="argument readonly_string", value=readonly_string, expected_type=type_hints["readonly_string"])
            check_type(argname="argument mutable_number", value=mutable_number, expected_type=type_hints["mutable_number"])
        jsii.create(self.__class__, self, [readonly_string, mutable_number])

    @jsii.member(jsii_name="method")
    def method(self) -> None:
        '''
        :deprecated: it was a bad idea

        :stability: deprecated
        '''
        return typing.cast(None, jsii.invoke(self, "method", []))

    @builtins.property
    @jsii.member(jsii_name="readonlyProperty")
    def readonly_property(self) -> builtins.str:
        '''
        :deprecated: this is not always "wazoo", be ready to be disappointed

        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.get(self, "readonlyProperty"))

    @builtins.property
    @jsii.member(jsii_name="mutableProperty")
    def mutable_property(self) -> typing.Optional[jsii.Number]:
        '''
        :deprecated: shouldn't have been mutable

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "mutableProperty"))

    @mutable_property.setter
    def mutable_property(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DeprecatedClass, "mutable_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mutableProperty", value)


@jsii.enum(jsii_type="jsii-calc.DeprecatedEnum")
class DeprecatedEnum(enum.Enum):
    '''
    :deprecated: your deprecated selection of bad options

    :stability: deprecated
    '''

    OPTION_A = "OPTION_A"
    '''
    :deprecated: option A is not great

    :stability: deprecated
    '''
    OPTION_B = "OPTION_B"
    '''
    :deprecated: option B is kinda bad, too

    :stability: deprecated
    '''


@jsii.data_type(
    jsii_type="jsii-calc.DeprecatedStruct",
    jsii_struct_bases=[],
    name_mapping={"readonly_property": "readonlyProperty"},
)
class DeprecatedStruct:
    def __init__(self, *, readonly_property: builtins.str) -> None:
        '''
        :param readonly_property: 

        :deprecated: it just wraps a string

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DeprecatedStruct.__init__)
            check_type(argname="argument readonly_property", value=readonly_property, expected_type=type_hints["readonly_property"])
        self._values: typing.Dict[str, typing.Any] = {
            "readonly_property": readonly_property,
        }

    @builtins.property
    def readonly_property(self) -> builtins.str:
        '''
        :deprecated: well, yeah

        :stability: deprecated
        '''
        result = self._values.get("readonly_property")
        assert result is not None, "Required property 'readonly_property' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeprecatedStruct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="jsii-calc.DerivedStruct",
    jsii_struct_bases=[scope.jsii_calc_lib.MyFirstStruct],
    name_mapping={
        "anumber": "anumber",
        "astring": "astring",
        "first_optional": "firstOptional",
        "another_required": "anotherRequired",
        "bool": "bool",
        "non_primitive": "nonPrimitive",
        "another_optional": "anotherOptional",
        "optional_any": "optionalAny",
        "optional_array": "optionalArray",
    },
)
class DerivedStruct(scope.jsii_calc_lib.MyFirstStruct):
    def __init__(
        self,
        *,
        anumber: jsii.Number,
        astring: builtins.str,
        first_optional: typing.Optional[typing.Sequence[builtins.str]] = None,
        another_required: datetime.datetime,
        bool: builtins.bool,
        non_primitive: "DoubleTrouble",
        another_optional: typing.Optional[typing.Mapping[builtins.str, scope.jsii_calc_lib.NumericValue]] = None,
        optional_any: typing.Any = None,
        optional_array: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A struct which derives from another struct.

        :param anumber: (deprecated) An awesome number value.
        :param astring: (deprecated) A string value.
        :param first_optional: 
        :param another_required: 
        :param bool: 
        :param non_primitive: An example of a non primitive property.
        :param another_optional: This is optional.
        :param optional_any: 
        :param optional_array: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DerivedStruct.__init__)
            check_type(argname="argument anumber", value=anumber, expected_type=type_hints["anumber"])
            check_type(argname="argument astring", value=astring, expected_type=type_hints["astring"])
            check_type(argname="argument first_optional", value=first_optional, expected_type=type_hints["first_optional"])
            check_type(argname="argument another_required", value=another_required, expected_type=type_hints["another_required"])
            check_type(argname="argument bool", value=bool, expected_type=type_hints["bool"])
            check_type(argname="argument non_primitive", value=non_primitive, expected_type=type_hints["non_primitive"])
            check_type(argname="argument another_optional", value=another_optional, expected_type=type_hints["another_optional"])
            check_type(argname="argument optional_any", value=optional_any, expected_type=type_hints["optional_any"])
            check_type(argname="argument optional_array", value=optional_array, expected_type=type_hints["optional_array"])
        self._values: typing.Dict[str, typing.Any] = {
            "anumber": anumber,
            "astring": astring,
            "another_required": another_required,
            "bool": bool,
            "non_primitive": non_primitive,
        }
        if first_optional is not None:
            self._values["first_optional"] = first_optional
        if another_optional is not None:
            self._values["another_optional"] = another_optional
        if optional_any is not None:
            self._values["optional_any"] = optional_any
        if optional_array is not None:
            self._values["optional_array"] = optional_array

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

    @builtins.property
    def another_required(self) -> datetime.datetime:
        result = self._values.get("another_required")
        assert result is not None, "Required property 'another_required' is missing"
        return typing.cast(datetime.datetime, result)

    @builtins.property
    def bool(self) -> builtins.bool:
        result = self._values.get("bool")
        assert result is not None, "Required property 'bool' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def non_primitive(self) -> "DoubleTrouble":
        '''An example of a non primitive property.'''
        result = self._values.get("non_primitive")
        assert result is not None, "Required property 'non_primitive' is missing"
        return typing.cast("DoubleTrouble", result)

    @builtins.property
    def another_optional(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, scope.jsii_calc_lib.NumericValue]]:
        '''This is optional.'''
        result = self._values.get("another_optional")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, scope.jsii_calc_lib.NumericValue]], result)

    @builtins.property
    def optional_any(self) -> typing.Any:
        result = self._values.get("optional_any")
        return typing.cast(typing.Any, result)

    @builtins.property
    def optional_array(self) -> typing.Optional[typing.List[builtins.str]]:
        result = self._values.get("optional_array")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DerivedStruct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="jsii-calc.DiamondBottom",
    jsii_struct_bases=[
        scope.jsii_calc_lib.DiamondLeft, scope.jsii_calc_lib.DiamondRight
    ],
    name_mapping={
        "hoisted_top": "hoistedTop",
        "left": "left",
        "right": "right",
        "bottom": "bottom",
    },
)
class DiamondBottom(scope.jsii_calc_lib.DiamondLeft, scope.jsii_calc_lib.DiamondRight):
    def __init__(
        self,
        *,
        hoisted_top: typing.Optional[builtins.str] = None,
        left: typing.Optional[jsii.Number] = None,
        right: typing.Optional[builtins.bool] = None,
        bottom: typing.Optional[datetime.datetime] = None,
    ) -> None:
        '''
        :param hoisted_top: 
        :param left: 
        :param right: 
        :param bottom: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DiamondBottom.__init__)
            check_type(argname="argument hoisted_top", value=hoisted_top, expected_type=type_hints["hoisted_top"])
            check_type(argname="argument left", value=left, expected_type=type_hints["left"])
            check_type(argname="argument right", value=right, expected_type=type_hints["right"])
            check_type(argname="argument bottom", value=bottom, expected_type=type_hints["bottom"])
        self._values: typing.Dict[str, typing.Any] = {}
        if hoisted_top is not None:
            self._values["hoisted_top"] = hoisted_top
        if left is not None:
            self._values["left"] = left
        if right is not None:
            self._values["right"] = right
        if bottom is not None:
            self._values["bottom"] = bottom

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

    @builtins.property
    def right(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: deprecated
        '''
        result = self._values.get("right")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def bottom(self) -> typing.Optional[datetime.datetime]:
        result = self._values.get("bottom")
        return typing.cast(typing.Optional[datetime.datetime], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DiamondBottom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="jsii-calc.DiamondInheritanceBaseLevelStruct",
    jsii_struct_bases=[],
    name_mapping={"base_level_property": "baseLevelProperty"},
)
class DiamondInheritanceBaseLevelStruct:
    def __init__(self, *, base_level_property: builtins.str) -> None:
        '''
        :param base_level_property: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DiamondInheritanceBaseLevelStruct.__init__)
            check_type(argname="argument base_level_property", value=base_level_property, expected_type=type_hints["base_level_property"])
        self._values: typing.Dict[str, typing.Any] = {
            "base_level_property": base_level_property,
        }

    @builtins.property
    def base_level_property(self) -> builtins.str:
        result = self._values.get("base_level_property")
        assert result is not None, "Required property 'base_level_property' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DiamondInheritanceBaseLevelStruct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="jsii-calc.DiamondInheritanceFirstMidLevelStruct",
    jsii_struct_bases=[DiamondInheritanceBaseLevelStruct],
    name_mapping={
        "base_level_property": "baseLevelProperty",
        "first_mid_level_property": "firstMidLevelProperty",
    },
)
class DiamondInheritanceFirstMidLevelStruct(DiamondInheritanceBaseLevelStruct):
    def __init__(
        self,
        *,
        base_level_property: builtins.str,
        first_mid_level_property: builtins.str,
    ) -> None:
        '''
        :param base_level_property: 
        :param first_mid_level_property: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DiamondInheritanceFirstMidLevelStruct.__init__)
            check_type(argname="argument base_level_property", value=base_level_property, expected_type=type_hints["base_level_property"])
            check_type(argname="argument first_mid_level_property", value=first_mid_level_property, expected_type=type_hints["first_mid_level_property"])
        self._values: typing.Dict[str, typing.Any] = {
            "base_level_property": base_level_property,
            "first_mid_level_property": first_mid_level_property,
        }

    @builtins.property
    def base_level_property(self) -> builtins.str:
        result = self._values.get("base_level_property")
        assert result is not None, "Required property 'base_level_property' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def first_mid_level_property(self) -> builtins.str:
        result = self._values.get("first_mid_level_property")
        assert result is not None, "Required property 'first_mid_level_property' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DiamondInheritanceFirstMidLevelStruct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="jsii-calc.DiamondInheritanceSecondMidLevelStruct",
    jsii_struct_bases=[DiamondInheritanceBaseLevelStruct],
    name_mapping={
        "base_level_property": "baseLevelProperty",
        "second_mid_level_property": "secondMidLevelProperty",
    },
)
class DiamondInheritanceSecondMidLevelStruct(DiamondInheritanceBaseLevelStruct):
    def __init__(
        self,
        *,
        base_level_property: builtins.str,
        second_mid_level_property: builtins.str,
    ) -> None:
        '''
        :param base_level_property: 
        :param second_mid_level_property: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DiamondInheritanceSecondMidLevelStruct.__init__)
            check_type(argname="argument base_level_property", value=base_level_property, expected_type=type_hints["base_level_property"])
            check_type(argname="argument second_mid_level_property", value=second_mid_level_property, expected_type=type_hints["second_mid_level_property"])
        self._values: typing.Dict[str, typing.Any] = {
            "base_level_property": base_level_property,
            "second_mid_level_property": second_mid_level_property,
        }

    @builtins.property
    def base_level_property(self) -> builtins.str:
        result = self._values.get("base_level_property")
        assert result is not None, "Required property 'base_level_property' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def second_mid_level_property(self) -> builtins.str:
        result = self._values.get("second_mid_level_property")
        assert result is not None, "Required property 'second_mid_level_property' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DiamondInheritanceSecondMidLevelStruct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="jsii-calc.DiamondInheritanceTopLevelStruct",
    jsii_struct_bases=[
        DiamondInheritanceFirstMidLevelStruct, DiamondInheritanceSecondMidLevelStruct
    ],
    name_mapping={
        "base_level_property": "baseLevelProperty",
        "first_mid_level_property": "firstMidLevelProperty",
        "second_mid_level_property": "secondMidLevelProperty",
        "top_level_property": "topLevelProperty",
    },
)
class DiamondInheritanceTopLevelStruct(
    DiamondInheritanceFirstMidLevelStruct,
    DiamondInheritanceSecondMidLevelStruct,
):
    def __init__(
        self,
        *,
        base_level_property: builtins.str,
        first_mid_level_property: builtins.str,
        second_mid_level_property: builtins.str,
        top_level_property: builtins.str,
    ) -> None:
        '''
        :param base_level_property: 
        :param first_mid_level_property: 
        :param second_mid_level_property: 
        :param top_level_property: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DiamondInheritanceTopLevelStruct.__init__)
            check_type(argname="argument base_level_property", value=base_level_property, expected_type=type_hints["base_level_property"])
            check_type(argname="argument first_mid_level_property", value=first_mid_level_property, expected_type=type_hints["first_mid_level_property"])
            check_type(argname="argument second_mid_level_property", value=second_mid_level_property, expected_type=type_hints["second_mid_level_property"])
            check_type(argname="argument top_level_property", value=top_level_property, expected_type=type_hints["top_level_property"])
        self._values: typing.Dict[str, typing.Any] = {
            "base_level_property": base_level_property,
            "first_mid_level_property": first_mid_level_property,
            "second_mid_level_property": second_mid_level_property,
            "top_level_property": top_level_property,
        }

    @builtins.property
    def base_level_property(self) -> builtins.str:
        result = self._values.get("base_level_property")
        assert result is not None, "Required property 'base_level_property' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def first_mid_level_property(self) -> builtins.str:
        result = self._values.get("first_mid_level_property")
        assert result is not None, "Required property 'first_mid_level_property' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def second_mid_level_property(self) -> builtins.str:
        result = self._values.get("second_mid_level_property")
        assert result is not None, "Required property 'second_mid_level_property' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def top_level_property(self) -> builtins.str:
        result = self._values.get("top_level_property")
        assert result is not None, "Required property 'top_level_property' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DiamondInheritanceTopLevelStruct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DisappointingCollectionSource(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.DisappointingCollectionSource",
):
    '''Verifies that null/undefined can be returned for optional collections.

    This source of collections is disappointing - it'll always give you nothing :(
    '''

    @jsii.python.classproperty
    @jsii.member(jsii_name="maybeList")
    def MAYBE_LIST(cls) -> typing.Optional[typing.List[builtins.str]]:
        '''Some List of strings, maybe?

        (Nah, just a billion dollars mistake!)
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.sget(cls, "maybeList"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="maybeMap")
    def MAYBE_MAP(cls) -> typing.Optional[typing.Mapping[builtins.str, jsii.Number]]:
        '''Some Map of strings to numbers, maybe?

        (Nah, just a billion dollars mistake!)
        '''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, jsii.Number]], jsii.sget(cls, "maybeMap"))


class DoNotOverridePrivates(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.DoNotOverridePrivates",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="changePrivatePropertyValue")
    def change_private_property_value(self, new_value: builtins.str) -> None:
        '''
        :param new_value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DoNotOverridePrivates.change_private_property_value)
            check_type(argname="argument new_value", value=new_value, expected_type=type_hints["new_value"])
        return typing.cast(None, jsii.invoke(self, "changePrivatePropertyValue", [new_value]))

    @jsii.member(jsii_name="privateMethodValue")
    def private_method_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "privateMethodValue", []))

    @jsii.member(jsii_name="privatePropertyValue")
    def private_property_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "privatePropertyValue", []))


class DoNotRecognizeAnyAsOptional(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.DoNotRecognizeAnyAsOptional",
):
    '''jsii#284: do not recognize "any" as an optional argument.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="method")
    def method(
        self,
        _required_any: typing.Any,
        _optional_any: typing.Any = None,
        _optional_string: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param _required_any: -
        :param _optional_any: -
        :param _optional_string: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DoNotRecognizeAnyAsOptional.method)
            check_type(argname="argument _required_any", value=_required_any, expected_type=type_hints["_required_any"])
            check_type(argname="argument _optional_any", value=_optional_any, expected_type=type_hints["_optional_any"])
            check_type(argname="argument _optional_string", value=_optional_string, expected_type=type_hints["_optional_string"])
        return typing.cast(None, jsii.invoke(self, "method", [_required_any, _optional_any, _optional_string]))


class DocumentedClass(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.DocumentedClass"):
    '''Here's the first line of the TSDoc comment.

    This is the meat of the TSDoc comment. It may contain
    multiple lines and multiple paragraphs.

    Multiple paragraphs are separated by an empty line.

    Example::

        x = 12 + 44
        s1 = "string"
        s2 = "string \nwith new newlines" # see https://github.com/aws/jsii/issues/2569
        s3 = """string
                    with
                    new lines"""
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="greet")
    def greet(self, *, name: typing.Optional[builtins.str] = None) -> jsii.Number:
        '''Greet the indicated person.

        This will print out a friendly greeting intended for the indicated person.

        :param name: The name of the greetee. Default: world

        :return:

        A number that everyone knows very well and represents the answer
        to the ultimate question
        '''
        greetee = Greetee(name=name)

        return typing.cast(jsii.Number, jsii.invoke(self, "greet", [greetee]))

    @jsii.member(jsii_name="hola")
    def hola(self) -> None:
        '''(experimental) Say ¡Hola!

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "hola", []))


class DontComplainAboutVariadicAfterOptional(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.DontComplainAboutVariadicAfterOptional",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="optionalAndVariadic")
    def optional_and_variadic(
        self,
        optional: typing.Optional[builtins.str] = None,
        *things: builtins.str,
    ) -> builtins.str:
        '''
        :param optional: -
        :param things: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DontComplainAboutVariadicAfterOptional.optional_and_variadic)
            check_type(argname="argument optional", value=optional, expected_type=type_hints["optional"])
            check_type(argname="argument things", value=things, expected_type=typing.Tuple[type_hints["things"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(builtins.str, jsii.invoke(self, "optionalAndVariadic", [optional, *things]))


@jsii.data_type(
    jsii_type="jsii-calc.DummyObj",
    jsii_struct_bases=[],
    name_mapping={"example": "example"},
)
class DummyObj:
    def __init__(self, *, example: builtins.str) -> None:
        '''
        :param example: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DummyObj.__init__)
            check_type(argname="argument example", value=example, expected_type=type_hints["example"])
        self._values: typing.Dict[str, typing.Any] = {
            "example": example,
        }

    @builtins.property
    def example(self) -> builtins.str:
        result = self._values.get("example")
        assert result is not None, "Required property 'example' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DummyObj(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DynamicPropertyBearer(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.DynamicPropertyBearer",
):
    '''Ensures we can override a dynamic property that was inherited.'''

    def __init__(self, value_store: builtins.str) -> None:
        '''
        :param value_store: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DynamicPropertyBearer.__init__)
            check_type(argname="argument value_store", value=value_store, expected_type=type_hints["value_store"])
        jsii.create(self.__class__, self, [value_store])

    @builtins.property
    @jsii.member(jsii_name="dynamicProperty")
    def dynamic_property(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dynamicProperty"))

    @dynamic_property.setter
    def dynamic_property(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DynamicPropertyBearer, "dynamic_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dynamicProperty", value)

    @builtins.property
    @jsii.member(jsii_name="valueStore")
    def value_store(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "valueStore"))

    @value_store.setter
    def value_store(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DynamicPropertyBearer, "value_store").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "valueStore", value)


class DynamicPropertyBearerChild(
    DynamicPropertyBearer,
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.DynamicPropertyBearerChild",
):
    def __init__(self, original_value: builtins.str) -> None:
        '''
        :param original_value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DynamicPropertyBearerChild.__init__)
            check_type(argname="argument original_value", value=original_value, expected_type=type_hints["original_value"])
        jsii.create(self.__class__, self, [original_value])

    @jsii.member(jsii_name="overrideValue")
    def override_value(self, new_value: builtins.str) -> builtins.str:
        '''Sets ``this.dynamicProperty`` to the new value, and returns the old value.

        :param new_value: the new value to be set.

        :return: the old value that was set.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DynamicPropertyBearerChild.override_value)
            check_type(argname="argument new_value", value=new_value, expected_type=type_hints["new_value"])
        return typing.cast(builtins.str, jsii.invoke(self, "overrideValue", [new_value]))

    @builtins.property
    @jsii.member(jsii_name="originalValue")
    def original_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "originalValue"))


class Entropy(metaclass=jsii.JSIIAbstractClass, jsii_type="jsii-calc.Entropy"):
    '''This class is used to validate that serialization and deserialization does not interpret ISO-8601-formatted timestampts to the native date/time object, as the jsii protocol has a $jsii$date wrapper for this purpose (node's JSON parsing does *NOT* detect dates automatically in this way, so host libraries should not either).'''

    def __init__(self, clock: "IWallClock") -> None:
        '''Creates a new instance of Entropy.

        :param clock: your implementation of ``WallClock``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Entropy.__init__)
            check_type(argname="argument clock", value=clock, expected_type=type_hints["clock"])
        jsii.create(self.__class__, self, [clock])

    @jsii.member(jsii_name="increase")
    def increase(self) -> builtins.str:
        '''Increases entropy by consuming time from the clock (yes, this is a long shot, please don't judge).

        :return: the time from the ``WallClock``.
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "increase", []))

    @jsii.member(jsii_name="repeat")
    @abc.abstractmethod
    def repeat(self, word: builtins.str) -> builtins.str:
        '''Implement this method such that it returns ``word``.

        :param word: the value to return.

        :return: ``word``.
        '''
        ...


class _EntropyProxy(Entropy):
    @jsii.member(jsii_name="repeat")
    def repeat(self, word: builtins.str) -> builtins.str:
        '''Implement this method such that it returns ``word``.

        :param word: the value to return.

        :return: ``word``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Entropy.repeat)
            check_type(argname="argument word", value=word, expected_type=type_hints["word"])
        return typing.cast(builtins.str, jsii.invoke(self, "repeat", [word]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Entropy).__jsii_proxy_class__ = lambda : _EntropyProxy


class EnumDispenser(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.EnumDispenser"):
    @jsii.member(jsii_name="randomIntegerLikeEnum")
    @builtins.classmethod
    def random_integer_like_enum(cls) -> AllTypesEnum:
        return typing.cast(AllTypesEnum, jsii.sinvoke(cls, "randomIntegerLikeEnum", []))

    @jsii.member(jsii_name="randomStringLikeEnum")
    @builtins.classmethod
    def random_string_like_enum(cls) -> "StringEnum":
        return typing.cast("StringEnum", jsii.sinvoke(cls, "randomStringLikeEnum", []))


class EraseUndefinedHashValues(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.EraseUndefinedHashValues",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="doesKeyExist")
    @builtins.classmethod
    def does_key_exist(
        cls,
        opts: typing.Union["EraseUndefinedHashValuesOptions", typing.Dict[str, typing.Any]],
        key: builtins.str,
    ) -> builtins.bool:
        '''Returns ``true`` if ``key`` is defined in ``opts``.

        Used to check that undefined/null hash values
        are being erased when sending values from native code to JS.

        :param opts: -
        :param key: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EraseUndefinedHashValues.does_key_exist)
            check_type(argname="argument opts", value=opts, expected_type=type_hints["opts"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "doesKeyExist", [opts, key]))

    @jsii.member(jsii_name="prop1IsNull")
    @builtins.classmethod
    def prop1_is_null(cls) -> typing.Mapping[builtins.str, typing.Any]:
        '''We expect "prop1" to be erased.'''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.sinvoke(cls, "prop1IsNull", []))

    @jsii.member(jsii_name="prop2IsUndefined")
    @builtins.classmethod
    def prop2_is_undefined(cls) -> typing.Mapping[builtins.str, typing.Any]:
        '''We expect "prop2" to be erased.'''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.sinvoke(cls, "prop2IsUndefined", []))


@jsii.data_type(
    jsii_type="jsii-calc.EraseUndefinedHashValuesOptions",
    jsii_struct_bases=[],
    name_mapping={"option1": "option1", "option2": "option2"},
)
class EraseUndefinedHashValuesOptions:
    def __init__(
        self,
        *,
        option1: typing.Optional[builtins.str] = None,
        option2: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param option1: 
        :param option2: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EraseUndefinedHashValuesOptions.__init__)
            check_type(argname="argument option1", value=option1, expected_type=type_hints["option1"])
            check_type(argname="argument option2", value=option2, expected_type=type_hints["option2"])
        self._values: typing.Dict[str, typing.Any] = {}
        if option1 is not None:
            self._values["option1"] = option1
        if option2 is not None:
            self._values["option2"] = option2

    @builtins.property
    def option1(self) -> typing.Optional[builtins.str]:
        result = self._values.get("option1")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def option2(self) -> typing.Optional[builtins.str]:
        result = self._values.get("option2")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EraseUndefinedHashValuesOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ExperimentalClass(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.ExperimentalClass",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        readonly_string: builtins.str,
        mutable_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param readonly_string: -
        :param mutable_number: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ExperimentalClass.__init__)
            check_type(argname="argument readonly_string", value=readonly_string, expected_type=type_hints["readonly_string"])
            check_type(argname="argument mutable_number", value=mutable_number, expected_type=type_hints["mutable_number"])
        jsii.create(self.__class__, self, [readonly_string, mutable_number])

    @jsii.member(jsii_name="method")
    def method(self) -> None:
        '''
        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "method", []))

    @builtins.property
    @jsii.member(jsii_name="readonlyProperty")
    def readonly_property(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "readonlyProperty"))

    @builtins.property
    @jsii.member(jsii_name="mutableProperty")
    def mutable_property(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "mutableProperty"))

    @mutable_property.setter
    def mutable_property(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExperimentalClass, "mutable_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mutableProperty", value)


@jsii.enum(jsii_type="jsii-calc.ExperimentalEnum")
class ExperimentalEnum(enum.Enum):
    '''
    :stability: experimental
    '''

    OPTION_A = "OPTION_A"
    '''
    :stability: experimental
    '''
    OPTION_B = "OPTION_B"
    '''
    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="jsii-calc.ExperimentalStruct",
    jsii_struct_bases=[],
    name_mapping={"readonly_property": "readonlyProperty"},
)
class ExperimentalStruct:
    def __init__(self, *, readonly_property: builtins.str) -> None:
        '''
        :param readonly_property: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ExperimentalStruct.__init__)
            check_type(argname="argument readonly_property", value=readonly_property, expected_type=type_hints["readonly_property"])
        self._values: typing.Dict[str, typing.Any] = {
            "readonly_property": readonly_property,
        }

    @builtins.property
    def readonly_property(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("readonly_property")
        assert result is not None, "Required property 'readonly_property' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExperimentalStruct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ExportedBaseClass(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.ExportedBaseClass",
):
    def __init__(self, success: builtins.bool) -> None:
        '''
        :param success: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ExportedBaseClass.__init__)
            check_type(argname="argument success", value=success, expected_type=type_hints["success"])
        jsii.create(self.__class__, self, [success])

    @builtins.property
    @jsii.member(jsii_name="success")
    def success(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "success"))


@jsii.data_type(
    jsii_type="jsii-calc.ExtendsInternalInterface",
    jsii_struct_bases=[],
    name_mapping={"boom": "boom", "prop": "prop"},
)
class ExtendsInternalInterface:
    def __init__(self, *, boom: builtins.bool, prop: builtins.str) -> None:
        '''
        :param boom: 
        :param prop: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ExtendsInternalInterface.__init__)
            check_type(argname="argument boom", value=boom, expected_type=type_hints["boom"])
            check_type(argname="argument prop", value=prop, expected_type=type_hints["prop"])
        self._values: typing.Dict[str, typing.Any] = {
            "boom": boom,
            "prop": prop,
        }

    @builtins.property
    def boom(self) -> builtins.bool:
        result = self._values.get("boom")
        assert result is not None, "Required property 'boom' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def prop(self) -> builtins.str:
        result = self._values.get("prop")
        assert result is not None, "Required property 'prop' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExtendsInternalInterface(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ExternalClass(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.ExternalClass"):
    '''
    :external: true
    '''

    def __init__(
        self,
        readonly_string: builtins.str,
        mutable_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param readonly_string: -
        :param mutable_number: -

        :external: true
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ExternalClass.__init__)
            check_type(argname="argument readonly_string", value=readonly_string, expected_type=type_hints["readonly_string"])
            check_type(argname="argument mutable_number", value=mutable_number, expected_type=type_hints["mutable_number"])
        jsii.create(self.__class__, self, [readonly_string, mutable_number])

    @jsii.member(jsii_name="method")
    def method(self) -> None:
        '''
        :external: true
        '''
        return typing.cast(None, jsii.invoke(self, "method", []))

    @builtins.property
    @jsii.member(jsii_name="readonlyProperty")
    def readonly_property(self) -> builtins.str:
        '''
        :external: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "readonlyProperty"))

    @builtins.property
    @jsii.member(jsii_name="mutableProperty")
    def mutable_property(self) -> typing.Optional[jsii.Number]:
        '''
        :external: true
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "mutableProperty"))

    @mutable_property.setter
    def mutable_property(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExternalClass, "mutable_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mutableProperty", value)


@jsii.enum(jsii_type="jsii-calc.ExternalEnum")
class ExternalEnum(enum.Enum):
    '''
    :external: true
    '''

    OPTION_A = "OPTION_A"
    '''
    :external: true
    '''
    OPTION_B = "OPTION_B"
    '''
    :external: true
    '''


@jsii.data_type(
    jsii_type="jsii-calc.ExternalStruct",
    jsii_struct_bases=[],
    name_mapping={"readonly_property": "readonlyProperty"},
)
class ExternalStruct:
    def __init__(self, *, readonly_property: builtins.str) -> None:
        '''
        :param readonly_property: 

        :external: true
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ExternalStruct.__init__)
            check_type(argname="argument readonly_property", value=readonly_property, expected_type=type_hints["readonly_property"])
        self._values: typing.Dict[str, typing.Any] = {
            "readonly_property": readonly_property,
        }

    @builtins.property
    def readonly_property(self) -> builtins.str:
        '''
        :external: true
        '''
        result = self._values.get("readonly_property")
        assert result is not None, "Required property 'readonly_property' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalStruct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GiveMeStructs(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.GiveMeStructs"):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="derivedToFirst")
    def derived_to_first(
        self,
        *,
        another_required: datetime.datetime,
        bool: builtins.bool,
        non_primitive: "DoubleTrouble",
        another_optional: typing.Optional[typing.Mapping[builtins.str, scope.jsii_calc_lib.NumericValue]] = None,
        optional_any: typing.Any = None,
        optional_array: typing.Optional[typing.Sequence[builtins.str]] = None,
        anumber: jsii.Number,
        astring: builtins.str,
        first_optional: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> scope.jsii_calc_lib.MyFirstStruct:
        '''Accepts a struct of type DerivedStruct and returns a struct of type FirstStruct.

        :param another_required: 
        :param bool: 
        :param non_primitive: An example of a non primitive property.
        :param another_optional: This is optional.
        :param optional_any: 
        :param optional_array: 
        :param anumber: (deprecated) An awesome number value.
        :param astring: (deprecated) A string value.
        :param first_optional: 
        '''
        derived = DerivedStruct(
            another_required=another_required,
            bool=bool,
            non_primitive=non_primitive,
            another_optional=another_optional,
            optional_any=optional_any,
            optional_array=optional_array,
            anumber=anumber,
            astring=astring,
            first_optional=first_optional,
        )

        return typing.cast(scope.jsii_calc_lib.MyFirstStruct, jsii.invoke(self, "derivedToFirst", [derived]))

    @jsii.member(jsii_name="readDerivedNonPrimitive")
    def read_derived_non_primitive(
        self,
        *,
        another_required: datetime.datetime,
        bool: builtins.bool,
        non_primitive: "DoubleTrouble",
        another_optional: typing.Optional[typing.Mapping[builtins.str, scope.jsii_calc_lib.NumericValue]] = None,
        optional_any: typing.Any = None,
        optional_array: typing.Optional[typing.Sequence[builtins.str]] = None,
        anumber: jsii.Number,
        astring: builtins.str,
        first_optional: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> "DoubleTrouble":
        '''Returns the boolean from a DerivedStruct struct.

        :param another_required: 
        :param bool: 
        :param non_primitive: An example of a non primitive property.
        :param another_optional: This is optional.
        :param optional_any: 
        :param optional_array: 
        :param anumber: (deprecated) An awesome number value.
        :param astring: (deprecated) A string value.
        :param first_optional: 
        '''
        derived = DerivedStruct(
            another_required=another_required,
            bool=bool,
            non_primitive=non_primitive,
            another_optional=another_optional,
            optional_any=optional_any,
            optional_array=optional_array,
            anumber=anumber,
            astring=astring,
            first_optional=first_optional,
        )

        return typing.cast("DoubleTrouble", jsii.invoke(self, "readDerivedNonPrimitive", [derived]))

    @jsii.member(jsii_name="readFirstNumber")
    def read_first_number(
        self,
        *,
        anumber: jsii.Number,
        astring: builtins.str,
        first_optional: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> jsii.Number:
        '''Returns the "anumber" from a MyFirstStruct struct;

        :param anumber: (deprecated) An awesome number value.
        :param astring: (deprecated) A string value.
        :param first_optional: 
        '''
        first = scope.jsii_calc_lib.MyFirstStruct(
            anumber=anumber, astring=astring, first_optional=first_optional
        )

        return typing.cast(jsii.Number, jsii.invoke(self, "readFirstNumber", [first]))

    @builtins.property
    @jsii.member(jsii_name="structLiteral")
    def struct_literal(self) -> scope.jsii_calc_lib.StructWithOnlyOptionals:
        return typing.cast(scope.jsii_calc_lib.StructWithOnlyOptionals, jsii.get(self, "structLiteral"))


@jsii.data_type(
    jsii_type="jsii-calc.Greetee",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class Greetee:
    def __init__(self, *, name: typing.Optional[builtins.str] = None) -> None:
        '''These are some arguments you can pass to a method.

        :param name: The name of the greetee. Default: world
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Greetee.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the greetee.

        :default: world
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Greetee(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GreetingAugmenter(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.GreetingAugmenter",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="betterGreeting")
    def better_greeting(self, friendly: scope.jsii_calc_lib.IFriendly) -> builtins.str:
        '''
        :param friendly: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GreetingAugmenter.better_greeting)
            check_type(argname="argument friendly", value=friendly, expected_type=type_hints["friendly"])
        return typing.cast(builtins.str, jsii.invoke(self, "betterGreeting", [friendly]))


@jsii.interface(jsii_type="jsii-calc.IAnonymousImplementationProvider")
class IAnonymousImplementationProvider(typing_extensions.Protocol):
    '''We can return an anonymous interface implementation from an override without losing the interface declarations.'''

    @jsii.member(jsii_name="provideAsClass")
    def provide_as_class(self) -> "Implementation":
        ...

    @jsii.member(jsii_name="provideAsInterface")
    def provide_as_interface(self) -> "IAnonymouslyImplementMe":
        ...


class _IAnonymousImplementationProviderProxy:
    '''We can return an anonymous interface implementation from an override without losing the interface declarations.'''

    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IAnonymousImplementationProvider"

    @jsii.member(jsii_name="provideAsClass")
    def provide_as_class(self) -> "Implementation":
        return typing.cast("Implementation", jsii.invoke(self, "provideAsClass", []))

    @jsii.member(jsii_name="provideAsInterface")
    def provide_as_interface(self) -> "IAnonymouslyImplementMe":
        return typing.cast("IAnonymouslyImplementMe", jsii.invoke(self, "provideAsInterface", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAnonymousImplementationProvider).__jsii_proxy_class__ = lambda : _IAnonymousImplementationProviderProxy


@jsii.interface(jsii_type="jsii-calc.IAnonymouslyImplementMe")
class IAnonymouslyImplementMe(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        ...

    @jsii.member(jsii_name="verb")
    def verb(self) -> builtins.str:
        ...


class _IAnonymouslyImplementMeProxy:
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IAnonymouslyImplementMe"

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @jsii.member(jsii_name="verb")
    def verb(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "verb", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAnonymouslyImplementMe).__jsii_proxy_class__ = lambda : _IAnonymouslyImplementMeProxy


@jsii.interface(jsii_type="jsii-calc.IAnotherPublicInterface")
class IAnotherPublicInterface(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="a")
    def a(self) -> builtins.str:
        ...

    @a.setter
    def a(self, value: builtins.str) -> None:
        ...


class _IAnotherPublicInterfaceProxy:
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IAnotherPublicInterface"

    @builtins.property
    @jsii.member(jsii_name="a")
    def a(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "a"))

    @a.setter
    def a(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IAnotherPublicInterface, "a").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "a", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAnotherPublicInterface).__jsii_proxy_class__ = lambda : _IAnotherPublicInterfaceProxy


@jsii.interface(jsii_type="jsii-calc.IBell")
class IBell(typing_extensions.Protocol):
    @jsii.member(jsii_name="ring")
    def ring(self) -> None:
        ...


class _IBellProxy:
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IBell"

    @jsii.member(jsii_name="ring")
    def ring(self) -> None:
        return typing.cast(None, jsii.invoke(self, "ring", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBell).__jsii_proxy_class__ = lambda : _IBellProxy


@jsii.interface(jsii_type="jsii-calc.IBellRinger")
class IBellRinger(typing_extensions.Protocol):
    '''Takes the object parameter as an interface.'''

    @jsii.member(jsii_name="yourTurn")
    def your_turn(self, bell: IBell) -> None:
        '''
        :param bell: -
        '''
        ...


class _IBellRingerProxy:
    '''Takes the object parameter as an interface.'''

    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IBellRinger"

    @jsii.member(jsii_name="yourTurn")
    def your_turn(self, bell: IBell) -> None:
        '''
        :param bell: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IBellRinger.your_turn)
            check_type(argname="argument bell", value=bell, expected_type=type_hints["bell"])
        return typing.cast(None, jsii.invoke(self, "yourTurn", [bell]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBellRinger).__jsii_proxy_class__ = lambda : _IBellRingerProxy


@jsii.interface(jsii_type="jsii-calc.IConcreteBellRinger")
class IConcreteBellRinger(typing_extensions.Protocol):
    '''Takes the object parameter as a calss.'''

    @jsii.member(jsii_name="yourTurn")
    def your_turn(self, bell: "Bell") -> None:
        '''
        :param bell: -
        '''
        ...


class _IConcreteBellRingerProxy:
    '''Takes the object parameter as a calss.'''

    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IConcreteBellRinger"

    @jsii.member(jsii_name="yourTurn")
    def your_turn(self, bell: "Bell") -> None:
        '''
        :param bell: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IConcreteBellRinger.your_turn)
            check_type(argname="argument bell", value=bell, expected_type=type_hints["bell"])
        return typing.cast(None, jsii.invoke(self, "yourTurn", [bell]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConcreteBellRinger).__jsii_proxy_class__ = lambda : _IConcreteBellRingerProxy


@jsii.interface(jsii_type="jsii-calc.IDeprecatedInterface")
class IDeprecatedInterface(typing_extensions.Protocol):
    '''
    :deprecated: useless interface

    :stability: deprecated
    '''

    @builtins.property
    @jsii.member(jsii_name="mutableProperty")
    def mutable_property(self) -> typing.Optional[jsii.Number]:
        '''
        :deprecated: could be better

        :stability: deprecated
        '''
        ...

    @mutable_property.setter
    def mutable_property(self, value: typing.Optional[jsii.Number]) -> None:
        ...

    @jsii.member(jsii_name="method")
    def method(self) -> None:
        '''
        :deprecated: services no purpose

        :stability: deprecated
        '''
        ...


class _IDeprecatedInterfaceProxy:
    '''
    :deprecated: useless interface

    :stability: deprecated
    '''

    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IDeprecatedInterface"

    @builtins.property
    @jsii.member(jsii_name="mutableProperty")
    def mutable_property(self) -> typing.Optional[jsii.Number]:
        '''
        :deprecated: could be better

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "mutableProperty"))

    @mutable_property.setter
    def mutable_property(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IDeprecatedInterface, "mutable_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mutableProperty", value)

    @jsii.member(jsii_name="method")
    def method(self) -> None:
        '''
        :deprecated: services no purpose

        :stability: deprecated
        '''
        return typing.cast(None, jsii.invoke(self, "method", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDeprecatedInterface).__jsii_proxy_class__ = lambda : _IDeprecatedInterfaceProxy


@jsii.interface(jsii_type="jsii-calc.IExperimentalInterface")
class IExperimentalInterface(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="mutableProperty")
    def mutable_property(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        ...

    @mutable_property.setter
    def mutable_property(self, value: typing.Optional[jsii.Number]) -> None:
        ...

    @jsii.member(jsii_name="method")
    def method(self) -> None:
        '''
        :stability: experimental
        '''
        ...


class _IExperimentalInterfaceProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IExperimentalInterface"

    @builtins.property
    @jsii.member(jsii_name="mutableProperty")
    def mutable_property(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "mutableProperty"))

    @mutable_property.setter
    def mutable_property(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IExperimentalInterface, "mutable_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mutableProperty", value)

    @jsii.member(jsii_name="method")
    def method(self) -> None:
        '''
        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "method", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IExperimentalInterface).__jsii_proxy_class__ = lambda : _IExperimentalInterfaceProxy


@jsii.interface(jsii_type="jsii-calc.IExtendsPrivateInterface")
class IExtendsPrivateInterface(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="moreThings")
    def more_things(self) -> typing.List[builtins.str]:
        ...

    @builtins.property
    @jsii.member(jsii_name="private")
    def private(self) -> builtins.str:
        ...

    @private.setter
    def private(self, value: builtins.str) -> None:
        ...


class _IExtendsPrivateInterfaceProxy:
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IExtendsPrivateInterface"

    @builtins.property
    @jsii.member(jsii_name="moreThings")
    def more_things(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "moreThings"))

    @builtins.property
    @jsii.member(jsii_name="private")
    def private(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "private"))

    @private.setter
    def private(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IExtendsPrivateInterface, "private").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "private", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IExtendsPrivateInterface).__jsii_proxy_class__ = lambda : _IExtendsPrivateInterfaceProxy


@jsii.interface(jsii_type="jsii-calc.IExternalInterface")
class IExternalInterface(typing_extensions.Protocol):
    '''
    :external: true
    '''

    @builtins.property
    @jsii.member(jsii_name="mutableProperty")
    def mutable_property(self) -> typing.Optional[jsii.Number]:
        '''
        :external: true
        '''
        ...

    @mutable_property.setter
    def mutable_property(self, value: typing.Optional[jsii.Number]) -> None:
        ...

    @jsii.member(jsii_name="method")
    def method(self) -> None:
        '''
        :external: true
        '''
        ...


class _IExternalInterfaceProxy:
    '''
    :external: true
    '''

    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IExternalInterface"

    @builtins.property
    @jsii.member(jsii_name="mutableProperty")
    def mutable_property(self) -> typing.Optional[jsii.Number]:
        '''
        :external: true
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "mutableProperty"))

    @mutable_property.setter
    def mutable_property(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IExternalInterface, "mutable_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mutableProperty", value)

    @jsii.member(jsii_name="method")
    def method(self) -> None:
        '''
        :external: true
        '''
        return typing.cast(None, jsii.invoke(self, "method", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IExternalInterface).__jsii_proxy_class__ = lambda : _IExternalInterfaceProxy


@jsii.interface(jsii_type="jsii-calc.IFriendlier")
class IFriendlier(scope.jsii_calc_lib.IFriendly, typing_extensions.Protocol):
    '''Even friendlier classes can implement this interface.'''

    @jsii.member(jsii_name="farewell")
    def farewell(self) -> builtins.str:
        '''Say farewell.'''
        ...

    @jsii.member(jsii_name="goodbye")
    def goodbye(self) -> builtins.str:
        '''Say goodbye.

        :return: A goodbye blessing.
        '''
        ...


class _IFriendlierProxy(
    jsii.proxy_for(scope.jsii_calc_lib.IFriendly), # type: ignore[misc]
):
    '''Even friendlier classes can implement this interface.'''

    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IFriendlier"

    @jsii.member(jsii_name="farewell")
    def farewell(self) -> builtins.str:
        '''Say farewell.'''
        return typing.cast(builtins.str, jsii.invoke(self, "farewell", []))

    @jsii.member(jsii_name="goodbye")
    def goodbye(self) -> builtins.str:
        '''Say goodbye.

        :return: A goodbye blessing.
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "goodbye", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFriendlier).__jsii_proxy_class__ = lambda : _IFriendlierProxy


@jsii.interface(jsii_type="jsii-calc.IIndirectlyImplemented")
class IIndirectlyImplemented(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="property")
    def property(self) -> builtins.str:
        ...

    @jsii.member(jsii_name="method")
    def method(self) -> jsii.Number:
        ...


class _IIndirectlyImplementedProxy:
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IIndirectlyImplemented"

    @builtins.property
    @jsii.member(jsii_name="property")
    def property(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "property"))

    @jsii.member(jsii_name="method")
    def method(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.invoke(self, "method", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIndirectlyImplemented).__jsii_proxy_class__ = lambda : _IIndirectlyImplementedProxy


@jsii.interface(jsii_type="jsii-calc.IInterfaceImplementedByAbstractClass")
class IInterfaceImplementedByAbstractClass(typing_extensions.Protocol):
    '''awslabs/jsii#220 Abstract return type.'''

    @builtins.property
    @jsii.member(jsii_name="propFromInterface")
    def prop_from_interface(self) -> builtins.str:
        ...


class _IInterfaceImplementedByAbstractClassProxy:
    '''awslabs/jsii#220 Abstract return type.'''

    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IInterfaceImplementedByAbstractClass"

    @builtins.property
    @jsii.member(jsii_name="propFromInterface")
    def prop_from_interface(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "propFromInterface"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInterfaceImplementedByAbstractClass).__jsii_proxy_class__ = lambda : _IInterfaceImplementedByAbstractClassProxy


@jsii.interface(jsii_type="jsii-calc.IInterfaceWithInternal")
class IInterfaceWithInternal(typing_extensions.Protocol):
    @jsii.member(jsii_name="visible")
    def visible(self) -> None:
        ...


class _IInterfaceWithInternalProxy:
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IInterfaceWithInternal"

    @jsii.member(jsii_name="visible")
    def visible(self) -> None:
        return typing.cast(None, jsii.invoke(self, "visible", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInterfaceWithInternal).__jsii_proxy_class__ = lambda : _IInterfaceWithInternalProxy


@jsii.interface(jsii_type="jsii-calc.IInterfaceWithMethods")
class IInterfaceWithMethods(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        ...

    @jsii.member(jsii_name="doThings")
    def do_things(self) -> None:
        ...


class _IInterfaceWithMethodsProxy:
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IInterfaceWithMethods"

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @jsii.member(jsii_name="doThings")
    def do_things(self) -> None:
        return typing.cast(None, jsii.invoke(self, "doThings", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInterfaceWithMethods).__jsii_proxy_class__ = lambda : _IInterfaceWithMethodsProxy


@jsii.interface(jsii_type="jsii-calc.IInterfaceWithOptionalMethodArguments")
class IInterfaceWithOptionalMethodArguments(typing_extensions.Protocol):
    '''awslabs/jsii#175 Interface proxies (and builders) do not respect optional arguments in methods.'''

    @jsii.member(jsii_name="hello")
    def hello(
        self,
        arg1: builtins.str,
        arg2: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param arg1: -
        :param arg2: -
        '''
        ...


class _IInterfaceWithOptionalMethodArgumentsProxy:
    '''awslabs/jsii#175 Interface proxies (and builders) do not respect optional arguments in methods.'''

    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IInterfaceWithOptionalMethodArguments"

    @jsii.member(jsii_name="hello")
    def hello(
        self,
        arg1: builtins.str,
        arg2: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param arg1: -
        :param arg2: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IInterfaceWithOptionalMethodArguments.hello)
            check_type(argname="argument arg1", value=arg1, expected_type=type_hints["arg1"])
            check_type(argname="argument arg2", value=arg2, expected_type=type_hints["arg2"])
        return typing.cast(None, jsii.invoke(self, "hello", [arg1, arg2]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInterfaceWithOptionalMethodArguments).__jsii_proxy_class__ = lambda : _IInterfaceWithOptionalMethodArgumentsProxy


@jsii.interface(jsii_type="jsii-calc.IInterfaceWithProperties")
class IInterfaceWithProperties(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="readOnlyString")
    def read_only_string(self) -> builtins.str:
        ...

    @builtins.property
    @jsii.member(jsii_name="readWriteString")
    def read_write_string(self) -> builtins.str:
        ...

    @read_write_string.setter
    def read_write_string(self, value: builtins.str) -> None:
        ...


class _IInterfaceWithPropertiesProxy:
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IInterfaceWithProperties"

    @builtins.property
    @jsii.member(jsii_name="readOnlyString")
    def read_only_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "readOnlyString"))

    @builtins.property
    @jsii.member(jsii_name="readWriteString")
    def read_write_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "readWriteString"))

    @read_write_string.setter
    def read_write_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IInterfaceWithProperties, "read_write_string").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readWriteString", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInterfaceWithProperties).__jsii_proxy_class__ = lambda : _IInterfaceWithPropertiesProxy


@jsii.interface(jsii_type="jsii-calc.IInterfaceWithPropertiesExtension")
class IInterfaceWithPropertiesExtension(
    IInterfaceWithProperties,
    typing_extensions.Protocol,
):
    @builtins.property
    @jsii.member(jsii_name="foo")
    def foo(self) -> jsii.Number:
        ...

    @foo.setter
    def foo(self, value: jsii.Number) -> None:
        ...


class _IInterfaceWithPropertiesExtensionProxy(
    jsii.proxy_for(IInterfaceWithProperties), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IInterfaceWithPropertiesExtension"

    @builtins.property
    @jsii.member(jsii_name="foo")
    def foo(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "foo"))

    @foo.setter
    def foo(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IInterfaceWithPropertiesExtension, "foo").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "foo", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInterfaceWithPropertiesExtension).__jsii_proxy_class__ = lambda : _IInterfaceWithPropertiesExtensionProxy


@jsii.interface(jsii_type="jsii-calc.IJSII417PublicBaseOfBase")
class IJSII417PublicBaseOfBase(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="hasRoot")
    def has_root(self) -> builtins.bool:
        ...

    @jsii.member(jsii_name="foo")
    def foo(self) -> None:
        ...


class _IJSII417PublicBaseOfBaseProxy:
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IJSII417PublicBaseOfBase"

    @builtins.property
    @jsii.member(jsii_name="hasRoot")
    def has_root(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "hasRoot"))

    @jsii.member(jsii_name="foo")
    def foo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "foo", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IJSII417PublicBaseOfBase).__jsii_proxy_class__ = lambda : _IJSII417PublicBaseOfBaseProxy


@jsii.interface(jsii_type="jsii-calc.IJavaReservedWordsInAnInterface")
class IJavaReservedWordsInAnInterface(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="while")
    def while_(self) -> builtins.str:
        ...

    @jsii.member(jsii_name="abstract")
    def abstract(self) -> None:
        ...

    @jsii.member(jsii_name="assert")
    def assert_(self) -> None:
        ...

    @jsii.member(jsii_name="boolean")
    def boolean(self) -> None:
        ...

    @jsii.member(jsii_name="break")
    def break_(self) -> None:
        ...

    @jsii.member(jsii_name="byte")
    def byte(self) -> None:
        ...

    @jsii.member(jsii_name="case")
    def case(self) -> None:
        ...

    @jsii.member(jsii_name="catch")
    def catch(self) -> None:
        ...

    @jsii.member(jsii_name="char")
    def char(self) -> None:
        ...

    @jsii.member(jsii_name="class")
    def class_(self) -> None:
        ...

    @jsii.member(jsii_name="const")
    def const(self) -> None:
        ...

    @jsii.member(jsii_name="continue")
    def continue_(self) -> None:
        ...

    @jsii.member(jsii_name="default")
    def default(self) -> None:
        ...

    @jsii.member(jsii_name="do")
    def do(self) -> None:
        ...

    @jsii.member(jsii_name="double")
    def double(self) -> None:
        ...

    @jsii.member(jsii_name="else")
    def else_(self) -> None:
        ...

    @jsii.member(jsii_name="enum")
    def enum(self) -> None:
        ...

    @jsii.member(jsii_name="extends")
    def extends(self) -> None:
        ...

    @jsii.member(jsii_name="false")
    def false(self) -> None:
        ...

    @jsii.member(jsii_name="final")
    def final(self) -> None:
        ...

    @jsii.member(jsii_name="finally")
    def finally_(self) -> None:
        ...

    @jsii.member(jsii_name="float")
    def float(self) -> None:
        ...

    @jsii.member(jsii_name="for")
    def for_(self) -> None:
        ...

    @jsii.member(jsii_name="goto")
    def goto(self) -> None:
        ...

    @jsii.member(jsii_name="if")
    def if_(self) -> None:
        ...

    @jsii.member(jsii_name="implements")
    def implements(self) -> None:
        ...

    @jsii.member(jsii_name="import")
    def import_(self) -> None:
        ...

    @jsii.member(jsii_name="instanceof")
    def instanceof(self) -> None:
        ...

    @jsii.member(jsii_name="int")
    def int(self) -> None:
        ...

    @jsii.member(jsii_name="interface")
    def interface(self) -> None:
        ...

    @jsii.member(jsii_name="long")
    def long(self) -> None:
        ...

    @jsii.member(jsii_name="native")
    def native(self) -> None:
        ...

    @jsii.member(jsii_name="null")
    def null(self) -> None:
        ...

    @jsii.member(jsii_name="package")
    def package(self) -> None:
        ...

    @jsii.member(jsii_name="private")
    def private(self) -> None:
        ...

    @jsii.member(jsii_name="protected")
    def protected(self) -> None:
        ...

    @jsii.member(jsii_name="public")
    def public(self) -> None:
        ...

    @jsii.member(jsii_name="return")
    def return_(self) -> None:
        ...

    @jsii.member(jsii_name="short")
    def short(self) -> None:
        ...

    @jsii.member(jsii_name="static")
    def static(self) -> None:
        ...

    @jsii.member(jsii_name="strictfp")
    def strictfp(self) -> None:
        ...

    @jsii.member(jsii_name="super")
    def super(self) -> None:
        ...

    @jsii.member(jsii_name="switch")
    def switch(self) -> None:
        ...

    @jsii.member(jsii_name="synchronized")
    def synchronized(self) -> None:
        ...

    @jsii.member(jsii_name="this")
    def this(self) -> None:
        ...

    @jsii.member(jsii_name="throw")
    def throw(self) -> None:
        ...

    @jsii.member(jsii_name="throws")
    def throws(self) -> None:
        ...

    @jsii.member(jsii_name="transient")
    def transient(self) -> None:
        ...

    @jsii.member(jsii_name="true")
    def true(self) -> None:
        ...

    @jsii.member(jsii_name="try")
    def try_(self) -> None:
        ...

    @jsii.member(jsii_name="void")
    def void(self) -> None:
        ...

    @jsii.member(jsii_name="volatile")
    def volatile(self) -> None:
        ...


class _IJavaReservedWordsInAnInterfaceProxy:
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IJavaReservedWordsInAnInterface"

    @builtins.property
    @jsii.member(jsii_name="while")
    def while_(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "while"))

    @jsii.member(jsii_name="abstract")
    def abstract(self) -> None:
        return typing.cast(None, jsii.invoke(self, "abstract", []))

    @jsii.member(jsii_name="assert")
    def assert_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "assert", []))

    @jsii.member(jsii_name="boolean")
    def boolean(self) -> None:
        return typing.cast(None, jsii.invoke(self, "boolean", []))

    @jsii.member(jsii_name="break")
    def break_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "break", []))

    @jsii.member(jsii_name="byte")
    def byte(self) -> None:
        return typing.cast(None, jsii.invoke(self, "byte", []))

    @jsii.member(jsii_name="case")
    def case(self) -> None:
        return typing.cast(None, jsii.invoke(self, "case", []))

    @jsii.member(jsii_name="catch")
    def catch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "catch", []))

    @jsii.member(jsii_name="char")
    def char(self) -> None:
        return typing.cast(None, jsii.invoke(self, "char", []))

    @jsii.member(jsii_name="class")
    def class_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "class", []))

    @jsii.member(jsii_name="const")
    def const(self) -> None:
        return typing.cast(None, jsii.invoke(self, "const", []))

    @jsii.member(jsii_name="continue")
    def continue_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "continue", []))

    @jsii.member(jsii_name="default")
    def default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "default", []))

    @jsii.member(jsii_name="do")
    def do(self) -> None:
        return typing.cast(None, jsii.invoke(self, "do", []))

    @jsii.member(jsii_name="double")
    def double(self) -> None:
        return typing.cast(None, jsii.invoke(self, "double", []))

    @jsii.member(jsii_name="else")
    def else_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "else", []))

    @jsii.member(jsii_name="enum")
    def enum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "enum", []))

    @jsii.member(jsii_name="extends")
    def extends(self) -> None:
        return typing.cast(None, jsii.invoke(self, "extends", []))

    @jsii.member(jsii_name="false")
    def false(self) -> None:
        return typing.cast(None, jsii.invoke(self, "false", []))

    @jsii.member(jsii_name="final")
    def final(self) -> None:
        return typing.cast(None, jsii.invoke(self, "final", []))

    @jsii.member(jsii_name="finally")
    def finally_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "finally", []))

    @jsii.member(jsii_name="float")
    def float(self) -> None:
        return typing.cast(None, jsii.invoke(self, "float", []))

    @jsii.member(jsii_name="for")
    def for_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "for", []))

    @jsii.member(jsii_name="goto")
    def goto(self) -> None:
        return typing.cast(None, jsii.invoke(self, "goto", []))

    @jsii.member(jsii_name="if")
    def if_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "if", []))

    @jsii.member(jsii_name="implements")
    def implements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "implements", []))

    @jsii.member(jsii_name="import")
    def import_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "import", []))

    @jsii.member(jsii_name="instanceof")
    def instanceof(self) -> None:
        return typing.cast(None, jsii.invoke(self, "instanceof", []))

    @jsii.member(jsii_name="int")
    def int(self) -> None:
        return typing.cast(None, jsii.invoke(self, "int", []))

    @jsii.member(jsii_name="interface")
    def interface(self) -> None:
        return typing.cast(None, jsii.invoke(self, "interface", []))

    @jsii.member(jsii_name="long")
    def long(self) -> None:
        return typing.cast(None, jsii.invoke(self, "long", []))

    @jsii.member(jsii_name="native")
    def native(self) -> None:
        return typing.cast(None, jsii.invoke(self, "native", []))

    @jsii.member(jsii_name="null")
    def null(self) -> None:
        return typing.cast(None, jsii.invoke(self, "null", []))

    @jsii.member(jsii_name="package")
    def package(self) -> None:
        return typing.cast(None, jsii.invoke(self, "package", []))

    @jsii.member(jsii_name="private")
    def private(self) -> None:
        return typing.cast(None, jsii.invoke(self, "private", []))

    @jsii.member(jsii_name="protected")
    def protected(self) -> None:
        return typing.cast(None, jsii.invoke(self, "protected", []))

    @jsii.member(jsii_name="public")
    def public(self) -> None:
        return typing.cast(None, jsii.invoke(self, "public", []))

    @jsii.member(jsii_name="return")
    def return_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "return", []))

    @jsii.member(jsii_name="short")
    def short(self) -> None:
        return typing.cast(None, jsii.invoke(self, "short", []))

    @jsii.member(jsii_name="static")
    def static(self) -> None:
        return typing.cast(None, jsii.invoke(self, "static", []))

    @jsii.member(jsii_name="strictfp")
    def strictfp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "strictfp", []))

    @jsii.member(jsii_name="super")
    def super(self) -> None:
        return typing.cast(None, jsii.invoke(self, "super", []))

    @jsii.member(jsii_name="switch")
    def switch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "switch", []))

    @jsii.member(jsii_name="synchronized")
    def synchronized(self) -> None:
        return typing.cast(None, jsii.invoke(self, "synchronized", []))

    @jsii.member(jsii_name="this")
    def this(self) -> None:
        return typing.cast(None, jsii.invoke(self, "this", []))

    @jsii.member(jsii_name="throw")
    def throw(self) -> None:
        return typing.cast(None, jsii.invoke(self, "throw", []))

    @jsii.member(jsii_name="throws")
    def throws(self) -> None:
        return typing.cast(None, jsii.invoke(self, "throws", []))

    @jsii.member(jsii_name="transient")
    def transient(self) -> None:
        return typing.cast(None, jsii.invoke(self, "transient", []))

    @jsii.member(jsii_name="true")
    def true(self) -> None:
        return typing.cast(None, jsii.invoke(self, "true", []))

    @jsii.member(jsii_name="try")
    def try_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "try", []))

    @jsii.member(jsii_name="void")
    def void(self) -> None:
        return typing.cast(None, jsii.invoke(self, "void", []))

    @jsii.member(jsii_name="volatile")
    def volatile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "volatile", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IJavaReservedWordsInAnInterface).__jsii_proxy_class__ = lambda : _IJavaReservedWordsInAnInterfaceProxy


@jsii.interface(jsii_type="jsii-calc.IJsii487External")
class IJsii487External(typing_extensions.Protocol):
    pass


class _IJsii487ExternalProxy:
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IJsii487External"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IJsii487External).__jsii_proxy_class__ = lambda : _IJsii487ExternalProxy


@jsii.interface(jsii_type="jsii-calc.IJsii487External2")
class IJsii487External2(typing_extensions.Protocol):
    pass


class _IJsii487External2Proxy:
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IJsii487External2"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IJsii487External2).__jsii_proxy_class__ = lambda : _IJsii487External2Proxy


@jsii.interface(jsii_type="jsii-calc.IJsii496")
class IJsii496(typing_extensions.Protocol):
    pass


class _IJsii496Proxy:
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IJsii496"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IJsii496).__jsii_proxy_class__ = lambda : _IJsii496Proxy


@jsii.interface(jsii_type="jsii-calc.IMutableObjectLiteral")
class IMutableObjectLiteral(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        ...

    @value.setter
    def value(self, value: builtins.str) -> None:
        ...


class _IMutableObjectLiteralProxy:
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IMutableObjectLiteral"

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IMutableObjectLiteral, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMutableObjectLiteral).__jsii_proxy_class__ = lambda : _IMutableObjectLiteralProxy


@jsii.interface(jsii_type="jsii-calc.INonInternalInterface")
class INonInternalInterface(IAnotherPublicInterface, typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="b")
    def b(self) -> builtins.str:
        ...

    @b.setter
    def b(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="c")
    def c(self) -> builtins.str:
        ...

    @c.setter
    def c(self, value: builtins.str) -> None:
        ...


class _INonInternalInterfaceProxy(
    jsii.proxy_for(IAnotherPublicInterface), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.INonInternalInterface"

    @builtins.property
    @jsii.member(jsii_name="b")
    def b(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "b"))

    @b.setter
    def b(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(INonInternalInterface, "b").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "b", value)

    @builtins.property
    @jsii.member(jsii_name="c")
    def c(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "c"))

    @c.setter
    def c(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(INonInternalInterface, "c").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "c", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INonInternalInterface).__jsii_proxy_class__ = lambda : _INonInternalInterfaceProxy


@jsii.interface(jsii_type="jsii-calc.IObjectWithProperty")
class IObjectWithProperty(typing_extensions.Protocol):
    '''Make sure that setters are properly called on objects with interfaces.'''

    @builtins.property
    @jsii.member(jsii_name="property")
    def property(self) -> builtins.str:
        ...

    @property.setter
    def property(self, value: builtins.str) -> None:
        ...

    @jsii.member(jsii_name="wasSet")
    def was_set(self) -> builtins.bool:
        ...


class _IObjectWithPropertyProxy:
    '''Make sure that setters are properly called on objects with interfaces.'''

    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IObjectWithProperty"

    @builtins.property
    @jsii.member(jsii_name="property")
    def property(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "property"))

    @property.setter
    def property(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IObjectWithProperty, "property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "property", value)

    @jsii.member(jsii_name="wasSet")
    def was_set(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.invoke(self, "wasSet", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IObjectWithProperty).__jsii_proxy_class__ = lambda : _IObjectWithPropertyProxy


@jsii.interface(jsii_type="jsii-calc.IOptionalMethod")
class IOptionalMethod(typing_extensions.Protocol):
    '''Checks that optional result from interface method code generates correctly.'''

    @jsii.member(jsii_name="optional")
    def optional(self) -> typing.Optional[builtins.str]:
        ...


class _IOptionalMethodProxy:
    '''Checks that optional result from interface method code generates correctly.'''

    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IOptionalMethod"

    @jsii.member(jsii_name="optional")
    def optional(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "optional", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOptionalMethod).__jsii_proxy_class__ = lambda : _IOptionalMethodProxy


@jsii.interface(jsii_type="jsii-calc.IPrivatelyImplemented")
class IPrivatelyImplemented(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="success")
    def success(self) -> builtins.bool:
        ...


class _IPrivatelyImplementedProxy:
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IPrivatelyImplemented"

    @builtins.property
    @jsii.member(jsii_name="success")
    def success(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "success"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPrivatelyImplemented).__jsii_proxy_class__ = lambda : _IPrivatelyImplementedProxy


@jsii.interface(jsii_type="jsii-calc.IPublicInterface")
class IPublicInterface(typing_extensions.Protocol):
    @jsii.member(jsii_name="bye")
    def bye(self) -> builtins.str:
        ...


class _IPublicInterfaceProxy:
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IPublicInterface"

    @jsii.member(jsii_name="bye")
    def bye(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "bye", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPublicInterface).__jsii_proxy_class__ = lambda : _IPublicInterfaceProxy


@jsii.interface(jsii_type="jsii-calc.IPublicInterface2")
class IPublicInterface2(typing_extensions.Protocol):
    @jsii.member(jsii_name="ciao")
    def ciao(self) -> builtins.str:
        ...


class _IPublicInterface2Proxy:
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IPublicInterface2"

    @jsii.member(jsii_name="ciao")
    def ciao(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "ciao", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPublicInterface2).__jsii_proxy_class__ = lambda : _IPublicInterface2Proxy


@jsii.interface(jsii_type="jsii-calc.IRandomNumberGenerator")
class IRandomNumberGenerator(typing_extensions.Protocol):
    '''Generates random numbers.'''

    @jsii.member(jsii_name="next")
    def next(self) -> jsii.Number:
        '''Returns another random number.

        :return: A random number.
        '''
        ...


class _IRandomNumberGeneratorProxy:
    '''Generates random numbers.'''

    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IRandomNumberGenerator"

    @jsii.member(jsii_name="next")
    def next(self) -> jsii.Number:
        '''Returns another random number.

        :return: A random number.
        '''
        return typing.cast(jsii.Number, jsii.invoke(self, "next", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRandomNumberGenerator).__jsii_proxy_class__ = lambda : _IRandomNumberGeneratorProxy


@jsii.interface(jsii_type="jsii-calc.IReturnJsii976")
class IReturnJsii976(typing_extensions.Protocol):
    '''Returns a subclass of a known class which implements an interface.'''

    @builtins.property
    @jsii.member(jsii_name="foo")
    def foo(self) -> jsii.Number:
        ...


class _IReturnJsii976Proxy:
    '''Returns a subclass of a known class which implements an interface.'''

    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IReturnJsii976"

    @builtins.property
    @jsii.member(jsii_name="foo")
    def foo(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "foo"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReturnJsii976).__jsii_proxy_class__ = lambda : _IReturnJsii976Proxy


@jsii.interface(jsii_type="jsii-calc.IReturnsNumber")
class IReturnsNumber(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="numberProp")
    def number_prop(self) -> scope.jsii_calc_lib.Number:
        ...

    @jsii.member(jsii_name="obtainNumber")
    def obtain_number(self) -> scope.jsii_calc_lib.IDoublable:
        ...


class _IReturnsNumberProxy:
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IReturnsNumber"

    @builtins.property
    @jsii.member(jsii_name="numberProp")
    def number_prop(self) -> scope.jsii_calc_lib.Number:
        return typing.cast(scope.jsii_calc_lib.Number, jsii.get(self, "numberProp"))

    @jsii.member(jsii_name="obtainNumber")
    def obtain_number(self) -> scope.jsii_calc_lib.IDoublable:
        return typing.cast(scope.jsii_calc_lib.IDoublable, jsii.invoke(self, "obtainNumber", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReturnsNumber).__jsii_proxy_class__ = lambda : _IReturnsNumberProxy


@jsii.interface(jsii_type="jsii-calc.IStableInterface")
class IStableInterface(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="mutableProperty")
    def mutable_property(self) -> typing.Optional[jsii.Number]:
        ...

    @mutable_property.setter
    def mutable_property(self, value: typing.Optional[jsii.Number]) -> None:
        ...

    @jsii.member(jsii_name="method")
    def method(self) -> None:
        ...


class _IStableInterfaceProxy:
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IStableInterface"

    @builtins.property
    @jsii.member(jsii_name="mutableProperty")
    def mutable_property(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "mutableProperty"))

    @mutable_property.setter
    def mutable_property(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IStableInterface, "mutable_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mutableProperty", value)

    @jsii.member(jsii_name="method")
    def method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "method", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStableInterface).__jsii_proxy_class__ = lambda : _IStableInterfaceProxy


@jsii.interface(jsii_type="jsii-calc.IStructReturningDelegate")
class IStructReturningDelegate(typing_extensions.Protocol):
    '''Verifies that a "pure" implementation of an interface works correctly.'''

    @jsii.member(jsii_name="returnStruct")
    def return_struct(self) -> "StructB":
        ...


class _IStructReturningDelegateProxy:
    '''Verifies that a "pure" implementation of an interface works correctly.'''

    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IStructReturningDelegate"

    @jsii.member(jsii_name="returnStruct")
    def return_struct(self) -> "StructB":
        return typing.cast("StructB", jsii.invoke(self, "returnStruct", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStructReturningDelegate).__jsii_proxy_class__ = lambda : _IStructReturningDelegateProxy


@jsii.interface(jsii_type="jsii-calc.IWallClock")
class IWallClock(typing_extensions.Protocol):
    '''Implement this interface.'''

    @jsii.member(jsii_name="iso8601Now")
    def iso8601_now(self) -> builtins.str:
        '''Returns the current time, formatted as an ISO-8601 string.'''
        ...


class _IWallClockProxy:
    '''Implement this interface.'''

    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IWallClock"

    @jsii.member(jsii_name="iso8601Now")
    def iso8601_now(self) -> builtins.str:
        '''Returns the current time, formatted as an ISO-8601 string.'''
        return typing.cast(builtins.str, jsii.invoke(self, "iso8601Now", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWallClock).__jsii_proxy_class__ = lambda : _IWallClockProxy


class ImplementInternalInterface(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.ImplementInternalInterface",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @builtins.property
    @jsii.member(jsii_name="prop")
    def prop(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prop"))

    @prop.setter
    def prop(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ImplementInternalInterface, "prop").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prop", value)


class Implementation(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.Implementation"):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))


@jsii.implements(IInterfaceWithInternal)
class ImplementsInterfaceWithInternal(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.ImplementsInterfaceWithInternal",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="visible")
    def visible(self) -> None:
        return typing.cast(None, jsii.invoke(self, "visible", []))


class ImplementsInterfaceWithInternalSubclass(
    ImplementsInterfaceWithInternal,
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.ImplementsInterfaceWithInternalSubclass",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])


class ImplementsPrivateInterface(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.ImplementsPrivateInterface",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @builtins.property
    @jsii.member(jsii_name="private")
    def private(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "private"))

    @private.setter
    def private(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ImplementsPrivateInterface, "private").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "private", value)


@jsii.data_type(
    jsii_type="jsii-calc.ImplictBaseOfBase",
    jsii_struct_bases=[scope.jsii_calc_base.BaseProps],
    name_mapping={"foo": "foo", "bar": "bar", "goo": "goo"},
)
class ImplictBaseOfBase(scope.jsii_calc_base.BaseProps):
    def __init__(
        self,
        *,
        foo: scope.jsii_calc_base_of_base.Very,
        bar: builtins.str,
        goo: datetime.datetime,
    ) -> None:
        '''
        :param foo: -
        :param bar: -
        :param goo: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ImplictBaseOfBase.__init__)
            check_type(argname="argument foo", value=foo, expected_type=type_hints["foo"])
            check_type(argname="argument bar", value=bar, expected_type=type_hints["bar"])
            check_type(argname="argument goo", value=goo, expected_type=type_hints["goo"])
        self._values: typing.Dict[str, typing.Any] = {
            "foo": foo,
            "bar": bar,
            "goo": goo,
        }

    @builtins.property
    def foo(self) -> scope.jsii_calc_base_of_base.Very:
        result = self._values.get("foo")
        assert result is not None, "Required property 'foo' is missing"
        return typing.cast(scope.jsii_calc_base_of_base.Very, result)

    @builtins.property
    def bar(self) -> builtins.str:
        result = self._values.get("bar")
        assert result is not None, "Required property 'bar' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def goo(self) -> datetime.datetime:
        result = self._values.get("goo")
        assert result is not None, "Required property 'goo' is missing"
        return typing.cast(datetime.datetime, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImplictBaseOfBase(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InterfaceCollections(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.InterfaceCollections",
):
    '''Verifies that collections of interfaces or structs are correctly handled.

    See: https://github.com/aws/jsii/issues/1196
    '''

    @jsii.member(jsii_name="listOfInterfaces")
    @builtins.classmethod
    def list_of_interfaces(cls) -> typing.List[IBell]:
        return typing.cast(typing.List[IBell], jsii.sinvoke(cls, "listOfInterfaces", []))

    @jsii.member(jsii_name="listOfStructs")
    @builtins.classmethod
    def list_of_structs(cls) -> typing.List["StructA"]:
        return typing.cast(typing.List["StructA"], jsii.sinvoke(cls, "listOfStructs", []))

    @jsii.member(jsii_name="mapOfInterfaces")
    @builtins.classmethod
    def map_of_interfaces(cls) -> typing.Mapping[builtins.str, IBell]:
        return typing.cast(typing.Mapping[builtins.str, IBell], jsii.sinvoke(cls, "mapOfInterfaces", []))

    @jsii.member(jsii_name="mapOfStructs")
    @builtins.classmethod
    def map_of_structs(cls) -> typing.Mapping[builtins.str, "StructA"]:
        return typing.cast(typing.Mapping[builtins.str, "StructA"], jsii.sinvoke(cls, "mapOfStructs", []))


class InterfacesMaker(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.InterfacesMaker"):
    '''We can return arrays of interfaces See aws/aws-cdk#2362.'''

    @jsii.member(jsii_name="makeInterfaces")
    @builtins.classmethod
    def make_interfaces(
        cls,
        count: jsii.Number,
    ) -> typing.List[scope.jsii_calc_lib.IDoublable]:
        '''
        :param count: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(InterfacesMaker.make_interfaces)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
        return typing.cast(typing.List[scope.jsii_calc_lib.IDoublable], jsii.sinvoke(cls, "makeInterfaces", [count]))


class Isomorphism(metaclass=jsii.JSIIAbstractClass, jsii_type="jsii-calc.Isomorphism"):
    '''Checks the "same instance" isomorphism is preserved within the constructor.

    Create a subclass of this, and assert that ``this.myself()`` actually returns
    ``this`` from within the constructor.
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="myself")
    def myself(self) -> "Isomorphism":
        return typing.cast("Isomorphism", jsii.invoke(self, "myself", []))


class _IsomorphismProxy(Isomorphism):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Isomorphism).__jsii_proxy_class__ = lambda : _IsomorphismProxy


class Issue2638(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.Issue2638"):
    '''Docstrings with period.

    :see: https://github.com/aws/jsii/issues/2638
    '''

    def __init__(self) -> None:
        '''First sentence.

        Second sentence. Third sentence.
        '''
        jsii.create(self.__class__, self, [])


class Issue2638B(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.Issue2638B"):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])


class JSII417PublicBaseOfBase(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.JSII417PublicBaseOfBase",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="makeInstance")
    @builtins.classmethod
    def make_instance(cls) -> "JSII417PublicBaseOfBase":
        return typing.cast("JSII417PublicBaseOfBase", jsii.sinvoke(cls, "makeInstance", []))

    @jsii.member(jsii_name="foo")
    def foo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "foo", []))

    @builtins.property
    @jsii.member(jsii_name="hasRoot")
    def has_root(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "hasRoot"))


class JSObjectLiteralForInterface(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.JSObjectLiteralForInterface",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="giveMeFriendly")
    def give_me_friendly(self) -> scope.jsii_calc_lib.IFriendly:
        return typing.cast(scope.jsii_calc_lib.IFriendly, jsii.invoke(self, "giveMeFriendly", []))

    @jsii.member(jsii_name="giveMeFriendlyGenerator")
    def give_me_friendly_generator(self) -> "IFriendlyRandomGenerator":
        return typing.cast("IFriendlyRandomGenerator", jsii.invoke(self, "giveMeFriendlyGenerator", []))


class JSObjectLiteralToNative(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.JSObjectLiteralToNative",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="returnLiteral")
    def return_literal(self) -> "JSObjectLiteralToNativeClass":
        return typing.cast("JSObjectLiteralToNativeClass", jsii.invoke(self, "returnLiteral", []))


class JSObjectLiteralToNativeClass(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.JSObjectLiteralToNativeClass",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @builtins.property
    @jsii.member(jsii_name="propA")
    def prop_a(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "propA"))

    @prop_a.setter
    def prop_a(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(JSObjectLiteralToNativeClass, "prop_a").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propA", value)

    @builtins.property
    @jsii.member(jsii_name="propB")
    def prop_b(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "propB"))

    @prop_b.setter
    def prop_b(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(JSObjectLiteralToNativeClass, "prop_b").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propB", value)


class JavaReservedWords(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.JavaReservedWords",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="abstract")
    def abstract(self) -> None:
        return typing.cast(None, jsii.invoke(self, "abstract", []))

    @jsii.member(jsii_name="assert")
    def assert_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "assert", []))

    @jsii.member(jsii_name="boolean")
    def boolean(self) -> None:
        return typing.cast(None, jsii.invoke(self, "boolean", []))

    @jsii.member(jsii_name="break")
    def break_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "break", []))

    @jsii.member(jsii_name="byte")
    def byte(self) -> None:
        return typing.cast(None, jsii.invoke(self, "byte", []))

    @jsii.member(jsii_name="case")
    def case(self) -> None:
        return typing.cast(None, jsii.invoke(self, "case", []))

    @jsii.member(jsii_name="catch")
    def catch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "catch", []))

    @jsii.member(jsii_name="char")
    def char(self) -> None:
        return typing.cast(None, jsii.invoke(self, "char", []))

    @jsii.member(jsii_name="class")
    def class_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "class", []))

    @jsii.member(jsii_name="const")
    def const(self) -> None:
        return typing.cast(None, jsii.invoke(self, "const", []))

    @jsii.member(jsii_name="continue")
    def continue_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "continue", []))

    @jsii.member(jsii_name="default")
    def default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "default", []))

    @jsii.member(jsii_name="do")
    def do(self) -> None:
        return typing.cast(None, jsii.invoke(self, "do", []))

    @jsii.member(jsii_name="double")
    def double(self) -> None:
        return typing.cast(None, jsii.invoke(self, "double", []))

    @jsii.member(jsii_name="else")
    def else_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "else", []))

    @jsii.member(jsii_name="enum")
    def enum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "enum", []))

    @jsii.member(jsii_name="extends")
    def extends(self) -> None:
        return typing.cast(None, jsii.invoke(self, "extends", []))

    @jsii.member(jsii_name="false")
    def false(self) -> None:
        return typing.cast(None, jsii.invoke(self, "false", []))

    @jsii.member(jsii_name="final")
    def final(self) -> None:
        return typing.cast(None, jsii.invoke(self, "final", []))

    @jsii.member(jsii_name="finally")
    def finally_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "finally", []))

    @jsii.member(jsii_name="float")
    def float(self) -> None:
        return typing.cast(None, jsii.invoke(self, "float", []))

    @jsii.member(jsii_name="for")
    def for_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "for", []))

    @jsii.member(jsii_name="goto")
    def goto(self) -> None:
        return typing.cast(None, jsii.invoke(self, "goto", []))

    @jsii.member(jsii_name="if")
    def if_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "if", []))

    @jsii.member(jsii_name="implements")
    def implements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "implements", []))

    @jsii.member(jsii_name="import")
    def import_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "import", []))

    @jsii.member(jsii_name="instanceof")
    def instanceof(self) -> None:
        return typing.cast(None, jsii.invoke(self, "instanceof", []))

    @jsii.member(jsii_name="int")
    def int(self) -> None:
        return typing.cast(None, jsii.invoke(self, "int", []))

    @jsii.member(jsii_name="interface")
    def interface(self) -> None:
        return typing.cast(None, jsii.invoke(self, "interface", []))

    @jsii.member(jsii_name="long")
    def long(self) -> None:
        return typing.cast(None, jsii.invoke(self, "long", []))

    @jsii.member(jsii_name="native")
    def native(self) -> None:
        return typing.cast(None, jsii.invoke(self, "native", []))

    @jsii.member(jsii_name="new")
    def new(self) -> None:
        return typing.cast(None, jsii.invoke(self, "new", []))

    @jsii.member(jsii_name="null")
    def null(self) -> None:
        return typing.cast(None, jsii.invoke(self, "null", []))

    @jsii.member(jsii_name="package")
    def package(self) -> None:
        return typing.cast(None, jsii.invoke(self, "package", []))

    @jsii.member(jsii_name="private")
    def private(self) -> None:
        return typing.cast(None, jsii.invoke(self, "private", []))

    @jsii.member(jsii_name="protected")
    def protected(self) -> None:
        return typing.cast(None, jsii.invoke(self, "protected", []))

    @jsii.member(jsii_name="public")
    def public(self) -> None:
        return typing.cast(None, jsii.invoke(self, "public", []))

    @jsii.member(jsii_name="return")
    def return_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "return", []))

    @jsii.member(jsii_name="short")
    def short(self) -> None:
        return typing.cast(None, jsii.invoke(self, "short", []))

    @jsii.member(jsii_name="static")
    def static(self) -> None:
        return typing.cast(None, jsii.invoke(self, "static", []))

    @jsii.member(jsii_name="strictfp")
    def strictfp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "strictfp", []))

    @jsii.member(jsii_name="super")
    def super(self) -> None:
        return typing.cast(None, jsii.invoke(self, "super", []))

    @jsii.member(jsii_name="switch")
    def switch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "switch", []))

    @jsii.member(jsii_name="synchronized")
    def synchronized(self) -> None:
        return typing.cast(None, jsii.invoke(self, "synchronized", []))

    @jsii.member(jsii_name="this")
    def this(self) -> None:
        return typing.cast(None, jsii.invoke(self, "this", []))

    @jsii.member(jsii_name="throw")
    def throw(self) -> None:
        return typing.cast(None, jsii.invoke(self, "throw", []))

    @jsii.member(jsii_name="throws")
    def throws(self) -> None:
        return typing.cast(None, jsii.invoke(self, "throws", []))

    @jsii.member(jsii_name="transient")
    def transient(self) -> None:
        return typing.cast(None, jsii.invoke(self, "transient", []))

    @jsii.member(jsii_name="true")
    def true(self) -> None:
        return typing.cast(None, jsii.invoke(self, "true", []))

    @jsii.member(jsii_name="try")
    def try_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "try", []))

    @jsii.member(jsii_name="void")
    def void(self) -> None:
        return typing.cast(None, jsii.invoke(self, "void", []))

    @jsii.member(jsii_name="volatile")
    def volatile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "volatile", []))

    @builtins.property
    @jsii.member(jsii_name="while")
    def while_(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "while"))

    @while_.setter
    def while_(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(JavaReservedWords, "while_").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "while", value)


@jsii.implements(IJsii487External2, IJsii487External)
class Jsii487Derived(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.Jsii487Derived"):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])


@jsii.implements(IJsii496)
class Jsii496Derived(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.Jsii496Derived"):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])


class JsiiAgent(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.JsiiAgent"):
    '''Host runtime version should be set via JSII_AGENT.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.python.classproperty
    @jsii.member(jsii_name="value")
    def value(cls) -> typing.Optional[builtins.str]:
        '''Returns the value of the JSII_AGENT environment variable.'''
        return typing.cast(typing.Optional[builtins.str], jsii.sget(cls, "value"))


class JsonFormatter(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.JsonFormatter"):
    '''Make sure structs are un-decorated on the way in.

    :see: https://github.com/aws/aws-cdk/issues/5066
    '''

    @jsii.member(jsii_name="anyArray")
    @builtins.classmethod
    def any_array(cls) -> typing.Any:
        return typing.cast(typing.Any, jsii.sinvoke(cls, "anyArray", []))

    @jsii.member(jsii_name="anyBooleanFalse")
    @builtins.classmethod
    def any_boolean_false(cls) -> typing.Any:
        return typing.cast(typing.Any, jsii.sinvoke(cls, "anyBooleanFalse", []))

    @jsii.member(jsii_name="anyBooleanTrue")
    @builtins.classmethod
    def any_boolean_true(cls) -> typing.Any:
        return typing.cast(typing.Any, jsii.sinvoke(cls, "anyBooleanTrue", []))

    @jsii.member(jsii_name="anyDate")
    @builtins.classmethod
    def any_date(cls) -> typing.Any:
        return typing.cast(typing.Any, jsii.sinvoke(cls, "anyDate", []))

    @jsii.member(jsii_name="anyEmptyString")
    @builtins.classmethod
    def any_empty_string(cls) -> typing.Any:
        return typing.cast(typing.Any, jsii.sinvoke(cls, "anyEmptyString", []))

    @jsii.member(jsii_name="anyFunction")
    @builtins.classmethod
    def any_function(cls) -> typing.Any:
        return typing.cast(typing.Any, jsii.sinvoke(cls, "anyFunction", []))

    @jsii.member(jsii_name="anyHash")
    @builtins.classmethod
    def any_hash(cls) -> typing.Any:
        return typing.cast(typing.Any, jsii.sinvoke(cls, "anyHash", []))

    @jsii.member(jsii_name="anyNull")
    @builtins.classmethod
    def any_null(cls) -> typing.Any:
        return typing.cast(typing.Any, jsii.sinvoke(cls, "anyNull", []))

    @jsii.member(jsii_name="anyNumber")
    @builtins.classmethod
    def any_number(cls) -> typing.Any:
        return typing.cast(typing.Any, jsii.sinvoke(cls, "anyNumber", []))

    @jsii.member(jsii_name="anyRef")
    @builtins.classmethod
    def any_ref(cls) -> typing.Any:
        return typing.cast(typing.Any, jsii.sinvoke(cls, "anyRef", []))

    @jsii.member(jsii_name="anyString")
    @builtins.classmethod
    def any_string(cls) -> typing.Any:
        return typing.cast(typing.Any, jsii.sinvoke(cls, "anyString", []))

    @jsii.member(jsii_name="anyUndefined")
    @builtins.classmethod
    def any_undefined(cls) -> typing.Any:
        return typing.cast(typing.Any, jsii.sinvoke(cls, "anyUndefined", []))

    @jsii.member(jsii_name="anyZero")
    @builtins.classmethod
    def any_zero(cls) -> typing.Any:
        return typing.cast(typing.Any, jsii.sinvoke(cls, "anyZero", []))

    @jsii.member(jsii_name="stringify")
    @builtins.classmethod
    def stringify(cls, value: typing.Any = None) -> typing.Optional[builtins.str]:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(JsonFormatter.stringify)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(typing.Optional[builtins.str], jsii.sinvoke(cls, "stringify", [value]))


class LevelOne(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.LevelOne"):
    '''Validates that nested classes get correct code generation for the occasional forward reference.'''

    def __init__(
        self,
        *,
        prop: typing.Union["LevelOne.PropProperty", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param prop: 
        '''
        props = LevelOneProps(prop=prop)

        jsii.create(self.__class__, self, [props])

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "LevelOneProps":
        return typing.cast("LevelOneProps", jsii.get(self, "props"))

    @jsii.data_type(
        jsii_type="jsii-calc.LevelOne.PropBooleanValue",
        jsii_struct_bases=[],
        name_mapping={"value": "value"},
    )
    class PropBooleanValue:
        def __init__(self, *, value: builtins.bool) -> None:
            '''
            :param value: 
            '''
            if __debug__:
                type_hints = typing.get_type_hints(LevelOne.PropBooleanValue.__init__)
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[str, typing.Any] = {
                "value": value,
            }

        @builtins.property
        def value(self) -> builtins.bool:
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.bool, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PropBooleanValue(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="jsii-calc.LevelOne.PropProperty",
        jsii_struct_bases=[],
        name_mapping={"prop": "prop"},
    )
    class PropProperty:
        def __init__(
            self,
            *,
            prop: typing.Union["LevelOne.PropBooleanValue", typing.Dict[str, typing.Any]],
        ) -> None:
            '''
            :param prop: 
            '''
            if isinstance(prop, dict):
                prop = LevelOne.PropBooleanValue(**prop)
            if __debug__:
                type_hints = typing.get_type_hints(LevelOne.PropProperty.__init__)
                check_type(argname="argument prop", value=prop, expected_type=type_hints["prop"])
            self._values: typing.Dict[str, typing.Any] = {
                "prop": prop,
            }

        @builtins.property
        def prop(self) -> "LevelOne.PropBooleanValue":
            result = self._values.get("prop")
            assert result is not None, "Required property 'prop' is missing"
            return typing.cast("LevelOne.PropBooleanValue", result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PropProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="jsii-calc.LevelOneProps",
    jsii_struct_bases=[],
    name_mapping={"prop": "prop"},
)
class LevelOneProps:
    def __init__(
        self,
        *,
        prop: typing.Union[LevelOne.PropProperty, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param prop: 
        '''
        if isinstance(prop, dict):
            prop = LevelOne.PropProperty(**prop)
        if __debug__:
            type_hints = typing.get_type_hints(LevelOneProps.__init__)
            check_type(argname="argument prop", value=prop, expected_type=type_hints["prop"])
        self._values: typing.Dict[str, typing.Any] = {
            "prop": prop,
        }

    @builtins.property
    def prop(self) -> LevelOne.PropProperty:
        result = self._values.get("prop")
        assert result is not None, "Required property 'prop' is missing"
        return typing.cast(LevelOne.PropProperty, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LevelOneProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="jsii-calc.LoadBalancedFargateServiceProps",
    jsii_struct_bases=[],
    name_mapping={
        "container_port": "containerPort",
        "cpu": "cpu",
        "memory_mib": "memoryMiB",
        "public_load_balancer": "publicLoadBalancer",
        "public_tasks": "publicTasks",
    },
)
class LoadBalancedFargateServiceProps:
    def __init__(
        self,
        *,
        container_port: typing.Optional[jsii.Number] = None,
        cpu: typing.Optional[builtins.str] = None,
        memory_mib: typing.Optional[builtins.str] = None,
        public_load_balancer: typing.Optional[builtins.bool] = None,
        public_tasks: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''jsii#298: show default values in sphinx documentation, and respect newlines.

        :param container_port: The container port of the application load balancer attached to your Fargate service. Corresponds to container port mapping. Default: 80
        :param cpu: The number of cpu units used by the task. Valid values, which determines your range of valid values for the memory parameter: 256 (.25 vCPU) - Available memory values: 0.5GB, 1GB, 2GB 512 (.5 vCPU) - Available memory values: 1GB, 2GB, 3GB, 4GB 1024 (1 vCPU) - Available memory values: 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB 2048 (2 vCPU) - Available memory values: Between 4GB and 16GB in 1GB increments 4096 (4 vCPU) - Available memory values: Between 8GB and 30GB in 1GB increments This default is set in the underlying FargateTaskDefinition construct. Default: 256
        :param memory_mib: The amount (in MiB) of memory used by the task. This field is required and you must use one of the following values, which determines your range of valid values for the cpu parameter: 0.5GB, 1GB, 2GB - Available cpu values: 256 (.25 vCPU) 1GB, 2GB, 3GB, 4GB - Available cpu values: 512 (.5 vCPU) 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB - Available cpu values: 1024 (1 vCPU) Between 4GB and 16GB in 1GB increments - Available cpu values: 2048 (2 vCPU) Between 8GB and 30GB in 1GB increments - Available cpu values: 4096 (4 vCPU) This default is set in the underlying FargateTaskDefinition construct. Default: 512
        :param public_load_balancer: Determines whether the Application Load Balancer will be internet-facing. Default: true
        :param public_tasks: Determines whether your Fargate Service will be assigned a public IP address. Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancedFargateServiceProps.__init__)
            check_type(argname="argument container_port", value=container_port, expected_type=type_hints["container_port"])
            check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
            check_type(argname="argument memory_mib", value=memory_mib, expected_type=type_hints["memory_mib"])
            check_type(argname="argument public_load_balancer", value=public_load_balancer, expected_type=type_hints["public_load_balancer"])
            check_type(argname="argument public_tasks", value=public_tasks, expected_type=type_hints["public_tasks"])
        self._values: typing.Dict[str, typing.Any] = {}
        if container_port is not None:
            self._values["container_port"] = container_port
        if cpu is not None:
            self._values["cpu"] = cpu
        if memory_mib is not None:
            self._values["memory_mib"] = memory_mib
        if public_load_balancer is not None:
            self._values["public_load_balancer"] = public_load_balancer
        if public_tasks is not None:
            self._values["public_tasks"] = public_tasks

    @builtins.property
    def container_port(self) -> typing.Optional[jsii.Number]:
        '''The container port of the application load balancer attached to your Fargate service.

        Corresponds to container port mapping.

        :default: 80
        '''
        result = self._values.get("container_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cpu(self) -> typing.Optional[builtins.str]:
        '''The number of cpu units used by the task.

        Valid values, which determines your range of valid values for the memory parameter:
        256 (.25 vCPU) - Available memory values: 0.5GB, 1GB, 2GB
        512 (.5 vCPU) - Available memory values: 1GB, 2GB, 3GB, 4GB
        1024 (1 vCPU) - Available memory values: 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB
        2048 (2 vCPU) - Available memory values: Between 4GB and 16GB in 1GB increments
        4096 (4 vCPU) - Available memory values: Between 8GB and 30GB in 1GB increments

        This default is set in the underlying FargateTaskDefinition construct.

        :default: 256
        '''
        result = self._values.get("cpu")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def memory_mib(self) -> typing.Optional[builtins.str]:
        '''The amount (in MiB) of memory used by the task.

        This field is required and you must use one of the following values, which determines your range of valid values
        for the cpu parameter:

        0.5GB, 1GB, 2GB - Available cpu values: 256 (.25 vCPU)

        1GB, 2GB, 3GB, 4GB - Available cpu values: 512 (.5 vCPU)

        2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB - Available cpu values: 1024 (1 vCPU)

        Between 4GB and 16GB in 1GB increments - Available cpu values: 2048 (2 vCPU)

        Between 8GB and 30GB in 1GB increments - Available cpu values: 4096 (4 vCPU)

        This default is set in the underlying FargateTaskDefinition construct.

        :default: 512
        '''
        result = self._values.get("memory_mib")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_load_balancer(self) -> typing.Optional[builtins.bool]:
        '''Determines whether the Application Load Balancer will be internet-facing.

        :default: true
        '''
        result = self._values.get("public_load_balancer")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def public_tasks(self) -> typing.Optional[builtins.bool]:
        '''Determines whether your Fargate Service will be assigned a public IP address.

        :default: false
        '''
        result = self._values.get("public_tasks")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancedFargateServiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MethodNamedProperty(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.MethodNamedProperty",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="property")
    def property(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "property", []))

    @builtins.property
    @jsii.member(jsii_name="elite")
    def elite(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "elite"))


@jsii.implements(IFriendlier, IRandomNumberGenerator)
class Multiply(
    BinaryOperation,
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.Multiply",
):
    '''The "*" binary operation.'''

    def __init__(
        self,
        lhs: scope.jsii_calc_lib.NumericValue,
        rhs: scope.jsii_calc_lib.NumericValue,
    ) -> None:
        '''Creates a BinaryOperation.

        :param lhs: Left-hand side operand.
        :param rhs: Right-hand side operand.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Multiply.__init__)
            check_type(argname="argument lhs", value=lhs, expected_type=type_hints["lhs"])
            check_type(argname="argument rhs", value=rhs, expected_type=type_hints["rhs"])
        jsii.create(self.__class__, self, [lhs, rhs])

    @jsii.member(jsii_name="farewell")
    def farewell(self) -> builtins.str:
        '''Say farewell.'''
        return typing.cast(builtins.str, jsii.invoke(self, "farewell", []))

    @jsii.member(jsii_name="goodbye")
    def goodbye(self) -> builtins.str:
        '''Say goodbye.'''
        return typing.cast(builtins.str, jsii.invoke(self, "goodbye", []))

    @jsii.member(jsii_name="next")
    def next(self) -> jsii.Number:
        '''Returns another random number.'''
        return typing.cast(jsii.Number, jsii.invoke(self, "next", []))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''String representation of the value.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        '''The value.'''
        return typing.cast(jsii.Number, jsii.get(self, "value"))


class NestedClassInstance(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.NestedClassInstance",
):
    @jsii.member(jsii_name="makeInstance")
    @builtins.classmethod
    def make_instance(
        cls,
    ) -> scope.jsii_calc_lib.custom_submodule_name.NestingClass.NestedClass:
        return typing.cast(scope.jsii_calc_lib.custom_submodule_name.NestingClass.NestedClass, jsii.sinvoke(cls, "makeInstance", []))


@jsii.data_type(
    jsii_type="jsii-calc.NestedStruct",
    jsii_struct_bases=[],
    name_mapping={"number_prop": "numberProp"},
)
class NestedStruct:
    def __init__(self, *, number_prop: jsii.Number) -> None:
        '''
        :param number_prop: When provided, must be > 0.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NestedStruct.__init__)
            check_type(argname="argument number_prop", value=number_prop, expected_type=type_hints["number_prop"])
        self._values: typing.Dict[str, typing.Any] = {
            "number_prop": number_prop,
        }

    @builtins.property
    def number_prop(self) -> jsii.Number:
        '''When provided, must be > 0.'''
        result = self._values.get("number_prop")
        assert result is not None, "Required property 'number_prop' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NestedStruct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NodeStandardLibrary(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.NodeStandardLibrary",
):
    '''Test fixture to verify that jsii modules can use the node standard library.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="cryptoSha256")
    def crypto_sha256(self) -> builtins.str:
        '''Uses node.js "crypto" module to calculate sha256 of a string.

        :return: "6a2da20943931e9834fc12cfe5bb47bbd9ae43489a30726962b576f4e3993e50"
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "cryptoSha256", []))

    @jsii.member(jsii_name="fsReadFile")
    def fs_read_file(self) -> builtins.str:
        '''Reads a local resource file (resource.txt) asynchronously.

        :return: "Hello, resource!"
        '''
        return typing.cast(builtins.str, jsii.ainvoke(self, "fsReadFile", []))

    @jsii.member(jsii_name="fsReadFileSync")
    def fs_read_file_sync(self) -> builtins.str:
        '''Sync version of fsReadFile.

        :return: "Hello, resource! SYNC!"
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "fsReadFileSync", []))

    @builtins.property
    @jsii.member(jsii_name="osPlatform")
    def os_platform(self) -> builtins.str:
        '''Returns the current os.platform() from the "os" node module.'''
        return typing.cast(builtins.str, jsii.get(self, "osPlatform"))


class NullShouldBeTreatedAsUndefined(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.NullShouldBeTreatedAsUndefined",
):
    '''jsii#282, aws-cdk#157: null should be treated as "undefined".'''

    def __init__(self, _param1: builtins.str, optional: typing.Any = None) -> None:
        '''
        :param _param1: -
        :param optional: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NullShouldBeTreatedAsUndefined.__init__)
            check_type(argname="argument _param1", value=_param1, expected_type=type_hints["_param1"])
            check_type(argname="argument optional", value=optional, expected_type=type_hints["optional"])
        jsii.create(self.__class__, self, [_param1, optional])

    @jsii.member(jsii_name="giveMeUndefined")
    def give_me_undefined(self, value: typing.Any = None) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NullShouldBeTreatedAsUndefined.give_me_undefined)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "giveMeUndefined", [value]))

    @jsii.member(jsii_name="giveMeUndefinedInsideAnObject")
    def give_me_undefined_inside_an_object(
        self,
        *,
        array_with_three_elements_and_undefined_as_second_argument: typing.Sequence[typing.Any],
        this_should_be_undefined: typing.Any = None,
    ) -> None:
        '''
        :param array_with_three_elements_and_undefined_as_second_argument: 
        :param this_should_be_undefined: 
        '''
        input = NullShouldBeTreatedAsUndefinedData(
            array_with_three_elements_and_undefined_as_second_argument=array_with_three_elements_and_undefined_as_second_argument,
            this_should_be_undefined=this_should_be_undefined,
        )

        return typing.cast(None, jsii.invoke(self, "giveMeUndefinedInsideAnObject", [input]))

    @jsii.member(jsii_name="verifyPropertyIsUndefined")
    def verify_property_is_undefined(self) -> None:
        return typing.cast(None, jsii.invoke(self, "verifyPropertyIsUndefined", []))

    @builtins.property
    @jsii.member(jsii_name="changeMeToUndefined")
    def change_me_to_undefined(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "changeMeToUndefined"))

    @change_me_to_undefined.setter
    def change_me_to_undefined(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NullShouldBeTreatedAsUndefined, "change_me_to_undefined").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "changeMeToUndefined", value)


@jsii.data_type(
    jsii_type="jsii-calc.NullShouldBeTreatedAsUndefinedData",
    jsii_struct_bases=[],
    name_mapping={
        "array_with_three_elements_and_undefined_as_second_argument": "arrayWithThreeElementsAndUndefinedAsSecondArgument",
        "this_should_be_undefined": "thisShouldBeUndefined",
    },
)
class NullShouldBeTreatedAsUndefinedData:
    def __init__(
        self,
        *,
        array_with_three_elements_and_undefined_as_second_argument: typing.Sequence[typing.Any],
        this_should_be_undefined: typing.Any = None,
    ) -> None:
        '''
        :param array_with_three_elements_and_undefined_as_second_argument: 
        :param this_should_be_undefined: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NullShouldBeTreatedAsUndefinedData.__init__)
            check_type(argname="argument array_with_three_elements_and_undefined_as_second_argument", value=array_with_three_elements_and_undefined_as_second_argument, expected_type=type_hints["array_with_three_elements_and_undefined_as_second_argument"])
            check_type(argname="argument this_should_be_undefined", value=this_should_be_undefined, expected_type=type_hints["this_should_be_undefined"])
        self._values: typing.Dict[str, typing.Any] = {
            "array_with_three_elements_and_undefined_as_second_argument": array_with_three_elements_and_undefined_as_second_argument,
        }
        if this_should_be_undefined is not None:
            self._values["this_should_be_undefined"] = this_should_be_undefined

    @builtins.property
    def array_with_three_elements_and_undefined_as_second_argument(
        self,
    ) -> typing.List[typing.Any]:
        result = self._values.get("array_with_three_elements_and_undefined_as_second_argument")
        assert result is not None, "Required property 'array_with_three_elements_and_undefined_as_second_argument' is missing"
        return typing.cast(typing.List[typing.Any], result)

    @builtins.property
    def this_should_be_undefined(self) -> typing.Any:
        result = self._values.get("this_should_be_undefined")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NullShouldBeTreatedAsUndefinedData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NumberGenerator(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.NumberGenerator"):
    '''This allows us to test that a reference can be stored for objects that implement interfaces.'''

    def __init__(self, generator: IRandomNumberGenerator) -> None:
        '''
        :param generator: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NumberGenerator.__init__)
            check_type(argname="argument generator", value=generator, expected_type=type_hints["generator"])
        jsii.create(self.__class__, self, [generator])

    @jsii.member(jsii_name="isSameGenerator")
    def is_same_generator(self, gen: IRandomNumberGenerator) -> builtins.bool:
        '''
        :param gen: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NumberGenerator.is_same_generator)
            check_type(argname="argument gen", value=gen, expected_type=type_hints["gen"])
        return typing.cast(builtins.bool, jsii.invoke(self, "isSameGenerator", [gen]))

    @jsii.member(jsii_name="nextTimes100")
    def next_times100(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.invoke(self, "nextTimes100", []))

    @builtins.property
    @jsii.member(jsii_name="generator")
    def generator(self) -> IRandomNumberGenerator:
        return typing.cast(IRandomNumberGenerator, jsii.get(self, "generator"))

    @generator.setter
    def generator(self, value: IRandomNumberGenerator) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NumberGenerator, "generator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generator", value)


class ObjectRefsInCollections(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.ObjectRefsInCollections",
):
    '''Verify that object references can be passed inside collections.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="sumFromArray")
    def sum_from_array(
        self,
        values: typing.Sequence[scope.jsii_calc_lib.NumericValue],
    ) -> jsii.Number:
        '''Returns the sum of all values.

        :param values: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ObjectRefsInCollections.sum_from_array)
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        return typing.cast(jsii.Number, jsii.invoke(self, "sumFromArray", [values]))

    @jsii.member(jsii_name="sumFromMap")
    def sum_from_map(
        self,
        values: typing.Mapping[builtins.str, scope.jsii_calc_lib.NumericValue],
    ) -> jsii.Number:
        '''Returns the sum of all values in a map.

        :param values: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ObjectRefsInCollections.sum_from_map)
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        return typing.cast(jsii.Number, jsii.invoke(self, "sumFromMap", [values]))


class ObjectWithPropertyProvider(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.ObjectWithPropertyProvider",
):
    @jsii.member(jsii_name="provide")
    @builtins.classmethod
    def provide(cls) -> IObjectWithProperty:
        return typing.cast(IObjectWithProperty, jsii.sinvoke(cls, "provide", []))


class Old(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.Old"):
    '''(deprecated) Old class.

    :deprecated:

    Use the new class or the old class whatever you want because
    whatever you like is always the best

    :stability: deprecated
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="doAThing")
    def do_a_thing(self) -> None:
        '''(deprecated) Doo wop that thing.

        :stability: deprecated
        '''
        return typing.cast(None, jsii.invoke(self, "doAThing", []))


class OptionalArgumentInvoker(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.OptionalArgumentInvoker",
):
    def __init__(self, delegate: IInterfaceWithOptionalMethodArguments) -> None:
        '''
        :param delegate: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OptionalArgumentInvoker.__init__)
            check_type(argname="argument delegate", value=delegate, expected_type=type_hints["delegate"])
        jsii.create(self.__class__, self, [delegate])

    @jsii.member(jsii_name="invokeWithOptional")
    def invoke_with_optional(self) -> None:
        return typing.cast(None, jsii.invoke(self, "invokeWithOptional", []))

    @jsii.member(jsii_name="invokeWithoutOptional")
    def invoke_without_optional(self) -> None:
        return typing.cast(None, jsii.invoke(self, "invokeWithoutOptional", []))


class OptionalConstructorArgument(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.OptionalConstructorArgument",
):
    def __init__(
        self,
        arg1: jsii.Number,
        arg2: builtins.str,
        arg3: typing.Optional[datetime.datetime] = None,
    ) -> None:
        '''
        :param arg1: -
        :param arg2: -
        :param arg3: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OptionalConstructorArgument.__init__)
            check_type(argname="argument arg1", value=arg1, expected_type=type_hints["arg1"])
            check_type(argname="argument arg2", value=arg2, expected_type=type_hints["arg2"])
            check_type(argname="argument arg3", value=arg3, expected_type=type_hints["arg3"])
        jsii.create(self.__class__, self, [arg1, arg2, arg3])

    @builtins.property
    @jsii.member(jsii_name="arg1")
    def arg1(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "arg1"))

    @builtins.property
    @jsii.member(jsii_name="arg2")
    def arg2(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arg2"))

    @builtins.property
    @jsii.member(jsii_name="arg3")
    def arg3(self) -> typing.Optional[datetime.datetime]:
        return typing.cast(typing.Optional[datetime.datetime], jsii.get(self, "arg3"))


@jsii.data_type(
    jsii_type="jsii-calc.OptionalStruct",
    jsii_struct_bases=[],
    name_mapping={"field": "field"},
)
class OptionalStruct:
    def __init__(self, *, field: typing.Optional[builtins.str] = None) -> None:
        '''
        :param field: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OptionalStruct.__init__)
            check_type(argname="argument field", value=field, expected_type=type_hints["field"])
        self._values: typing.Dict[str, typing.Any] = {}
        if field is not None:
            self._values["field"] = field

    @builtins.property
    def field(self) -> typing.Optional[builtins.str]:
        result = self._values.get("field")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OptionalStruct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OptionalStructConsumer(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.OptionalStructConsumer",
):
    def __init__(self, *, field: typing.Optional[builtins.str] = None) -> None:
        '''
        :param field: 
        '''
        optional_struct = OptionalStruct(field=field)

        jsii.create(self.__class__, self, [optional_struct])

    @builtins.property
    @jsii.member(jsii_name="parameterWasUndefined")
    def parameter_was_undefined(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "parameterWasUndefined"))

    @builtins.property
    @jsii.member(jsii_name="fieldValue")
    def field_value(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldValue"))


class OverridableProtectedMember(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.OverridableProtectedMember",
):
    '''
    :see: https://github.com/aws/jsii/issues/903
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="overrideMe")
    def _override_me(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "overrideMe", []))

    @jsii.member(jsii_name="switchModes")
    def switch_modes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "switchModes", []))

    @jsii.member(jsii_name="valueFromProtected")
    def value_from_protected(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "valueFromProtected", []))

    @builtins.property
    @jsii.member(jsii_name="overrideReadOnly")
    def _override_read_only(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "overrideReadOnly"))

    @builtins.property
    @jsii.member(jsii_name="overrideReadWrite")
    def _override_read_write(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "overrideReadWrite"))

    @_override_read_write.setter
    def _override_read_write(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OverridableProtectedMember, "_override_read_write").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overrideReadWrite", value)


class OverrideReturnsObject(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.OverrideReturnsObject",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="test")
    def test(self, obj: IReturnsNumber) -> jsii.Number:
        '''
        :param obj: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OverrideReturnsObject.test)
            check_type(argname="argument obj", value=obj, expected_type=type_hints["obj"])
        return typing.cast(jsii.Number, jsii.invoke(self, "test", [obj]))


@jsii.data_type(
    jsii_type="jsii-calc.ParentStruct982",
    jsii_struct_bases=[],
    name_mapping={"foo": "foo"},
)
class ParentStruct982:
    def __init__(self, *, foo: builtins.str) -> None:
        '''https://github.com/aws/jsii/issues/982.

        :param foo: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ParentStruct982.__init__)
            check_type(argname="argument foo", value=foo, expected_type=type_hints["foo"])
        self._values: typing.Dict[str, typing.Any] = {
            "foo": foo,
        }

    @builtins.property
    def foo(self) -> builtins.str:
        result = self._values.get("foo")
        assert result is not None, "Required property 'foo' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ParentStruct982(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PartiallyInitializedThisConsumer(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="jsii-calc.PartiallyInitializedThisConsumer",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="consumePartiallyInitializedThis")
    @abc.abstractmethod
    def consume_partially_initialized_this(
        self,
        obj: ConstructorPassesThisOut,
        dt: datetime.datetime,
        ev: AllTypesEnum,
    ) -> builtins.str:
        '''
        :param obj: -
        :param dt: -
        :param ev: -
        '''
        ...


class _PartiallyInitializedThisConsumerProxy(PartiallyInitializedThisConsumer):
    @jsii.member(jsii_name="consumePartiallyInitializedThis")
    def consume_partially_initialized_this(
        self,
        obj: ConstructorPassesThisOut,
        dt: datetime.datetime,
        ev: AllTypesEnum,
    ) -> builtins.str:
        '''
        :param obj: -
        :param dt: -
        :param ev: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PartiallyInitializedThisConsumer.consume_partially_initialized_this)
            check_type(argname="argument obj", value=obj, expected_type=type_hints["obj"])
            check_type(argname="argument dt", value=dt, expected_type=type_hints["dt"])
            check_type(argname="argument ev", value=ev, expected_type=type_hints["ev"])
        return typing.cast(builtins.str, jsii.invoke(self, "consumePartiallyInitializedThis", [obj, dt, ev]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, PartiallyInitializedThisConsumer).__jsii_proxy_class__ = lambda : _PartiallyInitializedThisConsumerProxy


class Polymorphism(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.Polymorphism"):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="sayHello")
    def say_hello(self, friendly: scope.jsii_calc_lib.IFriendly) -> builtins.str:
        '''
        :param friendly: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Polymorphism.say_hello)
            check_type(argname="argument friendly", value=friendly, expected_type=type_hints["friendly"])
        return typing.cast(builtins.str, jsii.invoke(self, "sayHello", [friendly]))


class Power(
    _CompositeOperation_1c4d123b,
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.Power",
):
    '''The power operation.'''

    def __init__(
        self,
        base: scope.jsii_calc_lib.NumericValue,
        pow: scope.jsii_calc_lib.NumericValue,
    ) -> None:
        '''Creates a Power operation.

        :param base: The base of the power.
        :param pow: The number of times to multiply.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Power.__init__)
            check_type(argname="argument base", value=base, expected_type=type_hints["base"])
            check_type(argname="argument pow", value=pow, expected_type=type_hints["pow"])
        jsii.create(self.__class__, self, [base, pow])

    @builtins.property
    @jsii.member(jsii_name="base")
    def base(self) -> scope.jsii_calc_lib.NumericValue:
        '''The base of the power.'''
        return typing.cast(scope.jsii_calc_lib.NumericValue, jsii.get(self, "base"))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> scope.jsii_calc_lib.NumericValue:
        '''The expression that this operation consists of.

        Must be implemented by derived classes.
        '''
        return typing.cast(scope.jsii_calc_lib.NumericValue, jsii.get(self, "expression"))

    @builtins.property
    @jsii.member(jsii_name="pow")
    def pow(self) -> scope.jsii_calc_lib.NumericValue:
        '''The number of times to multiply.'''
        return typing.cast(scope.jsii_calc_lib.NumericValue, jsii.get(self, "pow"))


class PropertyNamedProperty(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.PropertyNamedProperty",
):
    '''Reproduction for https://github.com/aws/jsii/issues/1113 Where a method or property named "property" would result in impossible to load Python code.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @builtins.property
    @jsii.member(jsii_name="property")
    def property(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "property"))

    @builtins.property
    @jsii.member(jsii_name="yetAnoterOne")
    def yet_anoter_one(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "yetAnoterOne"))


class PublicClass(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.PublicClass"):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="hello")
    def hello(self) -> None:
        return typing.cast(None, jsii.invoke(self, "hello", []))


class PythonReservedWords(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.PythonReservedWords",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="and")
    def and_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "and", []))

    @jsii.member(jsii_name="as")
    def as_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "as", []))

    @jsii.member(jsii_name="assert")
    def assert_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "assert", []))

    @jsii.member(jsii_name="async")
    def async_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "async", []))

    @jsii.member(jsii_name="await")
    def await_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "await", []))

    @jsii.member(jsii_name="break")
    def break_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "break", []))

    @jsii.member(jsii_name="class")
    def class_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "class", []))

    @jsii.member(jsii_name="continue")
    def continue_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "continue", []))

    @jsii.member(jsii_name="def")
    def def_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "def", []))

    @jsii.member(jsii_name="del")
    def del_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "del", []))

    @jsii.member(jsii_name="elif")
    def elif_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "elif", []))

    @jsii.member(jsii_name="else")
    def else_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "else", []))

    @jsii.member(jsii_name="except")
    def except_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "except", []))

    @jsii.member(jsii_name="finally")
    def finally_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "finally", []))

    @jsii.member(jsii_name="for")
    def for_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "for", []))

    @jsii.member(jsii_name="from")
    def from_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "from", []))

    @jsii.member(jsii_name="global")
    def global_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "global", []))

    @jsii.member(jsii_name="if")
    def if_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "if", []))

    @jsii.member(jsii_name="import")
    def import_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "import", []))

    @jsii.member(jsii_name="in")
    def in_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "in", []))

    @jsii.member(jsii_name="is")
    def is_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "is", []))

    @jsii.member(jsii_name="lambda")
    def lambda_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "lambda", []))

    @jsii.member(jsii_name="nonlocal")
    def nonlocal_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "nonlocal", []))

    @jsii.member(jsii_name="not")
    def not_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "not", []))

    @jsii.member(jsii_name="or")
    def or_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "or", []))

    @jsii.member(jsii_name="pass")
    def pass_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "pass", []))

    @jsii.member(jsii_name="raise")
    def raise_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "raise", []))

    @jsii.member(jsii_name="return")
    def return_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "return", []))

    @jsii.member(jsii_name="try")
    def try_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "try", []))

    @jsii.member(jsii_name="while")
    def while_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "while", []))

    @jsii.member(jsii_name="with")
    def with_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "with", []))

    @jsii.member(jsii_name="yield")
    def yield_(self) -> None:
        return typing.cast(None, jsii.invoke(self, "yield", []))


class ReferenceEnumFromScopedPackage(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.ReferenceEnumFromScopedPackage",
):
    '''See awslabs/jsii#138.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="loadFoo")
    def load_foo(self) -> typing.Optional[scope.jsii_calc_lib.EnumFromScopedModule]:
        return typing.cast(typing.Optional[scope.jsii_calc_lib.EnumFromScopedModule], jsii.invoke(self, "loadFoo", []))

    @jsii.member(jsii_name="saveFoo")
    def save_foo(self, value: scope.jsii_calc_lib.EnumFromScopedModule) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ReferenceEnumFromScopedPackage.save_foo)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "saveFoo", [value]))

    @builtins.property
    @jsii.member(jsii_name="foo")
    def foo(self) -> typing.Optional[scope.jsii_calc_lib.EnumFromScopedModule]:
        return typing.cast(typing.Optional[scope.jsii_calc_lib.EnumFromScopedModule], jsii.get(self, "foo"))

    @foo.setter
    def foo(
        self,
        value: typing.Optional[scope.jsii_calc_lib.EnumFromScopedModule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ReferenceEnumFromScopedPackage, "foo").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "foo", value)


class ReturnsPrivateImplementationOfInterface(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.ReturnsPrivateImplementationOfInterface",
):
    '''Helps ensure the JSII kernel & runtime cooperate correctly when an un-exported instance of a class is returned with a declared type that is an exported interface, and the instance inherits from an exported class.

    :return: an instance of an un-exported class that extends ``ExportedBaseClass``, declared as ``IPrivatelyImplemented``.

    :see: https://github.com/aws/jsii/issues/320
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @builtins.property
    @jsii.member(jsii_name="privateImplementation")
    def private_implementation(self) -> IPrivatelyImplemented:
        return typing.cast(IPrivatelyImplemented, jsii.get(self, "privateImplementation"))


@jsii.data_type(
    jsii_type="jsii-calc.RootStruct",
    jsii_struct_bases=[],
    name_mapping={"string_prop": "stringProp", "nested_struct": "nestedStruct"},
)
class RootStruct:
    def __init__(
        self,
        *,
        string_prop: builtins.str,
        nested_struct: typing.Optional[typing.Union[NestedStruct, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''This is here to check that we can pass a nested struct into a kwargs by specifying it as an in-line dictionary.

        This is cheating with the (current) declared types, but this is the "more
        idiomatic" way for Pythonists.

        :param string_prop: May not be empty.
        :param nested_struct: 
        '''
        if isinstance(nested_struct, dict):
            nested_struct = NestedStruct(**nested_struct)
        if __debug__:
            type_hints = typing.get_type_hints(RootStruct.__init__)
            check_type(argname="argument string_prop", value=string_prop, expected_type=type_hints["string_prop"])
            check_type(argname="argument nested_struct", value=nested_struct, expected_type=type_hints["nested_struct"])
        self._values: typing.Dict[str, typing.Any] = {
            "string_prop": string_prop,
        }
        if nested_struct is not None:
            self._values["nested_struct"] = nested_struct

    @builtins.property
    def string_prop(self) -> builtins.str:
        '''May not be empty.'''
        result = self._values.get("string_prop")
        assert result is not None, "Required property 'string_prop' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def nested_struct(self) -> typing.Optional[NestedStruct]:
        result = self._values.get("nested_struct")
        return typing.cast(typing.Optional[NestedStruct], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RootStruct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RootStructValidator(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.RootStructValidator",
):
    @jsii.member(jsii_name="validate")
    @builtins.classmethod
    def validate(
        cls,
        *,
        string_prop: builtins.str,
        nested_struct: typing.Optional[typing.Union[NestedStruct, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param string_prop: May not be empty.
        :param nested_struct: 
        '''
        struct = RootStruct(string_prop=string_prop, nested_struct=nested_struct)

        return typing.cast(None, jsii.sinvoke(cls, "validate", [struct]))


class RuntimeTypeChecking(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.RuntimeTypeChecking",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="methodWithDefaultedArguments")
    def method_with_defaulted_arguments(
        self,
        arg1: typing.Optional[jsii.Number] = None,
        arg2: typing.Optional[builtins.str] = None,
        arg3: typing.Optional[datetime.datetime] = None,
    ) -> None:
        '''
        :param arg1: -
        :param arg2: -
        :param arg3: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RuntimeTypeChecking.method_with_defaulted_arguments)
            check_type(argname="argument arg1", value=arg1, expected_type=type_hints["arg1"])
            check_type(argname="argument arg2", value=arg2, expected_type=type_hints["arg2"])
            check_type(argname="argument arg3", value=arg3, expected_type=type_hints["arg3"])
        return typing.cast(None, jsii.invoke(self, "methodWithDefaultedArguments", [arg1, arg2, arg3]))

    @jsii.member(jsii_name="methodWithOptionalAnyArgument")
    def method_with_optional_any_argument(self, arg: typing.Any = None) -> None:
        '''
        :param arg: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RuntimeTypeChecking.method_with_optional_any_argument)
            check_type(argname="argument arg", value=arg, expected_type=type_hints["arg"])
        return typing.cast(None, jsii.invoke(self, "methodWithOptionalAnyArgument", [arg]))

    @jsii.member(jsii_name="methodWithOptionalArguments")
    def method_with_optional_arguments(
        self,
        arg1: jsii.Number,
        arg2: builtins.str,
        arg3: typing.Optional[datetime.datetime] = None,
    ) -> None:
        '''Used to verify verification of number of method arguments.

        :param arg1: -
        :param arg2: -
        :param arg3: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RuntimeTypeChecking.method_with_optional_arguments)
            check_type(argname="argument arg1", value=arg1, expected_type=type_hints["arg1"])
            check_type(argname="argument arg2", value=arg2, expected_type=type_hints["arg2"])
            check_type(argname="argument arg3", value=arg3, expected_type=type_hints["arg3"])
        return typing.cast(None, jsii.invoke(self, "methodWithOptionalArguments", [arg1, arg2, arg3]))


@jsii.data_type(
    jsii_type="jsii-calc.SecondLevelStruct",
    jsii_struct_bases=[],
    name_mapping={
        "deeper_required_prop": "deeperRequiredProp",
        "deeper_optional_prop": "deeperOptionalProp",
    },
)
class SecondLevelStruct:
    def __init__(
        self,
        *,
        deeper_required_prop: builtins.str,
        deeper_optional_prop: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param deeper_required_prop: It's long and required.
        :param deeper_optional_prop: It's long, but you'll almost never pass it.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SecondLevelStruct.__init__)
            check_type(argname="argument deeper_required_prop", value=deeper_required_prop, expected_type=type_hints["deeper_required_prop"])
            check_type(argname="argument deeper_optional_prop", value=deeper_optional_prop, expected_type=type_hints["deeper_optional_prop"])
        self._values: typing.Dict[str, typing.Any] = {
            "deeper_required_prop": deeper_required_prop,
        }
        if deeper_optional_prop is not None:
            self._values["deeper_optional_prop"] = deeper_optional_prop

    @builtins.property
    def deeper_required_prop(self) -> builtins.str:
        '''It's long and required.'''
        result = self._values.get("deeper_required_prop")
        assert result is not None, "Required property 'deeper_required_prop' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deeper_optional_prop(self) -> typing.Optional[builtins.str]:
        '''It's long, but you'll almost never pass it.'''
        result = self._values.get("deeper_optional_prop")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecondLevelStruct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SingleInstanceTwoTypes(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.SingleInstanceTwoTypes",
):
    '''Test that a single instance can be returned under two different FQNs.

    JSII clients can instantiate 2 different strongly-typed wrappers for the same
    object. Unfortunately, this will break object equality, but if we didn't do
    this it would break runtime type checks in the JVM or CLR.
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="interface1")
    def interface1(self) -> "InbetweenClass":
        return typing.cast("InbetweenClass", jsii.invoke(self, "interface1", []))

    @jsii.member(jsii_name="interface2")
    def interface2(self) -> IPublicInterface:
        return typing.cast(IPublicInterface, jsii.invoke(self, "interface2", []))


class SingletonInt(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.SingletonInt"):
    '''Verifies that singleton enums are handled correctly.

    https://github.com/aws/jsii/issues/231
    '''

    @jsii.member(jsii_name="isSingletonInt")
    def is_singleton_int(self, value: jsii.Number) -> builtins.bool:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SingletonInt.is_singleton_int)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(builtins.bool, jsii.invoke(self, "isSingletonInt", [value]))


@jsii.enum(jsii_type="jsii-calc.SingletonIntEnum")
class SingletonIntEnum(enum.Enum):
    '''A singleton integer.'''

    SINGLETON_INT = "SINGLETON_INT"
    '''Elite!'''


class SingletonString(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.SingletonString"):
    '''Verifies that singleton enums are handled correctly.

    https://github.com/aws/jsii/issues/231
    '''

    @jsii.member(jsii_name="isSingletonString")
    def is_singleton_string(self, value: builtins.str) -> builtins.bool:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SingletonString.is_singleton_string)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(builtins.bool, jsii.invoke(self, "isSingletonString", [value]))


@jsii.enum(jsii_type="jsii-calc.SingletonStringEnum")
class SingletonStringEnum(enum.Enum):
    '''A singleton string.'''

    SINGLETON_STRING = "SINGLETON_STRING"
    '''1337.'''


@jsii.data_type(
    jsii_type="jsii-calc.SmellyStruct",
    jsii_struct_bases=[],
    name_mapping={"property": "property", "yet_anoter_one": "yetAnoterOne"},
)
class SmellyStruct:
    def __init__(
        self,
        *,
        property: builtins.str,
        yet_anoter_one: builtins.bool,
    ) -> None:
        '''
        :param property: 
        :param yet_anoter_one: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SmellyStruct.__init__)
            check_type(argname="argument property", value=property, expected_type=type_hints["property"])
            check_type(argname="argument yet_anoter_one", value=yet_anoter_one, expected_type=type_hints["yet_anoter_one"])
        self._values: typing.Dict[str, typing.Any] = {
            "property": property,
            "yet_anoter_one": yet_anoter_one,
        }

    @builtins.property
    def property(self) -> builtins.str:
        result = self._values.get("property")
        assert result is not None, "Required property 'property' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def yet_anoter_one(self) -> builtins.bool:
        result = self._values.get("yet_anoter_one")
        assert result is not None, "Required property 'yet_anoter_one' is missing"
        return typing.cast(builtins.bool, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SmellyStruct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SomeTypeJsii976(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.SomeTypeJsii976"):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="returnAnonymous")
    @builtins.classmethod
    def return_anonymous(cls) -> typing.Any:
        return typing.cast(typing.Any, jsii.sinvoke(cls, "returnAnonymous", []))

    @jsii.member(jsii_name="returnReturn")
    @builtins.classmethod
    def return_return(cls) -> IReturnJsii976:
        return typing.cast(IReturnJsii976, jsii.sinvoke(cls, "returnReturn", []))


class StableClass(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.StableClass"):
    def __init__(
        self,
        readonly_string: builtins.str,
        mutable_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param readonly_string: -
        :param mutable_number: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StableClass.__init__)
            check_type(argname="argument readonly_string", value=readonly_string, expected_type=type_hints["readonly_string"])
            check_type(argname="argument mutable_number", value=mutable_number, expected_type=type_hints["mutable_number"])
        jsii.create(self.__class__, self, [readonly_string, mutable_number])

    @jsii.member(jsii_name="method")
    def method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "method", []))

    @builtins.property
    @jsii.member(jsii_name="readonlyProperty")
    def readonly_property(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "readonlyProperty"))

    @builtins.property
    @jsii.member(jsii_name="mutableProperty")
    def mutable_property(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "mutableProperty"))

    @mutable_property.setter
    def mutable_property(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StableClass, "mutable_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mutableProperty", value)


@jsii.enum(jsii_type="jsii-calc.StableEnum")
class StableEnum(enum.Enum):
    OPTION_A = "OPTION_A"
    OPTION_B = "OPTION_B"


@jsii.data_type(
    jsii_type="jsii-calc.StableStruct",
    jsii_struct_bases=[],
    name_mapping={"readonly_property": "readonlyProperty"},
)
class StableStruct:
    def __init__(self, *, readonly_property: builtins.str) -> None:
        '''
        :param readonly_property: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StableStruct.__init__)
            check_type(argname="argument readonly_property", value=readonly_property, expected_type=type_hints["readonly_property"])
        self._values: typing.Dict[str, typing.Any] = {
            "readonly_property": readonly_property,
        }

    @builtins.property
    def readonly_property(self) -> builtins.str:
        result = self._values.get("readonly_property")
        assert result is not None, "Required property 'readonly_property' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StableStruct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StaticContext(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.StaticContext"):
    '''This is used to validate the ability to use ``this`` from within a static context.

    https://github.com/awslabs/aws-cdk/issues/2304
    '''

    @jsii.member(jsii_name="canAccessStaticContext")
    @builtins.classmethod
    def can_access_static_context(cls) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "canAccessStaticContext", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="staticVariable")
    def static_variable(cls) -> builtins.bool:  # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(builtins.bool, jsii.sget(cls, "staticVariable"))

    @static_variable.setter # type: ignore[no-redef]
    def static_variable(cls, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StaticContext, "static_variable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.sset(cls, "staticVariable", value)


class StaticHelloParent(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.StaticHelloParent",
):
    '''Static methods that override parent class are technically overrides (the inheritance of statics is part of the ES6 specification), but certain other languages such as Java do not carry statics in the inheritance chain at all, so they cannot be overridden, only hidden.

    The difference is fairly minor (for typical use-cases, the end result is the
    same), however this has implications on what the generated code should look
    like.
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="method")
    @builtins.classmethod
    def method(cls) -> None:
        return typing.cast(None, jsii.sinvoke(cls, "method", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="property")
    def property(cls) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.sget(cls, "property"))


class Statics(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.Statics"):
    def __init__(self, value: builtins.str) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Statics.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.create(self.__class__, self, [value])

    @jsii.member(jsii_name="staticMethod")
    @builtins.classmethod
    def static_method(cls, name: builtins.str) -> builtins.str:
        '''Jsdocs for static method.

        :param name: The name of the person to say hello to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Statics.static_method)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "staticMethod", [name]))

    @jsii.member(jsii_name="justMethod")
    def just_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "justMethod", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BAR")
    def BAR(cls) -> jsii.Number:
        '''Constants may also use all-caps.'''
        return typing.cast(jsii.Number, jsii.sget(cls, "BAR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ConstObj")
    def CONST_OBJ(cls) -> "DoubleTrouble":
        return typing.cast("DoubleTrouble", jsii.sget(cls, "ConstObj"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="Foo")
    def FOO(cls) -> builtins.str:
        '''Jsdocs for static property.'''
        return typing.cast(builtins.str, jsii.sget(cls, "Foo"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="zooBar")
    def ZOO_BAR(cls) -> typing.Mapping[builtins.str, builtins.str]:
        '''Constants can also use camelCase.'''
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.sget(cls, "zooBar"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="instance")
    def instance(cls) -> "Statics":  # pyright: ignore [reportGeneralTypeIssues]
        '''Jsdocs for static getter.

        Jsdocs for static setter.
        '''
        return typing.cast("Statics", jsii.sget(cls, "instance"))

    @instance.setter # type: ignore[no-redef]
    def instance(cls, value: "Statics") -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Statics, "instance").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.sset(cls, "instance", value)

    @jsii.python.classproperty
    @jsii.member(jsii_name="nonConstStatic")
    def non_const_static(cls) -> jsii.Number:  # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(jsii.Number, jsii.sget(cls, "nonConstStatic"))

    @non_const_static.setter # type: ignore[no-redef]
    def non_const_static(cls, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Statics, "non_const_static").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.sset(cls, "nonConstStatic", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))


@jsii.enum(jsii_type="jsii-calc.StringEnum")
class StringEnum(enum.Enum):
    A = "A"
    B = "B"
    C = "C"


class StripInternal(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.StripInternal"):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @builtins.property
    @jsii.member(jsii_name="youSeeMe")
    def you_see_me(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "youSeeMe"))

    @you_see_me.setter
    def you_see_me(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StripInternal, "you_see_me").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "youSeeMe", value)


@jsii.data_type(
    jsii_type="jsii-calc.StructA",
    jsii_struct_bases=[],
    name_mapping={
        "required_string": "requiredString",
        "optional_number": "optionalNumber",
        "optional_string": "optionalString",
    },
)
class StructA:
    def __init__(
        self,
        *,
        required_string: builtins.str,
        optional_number: typing.Optional[jsii.Number] = None,
        optional_string: typing.Optional[builtins.str] = None,
    ) -> None:
        '''We can serialize and deserialize structs without silently ignoring optional fields.

        :param required_string: 
        :param optional_number: 
        :param optional_string: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StructA.__init__)
            check_type(argname="argument required_string", value=required_string, expected_type=type_hints["required_string"])
            check_type(argname="argument optional_number", value=optional_number, expected_type=type_hints["optional_number"])
            check_type(argname="argument optional_string", value=optional_string, expected_type=type_hints["optional_string"])
        self._values: typing.Dict[str, typing.Any] = {
            "required_string": required_string,
        }
        if optional_number is not None:
            self._values["optional_number"] = optional_number
        if optional_string is not None:
            self._values["optional_string"] = optional_string

    @builtins.property
    def required_string(self) -> builtins.str:
        result = self._values.get("required_string")
        assert result is not None, "Required property 'required_string' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def optional_number(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("optional_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def optional_string(self) -> typing.Optional[builtins.str]:
        result = self._values.get("optional_string")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StructA(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="jsii-calc.StructB",
    jsii_struct_bases=[],
    name_mapping={
        "required_string": "requiredString",
        "optional_boolean": "optionalBoolean",
        "optional_struct_a": "optionalStructA",
    },
)
class StructB:
    def __init__(
        self,
        *,
        required_string: builtins.str,
        optional_boolean: typing.Optional[builtins.bool] = None,
        optional_struct_a: typing.Optional[typing.Union[StructA, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''This intentionally overlaps with StructA (where only requiredString is provided) to test htat the kernel properly disambiguates those.

        :param required_string: 
        :param optional_boolean: 
        :param optional_struct_a: 
        '''
        if isinstance(optional_struct_a, dict):
            optional_struct_a = StructA(**optional_struct_a)
        if __debug__:
            type_hints = typing.get_type_hints(StructB.__init__)
            check_type(argname="argument required_string", value=required_string, expected_type=type_hints["required_string"])
            check_type(argname="argument optional_boolean", value=optional_boolean, expected_type=type_hints["optional_boolean"])
            check_type(argname="argument optional_struct_a", value=optional_struct_a, expected_type=type_hints["optional_struct_a"])
        self._values: typing.Dict[str, typing.Any] = {
            "required_string": required_string,
        }
        if optional_boolean is not None:
            self._values["optional_boolean"] = optional_boolean
        if optional_struct_a is not None:
            self._values["optional_struct_a"] = optional_struct_a

    @builtins.property
    def required_string(self) -> builtins.str:
        result = self._values.get("required_string")
        assert result is not None, "Required property 'required_string' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def optional_boolean(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("optional_boolean")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def optional_struct_a(self) -> typing.Optional[StructA]:
        result = self._values.get("optional_struct_a")
        return typing.cast(typing.Optional[StructA], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StructB(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="jsii-calc.StructParameterType",
    jsii_struct_bases=[],
    name_mapping={"scope": "scope", "props": "props"},
)
class StructParameterType:
    def __init__(
        self,
        *,
        scope: builtins.str,
        props: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Verifies that, in languages that do keyword lifting (e.g: Python), having a struct member with the same name as a positional parameter results in the correct code being emitted.

        See: https://github.com/aws/aws-cdk/issues/4302

        :param scope: 
        :param props: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StructParameterType.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        self._values: typing.Dict[str, typing.Any] = {
            "scope": scope,
        }
        if props is not None:
            self._values["props"] = props

    @builtins.property
    def scope(self) -> builtins.str:
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def props(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("props")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StructParameterType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StructPassing(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.StructPassing"):
    '''Just because we can.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="howManyVarArgsDidIPass")
    @builtins.classmethod
    def how_many_var_args_did_i_pass(
        cls,
        _positional: jsii.Number,
        *inputs: "TopLevelStruct",
    ) -> jsii.Number:
        '''
        :param _positional: -
        :param inputs: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StructPassing.how_many_var_args_did_i_pass)
            check_type(argname="argument _positional", value=_positional, expected_type=type_hints["_positional"])
            check_type(argname="argument inputs", value=inputs, expected_type=typing.Tuple[type_hints["inputs"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(jsii.Number, jsii.sinvoke(cls, "howManyVarArgsDidIPass", [_positional, *inputs]))

    @jsii.member(jsii_name="roundTrip")
    @builtins.classmethod
    def round_trip(
        cls,
        _positional: jsii.Number,
        *,
        required: builtins.str,
        second_level: typing.Union[jsii.Number, typing.Union[SecondLevelStruct, typing.Dict[str, typing.Any]]],
        optional: typing.Optional[builtins.str] = None,
    ) -> "TopLevelStruct":
        '''
        :param _positional: -
        :param required: This is a required field.
        :param second_level: A union to really stress test our serialization.
        :param optional: You don't have to pass this.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StructPassing.round_trip)
            check_type(argname="argument _positional", value=_positional, expected_type=type_hints["_positional"])
        input = TopLevelStruct(
            required=required, second_level=second_level, optional=optional
        )

        return typing.cast("TopLevelStruct", jsii.sinvoke(cls, "roundTrip", [_positional, input]))


class StructUnionConsumer(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.StructUnionConsumer",
):
    @jsii.member(jsii_name="isStructA")
    @builtins.classmethod
    def is_struct_a(
        cls,
        struct: typing.Union[typing.Union[StructA, typing.Dict[str, typing.Any]], typing.Union[StructB, typing.Dict[str, typing.Any]]],
    ) -> builtins.bool:
        '''
        :param struct: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StructUnionConsumer.is_struct_a)
            check_type(argname="argument struct", value=struct, expected_type=type_hints["struct"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isStructA", [struct]))

    @jsii.member(jsii_name="isStructB")
    @builtins.classmethod
    def is_struct_b(
        cls,
        struct: typing.Union[typing.Union[StructA, typing.Dict[str, typing.Any]], typing.Union[StructB, typing.Dict[str, typing.Any]]],
    ) -> builtins.bool:
        '''
        :param struct: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StructUnionConsumer.is_struct_b)
            check_type(argname="argument struct", value=struct, expected_type=type_hints["struct"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isStructB", [struct]))


@jsii.data_type(
    jsii_type="jsii-calc.StructWithEnum",
    jsii_struct_bases=[],
    name_mapping={"foo": "foo", "bar": "bar"},
)
class StructWithEnum:
    def __init__(
        self,
        *,
        foo: StringEnum,
        bar: typing.Optional[AllTypesEnum] = None,
    ) -> None:
        '''
        :param foo: An enum value.
        :param bar: Optional enum value (of type integer). Default: AllTypesEnum.YOUR_ENUM_VALUE
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StructWithEnum.__init__)
            check_type(argname="argument foo", value=foo, expected_type=type_hints["foo"])
            check_type(argname="argument bar", value=bar, expected_type=type_hints["bar"])
        self._values: typing.Dict[str, typing.Any] = {
            "foo": foo,
        }
        if bar is not None:
            self._values["bar"] = bar

    @builtins.property
    def foo(self) -> StringEnum:
        '''An enum value.'''
        result = self._values.get("foo")
        assert result is not None, "Required property 'foo' is missing"
        return typing.cast(StringEnum, result)

    @builtins.property
    def bar(self) -> typing.Optional[AllTypesEnum]:
        '''Optional enum value (of type integer).

        :default: AllTypesEnum.YOUR_ENUM_VALUE
        '''
        result = self._values.get("bar")
        return typing.cast(typing.Optional[AllTypesEnum], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StructWithEnum(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="jsii-calc.StructWithJavaReservedWords",
    jsii_struct_bases=[],
    name_mapping={
        "default": "default",
        "assert_": "assert",
        "result": "result",
        "that": "that",
    },
)
class StructWithJavaReservedWords:
    def __init__(
        self,
        *,
        default: builtins.str,
        assert_: typing.Optional[builtins.str] = None,
        result: typing.Optional[builtins.str] = None,
        that: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param default: 
        :param assert_: 
        :param result: 
        :param that: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StructWithJavaReservedWords.__init__)
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
            check_type(argname="argument assert_", value=assert_, expected_type=type_hints["assert_"])
            check_type(argname="argument result", value=result, expected_type=type_hints["result"])
            check_type(argname="argument that", value=that, expected_type=type_hints["that"])
        self._values: typing.Dict[str, typing.Any] = {
            "default": default,
        }
        if assert_ is not None:
            self._values["assert_"] = assert_
        if result is not None:
            self._values["result"] = result
        if that is not None:
            self._values["that"] = that

    @builtins.property
    def default(self) -> builtins.str:
        result = self._values.get("default")
        assert result is not None, "Required property 'default' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assert_(self) -> typing.Optional[builtins.str]:
        result = self._values.get("assert_")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result(self) -> typing.Optional[builtins.str]:
        result = self._values.get("result")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def that(self) -> typing.Optional[builtins.str]:
        result = self._values.get("that")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StructWithJavaReservedWords(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Sum(
    _CompositeOperation_1c4d123b,
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.Sum",
):
    '''An operation that sums multiple values.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> scope.jsii_calc_lib.NumericValue:
        '''The expression that this operation consists of.

        Must be implemented by derived classes.
        '''
        return typing.cast(scope.jsii_calc_lib.NumericValue, jsii.get(self, "expression"))

    @builtins.property
    @jsii.member(jsii_name="parts")
    def parts(self) -> typing.List[scope.jsii_calc_lib.NumericValue]:
        '''The parts to sum.'''
        return typing.cast(typing.List[scope.jsii_calc_lib.NumericValue], jsii.get(self, "parts"))

    @parts.setter
    def parts(self, value: typing.List[scope.jsii_calc_lib.NumericValue]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Sum, "parts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parts", value)


@jsii.data_type(
    jsii_type="jsii-calc.SupportsNiceJavaBuilderProps",
    jsii_struct_bases=[],
    name_mapping={"bar": "bar", "id": "id"},
)
class SupportsNiceJavaBuilderProps:
    def __init__(
        self,
        *,
        bar: jsii.Number,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bar: Some number, like 42.
        :param id: An ``id`` field here is terrible API design, because the constructor of ``SupportsNiceJavaBuilder`` already has a parameter named ``id``. But here we are, doing it like we didn't care.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SupportsNiceJavaBuilderProps.__init__)
            check_type(argname="argument bar", value=bar, expected_type=type_hints["bar"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "bar": bar,
        }
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def bar(self) -> jsii.Number:
        '''Some number, like 42.'''
        result = self._values.get("bar")
        assert result is not None, "Required property 'bar' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''An ``id`` field here is terrible API design, because the constructor of ``SupportsNiceJavaBuilder`` already has a parameter named ``id``.

        But here we are, doing it like we didn't care.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SupportsNiceJavaBuilderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SupportsNiceJavaBuilderWithRequiredProps(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.SupportsNiceJavaBuilderWithRequiredProps",
):
    '''We can generate fancy builders in Java for classes which take a mix of positional & struct parameters.'''

    def __init__(
        self,
        id_: jsii.Number,
        *,
        bar: jsii.Number,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id_: some identifier of your choice.
        :param bar: Some number, like 42.
        :param id: An ``id`` field here is terrible API design, because the constructor of ``SupportsNiceJavaBuilder`` already has a parameter named ``id``. But here we are, doing it like we didn't care.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SupportsNiceJavaBuilderWithRequiredProps.__init__)
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        props = SupportsNiceJavaBuilderProps(bar=bar, id=id)

        jsii.create(self.__class__, self, [id_, props])

    @builtins.property
    @jsii.member(jsii_name="bar")
    def bar(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bar"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> jsii.Number:
        '''some identifier of your choice.'''
        return typing.cast(jsii.Number, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="propId")
    def prop_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "propId"))


class SyncVirtualMethods(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.SyncVirtualMethods",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="callerIsAsync")
    def caller_is_async(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.ainvoke(self, "callerIsAsync", []))

    @jsii.member(jsii_name="callerIsMethod")
    def caller_is_method(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.invoke(self, "callerIsMethod", []))

    @jsii.member(jsii_name="modifyOtherProperty")
    def modify_other_property(self, value: builtins.str) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyncVirtualMethods.modify_other_property)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "modifyOtherProperty", [value]))

    @jsii.member(jsii_name="modifyValueOfTheProperty")
    def modify_value_of_the_property(self, value: builtins.str) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyncVirtualMethods.modify_value_of_the_property)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "modifyValueOfTheProperty", [value]))

    @jsii.member(jsii_name="readA")
    def read_a(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.invoke(self, "readA", []))

    @jsii.member(jsii_name="retrieveOtherProperty")
    def retrieve_other_property(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "retrieveOtherProperty", []))

    @jsii.member(jsii_name="retrieveReadOnlyProperty")
    def retrieve_read_only_property(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "retrieveReadOnlyProperty", []))

    @jsii.member(jsii_name="retrieveValueOfTheProperty")
    def retrieve_value_of_the_property(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "retrieveValueOfTheProperty", []))

    @jsii.member(jsii_name="virtualMethod")
    def virtual_method(self, n: jsii.Number) -> jsii.Number:
        '''
        :param n: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyncVirtualMethods.virtual_method)
            check_type(argname="argument n", value=n, expected_type=type_hints["n"])
        return typing.cast(jsii.Number, jsii.invoke(self, "virtualMethod", [n]))

    @jsii.member(jsii_name="writeA")
    def write_a(self, value: jsii.Number) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyncVirtualMethods.write_a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "writeA", [value]))

    @builtins.property
    @jsii.member(jsii_name="readonlyProperty")
    def readonly_property(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "readonlyProperty"))

    @builtins.property
    @jsii.member(jsii_name="a")
    def a(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "a"))

    @a.setter
    def a(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyncVirtualMethods, "a").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "a", value)

    @builtins.property
    @jsii.member(jsii_name="callerIsProperty")
    def caller_is_property(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "callerIsProperty"))

    @caller_is_property.setter
    def caller_is_property(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyncVirtualMethods, "caller_is_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "callerIsProperty", value)

    @builtins.property
    @jsii.member(jsii_name="otherProperty")
    def other_property(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "otherProperty"))

    @other_property.setter
    def other_property(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyncVirtualMethods, "other_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "otherProperty", value)

    @builtins.property
    @jsii.member(jsii_name="theProperty")
    def the_property(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "theProperty"))

    @the_property.setter
    def the_property(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyncVirtualMethods, "the_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "theProperty", value)

    @builtins.property
    @jsii.member(jsii_name="valueOfOtherProperty")
    def value_of_other_property(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "valueOfOtherProperty"))

    @value_of_other_property.setter
    def value_of_other_property(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyncVirtualMethods, "value_of_other_property").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "valueOfOtherProperty", value)


class TestStructWithEnum(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.TestStructWithEnum",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="isStringEnumA")
    def is_string_enum_a(
        self,
        *,
        foo: StringEnum,
        bar: typing.Optional[AllTypesEnum] = None,
    ) -> builtins.bool:
        '''Returns true if ``foo`` is ``StringEnum.A``.

        :param foo: An enum value.
        :param bar: Optional enum value (of type integer). Default: AllTypesEnum.YOUR_ENUM_VALUE
        '''
        input = StructWithEnum(foo=foo, bar=bar)

        return typing.cast(builtins.bool, jsii.invoke(self, "isStringEnumA", [input]))

    @jsii.member(jsii_name="isStringEnumB")
    def is_string_enum_b(
        self,
        *,
        foo: StringEnum,
        bar: typing.Optional[AllTypesEnum] = None,
    ) -> builtins.bool:
        '''Returns true if ``foo`` is ``StringEnum.B`` and ``bar`` is ``AllTypesEnum.THIS_IS_GREAT``.

        :param foo: An enum value.
        :param bar: Optional enum value (of type integer). Default: AllTypesEnum.YOUR_ENUM_VALUE
        '''
        input = StructWithEnum(foo=foo, bar=bar)

        return typing.cast(builtins.bool, jsii.invoke(self, "isStringEnumB", [input]))

    @builtins.property
    @jsii.member(jsii_name="structWithFoo")
    def struct_with_foo(self) -> StructWithEnum:
        '''Returns ``foo: StringEnum.A``.'''
        return typing.cast(StructWithEnum, jsii.get(self, "structWithFoo"))

    @builtins.property
    @jsii.member(jsii_name="structWithFooBar")
    def struct_with_foo_bar(self) -> StructWithEnum:
        '''Returns ``foo: StringEnum.C`` and ``bar: AllTypesEnum.MY_ENUM_VALUE``.'''
        return typing.cast(StructWithEnum, jsii.get(self, "structWithFooBar"))


class Thrower(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.Thrower"):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="throwError")
    def throw_error(self) -> None:
        return typing.cast(None, jsii.invoke(self, "throwError", []))


@jsii.data_type(
    jsii_type="jsii-calc.TopLevelStruct",
    jsii_struct_bases=[],
    name_mapping={
        "required": "required",
        "second_level": "secondLevel",
        "optional": "optional",
    },
)
class TopLevelStruct:
    def __init__(
        self,
        *,
        required: builtins.str,
        second_level: typing.Union[jsii.Number, typing.Union[SecondLevelStruct, typing.Dict[str, typing.Any]]],
        optional: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param required: This is a required field.
        :param second_level: A union to really stress test our serialization.
        :param optional: You don't have to pass this.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TopLevelStruct.__init__)
            check_type(argname="argument required", value=required, expected_type=type_hints["required"])
            check_type(argname="argument second_level", value=second_level, expected_type=type_hints["second_level"])
            check_type(argname="argument optional", value=optional, expected_type=type_hints["optional"])
        self._values: typing.Dict[str, typing.Any] = {
            "required": required,
            "second_level": second_level,
        }
        if optional is not None:
            self._values["optional"] = optional

    @builtins.property
    def required(self) -> builtins.str:
        '''This is a required field.'''
        result = self._values.get("required")
        assert result is not None, "Required property 'required' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def second_level(self) -> typing.Union[jsii.Number, SecondLevelStruct]:
        '''A union to really stress test our serialization.'''
        result = self._values.get("second_level")
        assert result is not None, "Required property 'second_level' is missing"
        return typing.cast(typing.Union[jsii.Number, SecondLevelStruct], result)

    @builtins.property
    def optional(self) -> typing.Optional[builtins.str]:
        '''You don't have to pass this.'''
        result = self._values.get("optional")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TopLevelStruct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TwoMethodsWithSimilarCapitalization(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.TwoMethodsWithSimilarCapitalization",
):
    '''In TypeScript it is possible to have two methods with the same name but different capitalization.

    :see: https://github.com/aws/jsii/issues/2508
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="toIsoString")
    def to_iso_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "toIsoString", []))

    @jsii.member(jsii_name="toIsOString")
    def to_is_o_string(self) -> builtins.str:
        '''
        :deprecated: python requires that all alternatives are deprecated

        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "toIsOString", []))

    @builtins.property
    @jsii.member(jsii_name="fooBar")
    def foo_bar(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fooBar"))


class UmaskCheck(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.UmaskCheck"):
    '''Checks the current file permissions are cool (no funky UMASK down-scoping happened).

    :see: https://github.com/aws/jsii/issues/1765
    '''

    @jsii.member(jsii_name="mode")
    @builtins.classmethod
    def mode(cls) -> jsii.Number:
        '''This should return 0o644 (-rw-r--r--).'''
        return typing.cast(jsii.Number, jsii.sinvoke(cls, "mode", []))


class UnaryOperation(
    scope.jsii_calc_lib.Operation,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="jsii-calc.UnaryOperation",
):
    '''An operation on a single operand.'''

    def __init__(self, operand: scope.jsii_calc_lib.NumericValue) -> None:
        '''
        :param operand: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UnaryOperation.__init__)
            check_type(argname="argument operand", value=operand, expected_type=type_hints["operand"])
        jsii.create(self.__class__, self, [operand])

    @builtins.property
    @jsii.member(jsii_name="operand")
    def operand(self) -> scope.jsii_calc_lib.NumericValue:
        return typing.cast(scope.jsii_calc_lib.NumericValue, jsii.get(self, "operand"))


class _UnaryOperationProxy(
    UnaryOperation,
    jsii.proxy_for(scope.jsii_calc_lib.Operation), # type: ignore[misc]
):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, UnaryOperation).__jsii_proxy_class__ = lambda : _UnaryOperationProxy


@jsii.data_type(
    jsii_type="jsii-calc.UnionProperties",
    jsii_struct_bases=[],
    name_mapping={"bar": "bar", "foo": "foo"},
)
class UnionProperties:
    def __init__(
        self,
        *,
        bar: typing.Union[builtins.str, jsii.Number, AllTypes],
        foo: typing.Optional[typing.Union[builtins.str, jsii.Number]] = None,
    ) -> None:
        '''
        :param bar: 
        :param foo: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UnionProperties.__init__)
            check_type(argname="argument bar", value=bar, expected_type=type_hints["bar"])
            check_type(argname="argument foo", value=foo, expected_type=type_hints["foo"])
        self._values: typing.Dict[str, typing.Any] = {
            "bar": bar,
        }
        if foo is not None:
            self._values["foo"] = foo

    @builtins.property
    def bar(self) -> typing.Union[builtins.str, jsii.Number, AllTypes]:
        result = self._values.get("bar")
        assert result is not None, "Required property 'bar' is missing"
        return typing.cast(typing.Union[builtins.str, jsii.Number, AllTypes], result)

    @builtins.property
    def foo(self) -> typing.Optional[typing.Union[builtins.str, jsii.Number]]:
        result = self._values.get("foo")
        return typing.cast(typing.Optional[typing.Union[builtins.str, jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UnionProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(scope.jsii_calc_lib.custom_submodule_name.IReflectable)
class UpcasingReflectable(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.UpcasingReflectable",
):
    '''Ensures submodule-imported types from dependencies can be used correctly.'''

    def __init__(self, delegate: typing.Mapping[builtins.str, typing.Any]) -> None:
        '''
        :param delegate: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UpcasingReflectable.__init__)
            check_type(argname="argument delegate", value=delegate, expected_type=type_hints["delegate"])
        jsii.create(self.__class__, self, [delegate])

    @jsii.python.classproperty
    @jsii.member(jsii_name="reflector")
    def REFLECTOR(cls) -> scope.jsii_calc_lib.custom_submodule_name.Reflector:
        return typing.cast(scope.jsii_calc_lib.custom_submodule_name.Reflector, jsii.sget(cls, "reflector"))

    @builtins.property
    @jsii.member(jsii_name="entries")
    def entries(
        self,
    ) -> typing.List[scope.jsii_calc_lib.custom_submodule_name.ReflectableEntry]:
        return typing.cast(typing.List[scope.jsii_calc_lib.custom_submodule_name.ReflectableEntry], jsii.get(self, "entries"))


class UseBundledDependency(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.UseBundledDependency",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.invoke(self, "value", []))


class UseCalcBase(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.UseCalcBase"):
    '''Depend on a type from jsii-calc-base as a test for awslabs/jsii#128.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="hello")
    def hello(self) -> scope.jsii_calc_base.Base:
        return typing.cast(scope.jsii_calc_base.Base, jsii.invoke(self, "hello", []))


class UsesInterfaceWithProperties(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.UsesInterfaceWithProperties",
):
    def __init__(self, obj: IInterfaceWithProperties) -> None:
        '''
        :param obj: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UsesInterfaceWithProperties.__init__)
            check_type(argname="argument obj", value=obj, expected_type=type_hints["obj"])
        jsii.create(self.__class__, self, [obj])

    @jsii.member(jsii_name="justRead")
    def just_read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "justRead", []))

    @jsii.member(jsii_name="readStringAndNumber")
    def read_string_and_number(
        self,
        ext: IInterfaceWithPropertiesExtension,
    ) -> builtins.str:
        '''
        :param ext: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UsesInterfaceWithProperties.read_string_and_number)
            check_type(argname="argument ext", value=ext, expected_type=type_hints["ext"])
        return typing.cast(builtins.str, jsii.invoke(self, "readStringAndNumber", [ext]))

    @jsii.member(jsii_name="writeAndRead")
    def write_and_read(self, value: builtins.str) -> builtins.str:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(UsesInterfaceWithProperties.write_and_read)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(builtins.str, jsii.invoke(self, "writeAndRead", [value]))

    @builtins.property
    @jsii.member(jsii_name="obj")
    def obj(self) -> IInterfaceWithProperties:
        return typing.cast(IInterfaceWithProperties, jsii.get(self, "obj"))


class VariadicInvoker(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.VariadicInvoker"):
    def __init__(self, method: "VariadicMethod") -> None:
        '''
        :param method: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VariadicInvoker.__init__)
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
        jsii.create(self.__class__, self, [method])

    @jsii.member(jsii_name="asArray")
    def as_array(self, *values: jsii.Number) -> typing.List[jsii.Number]:
        '''
        :param values: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VariadicInvoker.as_array)
            check_type(argname="argument values", value=values, expected_type=typing.Tuple[type_hints["values"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(typing.List[jsii.Number], jsii.invoke(self, "asArray", [*values]))


class VariadicMethod(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.VariadicMethod"):
    def __init__(self, *prefix: jsii.Number) -> None:
        '''
        :param prefix: a prefix that will be use for all values returned by ``#asArray``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VariadicMethod.__init__)
            check_type(argname="argument prefix", value=prefix, expected_type=typing.Tuple[type_hints["prefix"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        jsii.create(self.__class__, self, [*prefix])

    @jsii.member(jsii_name="asArray")
    def as_array(
        self,
        first: jsii.Number,
        *others: jsii.Number,
    ) -> typing.List[jsii.Number]:
        '''
        :param first: the first element of the array to be returned (after the ``prefix`` provided at construction time).
        :param others: other elements to be included in the array.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VariadicMethod.as_array)
            check_type(argname="argument first", value=first, expected_type=type_hints["first"])
            check_type(argname="argument others", value=others, expected_type=typing.Tuple[type_hints["others"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(typing.List[jsii.Number], jsii.invoke(self, "asArray", [first, *others]))


class VirtualMethodPlayground(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.VirtualMethodPlayground",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="overrideMeAsync")
    def override_me_async(self, index: jsii.Number) -> jsii.Number:
        '''
        :param index: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMethodPlayground.override_me_async)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast(jsii.Number, jsii.ainvoke(self, "overrideMeAsync", [index]))

    @jsii.member(jsii_name="overrideMeSync")
    def override_me_sync(self, index: jsii.Number) -> jsii.Number:
        '''
        :param index: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMethodPlayground.override_me_sync)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast(jsii.Number, jsii.invoke(self, "overrideMeSync", [index]))

    @jsii.member(jsii_name="parallelSumAsync")
    def parallel_sum_async(self, count: jsii.Number) -> jsii.Number:
        '''
        :param count: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMethodPlayground.parallel_sum_async)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
        return typing.cast(jsii.Number, jsii.ainvoke(self, "parallelSumAsync", [count]))

    @jsii.member(jsii_name="serialSumAsync")
    def serial_sum_async(self, count: jsii.Number) -> jsii.Number:
        '''
        :param count: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMethodPlayground.serial_sum_async)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
        return typing.cast(jsii.Number, jsii.ainvoke(self, "serialSumAsync", [count]))

    @jsii.member(jsii_name="sumSync")
    def sum_sync(self, count: jsii.Number) -> jsii.Number:
        '''
        :param count: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMethodPlayground.sum_sync)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
        return typing.cast(jsii.Number, jsii.invoke(self, "sumSync", [count]))


class VoidCallback(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="jsii-calc.VoidCallback",
):
    '''This test is used to validate the runtimes can return correctly from a void callback.

    - Implement ``overrideMe`` (method does not have to do anything).
    - Invoke ``callMe``
    - Verify that ``methodWasCalled`` is ``true``.
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="callMe")
    def call_me(self) -> None:
        return typing.cast(None, jsii.invoke(self, "callMe", []))

    @jsii.member(jsii_name="overrideMe")
    @abc.abstractmethod
    def _override_me(self) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="methodWasCalled")
    def method_was_called(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "methodWasCalled"))


class _VoidCallbackProxy(VoidCallback):
    @jsii.member(jsii_name="overrideMe")
    def _override_me(self) -> None:
        return typing.cast(None, jsii.invoke(self, "overrideMe", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, VoidCallback).__jsii_proxy_class__ = lambda : _VoidCallbackProxy


class WithPrivatePropertyInConstructor(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.WithPrivatePropertyInConstructor",
):
    '''Verifies that private property declarations in constructor arguments are hidden.'''

    def __init__(self, private_field: typing.Optional[builtins.str] = None) -> None:
        '''
        :param private_field: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WithPrivatePropertyInConstructor.__init__)
            check_type(argname="argument private_field", value=private_field, expected_type=type_hints["private_field"])
        jsii.create(self.__class__, self, [private_field])

    @builtins.property
    @jsii.member(jsii_name="success")
    def success(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "success"))


@jsii.implements(IInterfaceImplementedByAbstractClass)
class AbstractClass(
    AbstractClassBase,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="jsii-calc.AbstractClass",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="abstractMethod")
    @abc.abstractmethod
    def abstract_method(self, name: builtins.str) -> builtins.str:
        '''
        :param name: -
        '''
        ...

    @jsii.member(jsii_name="nonAbstractMethod")
    def non_abstract_method(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.invoke(self, "nonAbstractMethod", []))

    @builtins.property
    @jsii.member(jsii_name="propFromInterface")
    def prop_from_interface(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "propFromInterface"))


class _AbstractClassProxy(
    AbstractClass,
    jsii.proxy_for(AbstractClassBase), # type: ignore[misc]
):
    @jsii.member(jsii_name="abstractMethod")
    def abstract_method(self, name: builtins.str) -> builtins.str:
        '''
        :param name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AbstractClass.abstract_method)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        return typing.cast(builtins.str, jsii.invoke(self, "abstractMethod", [name]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, AbstractClass).__jsii_proxy_class__ = lambda : _AbstractClassProxy


class Add(BinaryOperation, metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.Add"):
    '''The "+" binary operation.'''

    def __init__(
        self,
        lhs: scope.jsii_calc_lib.NumericValue,
        rhs: scope.jsii_calc_lib.NumericValue,
    ) -> None:
        '''Creates a BinaryOperation.

        :param lhs: Left-hand side operand.
        :param rhs: Right-hand side operand.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Add.__init__)
            check_type(argname="argument lhs", value=lhs, expected_type=type_hints["lhs"])
            check_type(argname="argument rhs", value=rhs, expected_type=type_hints["rhs"])
        jsii.create(self.__class__, self, [lhs, rhs])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''String representation of the value.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        '''The value.'''
        return typing.cast(jsii.Number, jsii.get(self, "value"))


@jsii.implements(IAnonymousImplementationProvider)
class AnonymousImplementationProvider(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.AnonymousImplementationProvider",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="provideAsClass")
    def provide_as_class(self) -> Implementation:
        return typing.cast(Implementation, jsii.invoke(self, "provideAsClass", []))

    @jsii.member(jsii_name="provideAsInterface")
    def provide_as_interface(self) -> IAnonymouslyImplementMe:
        return typing.cast(IAnonymouslyImplementMe, jsii.invoke(self, "provideAsInterface", []))


@jsii.implements(IBell)
class Bell(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.Bell"):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="ring")
    def ring(self) -> None:
        return typing.cast(None, jsii.invoke(self, "ring", []))

    @builtins.property
    @jsii.member(jsii_name="rung")
    def rung(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "rung"))

    @rung.setter
    def rung(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Bell, "rung").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rung", value)


@jsii.data_type(
    jsii_type="jsii-calc.ChildStruct982",
    jsii_struct_bases=[ParentStruct982],
    name_mapping={"foo": "foo", "bar": "bar"},
)
class ChildStruct982(ParentStruct982):
    def __init__(self, *, foo: builtins.str, bar: jsii.Number) -> None:
        '''
        :param foo: 
        :param bar: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ChildStruct982.__init__)
            check_type(argname="argument foo", value=foo, expected_type=type_hints["foo"])
            check_type(argname="argument bar", value=bar, expected_type=type_hints["bar"])
        self._values: typing.Dict[str, typing.Any] = {
            "foo": foo,
            "bar": bar,
        }

    @builtins.property
    def foo(self) -> builtins.str:
        result = self._values.get("foo")
        assert result is not None, "Required property 'foo' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bar(self) -> jsii.Number:
        result = self._values.get("bar")
        assert result is not None, "Required property 'bar' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChildStruct982(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(INonInternalInterface)
class ClassThatImplementsTheInternalInterface(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.ClassThatImplementsTheInternalInterface",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @builtins.property
    @jsii.member(jsii_name="a")
    def a(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "a"))

    @a.setter
    def a(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClassThatImplementsTheInternalInterface, "a").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "a", value)

    @builtins.property
    @jsii.member(jsii_name="b")
    def b(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "b"))

    @b.setter
    def b(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClassThatImplementsTheInternalInterface, "b").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "b", value)

    @builtins.property
    @jsii.member(jsii_name="c")
    def c(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "c"))

    @c.setter
    def c(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClassThatImplementsTheInternalInterface, "c").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "c", value)

    @builtins.property
    @jsii.member(jsii_name="d")
    def d(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "d"))

    @d.setter
    def d(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClassThatImplementsTheInternalInterface, "d").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "d", value)


@jsii.implements(INonInternalInterface)
class ClassThatImplementsThePrivateInterface(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.ClassThatImplementsThePrivateInterface",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @builtins.property
    @jsii.member(jsii_name="a")
    def a(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "a"))

    @a.setter
    def a(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClassThatImplementsThePrivateInterface, "a").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "a", value)

    @builtins.property
    @jsii.member(jsii_name="b")
    def b(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "b"))

    @b.setter
    def b(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClassThatImplementsThePrivateInterface, "b").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "b", value)

    @builtins.property
    @jsii.member(jsii_name="c")
    def c(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "c"))

    @c.setter
    def c(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClassThatImplementsThePrivateInterface, "c").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "c", value)

    @builtins.property
    @jsii.member(jsii_name="e")
    def e(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "e"))

    @e.setter
    def e(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClassThatImplementsThePrivateInterface, "e").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "e", value)


@jsii.implements(IInterfaceWithProperties)
class ClassWithPrivateConstructorAndAutomaticProperties(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.ClassWithPrivateConstructorAndAutomaticProperties",
):
    '''Class that implements interface properties automatically, but using a private constructor.'''

    @jsii.member(jsii_name="create")
    @builtins.classmethod
    def create(
        cls,
        read_only_string: builtins.str,
        read_write_string: builtins.str,
    ) -> "ClassWithPrivateConstructorAndAutomaticProperties":
        '''
        :param read_only_string: -
        :param read_write_string: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ClassWithPrivateConstructorAndAutomaticProperties.create)
            check_type(argname="argument read_only_string", value=read_only_string, expected_type=type_hints["read_only_string"])
            check_type(argname="argument read_write_string", value=read_write_string, expected_type=type_hints["read_write_string"])
        return typing.cast("ClassWithPrivateConstructorAndAutomaticProperties", jsii.sinvoke(cls, "create", [read_only_string, read_write_string]))

    @builtins.property
    @jsii.member(jsii_name="readOnlyString")
    def read_only_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "readOnlyString"))

    @builtins.property
    @jsii.member(jsii_name="readWriteString")
    def read_write_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "readWriteString"))

    @read_write_string.setter
    def read_write_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ClassWithPrivateConstructorAndAutomaticProperties, "read_write_string").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readWriteString", value)


@jsii.implements(IIndirectlyImplemented)
class FullCombo(BaseClass, metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.FullCombo"):
    pass


@jsii.interface(jsii_type="jsii-calc.IFriendlyRandomGenerator")
class IFriendlyRandomGenerator(
    IRandomNumberGenerator,
    scope.jsii_calc_lib.IFriendly,
    typing_extensions.Protocol,
):
    pass


class _IFriendlyRandomGeneratorProxy(
    jsii.proxy_for(IRandomNumberGenerator), # type: ignore[misc]
    jsii.proxy_for(scope.jsii_calc_lib.IFriendly), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IFriendlyRandomGenerator"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFriendlyRandomGenerator).__jsii_proxy_class__ = lambda : _IFriendlyRandomGeneratorProxy


@jsii.interface(jsii_type="jsii-calc.IInterfaceThatShouldNotBeADataType")
class IInterfaceThatShouldNotBeADataType(
    IInterfaceWithMethods,
    typing_extensions.Protocol,
):
    '''Even though this interface has only properties, it is disqualified from being a datatype because it inherits from an interface that is not a datatype.'''

    @builtins.property
    @jsii.member(jsii_name="otherValue")
    def other_value(self) -> builtins.str:
        ...


class _IInterfaceThatShouldNotBeADataTypeProxy(
    jsii.proxy_for(IInterfaceWithMethods), # type: ignore[misc]
):
    '''Even though this interface has only properties, it is disqualified from being a datatype because it inherits from an interface that is not a datatype.'''

    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IInterfaceThatShouldNotBeADataType"

    @builtins.property
    @jsii.member(jsii_name="otherValue")
    def other_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "otherValue"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInterfaceThatShouldNotBeADataType).__jsii_proxy_class__ = lambda : _IInterfaceThatShouldNotBeADataTypeProxy


@jsii.interface(jsii_type="jsii-calc.IJSII417Derived")
class IJSII417Derived(IJSII417PublicBaseOfBase, typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="property")
    def property(self) -> builtins.str:
        ...

    @jsii.member(jsii_name="bar")
    def bar(self) -> None:
        ...

    @jsii.member(jsii_name="baz")
    def baz(self) -> None:
        ...


class _IJSII417DerivedProxy(
    jsii.proxy_for(IJSII417PublicBaseOfBase), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.IJSII417Derived"

    @builtins.property
    @jsii.member(jsii_name="property")
    def property(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "property"))

    @jsii.member(jsii_name="bar")
    def bar(self) -> None:
        return typing.cast(None, jsii.invoke(self, "bar", []))

    @jsii.member(jsii_name="baz")
    def baz(self) -> None:
        return typing.cast(None, jsii.invoke(self, "baz", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IJSII417Derived).__jsii_proxy_class__ = lambda : _IJSII417DerivedProxy


@jsii.implements(IPublicInterface2)
class InbetweenClass(
    PublicClass,
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.InbetweenClass",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="ciao")
    def ciao(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "ciao", []))


class JSII417Derived(
    JSII417PublicBaseOfBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.JSII417Derived",
):
    def __init__(self, property: builtins.str) -> None:
        '''
        :param property: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(JSII417Derived.__init__)
            check_type(argname="argument property", value=property, expected_type=type_hints["property"])
        jsii.create(self.__class__, self, [property])

    @jsii.member(jsii_name="bar")
    def bar(self) -> None:
        return typing.cast(None, jsii.invoke(self, "bar", []))

    @jsii.member(jsii_name="baz")
    def baz(self) -> None:
        return typing.cast(None, jsii.invoke(self, "baz", []))

    @builtins.property
    @jsii.member(jsii_name="property")
    def _property(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "property"))


@jsii.implements(IFriendlier)
class Negate(UnaryOperation, metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.Negate"):
    '''The negation operation ("-value").'''

    def __init__(self, operand: scope.jsii_calc_lib.NumericValue) -> None:
        '''
        :param operand: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Negate.__init__)
            check_type(argname="argument operand", value=operand, expected_type=type_hints["operand"])
        jsii.create(self.__class__, self, [operand])

    @jsii.member(jsii_name="farewell")
    def farewell(self) -> builtins.str:
        '''Say farewell.'''
        return typing.cast(builtins.str, jsii.invoke(self, "farewell", []))

    @jsii.member(jsii_name="goodbye")
    def goodbye(self) -> builtins.str:
        '''Say goodbye.'''
        return typing.cast(builtins.str, jsii.invoke(self, "goodbye", []))

    @jsii.member(jsii_name="hello")
    def hello(self) -> builtins.str:
        '''Say hello!'''
        return typing.cast(builtins.str, jsii.invoke(self, "hello", []))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''String representation of the value.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        '''The value.'''
        return typing.cast(jsii.Number, jsii.get(self, "value"))


class StaticHelloChild(
    StaticHelloParent,
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.StaticHelloChild",
):
    @jsii.member(jsii_name="method")
    @builtins.classmethod
    def method(cls) -> None:
        return typing.cast(None, jsii.sinvoke(cls, "method", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="property")
    def property(cls) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.sget(cls, "property"))


class SupportsNiceJavaBuilder(
    SupportsNiceJavaBuilderWithRequiredProps,
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.SupportsNiceJavaBuilder",
):
    def __init__(
        self,
        id: jsii.Number,
        default_bar: typing.Optional[jsii.Number] = None,
        props: typing.Optional[typing.Union[SupportsNiceJavaBuilderProps, typing.Dict[str, typing.Any]]] = None,
        *rest: builtins.str,
    ) -> None:
        '''
        :param id: some identifier.
        :param default_bar: the default value of ``bar``.
        :param props: some props once can provide.
        :param rest: a variadic continuation.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SupportsNiceJavaBuilder.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument default_bar", value=default_bar, expected_type=type_hints["default_bar"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
            check_type(argname="argument rest", value=rest, expected_type=typing.Tuple[type_hints["rest"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        jsii.create(self.__class__, self, [id, default_bar, props, *rest])

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> jsii.Number:
        '''some identifier.'''
        return typing.cast(jsii.Number, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="rest")
    def rest(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rest"))


@jsii.implements(IFriendlyRandomGenerator)
class DoubleTrouble(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.DoubleTrouble"):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="hello")
    def hello(self) -> builtins.str:
        '''Say hello!'''
        return typing.cast(builtins.str, jsii.invoke(self, "hello", []))

    @jsii.member(jsii_name="next")
    def next(self) -> jsii.Number:
        '''Returns another random number.'''
        return typing.cast(jsii.Number, jsii.invoke(self, "next", []))


__all__ = [
    "AbstractClass",
    "AbstractClassBase",
    "AbstractClassReturner",
    "AbstractSuite",
    "Add",
    "AllTypes",
    "AllTypesEnum",
    "AllowedMethodNames",
    "AmbiguousParameters",
    "AnonymousImplementationProvider",
    "AsyncVirtualMethods",
    "AugmentableClass",
    "BaseClass",
    "BaseJsii976",
    "Bell",
    "BinaryOperation",
    "BurriedAnonymousObject",
    "Calculator",
    "CalculatorProps",
    "ChildStruct982",
    "ClassThatImplementsTheInternalInterface",
    "ClassThatImplementsThePrivateInterface",
    "ClassWithCollections",
    "ClassWithContainerTypes",
    "ClassWithDocs",
    "ClassWithJavaReservedWords",
    "ClassWithMutableObjectLiteralProperty",
    "ClassWithPrivateConstructorAndAutomaticProperties",
    "ConfusingToJackson",
    "ConfusingToJacksonStruct",
    "ConstructorPassesThisOut",
    "Constructors",
    "ConsumePureInterface",
    "ConsumerCanRingBell",
    "ConsumersOfThisCrazyTypeSystem",
    "ContainerProps",
    "DataRenderer",
    "Default",
    "DefaultedConstructorArgument",
    "Demonstrate982",
    "DeprecatedClass",
    "DeprecatedEnum",
    "DeprecatedStruct",
    "DerivedStruct",
    "DiamondBottom",
    "DiamondInheritanceBaseLevelStruct",
    "DiamondInheritanceFirstMidLevelStruct",
    "DiamondInheritanceSecondMidLevelStruct",
    "DiamondInheritanceTopLevelStruct",
    "DisappointingCollectionSource",
    "DoNotOverridePrivates",
    "DoNotRecognizeAnyAsOptional",
    "DocumentedClass",
    "DontComplainAboutVariadicAfterOptional",
    "DoubleTrouble",
    "DummyObj",
    "DynamicPropertyBearer",
    "DynamicPropertyBearerChild",
    "Entropy",
    "EnumDispenser",
    "EraseUndefinedHashValues",
    "EraseUndefinedHashValuesOptions",
    "ExperimentalClass",
    "ExperimentalEnum",
    "ExperimentalStruct",
    "ExportedBaseClass",
    "ExtendsInternalInterface",
    "ExternalClass",
    "ExternalEnum",
    "ExternalStruct",
    "FullCombo",
    "GiveMeStructs",
    "Greetee",
    "GreetingAugmenter",
    "IAnonymousImplementationProvider",
    "IAnonymouslyImplementMe",
    "IAnotherPublicInterface",
    "IBell",
    "IBellRinger",
    "IConcreteBellRinger",
    "IDeprecatedInterface",
    "IExperimentalInterface",
    "IExtendsPrivateInterface",
    "IExternalInterface",
    "IFriendlier",
    "IFriendlyRandomGenerator",
    "IIndirectlyImplemented",
    "IInterfaceImplementedByAbstractClass",
    "IInterfaceThatShouldNotBeADataType",
    "IInterfaceWithInternal",
    "IInterfaceWithMethods",
    "IInterfaceWithOptionalMethodArguments",
    "IInterfaceWithProperties",
    "IInterfaceWithPropertiesExtension",
    "IJSII417Derived",
    "IJSII417PublicBaseOfBase",
    "IJavaReservedWordsInAnInterface",
    "IJsii487External",
    "IJsii487External2",
    "IJsii496",
    "IMutableObjectLiteral",
    "INonInternalInterface",
    "IObjectWithProperty",
    "IOptionalMethod",
    "IPrivatelyImplemented",
    "IPublicInterface",
    "IPublicInterface2",
    "IRandomNumberGenerator",
    "IReturnJsii976",
    "IReturnsNumber",
    "IStableInterface",
    "IStructReturningDelegate",
    "IWallClock",
    "ImplementInternalInterface",
    "Implementation",
    "ImplementsInterfaceWithInternal",
    "ImplementsInterfaceWithInternalSubclass",
    "ImplementsPrivateInterface",
    "ImplictBaseOfBase",
    "InbetweenClass",
    "InterfaceCollections",
    "InterfacesMaker",
    "Isomorphism",
    "Issue2638",
    "Issue2638B",
    "JSII417Derived",
    "JSII417PublicBaseOfBase",
    "JSObjectLiteralForInterface",
    "JSObjectLiteralToNative",
    "JSObjectLiteralToNativeClass",
    "JavaReservedWords",
    "Jsii487Derived",
    "Jsii496Derived",
    "JsiiAgent",
    "JsonFormatter",
    "LevelOne",
    "LevelOneProps",
    "LoadBalancedFargateServiceProps",
    "MethodNamedProperty",
    "Multiply",
    "Negate",
    "NestedClassInstance",
    "NestedStruct",
    "NodeStandardLibrary",
    "NullShouldBeTreatedAsUndefined",
    "NullShouldBeTreatedAsUndefinedData",
    "NumberGenerator",
    "ObjectRefsInCollections",
    "ObjectWithPropertyProvider",
    "Old",
    "OptionalArgumentInvoker",
    "OptionalConstructorArgument",
    "OptionalStruct",
    "OptionalStructConsumer",
    "OverridableProtectedMember",
    "OverrideReturnsObject",
    "ParentStruct982",
    "PartiallyInitializedThisConsumer",
    "Polymorphism",
    "Power",
    "PropertyNamedProperty",
    "PublicClass",
    "PythonReservedWords",
    "ReferenceEnumFromScopedPackage",
    "ReturnsPrivateImplementationOfInterface",
    "RootStruct",
    "RootStructValidator",
    "RuntimeTypeChecking",
    "SecondLevelStruct",
    "SingleInstanceTwoTypes",
    "SingletonInt",
    "SingletonIntEnum",
    "SingletonString",
    "SingletonStringEnum",
    "SmellyStruct",
    "SomeTypeJsii976",
    "StableClass",
    "StableEnum",
    "StableStruct",
    "StaticContext",
    "StaticHelloChild",
    "StaticHelloParent",
    "Statics",
    "StringEnum",
    "StripInternal",
    "StructA",
    "StructB",
    "StructParameterType",
    "StructPassing",
    "StructUnionConsumer",
    "StructWithEnum",
    "StructWithJavaReservedWords",
    "Sum",
    "SupportsNiceJavaBuilder",
    "SupportsNiceJavaBuilderProps",
    "SupportsNiceJavaBuilderWithRequiredProps",
    "SyncVirtualMethods",
    "TestStructWithEnum",
    "Thrower",
    "TopLevelStruct",
    "TwoMethodsWithSimilarCapitalization",
    "UmaskCheck",
    "UnaryOperation",
    "UnionProperties",
    "UpcasingReflectable",
    "UseBundledDependency",
    "UseCalcBase",
    "UsesInterfaceWithProperties",
    "VariadicInvoker",
    "VariadicMethod",
    "VirtualMethodPlayground",
    "VoidCallback",
    "WithPrivatePropertyInConstructor",
    "cdk16625",
    "composition",
    "derived_class_has_no_properties",
    "interface_in_namespace_includes_classes",
    "interface_in_namespace_only_interface",
    "jsii3656",
    "module2530",
    "module2617",
    "module2647",
    "module2689",
    "module2692",
    "module2700",
    "module2702",
    "nodirect",
    "onlystatic",
    "python_self",
    "submodule",
]

publication.publish()

# Loading modules to ensure their types are registered with the jsii runtime library
from . import cdk16625
from . import composition
from . import derived_class_has_no_properties
from . import interface_in_namespace_includes_classes
from . import interface_in_namespace_only_interface
from . import jsii3656
from . import module2530
from . import module2617
from . import module2647
from . import module2689
from . import module2692
from . import module2700
from . import module2702
from . import nodirect
from . import onlystatic
from . import python_self
from . import submodule
