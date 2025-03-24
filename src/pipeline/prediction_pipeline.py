from src.Config.configuration import *
from src.Constants import *
from src.logger import logging
import os,sys
from src.utils import load_model
from  src.Exception import Custom_exception
import pandas as pd


class prediction_pipleline:
    def __init__(self):
        pass
    
    def predict(self,feautures):
        try:
        
            pre_processor_path=preproceesing_obj_path
            model_path=model_trainer_path
            preprocessor=load_model(pre_processor_path)
            model=load_model(model_path)
            data_scaled= preprocessor.transform(feautures)
            pred=model.predict(data_scaled)
            
            return pred
        
        except Exception as e:
            raise Custom_exception(e,sys)


"""categorical_column=['Type_of_order','Type_of_vehicle','Festival','City','Delivery_city']
            ordinal_columns=['Road_traffic_density','Weather_conditions']
            numerical_column=['Delivery_person_Age','Delivery_person_Ratings','Vehicle_condition','multiple_deliveries',
                    'Time_Orderd_hour','distance']"""
            
class  Customdata:
    def __init__(self,
                Type_of_order:str,
                Type_of_vehicle:str,
                Festival:str,
                City:str,
                Delivery_city:str,
                Road_traffic_density:int,
                Weather_conditions:int,
                Delivery_person_Age:float,   
                Delivery_person_Ratings:float,
                Vehicle_condition:float,
                multiple_deliveries:float,
                Time_Orderd_hour:float,
                distance:float):
        
        self.Type_of_order=Type_of_order,
        self.Type_of_vehicle=Type_of_vehicle,
        self.Festival=Festival,
        self.City=City,
        self.Delivery_city=Delivery_city,  
        self.Road_traffic_density=Road_traffic_density,
        self.Weather_conditions=Weather_conditions,
        self. Delivery_person_Age= Delivery_person_Age,
        self. Delivery_person_Ratings= Delivery_person_Ratings,
        self.Vehicle_condition=Vehicle_condition,
        self. multiple_deliveries= multiple_deliveries,
        self. Time_Orderd_hour= Time_Orderd_hour,
        self.distance=distance
        
                
    def get_data_as_dataframe(self):
        try:
            cutom_data_input_dict={
                "Type_of_order": self.Type_of_order,
                "Type_of_vehicle":self.Type_of_vehicle,
                "Is Festival" :self.Festival,
                "City_type":  self.City,
                "Delivery_city" : self.Delivery_city,  
                "Road_traffic_density":self.Road_traffic_density,
                "Weather_conditions"  :self.Weather_conditions,
                "Delivery_person_Age"   :self. Delivery_person_Age,
                " Delivery_person_Ratings"  :self. Delivery_person_Ratings,
                "Vehicle_condition" :self.Vehicle_condition,
                "multiple_deliveries" :self. multiple_deliveries,
                "Time_Orderd_hour" :self. Time_Orderd_hour,
                "distance" :self.distance    
            }
            df=pd.DataFrame(cutom_data_input_dict)
            return df
            
        except Exception as e:
            logging.info("error Occured in Custopm pipeline dataframe")
            raise Custom_exception(e,sys)     
                 
                 
                 
                 
    
            
        
    
    