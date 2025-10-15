---
applyTo: '**/*.py, **/*.ipynb'
---
ALWAYS check the documentation for any of the things mentioned here, don't assume your knowledge is complete and up-to-date all the time. Remember The Zen of Python.

# Coding Style Guidelines/Conventions

You MUST follow all of those conventions when writing Python code. Any code that violates these rules should be rewritten immediately:

* Follow PEP 8 standards ALWAYS, above any of the following conventions
* When in doubt, follow the Google Code Style for Python here: https://google.github.io/styleguide/pyguide.html
* Documentation must follow the Google Code Style for Python guidelines.
* Every module must have a docstring, functions must have docstrings when in line with the Google Code Style for Python section 3.8.3 rules.
* Features from recent Python releases (up to our project version) should be used instead of older code.
* Write modular code whenever possible.
* Use meaningful method, variable and parameter names, and always annotate the data types of parameters and return values.
* The documentation structure must be Sphinx compatible: https://www.sphinx-doc.org/en/master/
* For functions which implement mathematical/scientific concepts, add the actual mathematical formula as comment or to the docstrings.
* Code performance must be followed by using the Python Speed guidelines: https://wiki.python.org/moin/PythonSpeed
* Leverage existing libraries: Before writing your own solution, check if there's an existing library you can use.
* Use the built-in type hinting.

# Specific Instructions

* Don’t introduce new dependencies (library imports) when the desired functionality is already covered by existing dependencies.
* Avoid using magic numbers, prefer using named constants.
* Always use lazy % string logging.
* Don't use bare exceptions.
* Use namedtuples when: You need immutable data with named fields for better readability (replacing tuples with unclear indices, function returns, or lightweight data containers).
  Avoid namedtuples when: You need mutable data, dynamic fields, complex behavior, or performance-critical dynamic creation (use classes, dataclasses, or dicts instead).
* No context-dependent return types! Also: Avoid None as return type, rather raise an Exception instead.
* Be generous with defining Exception classes.
* Imports should be grouped in the following order:
  1. Standard library imports (such as re, math, datetime, cf. here )
  2. Related third party imports (such as numpy)
  3. Local application/library specific imports (such as mycode.mymodule.base)
* You should put a blank line between each group of imports.
* Avoid circular importing.
* Use Factory Method when: You have complex if/elif/else logic to create different objects with a common interface, or need to support multiple implementations of the same feature without modifying existing code.
  Avoid Factory Method when: You only have one concrete implementation, the creation logic is simple and unlikely to change, or the overhead of the pattern outweighs its benefits for your use case.

# Edge Cases and Testing

* Always include test cases for critical paths of the application.
* Account for common edge cases like empty inputs, invalid data types, and large datasets.
* Include comments for edge cases and the expected behavior in those cases.
* Write unit tests for functions and document them with docstrings explaining the test cases.

# Tools and Utilities

The preferences listed here are not definitive: if the alternative needs to be used for compatibility, do it

* `uv` is preferred over `pip`
* `ruff` must be used as the formatter and all code must follow ruff's default rules: https://docs.astral.sh/ruff/rules
* `polars` is preferred over `pandas`
* `pytest` is the preferred test framework, otherwise the alternative should be considered by the context of the code.
* `loguru` is preferred over the built-in logging library

THERE IS NO NEED TO MENTION THAT YOU HAVE FOLLOWED ANY OF THIS IN YOU RESPONSE, ONLY IF IT IS IMPORTANT TO UNDERSTAND THE ENTIRE COMMIT!
