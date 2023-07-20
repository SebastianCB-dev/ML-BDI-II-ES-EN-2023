# Standard libraries
import os
import time
from pathlib import Path

# External libraries
from gensim.models import Word2Vec

# Custom libraries
from services.database_service import DatabaseService
from services.logging_service import LoggingService
from preprocessing import Preprocessing

class Model:
    # Public Properties
    logger = LoggingService().get_logging()
    databaseService = None
    preprocessingService = None

    def __init__(self):
        """Constructor
           This function initializes the class
           Set the model and connect to the database
        """
        self.set_model()
        self.start_db()
        self.preprocessingService = Preprocessing()

    def set_model(self):    
        print(os.getcwd());    
        self.modelES = Word2Vec.load('model/depresion.es.model')
        self.logger.info("Model loaded")
    
    def getLogger(self):
        # This function returns the logger
        return self.logger

    def start_db(self):
        """Database
            This function starts the database connection
            * Set variables from .env file
        """
        self.databaseService = DatabaseService(os.getenv('POSTGRES_URL'))
        self.logger.info("Database connection started")

    def process_comments(self):
        while True:
            try:
                #comments = self.databaseService.get_comments()
                comments = [{'id': 99999, 'username': 'test', 'user_comment': 'test comment'}]
                for comment in comments:
                    self.logger.info(f"Processing comment: {comment['id']}- {comment['username']}")
                    # Get the BDI for the user
                    bdi = self.databaseService.get_bdi(comment['username'])
                    #TODO: Identify language of the comment and use the correct model
                    # language = self.languageService.identify_language(comment['user_comment'])
                    
                    # Process Comment
                    comment_test = 'Hola soi sebastian y tengo ganas de morirme hoy o suisidarme'
                    processed_comment = self.preprocessingService.process_comment(comment_test)

                    
                time.sleep(20)
            except Exception as e:
                self.logger.critical(f"Error with the Model: {e.__str__()}")
                time.sleep(120)
                continue