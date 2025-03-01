import os,sys
from src.Exception import Custom_exception
from src.logger import logging

try:
    value= 1/0
except Exception as e:
    eroor=Custom_exception(e,sys)
    logging.info(eroor)


    