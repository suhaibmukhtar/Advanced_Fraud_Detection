import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import logging
import sys
from exception import CustomException


## Specify directory for storing logs
log_dir="logs"
os.makedirs(log_dir,exist_ok=True)

## Logging configuration

logger=logging.getLogger("data_injestion")
logger.setLevel("DEBUG")

#adding console handler
console_logger=logging.StreamHandler()
console_logger.setLevel("DEBUG")

log_file_path=os.path.join(log_dir,"data_injestion.log")

##adding file-handler for storing logs on the file
file_handler=logging.FileHandler(log_file_path)
file_handler.setLevel("DEBUG")

##setting the formatter for displaying information in the better way
formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

#adding formatting to handlers
console_logger.setFormatter(formatter)
file_handler.setFormatter(formatter)

## Adding these two loggers in the logger object
logger.addHandler(console_logger)
logger.addHandler(file_handler)


### Loading dataset from the path
def load_dataset(d_path:str)->pd.DataFrame: #return type
    """
    This function reads the dataset from a url or a local path and returns a pandas DataFrame
    """
    try:    
        #reading the dataset from a file or url
        df=pd.read_csv(d_path)
        logger.debug(f"Dataset loaded from the path {d_path} Successfully!")
        return df
    except pd.errors.ParserError as e:
        logger.debug("Failed to parse the CSV file")
        raise CustomException(e,sys)
    except Exception as e:
        raise CustomException(e,sys)
    
if __name__=="__main__":
    #loading the dataset from the path
    data=load_dataset("experiments/card_transdata.csv")
    print(data)