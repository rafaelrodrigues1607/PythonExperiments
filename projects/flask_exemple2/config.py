# Configuration settings for the Flask application

class Config:
    SECRET_KEY = 'your_secret_key_here'
    DEBUG = True  # Set to False in production
    TESTING = False
    DATABASE_URI = 'sqlite:///your_database.db'  # Example database URI
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'