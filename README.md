# activate_virtualenv

`activate_virtualenv` is a Python project that offers a context manager that allows users to easily activate a virtual
environments programatically. A virtual environment is an isolated Python environment that allows users to manage and
install packages separately from their system Python installation. This project provides a simple and convenient way to
activate and (automatically) deactivate a virtual environment and start working within it.

## Installation

To install the `activate_virtualenv` package, you can use `pip`:

```shell
pip install activate_virtualenv
```

Or rye:

```shell
rye install activate_virtualenv
```

Or anything else that downloads packages from [PyPI](https://pypi.org/project/activate_virtualenv/).

## Usage

To use the `activate_virtualenv` context manager, you'll need to import it into your Python script. Here's how to get
started:

1. Import the `activate_virtualenv` context manager:

```python
from activate_virtualenv import activate_virtualenv
```

2. Create an instance of `activate_virtualenv` by providing the path to your target virtual environment:

```python
# Replace 'path_to_your_venv' with the actual path to your virtual environment.
with activate_virtualenv('path_to_your_venv'):
# Your code here
# The virtual environment is active within this block.
# The original environment is automatically restored when exiting the 'with' block.
```

### Example

Here's an example of how you can use `activate_virtualenv`:

```python
from activate_virtualenv import activate_virtualenv

# Specify the path to your virtual environment
venv_path = '/path/to/your/virtualenv'

# Activate the virtual environment temporarily
with activate_virtualenv(venv_path):
    # Your code that requires the virtual environment
    from subscript import function

    # Your dependencies in the specified virtual environment will be used here.
    function()

# Once you exit the 'with' block, you are back to your original environment.
# You can now use the modules and dependencies from your original environment.
```

## How It Works

The `activate_virtualenv` context manager temporarily modifies environment variables and Python's `sys` module to
activate the specified virtual environment. When you enter the `with` block, it runs the virtual environment activation
script `activate_this.py` found in the `bin` directory of the specified virtual environment. This sets up the
environment to use the
virtual environment's Python interpreter and dependencies. When you exit the `with` block, it restores the original
environment settings by manually undoing the changes made ny the activation script.

## Important Notes

- This script is intended for use in Python 3 environments.
- Ensure that the virtual environment path you provide is valid. It should be the path to the virtual environment's
  root directory.
- Make sure that the virtual environment contains the standard `activate_this.py` script in the `bin` directory. This
  script is required to activate the virtual environment. If you are using poetry, rye or virtualenv to manage your
  virtual environments, this script should be present by default.

## License

This project is licensed under the MIT License. For more information, please refer to the `LICENSE` file.

## Issues and Contributions

If you encounter any issues or have suggestions for improvements, please feel free
to [open an issue](https://github.com/usernein/activate_virtualenv/issues) or submit a pull request on
the [GitHub repository](https://github.com/usernein/activate_virtualenv).