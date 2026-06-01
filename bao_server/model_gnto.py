"""
GNTO model integration for vanilla BAO server (same shape as LIMAO's model_gnto.py).

Re-exports ``GntoRegression`` from the centralized GNTO adapter so this
bao_server can use it as a drop-in replacement for ``model.BaoRegression``
when ``ModelType = GNTO`` is set in bao.cfg.
"""

import sys
import os

_gnto_root = "/home/AiChaosN/Project/Phd/project/GNTO"
if not os.path.isdir(_gnto_root):
    raise ImportError(f"GNTO root not found at {_gnto_root}")
if _gnto_root not in sys.path:
    sys.path.append(_gnto_root)

from adapters.limao_adapter import GntoRegression, GNTOModel, GNTOFeaturizer, _inv_log1p

__all__ = ["GntoRegression", "GNTOModel", "GNTOFeaturizer", "_inv_log1p"]
