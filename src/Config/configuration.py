import os,sys
from src.Constants import *

data_path=os.path.join(root_dir,data_dir,data_dir_key)

raw_data_path= os.path.join(root_dir,artifact_dir,data_ingestion_dir,current_time,raw_data_dir,raw_data_dir_key)

train_data_path= os.path.join   (root_dir,artifact_dir,data_ingestion_dir,current_time,ingested_data_dir,train_data)
test_data_path= os.path.join(root_dir,artifact_dir,data_ingestion_dir,current_time,ingested_data_dir,test_data)
