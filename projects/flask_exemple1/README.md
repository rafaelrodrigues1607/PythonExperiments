# Flask Example 1

This directory contains the first example of a Flask application. Below are the details regarding the setup and usage of this application.

## Overview

The Flask Example 1 project demonstrates a simple web application built using the Flask framework. It includes basic routing and serves static files and HTML templates.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd project-name/projects/flask_exemple1
   ```

2. **Install dependencies**:
   Make sure you have Python and pip installed. Then, run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   You can start the Flask application by running:
   ```bash
   python app.py
   ```

4. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000` to view the application.

## Usage Guidelines

- The main page is served at the root URL (`/`).
- An about page is available at `/about`.

## Directory Structure

- `app.py`: The main application file that initializes the Flask app and sets up routes.
- `requirements.txt`: Lists the dependencies required for this Flask application.
- `config.py`: Contains configuration settings for the Flask application.
- `static/`: Directory for static files (CSS, JS, images).
- `templates/`: Directory for HTML templates used in the application.
- `README.md`: This file, providing documentation for the Flask Example 1 project.