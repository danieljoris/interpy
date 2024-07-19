from typing import Protocol

import pytest

from src._implements import implements
from src.errors import InvalidDecoratorUsageError, NotAnInterfaceError
from tests.conftest import FakeErrorInterface, FakeInterface


class TestImplements:

    def test_throws_exception_if_class_lacks_interface_id(self):
        success_message = (
            "FakeErrorInterface is not a Protocol and cannot be used as an interface."
        )
        with pytest.raises(
            NotAnInterfaceError,
            match=success_message,
        ) as exc_info:

            @implements(FakeErrorInterface)
            class DummyClass:
                def fake_method_1(self, attribute1: str, attribute2: int) -> float: ...

        assert hasattr(exc_info.value, "class_object_name")
        assert exc_info.value.class_object_name == FakeErrorInterface.__name__

    def test_throws_exception_if_is_a_method_and_not_a_class(self):
        expected_message = "The '@implements' decorator can only be used in classes."

        with pytest.raises(InvalidDecoratorUsageError) as exc_info:

            @implements(FakeInterface)
            def fake_method():
                return None

        assert exc_info.value.message == expected_message
        assert hasattr(exc_info.value, "class_object_name")
        assert exc_info.value.class_object_name == "fake_method"

    def should_throws_an_error_when_given_fake_method_as_a_interface_in_implements_decorator(
        self,
    ):
        expected_message = "fake_method is not a Protocol and cannot be used as an interface."

        with pytest.raises(NotAnInterfaceError) as exc_info:

            def fake_method():
                return None

            @implements(fake_method)
            class DummyClass:
                def fake_method_1(self, attribute1: str, attribute2: int) -> float: ...

        assert exc_info.value.message == expected_message
        assert hasattr(exc_info.value, "class_object_name")
        assert exc_info.value.class_object_name == "fake_method"
