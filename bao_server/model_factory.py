"""
Single source of truth for which regressor class to instantiate.

Reads ``ModelType`` from ``bao.cfg`` (default: BAO). All places that used to
hardcode ``model.BaoRegression(...)`` should now call ``get_regressor_class()``
so a single config knob switches the whole training/inference path.
"""

from config import read_config

_cfg = read_config()
MODEL_TYPE = _cfg.get("ModelType", "BAO").strip().upper()


def get_regressor_class():
    """Return the regressor class chosen by ModelType."""
    if MODEL_TYPE == "GNTO":
        import model_gnto
        return model_gnto.GntoRegression
    import model
    return model.BaoRegression
