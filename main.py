from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME_01 = "Data Ingestion stage"
STAGE_NAME_02 = "Data Validation stage"
try:
  logger.info(f"Starting {STAGE_NAME_01} and  {STAGE_NAME_02} pipeline")
  data_ingestion = DataIngestionTrainingPipeline()
  data_validation = DataValidationTrainingPipeline()
  data_ingestion.main()
  data_validation.main()
  logger.info(f"Finished {STAGE_NAME_01} and  {STAGE_NAME_02}  pipeline")
  
except Exception as e:
  logger.exception(e)
  raise e