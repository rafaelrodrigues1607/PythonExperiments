# Project Overview

This project is designed to explore various experiments and applications using Flask and Python. It includes simple test experiments as well as more complex Flask applications. The structure is organized to facilitate easy navigation and understanding of the different components.

## Project Structure

- **README.md**: Documentation for the overall project.
- **requirements.txt**: Lists the Python dependencies required for the project.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **projects/**: Contains all experiments, including simple tests and Flask applications.
  - **exp1_simple_test/**: A simple test experiment.
    - **main.py**: Entry point for the simple test experiment.
    - **utils.py**: Utility functions for the simple test experiment.
    - **README.md**: Documentation specific to the simple test experiment.
  - **flask_exemple1/**: The first Flask example application.
    - **app.py**: Main application file for the Flask app.
    - **requirements.txt**: Dependencies for the first Flask example.
    - **config.py**: Configuration settings for the Flask application.
    - **static/**: Contains static files (CSS, JS, images) for the Flask application.
    - **templates/**: Contains HTML templates for the Flask application.
    - **README.md**: Documentation specific to the first Flask example.
  - **flask_exemple2/**: The second Flask example application.
    - **app.py**: Main application file for the second Flask app.
    - **requirements.txt**: Dependencies for the second Flask example.
    - **static/**: Intended for static files for the second Flask example.
    - **templates/**: Intended for HTML templates for the second Flask example.
    - **config.py**: Configuration settings for the second Flask application.
    - **README.md**: Documentation specific to the second Flask example.
- **shared/**: Contains reusable modules.
  - **helpers.py**: Reusable helper functions.
  - **db_utils.py**: Utility functions for database operations.
  - **config.py**: Shared configuration settings.
  - **__init__.py**: Indicates that the shared directory is a Python package.
- **notebooks/**: Contains Jupyter notebooks for experiments.
  - **test_experiment.ipynb**: Jupyter notebook for testing experiments.
  - **data_analysis.ipynb**: Jupyter notebook for data analysis experiments.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd project-name
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Navigate to the desired project folder within `projects/` to run specific experiments or applications.

## Usage Guidelines

- For the simple test experiment, run `main.py` in the `exp1_simple_test/` directory.
- For the Flask applications, run `app.py` in the respective `flask_exemple1/` or `flask_exemple2/` directories.
- Refer to the individual README files in each project folder for more specific instructions and details.