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

from .. import IRandomNumberGenerator as _IRandomNumberGenerator_9643a8b9


class Cdk16625(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="jsii-calc.cdk16625.Cdk16625",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="test")
    def test(self) -> None:
        '''Run this function to verify that everything is working as it should.'''
        return typing.cast(None, jsii.invoke(self, "test", []))

    @jsii.member(jsii_name="unwrap")
    @abc.abstractmethod
    def _unwrap(self, gen: _IRandomNumberGenerator_9643a8b9) -> jsii.Number:
        '''Implement this functin to return ``gen.next()``. It is extremely important that the ``donotimport`` submodule is NEVER explicitly loaded in the testing application (otherwise this test is void).

        :param gen: a VERY pseudo random number generator.
        '''
        ...


class _Cdk16625Proxy(Cdk16625):
    @jsii.member(jsii_name="unwrap")
    def _unwrap(self, gen: _IRandomNumberGenerator_9643a8b9) -> jsii.Number:
        '''Implement this functin to return ``gen.next()``. It is extremely important that the ``donotimport`` submodule is NEVER explicitly loaded in the testing application (otherwise this test is void).

        :param gen: a VERY pseudo random number generator.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Cdk16625._unwrap)
            check_type(argname="argument gen", value=gen, expected_type=type_hints["gen"])
        return typing.cast(jsii.Number, jsii.invoke(self, "unwrap", [gen]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Cdk16625).__jsii_proxy_class__ = lambda : _Cdk16625Proxy


__all__ = [
    "Cdk16625",
    "donotimport",
]

publication.publish()

# Loading modules to ensure their types are registered with the jsii runtime library
from . import donotimport
