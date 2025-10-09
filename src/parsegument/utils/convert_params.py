import typing
import inspect
from ..Arguments import Argument, Flag, Operand

def convert_params(params: typing.OrderedDict):
    pass

def convert_param(param:inspect.Parameter):
    name = param.name
    param_type = param.annotation
    default = param.default
    if default == inspect.Parameter.empty:
        pass

