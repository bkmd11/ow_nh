import sys
from app import app, db

from app.models import Climb


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'climb': Climb, 'sys': sys}


# In no particular order
# Todo:
#  make prettier ----
#  add admin feature to update
#  actually build DB
#  set up email contact in case anyone like it?
#  actually climb and load pictures
