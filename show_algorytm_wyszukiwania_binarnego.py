# diag_python_env.py
import sys, inspect

print("Python executable:", sys.executable)
print("Python version:", sys.version.splitlines()[0])

# Test importu rich
try:
    import rich
    print("rich version:", getattr(rich, "__version__", "unknown"))
    print("rich location:", inspect.getfile(rich))
except Exception as e:
    print("Failed to import rich:", e)

# Test importu rich.image
try:
    import importlib
    importlib.import_module("rich.image")
    import rich.image
    print("rich.image import: OK")
    print("rich.image location:", inspect.getfile(rich.image))
except Exception as e:
    print("Failed to import rich.image:", e)