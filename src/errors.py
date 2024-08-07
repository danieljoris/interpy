# Class 'ClassB' does not have method 'test' declared or implemented.


# TypeError: Signature mismatch for method test in class ClassB.
# Expected (self, abc: str, de: float) -> bool, got ()


import inspect
from inspect import Signature


def get_object_name(obj: object):
    return (
        obj.__name__
        if inspect.ismethod(obj) or inspect.isfunction(obj) or inspect.isclass(obj)
        else str(type(obj))
    )


class NotAnInterfaceError(Exception):
    """Exception raised when a class is not an interface."""

    def __init__(self, class_object: object):
        self.class_object_name = get_object_name(class_object)
        self.message = (
            f"{self.class_object_name} is not a Protocol and cannot be used as an interface."
        )
        super().__init__(self.message)


class InvalidDecoratorUsageError(Exception):
    """Exception raised when the '@implements' decorator is used incorrectly."""

    def __init__(self, class_object):
        self.class_object_name = get_object_name(class_object)
        self.message = self.__generate_message()
        super().__init__(self.message)

    def __generate_message(self) -> str:
        return "The '@implements' decorator can only be used in classes."


class InterfaceMethodError(Exception):
    """Exception raised when Class does not have specific method declared or implemented."""

    def __init__(self, interface: object, method_name: str):
        self.interface_name = get_object_name(interface)
        self.method_name = method_name
        self.message = self._generate_message()
        super().__init__(self.message)

    def _generate_message(self) -> str:
        return f"Class '{self.interface_name}' does not have method '{self.method_name}' declared or implemented."


class MethodNotCallableError(Exception):
    def __init__(self, obj: object):
        self.not_callable = get_object_name(obj)
        self.message = self._generate_message()
        super().__init__(self.message)

    def _generate_message(self) -> str:
        return f"Method '{self.not_callable}' is not callable."


class MethodSignatureMismatchError(Exception):
    def __init__(
        self,
        method_name: str,
        class_name: str,
        expected_signature: Signature,
        actual_signature: Signature,
    ):
        self.method_name = method_name
        self.class_name = class_name
        self.expected_signature = expected_signature
        self.actual_signature = actual_signature
        self.message = self._generate_message()
        super().__init__(self.message)

    def _generate_message(self) -> str:
        return (
            f"Signature mismatch for method '{self.method_name}' in class '{self.class_name}'. "
            f"\nExpected: {self.expected_signature}, got: {self.actual_signature}"
        )
