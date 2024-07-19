import inspect
from typing import get_type_hints

from src._validators import (
    HasTheMethod,
    IsAClass,
    IsAMethod,
    IsAProtocol,
    MethodSignatureIsEqual,
    MethodTypeHintAreEqual,
)


def implements(*interfaces):
    __methods_to_ignore = ("__init__", "__subclasshook__")

    def decorator(cls):
        for interface in interfaces:
            IsAClass.is_satisfied_by(cls)
            IsAProtocol.is_satisfied_by(interface)

            interface_methods = inspect.getmembers(interface, predicate=inspect.isfunction)

            for method_name, interface_method in interface_methods:
                if method_name in __methods_to_ignore:
                    continue

                HasTheMethod.is_satisfied_by(method_name, cls)

                cls_method = getattr(cls, method_name)

                IsAMethod.is_satisfied_by(cls)

                # Check method signature
                interface_method_signature = inspect.signature(interface_method)
                class_method_signature = inspect.signature(cls_method)

                MethodSignatureIsEqual.is_satisfied_by(
                    interface_method_signature,
                    class_method_signature,
                    cls.__name__,
                    method_name,
                )

                # Check method type hints
                interface_method_type_hints = get_type_hints(interface_method)
                cls_method_type_hints = get_type_hints(cls_method)

                MethodTypeHintAreEqual.is_satisfied_by(
                    interface_method_type_hints,
                    cls_method_type_hints,
                    class_name=cls.__name__,
                    method_name=method_name,
                )

        return cls

    return decorator
