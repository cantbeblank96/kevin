import torch

# 版本信息
torch_version = torch.__version__.startswith("1") and int(torch.__version__.split(".", -1)[1]) <= 7


