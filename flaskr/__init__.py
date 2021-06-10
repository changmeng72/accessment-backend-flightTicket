from flask import Flask
from flask_restful import Api


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')    
    
    api = Api(app)    
     
    with app.app_context():
        from .flights import TicketRoute,  FlightRoute
        api.add_resource(TicketRoute,"/api/tickets")
        api.add_resource(FlightRoute,"/api/flights")
         
      
    return app
    
 






 