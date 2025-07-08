# End-to-End Machine Learning Project

## Project Overview
This project is an end-to-end machine learning pipeline designed to analyze student performance data and predict outcomes based on various features such as gender, parental education, and test preparation. The pipeline includes data ingestion, transformation, model training, and evaluation.

## Project Structure
```
END TO END/
├── README.md
├── requirements.txt
├── setup.py
├── src/
│   ├── __init__.py
│   ├── exception.py
│   ├── logger.py
│   ├── utils.py
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   ├── pipeline/
│   │   ├── predict_pipeline.py
│   │   ├── train_pipeline.py
├── notebook/
│   ├── 1 . EDA STUDENT PERFORMANCE .ipynb
├── artifacts/
│   ├── train.csv
│   ├── test.csv
│   ├── data.csv
│   ├── model.pkl
│   ├── preprocessor.pkl
├── templates/
│   ├── index.html
│   ├── home.html
├── application.py
```

## Key Components
### 1. Data Ingestion
- Reads the dataset from `notebook/data/stud.csv`.
- Splits the data into training and testing sets.
- Saves the processed data into the `artifacts` directory.

### 2. Data Transformation
- Handles preprocessing tasks such as encoding categorical variables and scaling numerical features.
- Saves preprocessing objects for future use.

### 3. Model Training
- Trains machine learning models using the training data.
- Evaluates models using cross-validation and hyperparameter tuning.

### 4. Prediction Pipeline
- Uses trained models to make predictions on new data.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the data ingestion script:
   ```bash
   python src/components/data_ingestion.py
   ```
2. Train the model:
   ```bash
   python src/pipeline/train_pipeline.py
   ```
3. Make predictions:
   ```bash
   python src/pipeline/predict_pipeline.py
   ```

## Logs
Logs are stored in the `logs` directory and provide detailed information about the execution of each pipeline step.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Updated Project Structure
```
END TO END/
├── README.md
├── requirements.txt
├── setup.py
├── src/
│   ├── __init__.py
│   ├── exception.py
│   ├── logger.py
│   ├── utils.py
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   ├── pipeline/
│   │   ├── predict_pipeline.py
│   │   ├── train_pipeline.py
├── notebook/
│   ├── 1 . EDA STUDENT PERFORMANCE .ipynb
├── artifacts/
│   ├── train.csv
│   ├── test.csv
│   ├── data.csv
│   ├── model.pkl
│   ├── preprocessor.pkl
├── templates/
│   ├── index.html
│   ├── home.html
├── application.py
```

## Smooth Running Instructions
### Step 1: Install Dependencies
Run the following command to install all required packages:
```cmd
pip install -r requirements.txt
```

### Step 2: Train the Model
Execute the training pipeline to generate the model and preprocessor artifacts:
```cmd
"C:/Users/ABHINAV KUMAR/anaconda3/Scripts/conda.exe" run -p "C:\Users\ABHINAV KUMAR\Desktop\Machine Learning\END TO END\venv" --no-capture-output python src/pipeline/train_pipeline.py
```

### Step 3: Start the Flask Application
Run the following command to start the web application:
```cmd
"C:/Users/ABHINAV KUMAR/anaconda3/Scripts/conda.exe" run -p "C:\Users\ABHINAV KUMAR\Desktop\Machine Learning\END TO END\venv" --no-capture-output python application.py
```

### Step 4: Access the Web Interface
Open your browser and navigate to `http://127.0.0.1:80` to use the prediction form.
