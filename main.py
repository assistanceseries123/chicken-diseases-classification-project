from src.chicken_diseases_classification_project import logger
from src.chicken_diseases_classification_project.components.data_ingestion import DataIngestion
from src.chicken_diseases_classification_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME="Data Ingestion Stage"

try:

    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completd <<<<<<<<<<<<<\n\nX============X")

except Exception as e:
    logger.exception(e)
    raise e