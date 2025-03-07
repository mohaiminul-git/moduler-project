import pandas as pd
from src.Config.configuration import *
from src.Constants import *
from src.logger import logging
import os,sys
from  src.Exception import Custom_exception
import numpy as np
from dataclasses import dataclass
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline

from  sklearn.svm import SVR
from  sklearn.ensemble import RandomForestRegressor
from  sklearn.ensemble  import GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from src.utils import model_evaluate,save_obj

@dataclass
class Model_trainerConfig:
    model_trainer_path: str=model_trainer_path

class Model_trainer:
    def __init__(self):
        self.model_trainerConfig=Model_trainerConfig()
    
    try:
    
        def initiate_model_training(self,train_arr, test_arr):
            x_train, y_train, x_test, y_test = (train_arr[:,:-1],train_arr[:,-1],
                                                test_arr[:,:-1],test_arr[:,-1])
            
            models={
                "Xgboost": XGBRegressor(),
                "GradianBoosting": GradientBoostingRegressor(),
                "Decision_tree":DecisionTreeRegressor(),
                "RandomForest":RandomForestRegressor(),
                "Svr":SVR()
            }
            
            model_report:dict=model_evaluate( x_train, y_train, x_test, y_test, models)
            print(model_report)
            
            best_model_score=max(sorted(model_report.values()))
            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model=models[best_model_name]
            
            logging.info(f"best model name :{best_model},R2 score{best_model_score}")
            
            save_obj(self.model_trainerConfig.model_trainer_path,best_model)
                
    except Exception as e:
            raise Custom_exception(e,sys)
        