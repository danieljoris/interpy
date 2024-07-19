import inspect
from typing import _ProtocolMeta, Type, Union

from src.errors import (
    InterfaceMethodError,
    InvalidDecoratorUsageError,
    MethodNotCallableError,
    MethodSignatureMismatchError,
    NotAnInterfaceError,
)


class IsAProtocol:
    @classmethod
    def is_satisfied_by(cls, candidate: Type[object]) -> Union[bool, None]:

        if not inspect.isclass(candidate):
            raise NotAnInterfaceError(candidate)
        elif not isinstance(candidate, _ProtocolMeta):
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
    ) -> Union[bool, None]:
        if not interface_method_signature == class_method_signature:
            raise MethodSignatureMismatchError(
                method_name, class_name, interface_method_signature, class_method_signature
            )

        return True


class MethodTypeHintAreEqual:
    @classmethod
    def is_satisfied_by(
        cls,
        interface_method_type_hints,
        class_method_type_hints,
        class_name: str,
        method_name: str,
    ) -> Union[bool, None]:
        if interface_method_type_hints != class_method_type_hints:
            raise TypeError(
                f"Type hints mismatch for method {method_name} in class {class_name}. "
                f"Expected {interface_method_type_hints}, got {class_method_type_hints}"
            )
        return True


class IsAClass:
    @classmethod
    def is_satisfied_by(cls, candidate: object) -> Union[bool, None]:
        if not isinstance(candidate, type) or not inspect.isclass(candidate):
            raise InvalidDecoratorUsageError(candidate)
        return True


class IsAMethod:
    @classmethod
    def is_satisfied_by(cls, candidate: object) -> Union[bool, None]:
        if not callable(candidate) or inspect.isclass(candidate):
            raise MethodNotCallableError(obj=candidate)
        return True


class HasTheMethod:
    @classmethod
    def is_satisfied_by(cls, method: str, interface: object) -> Union[bool, None]:
        if not hasattr(interface, method):
            raise InterfaceMethodError(interface=interface, method_name=method)

        return True
