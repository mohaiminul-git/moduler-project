import pandas as pd
from src.Config.configuration import *
from src.Constants import *
from src.logger import logging
import os,sys
from  src.Exception import Custom_exception
import numpy as np
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder,OneHotEncoder
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from src.utils import save_obj

class Feature_engeenering(BaseEstimator, TransformerMixin):
    def __init__(self):
        logging.info("******feature engeneering .....")
        
   
    def get_distance(self, df, lat1, lon1, lat2, lon2):
        # Ensure latitudes and longitudes are absolute values
        df[lat1] = df[lat1].abs()
        df[lat2] = df[lat2].abs()
        df.drop(df[(df['Restaurant_latitude'] < 8) & (df['Delivery_location_latitude'] < 8)].index,inplace=True)
        p = np.pi / 180
        a = (0.5 - np.cos((df[lat2] - df[lat1]) * p) / 2 +
             np.cos(df[lat1] * p) * np.cos(df[lat2] * p) *
             (1 - np.cos((df[lon2] - df[lon1]) * p)) / 2)
        df['distance'] = 12734 * np.arccos(np.clip(a, -1, 1))
        return df

    
    def extract_time(self,df):
        variables_list=['Time_Orderd','Time_Order_picked']
        df.dropna(subset=['Time_Orderd'], inplace= True)
        for var in variables_list:
            df[var] = df[var].replace(".",":")
            df[var] = pd.to_datetime(df[var],format="%H:%M", errors="coerce")
            df[f"{var}_hour"]=df[var].dt.hour.astype("Int32")
            df[f"{var}_min"]=df[var].dt.minute.astype("Int32")
        
            
    def extract_city(self,df):
        var='Delivery_person_ID'
        df['Delivery_city'] = df[var].str.split('RES', expand=True)[0]
       
            
    def drop_variables(self,df):
        try:
            col_list=["ID",'Delivery_person_ID','Restaurant_latitude','Restaurant_longitude','Delivery_location_latitude','Delivery_location_longitude',
            'Order_Date','Time_Orderd','Time_Orderd_min','Time_Order_picked_hour','Time_Order_picked_min' ]
            df.drop(columns=col_list,inplace=True) 
                 
        except Exception as e:
            raise Custom_exception(e,sys)
        
    def transform_feature(self, df):
        try:
            df = self.get_distance(df, 'Restaurant_latitude', 'Restaurant_longitude',
                                'Delivery_location_latitude', 'Delivery_location_longitude')
            self.extract_time(df)
            self.extract_city(df)
            self.drop_variables(df)
            return df
                
        except Exception as e:
            raise Custom_exception(e,sys)
        
    def fit(self,X,y=None):
        return self
    
    def transform(self,X:pd.DataFrame,y=None) -> pd.DataFrame:
        try:    
            transformed_df=self.transform_feature(X)
            return transformed_df
        except Exception as e:
            raise Custom_exception(e,sys)
    
 

@dataclass
class DataTransformationConfig():
    preproceesing_obj_path:str= preproceesing_obj_path
    preproceesing_train_data_path:str= preproceesing_train_data_path
    preproceesing_test_data_path:str = preproceesing_test_data_path
    feature_engeenering_obj_path:str=feature_engeenering_obj_path     
    

class Data_transformation:
    def __init__(self):
        self.dataTransformationConfig= DataTransformationConfig()
    
    def get_data_transformation_obj(self):
        try:
            Road_traffic_density=['Low','Medium','High','Jam']
            Weather_conditions=['Sunny','Cloudy','Windy','Fog','Sandstorms','Stormy']
            
            categorical_column=['Type_of_order','Type_of_vehicle','Festival','City','Delivery_city']
            ordinal_columns=['Road_traffic_density','Weather_conditions']
            numerical_column=['Delivery_person_Age','Delivery_person_Ratings','Vehicle_condition','multiple_deliveries',
                    'Time_Orderd_hour','distance']
            
            #numerical pipelineexit()
            numerical_pipeline=Pipeline(steps=[
                ("imputer",SimpleImputer()),
                ("sclaer",StandardScaler(with_mean=False))
                ])
            
            categorical_pipeline=Pipeline(steps=[
                ('impute',SimpleImputer(strategy='most_frequent')),
                ('onehot',OneHotEncoder(handle_unknown='ignore')),
                ('scaler',StandardScaler(with_mean=False))
            ])
            ordianl_pipeline=Pipeline(steps=[
                ('impute',SimpleImputer(strategy='most_frequent')),
                ('ordinal',OrdinalEncoder(categories=[Road_traffic_density,Weather_conditions])),
                ('scaler',StandardScaler(with_mean=False))   
                ])
            
            preprocessor= ColumnTransformer([
                ("numreic", numerical_pipeline,numerical_column),
                ("catagory",categorical_pipeline,categorical_column),
                ("ordinal",ordianl_pipeline,ordinal_columns)
            ])
            logging.info("Data_trasformation_obj_obtained")
            return preprocessor
        except Exception as e:
            raise Custom_exception(e,sys)
        
    def get_feature_engeneering_obj(self):
        try:
            feature_eng= Pipeline(steps=[("fe", Feature_engeenering())])
            return  feature_eng
        except Exception as e:
            raise Custom_exception(e,sys)
    
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_data=pd.read_csv(train_path)
            test_data=pd.read_csv(test_path)
            fe_obj=self.get_feature_engeneering_obj()
            train_data=fe_obj.fit_transform(train_data)
            test_data=fe_obj.transform(test_data)
            train_data.to_csv("train_data.csv")
            test_data.to_csv("test_data.csv")
            processing_obj=self.get_data_transformation_obj()
            traget_columns_name = "Time_taken (min)"

            X_train = train_data.drop(columns = traget_columns_name, axis = 1)
            y_train = train_data[traget_columns_name]

            X_test = test_data.drop(columns = traget_columns_name, axis = 1)
            y_test = test_data[traget_columns_name]
            X_train = processing_obj.fit_transform(X_train)
            X_test = processing_obj.transform(X_test)
            train_arr = np.c_[X_train, np.array(y_train)]
            test_arr = np.c_[X_test, np.array(y_test)]
            df_train = pd.DataFrame(train_arr)
            df_test = pd.DataFrame(test_arr)
            
           
            os.makedirs(os.path.dirname(self.dataTransformationConfig.preproceesing_train_data_path),exist_ok=True)
            df_train.to_csv(self.dataTransformationConfig.preproceesing_train_data_path,index=False,header=True)
            
            os.makedirs(os.path.dirname(self.dataTransformationConfig.preproceesing_test_data_path),exist_ok=True)
            df_test.to_csv(self.dataTransformationConfig.preproceesing_test_data_path, index=False,header=True)
            
            save_obj(
                    self.dataTransformationConfig.feature_engeenering_obj_path,fe_obj)
            
            save_obj(self.dataTransformationConfig.preproceesing_obj_path,processing_obj)
            
            return(train_arr,
                   test_arr,
                   self.dataTransformationConfig.preproceesing_obj_path)
        except Exception as e:
            raise Custom_exception(e,sys)
            
            
