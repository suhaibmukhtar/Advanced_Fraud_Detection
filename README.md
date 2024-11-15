<!DOCTYPE html>
<html>
<body>
    <h1>Advanced Credit Card Fraud Detection</h1>
    <h3>Overview of Project</h3>
    <p>
        This project focuses on developing a robust system for detecting credit card fraud using advanced ensemble techniques. 
        The system addresses critical challenges such as <strong>data imbalance</strong>, ensuring unbiased predictions and enhanced generalizability. 
        The project is structured with modular components for <strong>data ingestion</strong>, <strong>data transformation</strong>, 
        <strong>model training</strong>, and <strong>evaluation</strong>, emphasizing scalability and maintainability.
    </p>
    <p>
        To enhance interpretability, the project incorporates <strong>SHAP (SHapley Additive exPlanations)</strong> and 
        <strong>feature-importance analysis</strong>, enabling insights into the key features driving the model's predictions. 
        The deployment of the model will be carried out using <strong>Flask</strong> and <strong>Docker</strong>, ensuring seamless integration 
        with other applications and providing a scalable solution for real-world implementation.
    </p>

<h3>Project Structure</h3>
src/<br>
├── __init__.py              # Initializes the package<br>
├── components/              # Contains modular components<br>
│   ├── __init__.py          # Initializes the components package<br>
│   ├── data_ingestion.py    # Handles data loading from sources<br>
│   ├── data_transformation.py # Prepares and processes data (encoding, train-test split)<br>
│   ├── model_trainer.py     # Develops, trains, and evaluates the model<br>
├── pipeline/                # Orchestrates workflows<br>
│   ├── __init__.py          # Initializes the pipeline package<br>
│   ├── train_pipeline.py    # Executes training pipeline<br>
│   ├── prediction_pipeline.py # Executes prediction pipeline<br>
├── logger.py                # Tracks logs for debugging and analysis<br>
├── exception.py             # Handles custom exceptions<br>
├── utils.py                 # Contains shared utility functions<br>
    </pre>
    <p><em>Note: Project structure may have minor modifications as needed.</em></p>

    <h2>Installation</h2>

    <h4>1. Set Up Virtual Environment</h4>
    <ol>
        <li>Navigate to the desired folder in your terminal:</li>
        <pre>conda create -p venv python==3.9.1 -y</pre>
        <li>Activate the virtual environment:</li>
        <pre>conda activate "path-to-venv"</pre>
    </ol>

    <h4>2. Sync with GitHub</h4>
    <ol>
        <li>Create a GitHub repository.</li>
        <li>Initialize Git in your local project folder:</li>
        <pre>
git init
git add .  # Adds files to staging area
        </pre>
        <li>Set configuration variables (name and email):</li>
        <pre>
git config --global user.name "your-name"
git config --global user.email "your-email"
        </pre>
        <li>Add a <code>.gitignore</code> file using GitHub's Python template via the interface.</li>
        <li>Commit the files to the local repository:</li>
        <pre>git commit -m "Initial commit"</pre>
        <li>Add the GitHub repository URL as the remote origin:</li>
        <pre>git remote add origin https://github.com/your-username/your-repo-name.git</pre>
        <li>Set the branch to push to (e.g., main):</li>
        <pre>git branch -M main</pre>
        <li>Push the code to the remote repository:</li>
        <pre>git push origin main</pre>
    </ol>

<h4>3. Install Required Libraries</h4>
<p>Create requirements.txt with dependencies</p>
pandas
numpy
seaborn
matplotlib
-e .  ## will automatically call the setup.py
<p>After cloning the repository, install the required libraries by running:</p>
    <pre>pip install -r requirements.txt</pre>
<h4>Setup.py Script</h4>
The setup.py file ensures all required dependencies and metadata are specified. Below is the code included in the setup.py:<br>
<pre>
from setuptools import find_packages, setup
from typing import List

def get_requirements(file: str) -> List[str]:
    """
    Returns a list of libraries required for the project.
    """
    requirements = []
    HYPHEN_DOT_E = "-e ."
    with open(file, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_DOT_E in requirements:
            requirements.remove(HYPHEN_DOT_E)
    return requirements

setup(
    name="Advanced_Credit_Card_Fraud_Detection",
    version="1.0",
    author="Suhaib Mukhtar",
    author_email="suhaibmukhtar2@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
</pre>
<h4>Logging</h4>
Logs are generated using Python's logging module, with a separate logs directory created dynamically. The log file name is based on the current date and time. Example logging configuration is in logger.py:<br>
<pre>
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d-%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH, 
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("This is a log message")
</pre>

<h4>Exception Handling<h4>
Custom exceptions are handled using exception.py. The sys.exc_info() function is used to capture exception details such as type, message, and traceback for debugging.
</body>
</html>
