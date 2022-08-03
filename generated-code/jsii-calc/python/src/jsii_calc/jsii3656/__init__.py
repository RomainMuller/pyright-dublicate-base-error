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


@jsii.data_type(
    jsii_type="jsii-calc.jsii3656.ImplementMeOpts",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "count": "count"},
)
class ImplementMeOpts:
    def __init__(
        self,
        *,
        name: builtins.str,
        count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: 
        :param count: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ImplementMeOpts.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if count is not None:
            self._values["count"] = count

    @builtins.property
    def name(self) -> builtins.str:
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImplementMeOpts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OverrideMe(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="jsii-calc.jsii3656.OverrideMe",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="callAbstract")
    @builtins.classmethod
    def call_abstract(cls, receiver: "OverrideMe") -> builtins.bool:
        '''
        :param receiver: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OverrideMe.call_abstract)
            check_type(argname="argument receiver", value=receiver, expected_type=type_hints["receiver"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "callAbstract", [receiver]))

    @jsii.member(jsii_name="implementMe")
    @abc.abstractmethod
    def implement_me(
        self,
        *,
        name: builtins.str,
        count: typing.Optional[jsii.Number] = None,
    ) -> builtins.bool:
        '''
        :param name: 
        :param count: 
        '''
        ...


class _OverrideMeProxy(OverrideMe):
    @jsii.member(jsii_name="implementMe")
    def implement_me(
        self,
        *,
        name: builtins.str,
        count: typing.Optional[jsii.Number] = None,
    ) -> builtins.bool:
        '''
        :param name: 
        :param count: 
        '''
        opts = ImplementMeOpts(name=name, count=count)

        return typing.cast(builtins.bool, jsii.invoke(self, "implementMe", [opts]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, OverrideMe).__jsii_proxy_class__ = lambda : _OverrideMeProxy


__all__ = [
    "ImplementMeOpts",
    "OverrideMe",
]

publication.publish()
