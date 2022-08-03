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

import scope.jsii_calc_lib


class CompositeOperation(
    scope.jsii_calc_lib.Operation,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="jsii-calc.composition.CompositeOperation",
):
    '''Abstract operation composed from an expression of other operations.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''String representation of the value.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @builtins.property
    @jsii.member(jsii_name="expression")
    @abc.abstractmethod
    def expression(self) -> scope.jsii_calc_lib.NumericValue:
        '''The expression that this operation consists of.

        Must be implemented by derived classes.
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        '''The value.'''
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="decorationPostfixes")
    def decoration_postfixes(self) -> typing.List[builtins.str]:
        '''A set of postfixes to include in a decorated .toString().'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "decorationPostfixes"))

    @decoration_postfixes.setter
    def decoration_postfixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CompositeOperation, "decoration_postfixes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "decorationPostfixes", value)

    @builtins.property
    @jsii.member(jsii_name="decorationPrefixes")
    def decoration_prefixes(self) -> typing.List[builtins.str]:
        '''A set of prefixes to include in a decorated .toString().'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "decorationPrefixes"))

    @decoration_prefixes.setter
    def decoration_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CompositeOperation, "decoration_prefixes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "decorationPrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="stringStyle")
    def string_style(self) -> "CompositeOperation.CompositionStringStyle":
        '''The .toString() style.'''
        return typing.cast("CompositeOperation.CompositionStringStyle", jsii.get(self, "stringStyle"))

    @string_style.setter
    def string_style(self, value: "CompositeOperation.CompositionStringStyle") -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CompositeOperation, "string_style").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stringStyle", value)

    @jsii.enum(
        jsii_type="jsii-calc.composition.CompositeOperation.CompositionStringStyle"
    )
    class CompositionStringStyle(enum.Enum):
        '''Style of .toString() output for CompositeOperation.'''

        NORMAL = "NORMAL"
        '''Normal string expression.'''
        DECORATED = "DECORATED"
        '''Decorated string expression.'''


class _CompositeOperationProxy(
    CompositeOperation,
    jsii.proxy_for(scope.jsii_calc_lib.Operation), # type: ignore[misc]
):
    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> scope.jsii_calc_lib.NumericValue:
        '''The expression that this operation consists of.

        Must be implemented by derived classes.
        '''
        return typing.cast(scope.jsii_calc_lib.NumericValue, jsii.get(self, "expression"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, CompositeOperation).__jsii_proxy_class__ = lambda : _CompositeOperationProxy


__all__ = [
    "CompositeOperation",
]

publication.publish()
