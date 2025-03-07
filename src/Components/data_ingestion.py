from src.Config.configuration import *
from src.Constants import *
from src.logger import logging
import os,sys
from sklearn.model_selection import train_test_split
from  src.Exception import Custom_exception
import numpy as np
import pandas as pd
from dataclasses import dataclass
from src.Components.data_transformation import  Data_transformation
from src.utils import save_obj
from src.Components.model_trainer import Model_trainer

@dataclass
class Dataingestion_Config:
    train_data_path: str=train_data_path
    test_data_path:str=test_data_path
    raw_data_path:str=raw_data_path

class Data_Ingestion:
    def __init__(self):
        self.dataingestion_config = Dataingestion_Config()
        
    def initiate_data_ingestion(self):
        
        try:
            data= pd.read_csv(data_path)
            
            os.makedirs(os.path.dirname(self.dataingestion_config.raw_data_path), exist_ok=True)
            data.to_csv(self.dataingestion_config.raw_data_path, index=False)
            
            train_data, test_data= train_test_split(data,test_size=0.30,random_state=42)
            os.makedirs(os.path.dirname(self.dataingestion_config.train_data_path), exist_ok=True)
            train_data.to_csv (self.dataingestion_config.train_data_path,index=False, header= True)
            
            os.makedirs(os.path.dirname(self.dataingestion_config.test_data_path), exist_ok=True)
            test_data.to_csv(self.dataingestion_config.test_data_path,index=False, header= True)
            
            return (
                self.dataingestion_config.train_data_path,
                self.dataingestion_config.test_data_path
                )    
            
            
        except Exception as e:
            raise Custom_exception(e,sys)


if __name__ == "__main__":
    obj= Data_Ingestion()
    train_data,test_data = obj.initiate_data_ingestion()
    data_transformation= Data_transformation()
    train_arr,test_arr,process=data_transformation.initiate_data_transformation(train_data,test_data)
    model_trainer=Model_trainer()
    print(model_trainer.initiate_model_training(train_arr, test_arr))