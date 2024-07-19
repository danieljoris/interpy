# interpy
Interpy is a Python library for creating interfaces in code, similar to what happens in languages like C#. This project aims to provide a structured, easy and standardized way to define interfaces in Python.

![Build Status](https://img.shields.io/github/actions/workflow/status/danieljoris/interpy/ci.yml?branch=main)
![Coverage Status](https://img.shields.io/codecov/c/github/danieljoris/interpy)
![License](https://img.shields.io/github/license/danieljoris/interpy)

---

## 📋 Table of Contents

- [📥 Installation](#-installation)
- [🚀 Usage](#-usage)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [📧 Contact](#-contact)

---

## 📥 Installation

To install Interpy with `pip`, you can use the following command:

```bash
pip install interpy
```
If you are using `poetry` you can use the command:

```bash
poetry add interpy
```

---

## 🚀 Usage

Here is a basic example of how to use Interpy:

```python

class FakeInterface(Protocol):
    def fake_method(self, attr1: float, attr2: float) -> float: ...

@implements(FakeInterface)
class Fake:
    def fake_method(self, attr1: float, attr2: float) -> float:
        return attr1 + attr2
```

If you implement the class incorrectly, you will see the power of interpy as in the example below:

```python

class FakeInterface(Protocol):
    def fake_method(self, attr1: float, attr2: float) -> float: ...

@implements(FakeInterface)
class Fake:
    def fake_method(self, attr1: float, attr2: int) -> float:
        return attr1 + attr2
```

The example above will generate an error when the Python interpreter reads the code.

Interpy currently covers the following implementation errors:

- `InvalidDecoratorUsageError` - This error will be generated if the *@implements* decorator is used in a method and not in a class;
- `NotAnInterfaceError` - This error will be generated if the send parameter to *@implements* decorator is not an Protocol([PEP 0544](https://peps.python.org/pep-0544/));
- `InterfaceMethodError` - This error occurs when a class implementing an interface does not have a specific method declared or implemented;
- `MethodNotCallableError` - This error occurs when a specific method in the class is not callable (e.g., a property or instance attribute);
- `MethodSignatureMismatchError` - This error occurs when a method signature mismatch happens. We will provide what is expected and what we received;

---


## 🤝 Contributing
If you would like to contribute to Interpy, please follow these steps:

1. Fork the repository
    `git clone git@github.com:danieljoris/interpy.git`
2. Create a branch for your feature 
    `git checkout -b feature/your-feature`
3. Commit your changes 
    `git commit -m 'Add your feature`
4. Push to the branch 
    `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for more details.

---

## 📧 Contact

Feel free to adjust and add more features as needed. If you need anything more specific or additional adjustments, let me know!