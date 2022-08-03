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


class OnlyStaticMethods(
    metaclass=jsii.JSIIMeta,
    jsii_type="jsii-calc.onlystatic.OnlyStaticMethods",
):
    '''Test for https://github.com/aws/jsii/issues/2617.'''

    @jsii.member(jsii_name="staticMethod")
    @builtins.classmethod
    def static_method(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sinvoke(cls, "staticMethod", []))


__all__ = [
    "OnlyStaticMethods",
]

publication.publish()
