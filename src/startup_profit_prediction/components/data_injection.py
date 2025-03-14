from pathlib import Path  
import os  
from urllib.parse import quote  

import pandas as pd  
from sqlalchemy import create_engine, text  

from startup_profit_prediction import logger  
from startup_profit_prediction.utils.common import get_size
from startup_profit_prediction.entity.config_entity import DataIngestionConfig  


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def fetch_data_from_database(self):
        if not os.path.exists(self.config.load_data):

            engine = create_engine(f"mysql+pymysql://root:{quote('Reva@0411')}@localhost/startup")
            sql = text(self.config.source_query)
            with engine.connect() as connection:
                result = connection.execute(sql)
                df = pd.DataFrame(result.fetchall(), columns=result.keys())
        
            df.to_csv(self.config.load_data, index=False)
            logger.info(f"{self.config.load_data} downloaded! with following info: loanDataset.csv")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.load_data))}")