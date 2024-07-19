import pytest
from typing import Protocol
from src.errors import (
    InterfaceMethodError,
    InvalidDecoratorUsageError,
    MethodNotCallableError,
    MethodSignatureMismatchError,
    NotAnInterfaceError,
)
import inspect

from src._validators import (
    IsAProtocol,
    MethodSignatureIsEqual,
    MethodTypeHintAreEqual,
    IsAClass,
    IsAMethod,
    HasTheMethod,
)

primitive_values = [
    42,  # int
    3.14,  # float
    "hello",  # str
    True,  # bool
    b"hello",  # bytes
    None,  # NoneType
]


class TestIsAProtocol:

    @pytest.mark.parametrize("value", primitive_values)
    def test_should_raises_an_error_when_data_of_primitive_type_is_given(self, value):
        with pytest.raises(NotAnInterfaceError) as exc_info:
            IsAProtocol.is_satisfied_by(value)

        assert (
            exc_info.value.message
            == f"{type(value)} is not a Protocol and cannot be used as an interface."
        )
        assert exc_info.value.class_object_name == str(type(value))

    def test_test_should_raises_an_error_when_not_a_protocol_class_is_given(self):
        class NotAProtocol:
            pass

        with pytest.raises(NotAnInterfaceError):
            IsAProtocol.is_satisfied_by(NotAProtocol)

    def test_given_a_protocol_class_when_checked_then_does_not_raise(self):
        class AProtocol(Protocol):
            pass

        result = IsAProtocol.is_satisfied_by(AProtocol)

        assert result is True


class TestMethodSignatureIsEqual:

    def test_should_raises_an_error_when_lambda_func_mismatched_signatures_is_sent(
        self,
    ):
        sig1 = inspect.signature(lambda self, a: None)
        sig2 = inspect.signature(lambda self, a, b: None)

        with pytest.raises(MethodSignatureMismatchError):
            MethodSignatureIsEqual.is_satisfied_by(sig1, sig2, "ClassName", "method_name")

    def test_should_raises_an_error_when_func_mismatched_signatures_is_sent(
        self,
    ):
        def func1(a: str, b: float): ...

        def func2(a: str, b: int): ...

        sig1 = inspect.signature(func1)
        sig2 = inspect.signature(func2)

        with pytest.raises(MethodSignatureMismatchError):
            MethodSignatureIsEqual.is_satisfied_by(sig1, sig2, "ClassName", "method_name")

    def test_should_raises_an_error_when_method_mismatched_signatures_is_sent(
        self,
    ):
        class A:
            def func1(self, a: str, b: float): ...

        class B:
            def func2(self, a: str, b: int): ...

        sig1 = inspect.signature(A.func1)
        sig2 = inspect.signature(B.func2)

        with pytest.raises(MethodSignatureMismatchError):
            MethodSignatureIsEqual.is_satisfied_by(sig1, sig2, "ClassName", "method_name")

    def test_given_matching_signatures_when_checked_then_does_not_raise(self):
        sig1 = inspect.signature(lambda self, a: None)
        sig2 = inspect.signature(lambda self, a: None)

        result = MethodSignatureIsEqual.is_satisfied_by(sig1, sig2, "ClassName", "method_name")

        assert result is True


class TestMethodTypeHintAreEqual:
    def test_given_mismatched_type_hints_when_checked_then_raises_typeerror(self):
        type_hints1 = {"a": int}
        type_hints2 = {"a": str}

        with pytest.raises(TypeError):
            MethodTypeHintAreEqual.is_satisfied_by(
                type_hints1, type_hints2, "ClassName", "method_name"
            )

    def test_given_matching_type_hints_when_checked_then_does_not_raise(self):
        type_hints1 = {"a": int}
        type_hints2 = {"a": int}

        try:
            MethodTypeHintAreEqual.is_satisfied_by(
                type_hints1, type_hints2, "ClassName", "method_name"
            )
        except TypeError:
            pytest.fail(
                "MethodTypeHintAreEqual.is_satisfied_by() raised TypeError unexpectedly!"
            )


class TestIsAClass:

    @pytest.mark.parametrize("value", primitive_values)
    def test_given_not_a_class_when_checked_then_raises_invaliddecoratorusageerror(
        self, value
    ):
        with pytest.raises(InvalidDecoratorUsageError):
            IsAClass.is_satisfied_by(value)

    def test_given_a_class_when_checked_then_does_not_raise(self):
        class AClass:
            pass

        result = IsAClass.is_satisfied_by(AClass)
        assert result is True


class TestIsAMethod:
    def test_given_not_a_callable_when_checked_then_raises_methodnotcallableerror(self):
        class DummyClass:
            method = "not a callable"

        with pytest.raises(MethodNotCallableError):
            IsAMethod.is_satisfied_by(DummyClass)

    def test_given_a_callable_when_checked_then_does_not_raise(self):
        class DummyClass:
            def method(self):
                pass

        result = IsAMethod.is_satisfied_by(DummyClass.method)

        assert result is True


class TestHasTheMethod:
    def test_given_class_without_method_when_checked_then_raises_interfacemethoderror(self):
        class DummyClass:
            pass

        with pytest.raises(InterfaceMethodError):
            HasTheMethod.is_satisfied_by("method", DummyClass)

    def test_given_class_with_method_when_checked_then_does_not_raise(self):
        class DummyClass:
            def method(self):
                pass

        try:
            HasTheMethod.is_satisfied_by("method", DummyClass)
        except InterfaceMethodError:
            pytest.fail(
                "HasTheMethod.is_satisfied_by() raised InterfaceMethodError unexpectedly!"
            )
