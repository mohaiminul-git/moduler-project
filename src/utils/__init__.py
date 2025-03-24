from src.logger import logging
from src.Exception import Custom_exception
import os,sys
import pickle
from sklearn.metrics import r2_score

def save_obj(file_path,obj):
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        
        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        raise Custom_exception(e,sys)
    
def model_evaluate(x_train,y_train,x_test,y_test,models):
    try:
        report={}
        for i in range(len(models)):
            model=list(models.values())[i]
            model.fit(x_train, y_train)
            Y_test_pred=model.predict(x_test)
            test_model_score=r2_score(Y_test_pred,y_test)
            report[list(models.keys())[i]]=test_model_score
            
        return report
    except Exception as e:
            raise Custom_exception(e,sys)
        
        
def load_model(file_path):
    try:
        with open (file_path,"rb") as f:
            return pickle.load(f) 
    except Exception as e:
        logging.info("exception occured while loadind an object")
        raise Custom_exception(e,sys)
     

            
        
        