from inspect import Signature
from typing import Protocol
from src.errors import (
    InterfaceMethodError,
    InvalidDecoratorUsageError,
    MethodNotCallableError,
    MethodSignatureMismatchError,
    NotAnInterfaceError,
)


class IsAProtocol:
    @classmethod
    def is_satisfied_by(cls, candidate) -> None:
        if not issubclass(candidate, Protocol):
            raise NotAnInterfaceError(candidate)


class MethodSignatureIsEqual:
    @classmethod
    def is_satisfied_by(
        cls,
        interface_method_signature: Signature,
        class_method_signature: Signature,
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
        if not isinstance(candidate, type):
            raise InvalidDecoratorUsageError(candidate)


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
