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

import scope.jsii_calc_base_of_base


class Base(metaclass=jsii.JSIIAbstractClass, jsii_type="@scope/jsii-calc-base.Base"):
    '''A base class.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="typeName")
    def type_name(self) -> typing.Any:
        '''
        :return: the name of the class (to verify native type names are created for derived classes).
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "typeName", []))


class _BaseProxy(Base):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Base).__jsii_proxy_class__ = lambda : _BaseProxy


@jsii.data_type(
    jsii_type="@scope/jsii-calc-base.BaseProps",
    jsii_struct_bases=[scope.jsii_calc_base_of_base.VeryBaseProps],
    name_mapping={"foo": "foo", "bar": "bar"},
)
class BaseProps(scope.jsii_calc_base_of_base.VeryBaseProps):
    def __init__(
        self,
        *,
        foo: scope.jsii_calc_base_of_base.Very,
        bar: builtins.str,
    ) -> None:
        '''
        :param foo: -
        :param bar: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BaseProps.__init__)
            check_type(argname="argument foo", value=foo, expected_type=type_hints["foo"])
            check_type(argname="argument bar", value=bar, expected_type=type_hints["bar"])
        self._values: typing.Dict[str, typing.Any] = {
            "foo": foo,
            "bar": bar,
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

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@scope/jsii-calc-base.IBaseInterface")
class IBaseInterface(
    scope.jsii_calc_base_of_base.IVeryBaseInterface,
    typing_extensions.Protocol,
):
    @jsii.member(jsii_name="bar")
    def bar(self) -> None:
        ...


class _IBaseInterfaceProxy(
    jsii.proxy_for(scope.jsii_calc_base_of_base.IVeryBaseInterface), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "@scope/jsii-calc-base.IBaseInterface"

    @jsii.member(jsii_name="bar")
    def bar(self) -> None:
        return typing.cast(None, jsii.invoke(self, "bar", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBaseInterface).__jsii_proxy_class__ = lambda : _IBaseInterfaceProxy


class StaticConsumer(
    metaclass=jsii.JSIIMeta,
    jsii_type="@scope/jsii-calc-base.StaticConsumer",
):
    '''Hides the transitive dependency of base-of-base.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="consume")
    @builtins.classmethod
    def consume(cls, *args: typing.Any) -> None:
        '''
        :param args: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StaticConsumer.consume)
            check_type(argname="argument args", value=args, expected_type=typing.Tuple[type_hints["args"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.sinvoke(cls, "consume", [*args]))


__all__ = [
    "Base",
    "BaseProps",
    "IBaseInterface",
    "StaticConsumer",
]

publication.publish()
