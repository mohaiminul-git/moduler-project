import os,sys
from src.Constants import *

data_path=os.path.join(root_dir,data_dir,data_dir_key)

raw_data_path= os.path.join(root_dir,artifact_dir,data_ingestion_dir,current_time,raw_data_dir,raw_data_dir_key)

train_data_path= os.path.join   (root_dir,artifact_dir,data_ingestion_dir,current_time,ingested_data_dir,train_data)
test_data_path= os.path.join(root_dir,artifact_dir,data_ingestion_dir,current_time,ingested_data_dir,test_data)

#data_transformation
#preproceesing_data_path= os.path.join(root_dir, artifact_dir,data_transformation_artifacts)

preproceesing_obj_path= os.path.join(root_dir, artifact_dir,data_transformation_artifacts,data_processor_dir,
                                data_processor_dir_key)

preproceesing_train_data_path= os.path.join(root_dir, artifact_dir,data_transformation_artifacts,transformed_data_dir,
                                            transformed_train_data_dir_key)
preproceesing_test_data_path= os.path.join(root_dir, artifact_dir,data_transformation_artifacts,transformed_data_dir,
                                            transformed_test_data_dir_key)

feature_engeenering_obj_path= os.path.join(root_dir,artifact_dir,data_transformation_artifacts,data_processor_dir,
                                           "featue_engeenering.pkl")

##model Trainer
model_trainer_path= os.path.join(root_dir, artifact_dir,model_trainer_artifacts,model_trainer_artifacts_key)