from main import app, Comment, db, Post, User

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, Comment=Comment, db=db, Post=Post, User=User)
