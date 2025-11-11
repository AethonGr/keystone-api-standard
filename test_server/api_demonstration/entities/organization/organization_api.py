"""
This module defines the `OrganizationAPI` class, which provides methods to handle
organization-related API endpoints. It includes methods for creating, retrieving,
updating, and deleting organization data.

The `OrganizationAPI` class interacts with the `OrganizationAccess` class to perform
database operations. It uses Flask's jsonify and request modules to handle
HTTP requests and responses. The API methods return JSON responses with
appropriate status codes, including success messages, error messages,
and the requested data.
"""

from flask import Response, jsonify, request

from ...data_model import Organization

from .organization_access import OrganizationAccess


class OrganizationAPI:
    """
    Handles organization-related API endpoints.

    This class provides methods to create, retrieve, update, and delete organization data.
    """

    def __init__(self):
        """
        Initializes the OrganizationAPI.
        """
        # Initialize the OrganizationAccess instance for accessing organization data
        self.organization_access = OrganizationAccess()

    def add_organization(self) -> Response:
        """
        Create new organization data.

        Args:
            None

        Returns:
            Response: The response indicating success or failure with status code.
        """
        try:
            # Parse JSON data from the request body
            data = request.get_json()

            # Validate and map data to the Organization model
            validated_data = Organization(**data)

            # Call sub-API to add data
            organization_data = self.organization_access.add_organization(
                validated_data
            )

            return (
                jsonify(
                    {
                        "message": "Organization data created successfully",
                        # Serialize the response data
                        "data": organization_data.model_dump(),
                    }
                ),
                # HTTP status code for resource creation
                201,
            )

        except ValueError as e:
            # Handle bad request errors
            return jsonify({"error": "Bad request", "message": str(e)}), 400

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_organization(self) -> Response:
        """
        Get all organization data, optionally filtered by type.

        Args:
            None

        Returns:
            Response: The response containing the organization data or error message.
        """
        try:
            # Get organization type from query parameters
            organization_type = request.args.get("type")

            # Fetch all organization data
            organization_data = self.organization_access.get_organization(
                organization_type
            )

            if organization_data:
                # Validate and map each record
                validated_data = [Organization(**data) for data in organization_data]

                return (
                    jsonify(
                        {
                            "message": "Organization data retrieved successfully",
                            # Serialize each record
                            "data": [org.model_dump() for org in validated_data],
                        }
                    ),
                    # HTTP status code for success
                    200,
                )
            else:
                # Handle case where no data is found
                return (
                    jsonify(
                        {
                            "error": "Not Found",
                            "message": "No organizations found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_organization_by_id(self, organization_id: int) -> Response:
        """
        Get organization data by organization ID.

        Args:
            organization_id (int): The ID of the organization.

        Returns:
            Response: The response containing the organization data or error message.
        """
        try:
            # Validate required parameters
            if not organization_id:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Organization ID is required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get organization data
            organization_data = self.organization_access.get_organization_by_id(
                organization_id
            )

            # Check if organization data is found
            if organization_data:
                # Validate and map data to the Organization model
                validated_data = Organization(**organization_data)

                return (
                    jsonify(
                        {
                            "message": "Organization data retrieved successfully",
                            # Serialize the response data
                            "data": validated_data.model_dump(),
                        }
                    ),
                    # HTTP status code for success
                    200,
                )
            else:
                return (
                    jsonify(
                        {
                            "error": "Not Found",
                            "message": "Organization not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def update_organization_by_id(self, organization_id: int) -> Response:
        """
        Update organization data by organization ID.

        Args:
            organization_id (int): The ID of the organization.

        Returns:
            Response: The response indicating success or failure with status code.
        """
        try:
            # Validate required parameters
            if not organization_id:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Organization ID is required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get organization data
            organization_data = self.organization_access.get_organization_by_id(
                organization_id
            )

            # Check if organization data is found
            if not organization_data:
                return (
                    jsonify(
                        {
                            "error": "Not Found",
                            "message": "Organization not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

            # Parse JSON data from the request body
            data = request.get_json()

            # Call sub-API to update organization data
            updated_organization_data = (
                self.organization_access.update_organization_by_id(
                    organization_id, data
                )
            )

            # Validate and map data to the Organization model
            validated_updated_organization_data = Organization(
                **updated_organization_data
            )

            return (
                jsonify(
                    {
                        "message": "Organization data updated successfully",
                        # Serialize the response data
                        "data": validated_updated_organization_data.model_dump(),
                    }
                ),
                # HTTP status code for successful update
                200,
            )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def delete_organization_by_id(self, organization_id: int) -> Response:
        """
        Delete specific organization data by organization ID.

        Args:
            organization_id (int): The ID of the organization.

        Returns:
            Response: The response indicating success or failure with status code.
        """
        try:
            # Validate required parameters
            if not organization_id:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Organization ID is required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to delete data
            is_deleted = self.organization_access.delete_organization_by_id(
                organization_id
            )

            # Check if the deletion was successful
            if is_deleted:
                return (
                    jsonify(
                        {
                            "message": "Organization data deleted successfully",
                        }
                    ),
                    # HTTP status code for successful deletion
                    204,
                )

            # Handle case where the organization is not found
            return (
                jsonify(
                    {
                        "error": "Not Found",
                        "message": "Organization not found",
                    }
                ),
                # HTTP status code for resource not found
                404,
            )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500
