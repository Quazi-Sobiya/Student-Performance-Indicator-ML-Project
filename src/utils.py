import os
import sys

import numpy as np
import pandas as pd
import dill

from src.exception import CustomException

def save_object(save_path,obj):
    try:
        dir_path=os.path.dirname(save_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(save_path, "wb") as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)




