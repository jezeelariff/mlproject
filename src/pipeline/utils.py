import os
import sys

import numpy as np
import pandas as pd
import dill


from src.pipeline.exception import CustomException


def save_object(obj, file_path):
    """
    Save the object to a file
    """

    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj: #wb - writeby
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys) from e