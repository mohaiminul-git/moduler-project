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