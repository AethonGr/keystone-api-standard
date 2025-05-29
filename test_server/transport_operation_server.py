"""
This script defines a simple Flask server for managing transport operation-related
API endpoints. It initializes the server, sets up the API endpoints, and provides
methods for handling HTTP requests related to transport operations data.

The server is designed to work with the `OrchestratorAPI`, which manages the
transport operation data. The endpoints are defined in a separate YAML file and
are loaded into the server using the `EndpointsHandler` class.
"""

from flask import Flask

from .api_demonstration import EndpointsHandler, OrchestratorAPI


class TransportOperationServer:
    """Sample server for Transport Operation API."""

    def __init__(self):
        """
        Initialize Flask app and Keystone API Standard.

        This method sets up:
        - A Flask application for handling HTTP requests.
        - The OrchestratorAPI for managing transport operation data.
        - EndpointsHandler for managing the API endpoints.
        """
        # Initialize Flask app
        self.app = Flask(__name__)

        # Initialize Keystone API Standard
        self.orchestrator_api = OrchestratorAPI()

        # Initialize EndpointsHandler
        self.endpoints_handler = EndpointsHandler()

        # Transport Operation endpoints
        self.app.add_url_rule(
            self.endpoints_handler.get_endpoint(
                "transport_operation", "get_transport_operation"
            ),
            "get_transport_operation",
            self.orchestrator_api.get_transport_operation,
            methods=["GET"],
        )
        self.app.add_url_rule(
            self.endpoints_handler.get_endpoint(
                "transport_operation", "get_transport_operation_by_plate_number"
            ),
            "get_transport_operation_by_plate_number",
            self.orchestrator_api.get_transport_operation_by_plate_number,
            methods=["GET"],
        )

    def run(self):
        """
        Run the Flask server.
        """
        # Start the Flask server
        self.app.run()


if __name__ == "__main__":
    server = TransportOperationServer()
    server.run()
