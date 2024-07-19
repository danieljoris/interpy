from typing import Protocol, Union
from src.errors import (
    InterfaceMethodError,
    InvalidDecoratorUsageError,
    MethodNotCallableError,
    MethodSignatureMismatchError,
    NotAnInterfaceError,
)
import inspect


class IsAProtocol:
    @classmethod
    def is_satisfied_by(cls, candidate) -> Union[bool, None]:

        if not inspect.isclass(candidate):
            raise NotAnInterfaceError(candidate)
        elif not issubclass(candidate, Protocol):
            raise NotAnInterfaceError(candidate)

        return True


class MethodSignatureIsEqual:
    @classmethod
    def is_satisfied_by(
        cls,
        interface_method_signature: inspect.Signature,
        class_method_signature: inspect.Signature,
        class_name: str,
        method_name: str,
    ) -> None:
        if not interface_method_signature == class_method_signature:
            raise MethodSignatureMismatchError(
                method_name, class_name, interface_method_signature, class_method_signature
            )


class MethodTypeHintAreEqual:
    @classmethod
    def is_satisfied_by(
        cls,
        interface_method_type_hints,
        class_method_type_hints,
        class_name: str,
        method_name: str,
    ):
        if interface_method_type_hints != class_method_type_hints:
            raise TypeError(
                f"Type hints mismatch for method {method_name} in class {class_name}. "
                f"Expected {interface_method_type_hints}, got {class_method_type_hints}"
            )


class IsAClass:
    @classmethod
    def is_satisfied_by(cls, candidate: object):
        if not isinstance(candidate, type) or not inspect.isclass(candidate):
            raise InvalidDecoratorUsageError(candidate)
        return True


class IsAMethod:
    @classmethod
    def is_satisfied_by(cls, candidate: object, method: str) -> None:
        if not callable(candidate):
            raise MethodNotCallableError(method_name=method, class_name=candidate.__name__)


class HasTheMethod:
    @classmethod
    def is_satisfied_by(cls, method: str, interface: object):
        if not hasattr(interface, method):
            raise InterfaceMethodError(interface_name=interface.__name__, method_name=method)
