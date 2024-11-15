<h1>Advanced Credit Card Fraud Detection</h1>
<h3>Overview of project<h3>
This project focuses on developing a robust system for detecting credit card fraud using advanced ensemble techniques. The system addresses critical challenges such as data imbalance, ensuring unbiased predictions and enhanced generalizability. The project is structured with modular components for data ingestion, data transformation, model training, and evaluation, emphasizing scalability and maintainability.</p>
To enhance interpretability, the project incorporates SHAP (SHapley Additive exPlanations) and feature-importance analysis, enabling insights into the key features driving the model's predictions. The deployment of the model will be carried out using Flask and Docker, ensuring seamless integration with other applications and providing a scalable solution for real-world implementation.
<h2>Project Structure</h2>
src/ <br>
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
May have some modifications as well<br>

<h2>Installation</h1>
<h4>1. Set Up Virtual Environment</h4>
<ol>
    <ul>avigate to the desired folder in your terminal:</ul>
    conda create -p venv python==3.9.1 -y
    <ul>Activate the virtual environment</ul>
    conda activate "path-to-venv"
</ol>
<h4>2. Sync with GitHub</h4>
<ol>
    <li>Create a GitHub repository.</li>
    <li>Initialize Git in your local project folder:</li>
        git init
        git add . #addes files to stagging area
    <li>Add configuration variable such as name and email</li>
        git config --global user.name "your-name"
        git config --global user.email "your-email"
    <li>Add a .gitignore file from GitHub's template for Python.(using interface)<li>
    <li>Commit files so that they are added to local reposity</li>
        git commit -m "Initial commit"
    <li>Copy the https url from the Github repository and add that as origin</li>
        git remote add origin https://github.com/your-username/your-repo-name.git
    <li>Select the branch to push to</li>
        git branch -M main #if we have to push to main branch
    <li>Push the code on the remote repository</li>
        git push origin main
</ol>
<h4>3. Install Required Libraries</h4>

