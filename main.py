from startup_profit_prediction import logger 
from startup_profit_prediction.pipeline.stage_01_data_injection import DataIngestionTrainingPipeLine


"""
Data ingestion from the mySQL database 💉  
"""

STAGE_NAME = "Data Injection Stage"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_ingestion = DataIngestionTrainingPipeLine()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
