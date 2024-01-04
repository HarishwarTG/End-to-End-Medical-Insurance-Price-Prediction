import os
import sys
from src.exception import CustomException
from src.logger import logging 
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_file_path: str=os.path.join("artifacts","train.csv")
    test_file_path: str=os.path.join("artifacts","test.csv")
    raw_file_path: str=os.path.join("artifacts","raw_data.csv")
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def intiate_data_ingestion(self):
        logging.info("Enterd Data ingestion method")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info("Dataframe is created")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_file_path),exist_ok=True)
            
            pd.to_csv(self.ingestion_config.raw_file_path,index=False,header=True)
            logging.info("Data Ingestion started")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=40)
            train_set.to_csv(self.ingestion_config.train_file_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_file_path,index=False,header=True)
            
            logging.info("Data ingestion completed")
            
            return(
                self.ingestion_config.train_file_path,
                self.ingestion_config.test_file_path
            )
            
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=='__main__':
    obj=DataIngestion()
    obj.intiate_data_ingestion()