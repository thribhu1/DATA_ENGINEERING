from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
  logger.info(f"Starting {STAGE_NAME} pipeline")
  data_ingestion = DataIngestionTrainingPipeline()
  data_ingestion.main()
  logger.info(f"Finished {STAGE_NAME} pipeline")
  
except Exception as e:
  logger.exception(e)
  raise e