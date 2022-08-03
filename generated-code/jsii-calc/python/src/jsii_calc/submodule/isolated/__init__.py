'''
# Read you, read me

This is the readme of the `jsii-calc.submodule.isolated` module.
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

from ..._jsii import *

from ..child import (
    KwargsProps as _KwargsProps_c7855dcf, SomeEnum as _SomeEnum_b2e41d92
)


class Kwargs(metaclass=jsii.JSIIMeta, jsii_type="jsii-calc.submodule.isolated.Kwargs"):
    '''Ensures imports are correctly registered for kwargs lifted properties from super-structs.'''

    @jsii.member(jsii_name="method")
    @builtins.classmethod
    def method(
        cls,
        *,
        extra: typing.Optional[builtins.str] = None,
        prop: _SomeEnum_b2e41d92,
    ) -> builtins.bool:
        '''
        :param extra: 
        :param prop: 
        '''
        props = _KwargsProps_c7855dcf(extra=extra, prop=prop)

        return typing.cast(builtins.bool, jsii.sinvoke(cls, "method", [props]))


__all__ = [
    "Kwargs",
]

publication.publish()
