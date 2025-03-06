from src.logger import logging
from src.Exception import Custom_exception
import os,sys
import pickle

def save_obj(file_path,obj):
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        
        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        raise Custom_exception(e,sys)