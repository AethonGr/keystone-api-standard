"""
This module defines the `DriverAPI` class, which provides methods to handle
driver-related API endpoints. It includes methods for creating, retrieving,
updating, and deleting driver data, as well as retrieving information about
driver's licenses, tachograph cards, and traffic violations.

The `DriverAPI` class interacts with the `DriverAccess` class to perform
database operations. It uses Flask's jsonify and request modules to handle
HTTP requests and responses. The API methods return JSON responses with
appropriate status codes, including success messages, error messages,
and the requested data.
"""

from flask import Response, jsonify, request

from ...data_model import Driver, License, TachographCard, TrafficViolation

from .driver_access import DriverAccess


class DriverAPI:
    """
    Handles driver-related API endpoints.

    This class provides methods to create, retrieve, update, and delete driver data,
    as well as to retrieve information about driver's licenses, tachograph cards,
    and traffic violations.
    """

    def __init__(self):
        """
        Initializes the DriverAPI.
        """
        # Initialize the DriverAccess instance for accessing driver data
        self.driver_access = DriverAccess()

    def add_driver(self) -> Response:
        """
        Create new driver data.

        Args:
            None

        Returns:
            Response: The response indicating success or failure with status code.
        """
        try:
            # Parse JSON data from the request body
            data = request.get_json()

            # Validate and map data to the Driver model
            validated_data = Driver(**data)

            # Call sub-API to add data
            driver_data = self.driver_access.add_driver(validated_data)

            return (
                jsonify(
                    {
                        "message": "Driver data created successfully",
                        # Serialize the response data
                        "data": driver_data.model_dump(),
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

    def get_driver(self) -> Response:
        """
        Get all driver data.

        Args:
            None

        Returns:
            Response: The response containing the driver data or error message.
        """
        try:
            # Fetch all driver data
            driver_data = self.driver_access.get_driver()

            # Check if driver data is found
            if driver_data:
                # Validate and map each record
                validated_data = [Driver(**data) for data in driver_data]

                return (
                    jsonify(
                        {
                            "message": "Driver data retrieved successfully",
                            # Serialize each record
                            "data": [driver.model_dump() for driver in validated_data],
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
                            "message": "Driver data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_driver_by_vat(self, countryCode: str, vat: str) -> Response:
        """
        Get driver data by country code and vat number.

        Args:
            countryCode (str): Country code of vehicle registration
            vat (str): Vat number of the driver

        Returns:
            Response: The response with the driver data or error message.
        """
        try:
            # Validate required parameters
            if not countryCode or not vat:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Country code and vat number are required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get driver data
            driver_data = self.driver_access.get_driver_by_vat(countryCode, vat)

            # Check if driver data is found
            if driver_data:
                # Validate and map data to the Driver model
                validated_data = Driver(**driver_data)
                return (
                    jsonify(
                        {
                            "message": "Driver data retrieved successfully",
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
                            "message": "Driver data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def update_driver_by_vat(self, countryCode: str, vat: str) -> Response:
        """
        Update driver data by country code and vat number.

        Args:
            countryCode (str): Country code of vehicle registration
            vat (str): Vat number of the driver

        Returns:
            Response: The response with the updated driver data or error message.
        """
        try:
            # Validate required parameters
            if not countryCode or not vat:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Country code and vat number are required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get driver data
            driver_data = self.driver_access.get_driver_by_vat(countryCode, vat)

            # Check if driver data is found
            if not driver_data:
                return (
                    jsonify(
                        {
                            "error": "Not Found",
                            "message": "Driver data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

            # Parse JSON data from the request body
            data = request.get_json()

            # Call sub-API to update driver data
            updated_driver_data = self.driver_access.update_driver_by_vat(
                countryCode, vat, data
            )

            # Validate and map data to the Driver model
            validated_updated_driver_data = Driver(**updated_driver_data)

            return (
                jsonify(
                    {
                        "message": "Driver data updated successfully",
                        # Serialize the response data
                        "data": validated_updated_driver_data.model_dump(),
                    }
                ),
                # HTTP status code for successful update
                200,
            )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def delete_driver_by_vat(self, countryCode: str, vat: str) -> Response:
        """
        Delete specific driver data.

        Args:
            countryCode (str): Country code of vehicle registration
            vat (str): Vat number of the driver

        Returns:
            Response: The response indicating success or error with status code.
        """
        try:
            # Validate required parameters
            if not countryCode or not vat:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Country code and vat number are required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to delete data
            is_deleted = self.driver_access.get_driver_by_vat(countryCode, vat)

            # Check if the deletion was successful
            if is_deleted:
                return (
                    jsonify(
                        {
                            "message": "Driver data deleted successfully",
                        }
                    ),
                    # HTTP status code for successful deletion
                    200,
                )

            # Handle case where the driver is not found
            return (
                jsonify(
                    {
                        "error": "Not Found",
                        "message": "Driver data not found",
                    }
                ),
                # HTTP status code for resource not found
                404,
            )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_license_by_vat(self, countryCode: str, vat: str) -> Response:
        """
        Get details about the driver's license by country code and vat number.

        Args:
            countryCode (str): Country code of vehicle registration
            vat (str): Vat number of the driver

        Returns:
            Response: The response with the license data or error message.
        """
        try:
            # Validate required parameters
            if not countryCode or not vat:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Country code and vat number are required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get license data
            license_data = self.driver_access.get_license_by_vat(countryCode, vat)

            # Check if license data is found
            if license_data:
                # Validate and map data to the License model
                validated_data = License(**license_data)
                return (
                    jsonify(
                        {
                            "message": "License data retrieved successfully",
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
                            "message": "License data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_traffic_violation_by_vat(self, countryCode: str, vat: str) -> Response:
        """
        Get details about the driver's traffic violations by country code and vat number.

        Args:
            countryCode (str): Country code of vehicle registration
            vat (str): Vat number of the driver

        Returns:
            Response: The response with the traffic violation data or error message.
        """
        try:
            # Validate required parameters
            if not countryCode or not vat:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Country code and vat number are required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get traffic violation data
            traffic_violation_data = self.driver_access.get_traffic_violation_by_vat(
                countryCode, vat
            )

            # Check if traffic violation data is found
            if traffic_violation_data:
                # Validate and map each record to the TrafficViolation model
                validated_data = [
                    TrafficViolation(**data) for data in traffic_violation_data
                ]

                return (
                    jsonify(
                        {
                            "message": "Driver's traffic violation data retrieved successfully",
                            # Serialize each record
                            "data": [
                                traffic_violation.model_dump()
                                for traffic_violation in validated_data
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
                            "message": "Driver's traffic violation data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_traffic_violation_by_vat_and_traffic_violation_id(
        self, countryCode: str, vat: str, trafficViolationId: int
    ) -> Response:
        """
        Get specific driver's traffic violation data by country code, vat number and traffic violation id.

        Args:
            countryCode (str): Country code of vehicle registration
            vat (str): Vat number of the driver
            trafficViolationId (int): Traffic violation ID

        Returns:
            Response: The response with the traffic violation data or error message.
        """
        try:
            # Validate required parameters
            if not countryCode or not vat or not trafficViolationId:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Country code, vat number and traffic violation ID are required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get traffic violation data
            traffic_violation_data = self.driver_access.get_traffic_violation_by_vat_and_traffic_violation_id(
                countryCode, vat, trafficViolationId
            )

            # Check if traffic violation data is found
            if traffic_violation_data:
                # Validate and map data to the TrafficViolation model
                validated_data = TrafficViolation(**traffic_violation_data)

                return (
                    jsonify(
                        {
                            "message": "Driver's traffic violation data retrieved successfully",
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
                            "message": "Driver's traffic violation data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_tachograph_card_by_vat(self, countryCode: str, vat: str) -> Response:
        """
        Get details about the driver's tachograph cards data by country code and vat number.

        Args:
            countryCode (str): Country code of vehicle registration
            vat (str): Vat number of the driver

        Returns:
            Response: The response with the tachograph card data or error message.
        """
        try:
            # Validate required parameters
            if not countryCode or not vat:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Country code and plate number are required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get tachograph card data
            tachograph_card_data = self.driver_access.get_tachograph_card_by_vat(
                countryCode, vat
            )

            # Check if tachograph card data is found
            if tachograph_card_data:
                # Validate and map each record to the TachographCard model
                validated_data = [
                    TachographCard(**data) for data in tachograph_card_data
                ]

                return (
                    jsonify(
                        {
                            "message": "Tachograph card data retrieved successfully",
                            # Serialize each record
                            "data": [
                                tachograph_card.model_dump()
                                for tachograph_card in validated_data
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
                            "message": "Tachograph card data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_tachograph_card_by_vat_and_tachograph_card_id(
        self, countryCode: str, vat: str, tachographCardId: str
    ) -> Response:
        """
        Get specific driver's tachograph card data by country code, vat number and tachograph card id.

        Args:
            countryCode (str): Country code of vehicle registration
            vat (str): Vat number of the driver
            tachographCardId (str): Tachograph card ID

        Returns:
            Response: The response with the tachograph card data or error message.
        """
        try:
            # Validate required parameters
            if not countryCode or not vat or not tachographCardId:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Country code, vat number and tachograph card ID are required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get tachograph card data
            tachograph_card_data = (
                self.driver_access.get_tachograph_card_by_vat_and_tachograph_card_id(
                    countryCode, vat, tachographCardId
                )
            )

            # Check if tachograph card data is found
            if tachograph_card_data:
                # Validate and map data to the TachographCard model
                validated_data = TachographCard(**tachograph_card_data)

                return (
                    jsonify(
                        {
                            "message": "Tachograph card data retrieved successfully",
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
                            "message": "Tachograph card data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500
