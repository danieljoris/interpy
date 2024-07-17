# Class 'ClassB' does not have method 'test' declared or implemented.


# TypeError: Signature mismatch for method test in class ClassB.
# Expected (self, abc: str, de: float) -> bool, got ()


class NotAnInterfaceError(Exception):
    """Exception raised when a class is not an interface."""

    def __init__(self, class_object: object):
        self.class_object_name = class_object.__name__
        self.message = (
            f"{self.class_object_name} is not a Protocol and cannot be used as an interface."
        )
        super().__init__(self.message)


class InvalidDecoratorUsageError(Exception):
    """Exception raised when the '@implements' decorator is used incorrectly."""

    def __init__(self, class_object):
        self.class_object_name = class_object.__name__
        self.message = "The '@implements' decorator can only be used in classes."
        super().__init__(self.message)
