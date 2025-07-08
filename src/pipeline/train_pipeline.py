import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

def start_training_pipeline():
    try:
        # Data Ingestion
        data_ingestion = DataIngestion()
        train_data, test_data = data_ingestion.initiate_data_ingestion()

        # Data Transformation
        data_transformation = DataTransformation()
        train_array, test_array, _ = data_transformation.initiate_data_transformation(train_data, test_data)

        # Model Training
        model_trainer = ModelTrainer()
        model_trainer.initiate_model_trainer(train_array, test_array)

        print("Training pipeline executed successfully.")
    except Exception as e:
        print(f"Error in training pipeline: {e}")

if __name__ == "__main__":
    start_training_pipeline()