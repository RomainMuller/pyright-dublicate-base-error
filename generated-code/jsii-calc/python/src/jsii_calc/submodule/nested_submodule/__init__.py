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

from ..child import Goodness as _Goodness_2df26737
from .deeply_nested import INamespaced as _INamespaced_e2f386ad


@jsii.implements(_INamespaced_e2f386ad)
class Namespaced(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="jsii-calc.submodule.nested_submodule.Namespaced",
):
    @builtins.property
    @jsii.member(jsii_name="definedAt")
    def defined_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "definedAt"))

    @builtins.property
    @jsii.member(jsii_name="goodness")
    @abc.abstractmethod
    def goodness(self) -> _Goodness_2df26737:
        ...


class _NamespacedProxy(Namespaced):
    @builtins.property
    @jsii.member(jsii_name="goodness")
    def goodness(self) -> _Goodness_2df26737:
        return typing.cast(_Goodness_2df26737, jsii.get(self, "goodness"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Namespaced).__jsii_proxy_class__ = lambda : _NamespacedProxy


__all__ = [
    "Namespaced",
    "deeply_nested",
]

publication.publish()

# Loading modules to ensure their types are registered with the jsii runtime library
from . import deeply_nested
