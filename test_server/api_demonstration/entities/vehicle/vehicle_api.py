"""
This module defines the `VehicleAPI` class, which provides methods to handle
vehicle-related API endpoints. It includes methods for creating, retrieving,
updating, and deleting vehicle data, as well as retrieving information about
geolocation, owner, insurance, and revision details.

The `VehicleAPI` class interacts with the `VehicleAccess` class to perform
database operations. It uses Flask's jsonify and request modules to handle
HTTP requests and responses. The API methods return JSON responses with
appropriate status codes, including success messages, error messages,
and the requested data.
"""

from flask import Response, jsonify, request

from ...data_model import Geolocation, Insurance, Owner, Revision, Vehicle

from .vehicle_access import VehicleAccess


class VehicleAPI:
    """
    Handles vehicle-related API endpoints.

    This class provides methods to create, retrieve, update, and delete vehicle data,
    as well as to manage geolocation, owner, insurance, and revision information.
    """

    def __init__(self):
        """
        Initializes the VehicleAPI.
        """
        # Initialize the VehicleAccess instance for accessing vehicle data
        self.vehicle_access = VehicleAccess()

    def add_vehicle(self) -> Response:
        """
        Create new vehicle data.

        Args:
            None

        Returns:
            Response: The response indicating success or failure with status code.
        """
        try:
            # Parse JSON data from the request body
            data = request.get_json()

            # Validate and map data to the Vehicle model
            validated_data = Vehicle(**data)

            # Call sub-API to add data
            vehicle_data = self.vehicle_access.add_vehicle(validated_data)

            return (
                jsonify(
                    {
                        "message": "Vehicle data created successfully",
                        # Serialize the response data
                        "data": vehicle_data.model_dump(),
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

    def get_vehicle(self) -> Response:
        """
        Get all vehicle data.

        Args:
            None

        Returns:
            Response: The response containing the vehicle data or error message.
        """
        try:
            # Fetch all vehicle data
            vehicle_data = self.vehicle_access.get_vehicle()

            if vehicle_data:
                # Validate and map each record
                validated_data = [Vehicle(**data) for data in vehicle_data]

                return (
                    jsonify(
                        {
                            "message": "Vehicle data retrieved successfully",
                            # Serialize each record
                            "data": [
                                vehicle.model_dump() for vehicle in validated_data
                            ],
                        }
                    ),
                    # HTTP status code for successful retrieval
                    200,
                )
            else:
                # Handle case where no data is found
                return (
                    jsonify(
                        {
                            "error": "Not Found",
                            "message": "Vehicle data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_vehicle_by_plate_number(
        self, countryCode: str, plateNumber: str
    ) -> Response:
        """
        Get vehicle data by country code and license plate number.

        Args:
            countryCode (str): The country code of the vehicle
            plateNumber (str): The license plate number of the vehicle

        Returns:
            Response: The response with the vehicle data or error message.
        """
        try:
            # Validate required parameters
            if not countryCode or not plateNumber:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Country code and license plate number are required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get vehicle data
            vehicle_data = self.vehicle_access.get_vehicle_by_plate_number(
                countryCode, plateNumber
            )

            # Check if vehicle data is found
            if vehicle_data:
                # Validate and map data to the Vehicle model
                validated_data = Vehicle(**vehicle_data)

                return (
                    jsonify(
                        {
                            "message": "Vehicle data retrieved successfully",
                            # Serialize the response data
                            "data": validated_data.model_dump(),
                        }
                    ),
                    # HTTP status code for successful retrieval
                    200,
                )
            else:
                return (
                    jsonify(
                        {
                            "error": "Not Found",
                            "message": "Vehicle data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def update_vehicle_by_plate_number(
        self, countryCode: str, plateNumber: str
    ) -> Response:
        """
        Update vehicle data by country code and license plate number.

        Args:
            countryCode (str): The country code of the vehicle
            plateNumber (str): The license plate number of the vehicle

        Returns:
            Response: The response with the updated vehicle data or error message.
        """
        try:
            # Validate required parameters
            if not countryCode or not plateNumber:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Country code and license plate number are required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get vehicle data
            vehicle_data = self.vehicle_access.get_vehicle_by_plate_number(
                countryCode, plateNumber
            )

            # Check if vehicle data is found
            if not vehicle_data:
                return (
                    jsonify(
                        {
                            "error": "Not Found",
                            "message": "Vehicle data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

            # Parse JSON data from the request body
            data = request.get_json()

            # Call sub-API to update vehicle data
            updated_vehicle_data = self.vehicle_access.update_vehicle_by_plate_number(
                countryCode, plateNumber, data
            )

            # Validate and map data to the Vehicle model
            validated_updated_vehicle_data = Vehicle(**updated_vehicle_data)

            return (
                jsonify(
                    {
                        "message": "Vehicle data updated successfully",
                        # Serialize the response data
                        "data": validated_updated_vehicle_data.model_dump(),
                    }
                ),
                # HTTP status code for successful update
                200,
            )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def delete_vehicle_by_plate_number(
        self, countryCode: str, plateNumber: str
    ) -> Response:
        """
        Delete specific vehicle data by country code and license plate number.

        Args:
            countryCode (str): The country code of the vehicle
            plateNumber (str): The license plate number of the vehicle

        Returns:
            Response: The response indicating success or error with status code.
        """
        try:
            # Validate required parameters
            if not countryCode or not plateNumber:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Country code and license plate number are required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to delete data
            is_deleted = self.vehicle_access.delete_vehicle_by_plate_number(
                countryCode, plateNumber
            )

            # Check if the deletion was successful
            if is_deleted:
                return (
                    jsonify(
                        {
                            "message": "Vehicle data deleted successfully",
                        }
                    ),
                    # HTTP status code for successful deletion
                    200,
                )

            # Handle case where the vehicle is not found
            return (
                jsonify(
                    {
                        "error": "Not Found",
                        "message": "Vehicle data not found",
                    }
                ),
                # HTTP status code for resource not found
                404,
            )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_geolocation_by_plate_number(
        self, countryCode: str, plateNumber: str
    ) -> Response:
        """
        Get details about the geolocation of vehicle by country code and license plate number.

        Args:
            countryCode (str): The country code of the vehicle
            plateNumber (str): The license plate number of the vehicle

        Returns:
            Response: The response with the vehicle data or error message.
        """
        try:
            # Validate required parameters
            if not countryCode or not plateNumber:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Country code and license plate number are required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get geolocation data
            geolocation_data = self.vehicle_access.get_geolocation_by_plate_number(
                countryCode, plateNumber
            )

            # Check if geolocation data is found
            if geolocation_data:
                # Validate and map data to the Geolocation model
                validated_data = Geolocation(**geolocation_data)

                return (
                    jsonify(
                        {
                            "message": "Geolocation data retrieved successfully",
                            # Serialize the response data
                            "data": validated_data.model_dump(),
                        }
                    ),
                    # HTTP status code for successful retrieval
                    200,
                )
            else:
                return (
                    jsonify(
                        {
                            "error": "Not Found",
                            "message": "Geolocation data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def append_geolocation_by_plate_number(
        self, countryCode: str, plateNumber: str
    ) -> Response:
        """
        Append new vehicle's geolocation data by country code and license plate number.

        Args:
            countryCode (str): The country code of the vehicle
            plateNumber (str): The license plate number of the vehicle

        Returns:
            Response: The response with the updated vehicle data or error message.
        """
        try:
            # Validate required parameters
            if not countryCode or not plateNumber:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Country code and license plate number are required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get vehicle data
            vehicle_data = self.vehicle_access.get_vehicle_by_plate_number(
                countryCode, plateNumber
            )

            # Check if vehicle data is found
            if not vehicle_data:
                return (
                    jsonify(
                        {
                            "error": "Not Found",
                            "message": "Vehicle data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

            # Parse JSON data from the request body
            data = request.get_json()

            # Call sub-API to append geolocation data
            appended_geolocation_data = (
                self.vehicle_access.append_geolocation_by_plate_number(
                    countryCode, plateNumber, data
                )
            )

            # Validate and map data to the Geolocation model
            validated_appended_geolocation_data = Geolocation(
                **appended_geolocation_data
            )

            return (
                jsonify(
                    {
                        "message": "Geolocation data appended successfully",
                        # Serialize the response data
                        "data": validated_appended_geolocation_data.model_dump(),
                    }
                ),
                # HTTP status code for successful append
                200,
            )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_owner_by_plate_number(self, countryCode: str, plateNumber: str) -> Response:
        """
        Get details about the owner of vehicle by country code and license plate number.

        Args:
            countryCode (str): The country code of the vehicle
            plateNumber (str): The license plate number of the vehicle

        Returns:
            Response: The response with the vehicle data or error message.
        """
        try:
            # Validate required parameters
            if not countryCode or not plateNumber:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Country code and license plate number are required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get owner data
            owner_data = self.vehicle_access.get_owner_by_plate_number(
                countryCode, plateNumber
            )

            # Check if owner data is found
            if owner_data:
                # Validate and map data to the Owner model
                validated_data = Owner(**owner_data)

                return (
                    jsonify(
                        {
                            "message": "Owner data retrieved successfully",
                            # Serialize the response data
                            "data": validated_data.model_dump(),
                        }
                    ),
                    # HTTP status code for successful retrieval
                    200,
                )
            else:
                return (
                    jsonify(
                        {
                            "error": "Not Found",
                            "message": "Owner data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_insurance_by_plate_number(
        self, countryCode: str, plateNumber: str
    ) -> Response:
        """
        Get details about the insurances of vehicle by country code and license plate number.

        Args:
            countryCode (str): The country code of the vehicle
            plateNumber (str): The license plate number of the vehicle

        Returns:
            Response: The response with the vehicle data or error message.
        """
        try:
            # Validate required parameters
            if not countryCode or not plateNumber:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Country code and license plate number are required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get insurance data
            insurance_data = self.vehicle_access.get_insurance_by_plate_number(
                countryCode, plateNumber
            )

            # Check if insurance data is found
            if insurance_data:
                # Validate and map each record to the Insurance model
                validated_data = [Insurance(**data) for data in insurance_data]

                return (
                    jsonify(
                        {
                            "message": "Insurance data retrieved successfully",
                            # Serialize each record
                            "data": [
                                insurance.model_dump() for insurance in validated_data
                            ],
                        }
                    ),
                    # HTTP status code for successful retrieval
                    200,
                )
            else:
                return (
                    jsonify(
                        {
                            "error": "Not Found",
                            "message": "Insurance data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_insurance_by_plate_number_and_insurance_id(
        self, countryCode: str, plateNumber: str, insuranceId: int
    ) -> Response:
        """
        Get details about the insurance of vehicle by country code, license plate number and insurance id.

        Args:
            countryCode (str): Country code of vehicle registration
            plateNumber (str): License plate number
            insuranceId (int): Insurance ID

        Returns:
            Response: The response with the insurance data or error message.
        """
        try:
            # Validate required parameters
            if not countryCode or not plateNumber or not insuranceId:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Country code, plate number and insurance ID are required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get insurance data
            insurance_data = (
                self.vehicle_access.get_insurance_by_plate_number_and_insurance_id(
                    countryCode, plateNumber, insuranceId
                )
            )

            # Check if insurance data is found
            if insurance_data:
                # Validate and map data to the Insurance model
                validated_data = Insurance(**insurance_data)

                return (
                    jsonify(
                        {
                            "message": "Insurance data retrieved successfully",
                            # Serialize the response data
                            "data": validated_data.model_dump(),
                        }
                    ),
                    # HTTP status code for successful retrieval
                    200,
                )
            else:
                return (
                    jsonify(
                        {
                            "error": "Not Found",
                            "message": "Insurance data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_revision_by_plate_number(
        self, countryCode: str, plateNumber: str
    ) -> Response:
        """
        Get details about the revisions of vehicle by country code and license plate number.

        Args:
            countryCode (str): The country code of the vehicle
            plateNumber (str): The license plate number of the vehicle

        Returns:
            Response: The response with the vehicle data or error message.
        """
        try:
            # Validate required parameters
            if not countryCode or not plateNumber:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Country code and license plate number are required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get revision data
            revision_data = self.vehicle_access.get_revision_by_plate_number(
                countryCode, plateNumber
            )

            # Check if revision data is found
            if revision_data:
                # Validate and map each record to the Revision model
                validated_data = [Revision(**data) for data in revision_data]

                return (
                    jsonify(
                        {
                            "message": "Revision data retrieved successfully",
                            # Serialize each record
                            "data": [
                                revision.model_dump() for revision in validated_data
                            ],
                        }
                    ),
                    # HTTP status code for successful retrieval
                    200,
                )
            else:
                return (
                    jsonify(
                        {
                            "error": "Not Found",
                            "message": "Revision data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_revision_by_plate_number_and_revision_id(
        self, countryCode: str, plateNumber: str, revisionId: int
    ) -> Response:
        """
        Get details about the revision of vehicle by country code, license plate number and revision id.

        Args:
            countryCode (str): Country code of vehicle registration
            plateNumber (str): License plate number
            revisionId (int): Revision ID

        Returns:
            Response: The response with the revision data or error message.
        """
        try:
            # Validate required parameters
            if not countryCode or not plateNumber or not revisionId:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Country code, plate number and revision ID are required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get revision data
            revision_data = (
                self.vehicle_access.get_revision_by_plate_number_and_revision_id(
                    countryCode, plateNumber, revisionId
                )
            )

            # Check if revision data is found
            if revision_data:
                # Validate and map data to the Revision models
                validated_data = Revision(**revision_data)

                return (
                    jsonify(
                        {
                            "message": "Revision data retrieved successfully",
                            # Serialize the response data
                            "data": validated_data.model_dump(),
                        }
                    ),
                    # HTTP status code for successful retrieval
                    200,
                )
            else:
                # Handle case where no data is found
                return (
                    jsonify(
                        {
                            "error": "Not Found",
                            "message": "Revision data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500
