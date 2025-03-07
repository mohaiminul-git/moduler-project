import os,sys
from datetime import datetime

def get_current_time_stamp():
    return datetime.now().strftime("%Y-%m-%d %H-%M-%S")

current_time= get_current_time_stamp()

root_dir=os.getcwd()
data_dir= "Data"
data_dir_key="finalTrain.csv"

artifact_dir="Artifacts"
data_ingestion_dir="data_ingestaion"
raw_data_dir="raw_data"
ingested_data_dir="ingested_data"
raw_data_dir_key="raw.csv"
train_data="train.csv"
test_data="test.csv"

#data_transformation
data_transformation_artifacts="data_transformation"
data_processor_dir="processor"
data_processor_dir_key="processor.pkl"
transformed_data_dir="transformed_data"
transformed_train_data_dir_key="train.csv"
transformed_test_data_dir_key= "test.csv"

#mode training
model_trainer_artifacts="model_trainer"
model_trainer_artifacts_key="trained_model.pkl"

