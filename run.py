import os
from flask import Flask
from config import app_config
from fizzbuzzapi.views import fizz_buzz_api_app

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to Alessandro's FizzBuzz!"

# Register all the blueprints
app.register_blueprint(fizz_buzz_api_app)

# Load configurations from config.py file
app.config.from_object(app_config)

app.run(host=os.environ['IP'], 
        port=int(os.environ['PORT']))
    
    
