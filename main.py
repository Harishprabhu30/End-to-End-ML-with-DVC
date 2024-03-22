from CNN_Classifier import logger
from CNN_Classifier.pipeline.stage_01_data_ingestion import *
from CNN_Classifier.pipeline.stage_02_prepare_base_model import *


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx========================x")
except Exception as e:
    logger.exception(e)
    raise e

###############################################################################################################

STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_ingestion = PrepareBaseModelTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx========================x")
except Exception as e:
    logger.exception(e)
    raise e
