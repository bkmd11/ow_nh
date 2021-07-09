import sys
from app import app, db

from app.models import Climb


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'climb': Climb, 'sys': sys}

