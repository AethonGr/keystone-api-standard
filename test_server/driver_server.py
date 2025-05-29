"""
This script defines a simple Flask server for managing driver-related API endpoints.
It initializes the server, sets up the API endpoints, and provides methods for handling
HTTP requests related to drivers data.

The server is designed to work with the `OrchestratorAPI`, which manages the driver data.
The endpoints are defined in a separate YAML file and are loaded into the server using
the `EndpointsHandler` class.
"""

from flask import Flask

from .api_demonstration import EndpointsHandler, OrchestratorAPI


class DriverServer:
    """Sample server for Driver API."""

    def __init__(self):
        """
        Initialize Flask app and Keystone API Standard.

        This method sets up:
        - A Flask application for handling HTTP requests.
        - The OrchestratorAPI for managing driver data.
        - EndpointsHandler for managing the API endpoints.
        """
        # Initialize Flask app
        self.app = Flask(__name__)

        # Initialize Keystone API Standard
        self.orchestrator_api = OrchestratorAPI()

        # Initialize EndpointsHandler
        self.endpoints_handler = EndpointsHandler()

        # Driver endpoints
        self.app.add_url_rule(
            self.endpoints_handler.get_endpoint("driver", "get_driver"),
            "get_driver",
            self.orchestrator_api.get_driver,
            methods=["GET"],
        )

        self.app.add_url_rule(
            self.endpoints_handler.get_endpoint(
                "driver", "get_tachograph_card_by_vat_and_tachograph_card_id"
            ),
            "get_tachograph_card_by_vat_and_tachograph_card_id",
            self.orchestrator_api.get_tachograph_card_by_vat_and_tachograph_card_id,
            methods=["GET"],
        )

    def run(self):
        """
        Run the Flask server.
        """
        # Start the Flask server
        self.app.run()


if __name__ == "__main__":
    server = DriverServer()
    server.run()
