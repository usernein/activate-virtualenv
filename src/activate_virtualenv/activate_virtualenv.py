import os
import sys
from contextlib import AbstractContextManager
from pathlib import Path


class ActivateVirtualenv(AbstractContextManager):
    def __init__(self, venv_path):
        self.venv_path = venv_path
        self.venv_activate_path = Path(self.venv_path) / "bin" / "activate_this.py"

        self.original_path = os.getenv("PATH")
        self.original_virtual_env = os.getenv("VIRTUAL_ENV")
        self.original_virtual_env_prompt = os.getenv("VIRTUAL_ENV_PROMPT")
        self.original_sys_path = [*sys.path]
        self.original_sys_prefix = sys.prefix
        self.original_modules = [*sys.modules.keys()]

    def __enter__(self):
        with Path(self.venv_activate_path).open("rb") as f:
            code = compile(f.read(), self.venv_activate_path, "exec")
            exec(code, {"__file__": self.venv_activate_path})

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.original_path is not None:
            os.environ["PATH"] = self.original_path
        if self.original_virtual_env is not None:
            os.environ["VIRTUAL_ENV"] = self.original_virtual_env
        if self.original_virtual_env_prompt is not None:
            os.environ["VIRTUAL_ENV_PROMPT"] = self.original_virtual_env_prompt

        sys.path[:] = self.original_sys_path
        sys.prefix = self.original_sys_prefix

        diff_modules = set(sys.modules.keys()) - set(self.original_modules)
        for module in diff_modules:
            del sys.modules[module]

        if exc_type is not None:
            raise exc_type(exc_val).with_traceback(exc_tb)


activate_virtualenv = ActivateVirtualenv
