"""
Autor: Matias Martelossi
Creation: 17/09/2022
"""
import os

from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

# DB initialize
# db variable use for create models from here
db = SQLAlchemy()

# Swagger initialize document
swagger_config = {
    "title": "App API",
    "uiversion": 3,
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/api/doc"
}
SWAGGER_TEMPLATE = {
    "swagger": "2.0",
    "info": {
        "title": "App Api",
        "description": "Api for all service",
        "contact": {
            "responsibleOrganization": "MnM",
            "responsibleDeveloper": "Matias Martelossi",
            "email": "matiasmartelossi@gmail.com",
            "url": "",
        },
        "version": "1.0.0"
    },
    "host": os.environ.get('BASE_URL'),  # overrides localhost:500
    "basePath": "",  # base bash for blueprint registration
    "schemes": ["http", "https"],
    "operationId": "data",
    "securityDefinitions": {"APIKeyHeader": {"type": "apiKey", "name": "Authorization", "in": "header"}}
}
swagger = Swagger(config=swagger_config, template=SWAGGER_TEMPLATE)

