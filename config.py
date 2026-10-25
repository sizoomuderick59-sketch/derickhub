import os
from app.config import config

# Export default configuration
current_config = config[os.getenv('FLASK_ENV', 'development')]
