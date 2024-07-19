from typing import Protocol


class FakeInterface(Protocol):
    def fake_method_1(self, attribute1: str, attribute2: int) -> float:
        return 1.0


class FakeErrorInterface:
    def fake_method_1(self, attribute1: str, attribute2: int) -> float:
        return 1.0


class DummyClass:
    def fake_method_1(self, attribute1: str, attribute2: int) -> float:
        return 1.0
