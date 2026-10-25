import os
from app import create_app
from app.models import db

app = create_app(os.getenv('FLASK_ENV', 'development'))

# Create any missing tables (e.g. login_events) on startup, including under gunicorn.
# create_all() never alters or drops existing tables, so this is safe on an existing database.
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # Run development server on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
