from flask import Flask
from .views import logger

app=Flask(__name__)

app.register_blueprint(logger.blue)