from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME_01 = "Data Ingestion stage"
STAGE_NAME_02 = "Data Validation stage"
STAGE_NAME_03 = "Data Transformation stage"
STAGE_NAME_04 = "Model Training stage"
STAGE_NAME_05 = "Model Evaluation stage"
try:
  logger.info(f"Starting {STAGE_NAME_01} and  {STAGE_NAME_02} and {STAGE_NAME_03} and {STAGE_NAME_04} and {STAGE_NAME_05} pipeline")
  data_ingestion = DataIngestionTrainingPipeline()
  data_validation = DataValidationTrainingPipeline()
  data_transformation = DataTransformationTrainingPipeline()
  modelTrainer = ModelTrainingPipeline()
  modelEvaluation = ModelEvaluationTrainingPipeline()
  data_ingestion.main()
  data_validation.main()
  data_transformation.main()
  modelTrainer.main()
  modelEvaluation.main()
  logger.info(f"Finished {STAGE_NAME_01} and  {STAGE_NAME_02} and {STAGE_NAME_03} and {STAGE_NAME_04} and {STAGE_NAME_05} pipeline")
  
except Exception as e:
  logger.exception(e)
  raise e