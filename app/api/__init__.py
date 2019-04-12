from flask import Blueprint
from flask_restplus import Api


# API Blueprint Application
apiBlueprint = Blueprint('apiBlueprint', 
                            __name__,
                            url_prefix = '/v1',
                        )

# Decorator instance in each APIs
apiRestful = Api(apiBlueprint,
                    version = '1.0',
                    title = 'gaesaenack API',
                    description = 'gae_sae_nack Flask Webpage Rendering API',
                    default = 'app.api.__init__.py',
                    default_label = 'gaesaenack API LIST',
                    ui = True,  # False: Make Swagger UI disable
                    # doc = True, # False: Do not use Swagger UI
                )

# API Routing with @apiRestful.route
from app.api.admin import *
from app.api.index import *
