import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ...._jsii import *


@jsii.interface(
    jsii_type="jsii-calc.submodule.nested_submodule.deeplyNested.INamespaced"
)
class INamespaced(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="definedAt")
    def defined_at(self) -> builtins.str:
        ...


class _INamespacedProxy:
    __jsii_type__: typing.ClassVar[str] = "jsii-calc.submodule.nested_submodule.deeplyNested.INamespaced"

    @builtins.property
    @jsii.member(jsii_name="definedAt")
    def defined_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "definedAt"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INamespaced).__jsii_proxy_class__ = lambda : _INamespacedProxy


__all__ = [
    "INamespaced",
]

publication.publish()
