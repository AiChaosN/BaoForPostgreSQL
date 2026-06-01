from model_factory import MODEL_TYPE

PG_OPTIMIZER_INDEX = 0

if MODEL_TYPE == "GNTO":
    DEFAULT_MODEL_PATH = "bao_default_model_gnto"
    TMP_MODEL_PATH = "bao_tmp_model_gnto"
    OLD_MODEL_PATH = "bao_previous_model_gnto"
else:
    DEFAULT_MODEL_PATH = "bao_default_model"
    TMP_MODEL_PATH = "bao_tmp_model"
    OLD_MODEL_PATH = "bao_previous_model"
