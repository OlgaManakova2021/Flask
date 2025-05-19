from packaging import version
import numpy as np

required_version = "1.21.0"
if version.parse(np.__version__) >= version.parse(required_version):
    print("Версия NumPy подходит")
else:
    print("Обновите NumPy")
