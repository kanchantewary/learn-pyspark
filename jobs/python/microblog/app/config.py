import os

class config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'you-will-never-guess'

