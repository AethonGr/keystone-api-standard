"""
This module defines the EndpointsHandler class, which is responsible for loading and
managing API endpoints defined in a YAML file. The class provides methods to retrieve
specific endpoints based on a parent key and a endpoint key.
"""

from typing import Any, Dict
import os
import yaml


class EndpointsHandler:
    """
    A class to handle and provide access to API endpoints.

    This class loads endpoints from a YAML file and provides methods to retrieve
    specific endpoints based on a parent key and a endpoint key. The endpoints are
    structured, allowing for easy access and management of API endpoints.
    """

    def __init__(self, endpoints_file: str = "endpoints.yaml") -> None:
        """
        Initialize the EndpointsHandler by loading endpoints from a YAML file.

        Args:
            endpoints_file (str): Path to the YAML file containing endpoint definitions.
        """
        # Resolve the path to the YAML file in the same directory as this script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        endpoints_path = os.path.join(script_dir, endpoints_file)

        # Load the endpoints from the specified YAML file
        with open(endpoints_path, "r") as file:
            self.endpoints: Dict[str, Any] = yaml.safe_load(file)

    def get_endpoint(self, parent: str, endpoint: str) -> str:
        """
        Retrieve a endpoint by its parent and specific endpoint key.

        Args:
            parent (str): The parent key in the endpoint hierarchy.
            endpoint (str): The specific endpoint key under the parent.

        Returns:
            str: The endpoint string corresponding to the parent and endpoint keys.
        """
        # Check if the parent and endpoint exist in the endpoints dictionary
        if parent not in self.endpoints:
            raise KeyError(
                f"Parent key '{parent}' not found in the endpoint hierarchy."
            )

        # Check if the endpoint exists under the specified parent
        if endpoint not in self.endpoints[parent]:
            raise KeyError(
                f"Endpoint key '{endpoint}' not found under parent '{parent}'."
            )

        # Return the endpoint string
        return self.endpoints[parent][endpoint]
