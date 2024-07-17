from inspect import Signature
from typing import Protocol
from src.errors import InvalidDecoratorUsageError, NotAnInterfaceError


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
            raise TypeError(
                f"Signature mismatch for method {method_name} in class {class_name}. "
                f"\nExpected {interface_method_signature}, got {class_method_signature}"
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
            raise TypeError(f"{method} in class {candidate.__name__} is not callable")


class HasTheMethod:
    @classmethod
    def is_satisfied_by(cls, method: str, interface: object):
        if not hasattr(interface, method):
            raise TypeError(
                f"Class '{interface.__name__}' does not have method '{method}' declared or implemented."
            )
