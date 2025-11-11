"""
This script defines a simple Flask server for managing organization API endpoints.
It initializes the server, sets up the API endpoints, and provides methods for
handling HTTP requests related to organization data.

The server is designed to work with the `OrchestratorAPI`, which manages the
organization data. The endpoints are defined in a separate YAML file and
are loaded into the server using the `EndpointsHandler` class.
"""

from flask import Flask

from .api_demonstration import EndpointsHandler, OrchestratorAPI


class OrganizationServer:
    """Sample server for Organization APIs."""

    def __init__(self):
        """
        Initialize Flask app and Keystone API Standard.

        This method sets up:
        - A Flask application for handling HTTP requests.
        - The OrchestratorAPI for managing organization data.
        - EndpointsHandler for managing the API endpoints.
        """
        # Initialize Flask app
        self.app = Flask(__name__)

        # Initialize Keystone API Standard
        self.orchestrator_api = OrchestratorAPI()

        # Initialize EndpointsHandler
        self.endpoints_handler = EndpointsHandler()

        # Organization endpoints
        self.app.add_url_rule(
            self.endpoints_handler.get_endpoint("organization", "get_organization"),
            "get_organization",
            self.orchestrator_api.get_organization,
            methods=["GET"],
        )

    def run(self):
        """
        Run the Flask server.
        """
        # Start the Flask server
        self.app.run()


if __name__ == "__main__":
    # Initialize the OrganizationServer class
    server = OrganizationServer()

    # Run the server
    server.run()
