from src.Config.configuration import *
from src.Constants import *
from src.logger import logging
import os,sys
from src.Components.data_transformation import  Data_transformation
from src.Components.model_trainer import Model_trainer
from src.Components.data_ingestion import Data_Ingestion
class Train:
    def __init__(self):
        self.c=0
        print(f"****************{self.c}*******************")
    def main(self):
        obj= Data_Ingestion()
        train_data,test_data = obj.initiate_data_ingestion()
        data_transformation= Data_transformation()
        train_arr,test_arr,process=data_transformation.initiate_data_transformation(train_data,test_data)
        model_trainer=Model_trainer()
        model_trainer.initiate_model_training(train_arr, test_arr)