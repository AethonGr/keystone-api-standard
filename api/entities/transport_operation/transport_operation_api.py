"""
This module defines the `TransportOperationAPI` class, which provides methods to handle
transport operation-related API endpoints. It includes methods for creating, reading,
updating, and deleting transport operation data, as well as managing related schedule,
phase, and document data.

The `TransportOperationAPI` class interacts with the `TransportOperationAccess` class
to perform database operations. It uses Flask's jsonify and request modules to handle
HTTP requests and responses. The API methods return JSON responses with
appropriate status codes, including success messages, error messages,
and the requested data.
"""

from uuid import UUID

from flask import Response, jsonify, request

from ...data_model import (
    Document,
    EcmrModel,
    Location,
    Mode,
    Phase,
    Schedule,
    TransportOperation,
)
from .transport_operation_access import TransportOperationAccess


class TransportOperationAPI:
    """
    Handles transport operation-related API endpoints.

    This class provides methods to create, read, update, and delete transport operation data,
    as well as manage related schedule, phase, and document data.
    """

    def __init__(self):
        """
        Initialize the TransportOperationAPI.
        """
        # Initialize the TransportOperationAccess instance for accessing transport operation data
        self.transport_operation_access = TransportOperationAccess()

    def add_transport_operation(self) -> Response:
        """
        Create new transport operation data.

        Args:
            None

        Returns:
            Response: The response indicating success or error with status code.
        """
        try:
            # Parse JSON data from the request body
            data = request.get_json()

            # Validate and map data to the TransportOperation model
            validated_data = TransportOperation(**data)

            # Call sub-API to add data
            transport_operation_data = (
                self.transport_operation_access.add_transport_operation(validated_data)
            )

            return (
                jsonify(
                    {
                        "message": "Transport operation data created successfully",
                        # Serialize the response data
                        "data": transport_operation_data.model_dump(),
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

    def get_transport_operation(self) -> Response:
        """
        Get all transport operation data.

        Args:
            None

        Returns:
            Response: The response with the transport operation data or error message.
        """
        try:
            # Get query parameters
            operator_id = request.args.get("operatorId")
            driver_id = request.args.get("driverId")
            location_mode = request.args.get("locationMode")
            starting_point_international_code = request.args.get(
                "startingPointInternationalCode"
            )
            ending_point_international_code = request.args.get(
                "endingPointInternationalCode"
            )

            # Call sub-API to get data
            transport_operation_data = (
                self.transport_operation_access.get_transport_operation(
                    operator_id,
                    driver_id,
                    location_mode,
                    starting_point_international_code,
                    ending_point_international_code,
                )
            )

            # Check if data is available
            if transport_operation_data:
                # Validate and map each record
                validated_data = [
                    TransportOperation(**data) for data in transport_operation_data
                ]

                return (
                    jsonify(
                        {
                            "message": "Transport operation data retrieved successfully",
                            # Serialize each record
                            "data": [
                                transport_operation.model_dump()
                                for transport_operation in validated_data
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
                            "message": "Transport operation data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_transport_operation_by_id(self, transportOperationId: int) -> Response:
        """
        Get a specific transport operation data by ID.

        Args:
            transportOperationId (int): Unique transport operation identifier

        Returns:
            Response: The response with the transport operation data or error message.
        """
        try:
            # Get query parameters
            operator_id = request.args.get("operatorId")

            # Validate required parameters
            if not transportOperationId:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Transport operation ID is required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get data
            transport_operation_data = (
                self.transport_operation_access.get_transport_operation_by_id(
                    transportOperationId, operator_id
                )
            )

            # Check if data is available
            if transport_operation_data:
                # Validate and map data to the TransportOperation model
                validated_data = TransportOperation(**transport_operation_data)

                return (
                    jsonify(
                        {
                            "message": "Transport operation data retrieved successfully",
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
                            "message": "Transport operation data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def update_transport_operation_by_id(self, transportOperationId: int) -> Response:
        """
        Update data for a specific transport operation by ID.

        Args:
            transportOperationId (int): Unique transport operation identifier

        Returns:
            Response: The response with updated transport operation data or error message.
        """
        try:
            # Validate required parameters
            if not transportOperationId:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Transport operation ID is required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get data
            transport_operation_data = (
                self.transport_operation_access.get_transport_operation_by_id(
                    transportOperationId
                )
            )

            # Check if data is available
            if not transport_operation_data:
                return (
                    jsonify(
                        {
                            "error": "Not Found",
                            "message": "Transport operation data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

            # Parse JSON data from the request body
            data = request.get_json()

            # Call sub-API to update data
            updated_transport_operation_data = (
                self.transport_operation_access.update_transport_operation_by_id(
                    transportOperationId, data
                )
            )

            # Validate and map data to the TransportOperation model
            validated_updated_transport_operation_data = TransportOperation(
                **updated_transport_operation_data
            )

            return (
                jsonify(
                    {
                        "message": "Transport operation data updated successfully",
                        # Serialize the response data
                        "data": validated_updated_transport_operation_data.model_dump(),
                    }
                ),
                # HTTP status code for successful update
                200,
            )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def delete_transport_operation_by_id(self, transportOperationId: int) -> Response:
        """
        Delete specific transport operation data by ID.

        Args:
            transportOperationId (int): Unique transport operation identifier

        Returns:
            Response: The response indicating success or error message.
        """
        try:
            # Validate required parameters
            if not transportOperationId:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Transport operation ID is required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to delete data
            is_deleted = (
                self.transport_operation_access.delete_transport_operation_by_id(
                    transportOperationId
                )
            )

            # Check if the deletion was successful
            if is_deleted:
                return (
                    jsonify(
                        {
                            "message": "Transport operation data deleted successfully",
                        }
                    ),
                    204,  # HTTP status code for successful deletion
                )

            # Handle case where the transport operation is not found
            return (
                jsonify(
                    {
                        "error": "Not Found",
                        "message": "Transport operation data not found",
                    }
                ),
                404,  # HTTP status code for resource not found
            )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_schedule_by_transport_operation_id(
        self, transportOperationId: int
    ) -> Response:
        """
        Get schedule data related to a specific transport operation by ID.

        Args:
            transportOperationId (int): Unique identifier for the transport operation

        Returns:
            Response: The response with the schedule data or error message.
        """
        try:
            # Get query parameters
            operator_id = request.args.get("operatorId")

            # Validate required parameters
            if not transportOperationId:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Transport operation ID is required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get schedule data
            schedule_data = (
                self.transport_operation_access.get_schedule_by_transport_operation_id(
                    transportOperationId, operator_id
                )
            )

            # Check if data is available
            if schedule_data:
                # Validate and map data to the Schedule model
                validated_data = Schedule(**schedule_data)

                return (
                    jsonify(
                        {
                            "message": "Schedule data retrieved successfully",
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
                            "message": "Schedule data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def update_schedule_by_transport_operation_id(
        self, transportOperationId: int
    ) -> Response:
        """
        Update schedule data related to a specific transport operation by ID.

        Args:
            transportOperationId (int): Unique identifier for the transport operation

        Returns:
            Response: The response with the updated schedule data or error message.
        """
        try:
            # Validate required parameters
            if not transportOperationId:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Transport operation ID is required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get transport operation data
            transport_operation_data = (
                self.transport_operation_access.get_transport_operation_by_id(
                    transportOperationId
                )
            )

            # Check if data is available
            if not transport_operation_data:
                return (
                    jsonify(
                        {
                            "error": "Not Found",
                            "message": "Transport operation data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

            # Parse JSON data from the request body
            data = request.get_json()

            # Call sub-API to update schedule data
            updated_schedule_data = self.transport_operation_access.update_schedule_by_transport_operation_id(
                transportOperationId, data
            )

            # Validate and map data to the Schedule model
            validated_updated_schedule_data = Schedule(**updated_schedule_data)

            return (
                jsonify(
                    {
                        "message": "Schedule data updated successfully",
                        # Serialize the response data
                        "data": validated_updated_schedule_data.model_dump(),
                    }
                ),
                # HTTP status code for successful update
                200,
            )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_phase_by_transport_operation_id(
        self, transportOperationId: int
    ) -> Response:
        """
        Get phase data related to a specific transport operation by ID.

        Args:
            transportOperationId (int): Unique identifier for the transport operation

        Returns:
            Response: The response with the phase data or error message.
        """
        try:
            # Get query parameters
            operator_id = request.args.get("operatorId")

            # Validate required parameters
            if not transportOperationId:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Transport operation ID is required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get phase data
            phase_data = (
                self.transport_operation_access.get_phase_by_transport_operation_id(
                    transportOperationId, operator_id
                )
            )

            # Check if data is available
            if phase_data:
                # Validate and map each record to the Phase model
                validated_data = [Phase(**data) for data in phase_data]

                return (
                    jsonify(
                        {
                            "message": "Phase data retrieved successfully",
                            # Serialize each record
                            "data": [phase.model_dump() for phase in validated_data],
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
                            "message": "Phase data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def append_phase_by_transport_operation_id(
        self, transportOperationId: int
    ) -> Response:
        """
        Append phase data for a specific transport operation by ID.

        Args:
            transportOperationId (int): Unique identifier for the transport operation

        Returns:
            Response: The response with the appended phase data or error message.
        """
        try:
            # Validate required parameters
            if not transportOperationId:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Transport operation ID is required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get transport operation data
            transport_operation_data = (
                self.transport_operation_access.get_transport_operation_by_id(
                    transportOperationId
                )
            )

            # Check if data is available
            if not transport_operation_data:
                return (
                    jsonify(
                        {
                            "error": "Not Found",
                            "message": "Transport operation data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

            # Parse JSON data from the request body
            data = request.get_json()

            # Call sub-API to append phase data
            appended_phase_data = (
                self.transport_operation_access.append_phase_by_transport_operation_id(
                    transportOperationId, data
                )
            )

            # Validate and map data to the Phase model
            validated_appended_phase_data = Phase(**appended_phase_data)

            return (
                jsonify(
                    {
                        "message": "Phase data appended successfully",
                        # Serialize the response data
                        "data": validated_appended_phase_data.model_dump(),
                    }
                ),
                # HTTP status code for successful append
                200,
            )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_phase_by_transport_operation_id_and_phase_id(
        self, transportOperationId: int, phaseId: int
    ) -> Response:
        """
        Get specific phase data related to a transport operation by ID and phase ID.

        Args:
            transportOperationId (int): Unique identifier for the transport operation
            phaseId (int): Unique identifier for the phase

        Returns:
            Response: The response with the phase data or error message.
        """
        try:
            # Validate required parameters
            if not transportOperationId or not phaseId:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Transport operation ID and phase ID are required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get phase data
            phase_data = self.transport_operation_access.get_phase_by_transport_operation_id_and_phase_id(
                transportOperationId, phaseId
            )

            # Check if data is available
            if phase_data:
                # Validate and map data to the Phase model
                validated_data = Phase(**phase_data)

                return (
                    jsonify(
                        {
                            "message": "Phase data retrieved successfully",
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
                            "message": "Phase data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def update_phase_by_transport_operation_id_and_phase_id(
        self, transportOperationId: int, phaseId: int
    ) -> Response:
        """
        Update phase data related to a specific transport operation by ID and phase ID.

        Args:
            transportOperationId (int): Unique identifier for the transport operation
            phaseId (int): Unique identifier for the phase

        Returns:
            Response: The response with the updated phase data or error message.
        """
        try:
            # Validate required parameters
            if not transportOperationId or not phaseId:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Transport operation ID and phase ID are required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get transport operation data
            transport_operation_data = (
                self.transport_operation_access.get_transport_operation_by_id(
                    transportOperationId
                )
            )

            # Check if data is available
            if not transport_operation_data:
                return (
                    jsonify(
                        {
                            "error": "Not Found",
                            "message": "Transport operation data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

            # Parse JSON data from the request body
            data = request.get_json()

            # Call sub-API to update phase data
            updated_phase_data = self.transport_operation_access.update_phase_by_transport_operation_id_and_phase_id(
                transportOperationId, phaseId, data
            )

            # Validate and map data to the Phase model
            validated_updated_phase_data = Phase(**updated_phase_data)

            return (
                jsonify(
                    {
                        "message": "Phase data updated successfully",
                        # Serialize the response data
                        "data": validated_updated_phase_data.model_dump(),
                    }
                ),
                # HTTP status code for successful update
                200,
            )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_document_by_transport_operation_id(
        self, transportOperationId: int
    ) -> Response:
        """
        Get document data related to a specific transport operation by ID.

        Args:
            transportOperationId (int): Unique identifier for the transport operation

        Returns:
            Response: The response with the document data or error message.
        """
        try:
            # Get query parameters
            operator_id = request.args.get("operatorId")

            # Validate required parameters
            if not transportOperationId:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Transport operation ID is required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get document data
            document_data = (
                self.transport_operation_access.get_document_by_transport_operation_id(
                    transportOperationId, operator_id
                )
            )

            # Check if data is available
            if document_data:
                # Validate and map each record to the Document model
                validated_data = [Document(**data) for data in document_data]

                return (
                    jsonify(
                        {
                            "message": "Document data retrieved successfully",
                            # Serialize each record
                            "data": [
                                document.model_dump() for document in validated_data
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
                            "message": "Document data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def append_document_by_transport_operation_id(
        self, transportOperationId: int
    ) -> Response:
        """
        Append document data for a specific transport operation by ID.

        Args:
            transportOperationId (int): Unique identifier for the transport operation

        Returns:
            Response: The response with the appended document data or error message.
        """
        try:
            # Validate required parameters
            if not transportOperationId:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Transport operation ID is required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get transport operation data
            transport_operation_data = (
                self.transport_operation_access.get_transport_operation_by_id(
                    transportOperationId
                )
            )

            # Check if data is available
            if not transport_operation_data:
                return (
                    jsonify(
                        {
                            "error": "Not Found",
                            "message": "Transport operation data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

            # Parse JSON data from the request body
            data = request.get_json()

            # Call sub-API to append document data
            appended_document_data = self.transport_operation_access.append_document_by_transport_operation_id(
                transportOperationId, data
            )

            # Validate and map data to the Document model
            validated_appended_document_data = Document(**appended_document_data)

            return (
                jsonify(
                    {
                        "message": "Document data appended successfully",
                        # Serialize the response data
                        "data": validated_appended_document_data.model_dump(),
                    }
                ),
                # HTTP status code for successful append
                200,
            )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_document_by_transport_operation_id_and_reference_code(
        self, transportOperationId: int, referenceCode: str
    ) -> Response:
        """
        Get specific document data by transport operation ID and reference code.

        Args:
            transportOperationId (int): Unique identifier for the transport operation
            referenceCode (str): Reference code of the document

        Returns:
            Response: The response with the document data or error message.
        """
        try:
            # Validate required parameters
            if not transportOperationId or not referenceCode:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Transport operation ID and reference code are required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get document data
            document_data = self.transport_operation_access.get_document_by_transport_operation_id_and_reference_code(
                transportOperationId, referenceCode
            )

            # Check if data is available
            if document_data:
                # Validate and map data to the Document model
                validated_data = Document(**document_data)

                return (
                    jsonify(
                        {
                            "message": "Document data retrieved successfully",
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
                            "message": "Document data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def update_document_by_transport_operation_id_and_reference_code(
        self, transportOperationId: int, referenceCode: str
    ) -> Response:
        """
        Update document data related to a specific transport operation by ID and reference code.

        Args:
            transportOperationId (int): Unique identifier for the transport operation
            referenceCode (str): Reference code of the document

        Returns:
            Response: The response with the updated document data or error message.
        """
        try:
            # Validate required parameters
            if not transportOperationId or not referenceCode:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Transport operation ID and reference code are required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get transport operation data
            transport_operation_data = (
                self.transport_operation_access.get_transport_operation_by_id(
                    transportOperationId
                )
            )

            # Check if data is available
            if not transport_operation_data:
                return (
                    jsonify(
                        {
                            "error": "Not Found",
                            "message": "Transport operation data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

            # Parse JSON data from the request body
            data = request.get_json()

            # Call sub-API to update document data
            updated_document_data = self.transport_operation_access.update_document_by_transport_operation_id_and_reference_code(
                transportOperationId, referenceCode, data
            )

            # Validate and map data to the Document model
            validated_updated_document_data = Document(**updated_document_data)

            return (
                jsonify(
                    {
                        "message": "Document data updated successfully",
                        # Serialize the response data
                        "data": validated_updated_document_data.model_dump(),
                    }
                ),
                # HTTP status code for successful update
                200,
            )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def delete_document_by_transport_operation_id_and_reference_code(
        self, transportOperationId: int, referenceCode: str
    ) -> Response:
        """
        Delete specific document data by transport operation ID and reference code.

        Args:
            transportOperationId (int): Unique identifier for the transport operation
            referenceCode (str): Reference code of the document

        Returns:
            Response: The response indicating success or error message.
        """
        try:
            # Validate required parameters
            if not transportOperationId or not referenceCode:
                # Validate required parameters
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Transport operation ID and reference code are required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to delete the document
            is_deleted = self.transport_operation_access.delete_document_by_transport_operation_id_and_reference_code(
                transportOperationId, referenceCode
            )

            # Check if the deletion was successful
            if is_deleted:
                return (
                    jsonify(
                        {
                            "message": "Document data deleted successfully",
                        }
                    ),
                    204,  # HTTP status code for successful deletion
                )

            # Handle case where the document is not found
            return (
                jsonify(
                    {
                        "error": "Not Found",
                        "message": "Document data not found",
                    }
                ),
                404,  # HTTP status code for resource not found
            )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_transport_operation_by_plate_number(
        self, countryCode: str, plateNumber: str
    ) -> Response:
        """
        Get ongoing transport operation data by country code and license plate number.

        Args:
            countryCode (str): The country code of the vehicle
            plateNumber (str): The license plate number of the vehicle

        Returns:
            Response: The response with the transport operation data or error message.
        """
        try:
            # Get query parameters
            phase_state = request.args.get("phaseState")

            # Validate required parameters
            if not countryCode or not plateNumber:
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

            # Call sub-API to get data
            transport_operation_data = (
                self.transport_operation_access.get_transport_operation_by_plate_number(
                    countryCode, plateNumber, phase_state
                )
            )

            # Check if data is available
            if transport_operation_data:
                # Validate and map data to the TransportOperation model
                validated_data = TransportOperation(**transport_operation_data)

                return (
                    jsonify(
                        {
                            "message": "Transport operation data retrieved successfully",
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
                            "message": "Transport operation data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_schedule_by_plate_number(
        self, countryCode: str, plateNumber: str
    ) -> Response:
        """
        Get details about the schedule of the ongoing transport operation by country code and license plate number.

        Args:
            countryCode (str): Country code of vehicle registration
            plateNumber (str): License plate number

        Returns:
            Response: The response with the schedule data or error message.
        """
        try:
            # Validate required parameters
            if not countryCode or not plateNumber:
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

            # Call sub-API to get schedule data
            schedule_data = (
                self.transport_operation_access.get_schedule_by_plate_number(
                    countryCode, plateNumber
                )
            )

            # Check if data is available
            if schedule_data:
                # Validate and map data to the Schedule model
                validated_data = Schedule(**schedule_data)

                return (
                    jsonify(
                        {
                            "message": "Schedule data retrieved successfully",
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
                            "message": "Schedule data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_phase_by_plate_number(self, countryCode: str, plateNumber: str) -> Response:
        """
        Get details about all the phases of the ongoing transport operation by country code and license plate number.

        Args:
            countryCode (str): Country code of vehicle registration
            plateNumber (str): License plate number

        Returns:
            Response: The response with the phase data or error message.
        """
        try:
            # Validate required parameters
            if not countryCode or not plateNumber:
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

            # Call sub-API to get phase data
            phase_data = self.transport_operation_access.get_phase_by_plate_number(
                countryCode, plateNumber
            )

            # Check if data is available
            if phase_data:
                # Validate and map each record to the Phase model
                validated_data = [Phase(**data) for data in phase_data]

                return (
                    jsonify(
                        {
                            "message": "Phase data retrieved successfully",
                            # Serialize each record
                            "data": [phase.model_dump() for phase in validated_data],
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
                            "message": "Phase data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_phase_by_plate_number_and_phase_id(
        self, countryCode: str, plateNumber: str, phaseId: int
    ) -> Response:
        """
        Get specific phase data related to the ongoing transport operation by country code, license plate number, and phase ID.

        Args:
            countryCode (str): The country code of the vehicle
            plateNumber (str): The license plate number of the vehicle
            phaseId (int): Unique identifier for the phase

        Returns:
            Response: The response with the phase data or error message.
        """
        try:
            # Validate required parameters
            if not countryCode or not plateNumber or not phaseId:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Country code, plate number, and phase ID are required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get phase data
            phase_data = (
                self.transport_operation_access.get_phase_by_plate_number_and_phase_id(
                    countryCode, plateNumber, phaseId
                )
            )

            # Check if data is available
            if phase_data:
                # Validate and map data to the Phase model
                validated_data = Phase(**phase_data)

                return (
                    jsonify(
                        {
                            "message": "Phase data retrieved successfully",
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
                            "message": "Phase data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_document_by_plate_number(
        self, countryCode: str, plateNumber: str
    ) -> Response:
        """
        Get all international consignment notes related to the ongoing transport operation by country code and license plate number.

        Args:
            countryCode (str): The country code of the vehicle
            plateNumber (str): The license plate number of the vehicle

        Returns:
            Response: The response with the document data or error message.
        """
        try:
            # Validate required parameters
            if not countryCode or not plateNumber:
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

            # Call sub-API to get document data
            document_data = (
                self.transport_operation_access.get_document_by_plate_number(
                    countryCode, plateNumber
                )
            )

            # Check if data is available
            if document_data:
                # Validate and map each record to the Document model
                validated_data = [Document(**data) for data in document_data]

                return (
                    jsonify(
                        {
                            "message": "Document data retrieved successfully",
                            # Serialize each record
                            "data": [
                                document.model_dump() for document in validated_data
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
                            "message": "Document data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_document_by_plate_number_and_reference_code(
        self, countryCode: str, plateNumber: str, referenceCode: str
    ) -> Response:
        """
        Get specific international consignment notes data related to the ongoing transport operation by country code, license plate number, and reference code.

        Args:
            countryCode (str): The country code of the vehicle
            plateNumber (str): The license plate number of the vehicle
            referenceCode (str): Reference code of the document

        Returns:
            Response: The response with the document data or error message.
        """
        try:
            # Validate required parameters
            if not countryCode or not plateNumber or not referenceCode:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Country code, plate number, and reference code are required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get document data
            document_data = self.transport_operation_access.get_document_by_plate_number_and_reference_code(
                countryCode, plateNumber, referenceCode
            )

            # Check if data is available
            if document_data:
                # Validate and map data to the Document model
                validated_data = Document(**document_data)

                return (
                    jsonify(
                        {
                            "message": "Document data retrieved successfully",
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
                            "message": "Document data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_location(self) -> Response:
        """
        Get all locations related to transport operations.

        Args:
            None

        Returns:
            Response: The response with the location data or error message.
        """
        try:
            # Call sub-API to get location data
            location_data = self.transport_operation_access.get_location()

            # Check if data is available
            if location_data:
                # Validate and map each record to the Location model
                validated_data = [Location(**data) for data in location_data]

                return (
                    jsonify(
                        {
                            "message": "Location data retrieved successfully",
                            # Serialize each record
                            "data": [
                                location.model_dump() for location in validated_data
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
                            "message": "Location data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_location_by_mode(self, mode: str) -> Response:
        """
        Get all locations related to transport operations by location mode.

        Args:
            mode (str): The mode of location. It must be one of the values defined in the Mode enum.

        Returns:
            Response: The response with the location data or error message.
        """
        try:
            # Validate required parameters
            if not mode:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Mode is required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Validate mode value
            if mode not in Mode.__members__:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "Invalid mode value. Must be one of: "
                            + ", ".join(Mode.__members__.keys()),
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to get location data by mode
            location_data = self.transport_operation_access.get_location_by_mode(mode)

            # Check if data is available
            if location_data:
                # Validate and map each record to the Location model
                validated_data = [Location(**data) for data in location_data]

                return (
                    jsonify(
                        {
                            "message": "Location data retrieved successfully",
                            # Serialize each record
                            "data": [
                                location.model_dump() for location in validated_data
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
                            "message": "Location data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def add_ecmr(self) -> Response:
        """
        Create new eCMR data.

        Args:
            None

        Returns:
            Response: The response indicating success or error with status code.
        """
        try:
            # Parse JSON data from the request body
            data = request.get_json()

            # Validate and map data to the EcmrModel model
            validated_data = EcmrModel(**data)

            # Call sub-API to add eCMR data
            ecmr_data = self.transport_operation_access.add_ecmr(validated_data)

            return (
                jsonify(
                    {
                        "message": "eCMR data created successfully",
                        # Serialize the response data
                        "data": ecmr_data.model_dump(),
                    }
                ),
                # HTTP status code for resource created
                201,
            )

        except ValueError as e:
            # Handle bad request errors
            return jsonify({"error": "Bad request", "message": str(e)}), 400

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def get_ecmr_by_id(self, id: UUID) -> Response:
        """
        Get eCMR data by ID.

        Args:
            id (UUID): The ID assigned to the eCMR by the eCMR Connector service upon creation.

        Returns:
            Response: The response with the eCMR data or error message.
        """
        try:
            # Validate required parameters
            if not id:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "eCMR ID is required",
                        }
                    ),
                    400,
                )

            # Call sub-API to get eCMR data by ID
            ecmr_data = self.transport_operation_access.get_ecmr_by_id(id)

            # Check if data is available
            if ecmr_data:
                # Validate and map data to the EcmrModel model
                validated_data = EcmrModel(**ecmr_data)
                return (
                    jsonify(
                        {
                            "message": "eCMR data retrieved successfully",
                            # Serialize the response data
                            "data": validated_data.model_dump(),
                        }
                    ),
                    # HTTP status code for successful retrieval
                    200,
                )
            # Handle case where no data is found
            return (
                jsonify({"error": "Not Found", "message": "eCMR data not found"}),
                # HTTP status code for resource not found
                404,
            )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def update_ecmr_by_id(self, id: UUID) -> Response:
        """
        Update eCMR data by ID.

        Args:
            id (UUID): The ID assigned to the eCMR by the eCMR Connector service upon creation.

        Returns:
            Response: The response indicating success or error with status code.
        """
        try:
            # Validate required parameters
            if not id:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "eCMR ID is required",
                        }
                    ),
                    400,
                )

            # Call sub-API to get eCMR data by ID
            ecmr_data = self.transport_operation_access.get_ecmr_by_id(id)

            # Check if data is available
            if not ecmr_data:
                return (
                    jsonify(
                        {
                            "error": "Not Found",
                            "message": "eCMR data not found",
                        }
                    ),
                    # HTTP status code for resource not found
                    404,
                )

            # Parse JSON data from the request body
            data = request.get_json()

            # Call sub-API to update eCMR data by ID
            updated_ecmr_data = self.transport_operation_access.update_ecmr_by_id(
                id, data
            )

            # Validate and map data to the EcmrModel model
            validated_updated_ecmr_data = EcmrModel(**updated_ecmr_data)

            return (
                jsonify(
                    {
                        "message": "eCMR data updated successfully",
                        # Serialize the response data
                        "data": validated_updated_ecmr_data.model_dump(),
                    }
                ),
                # HTTP status code for successful update
                200,
            )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    def delete_ecmr_by_id(self, id: UUID) -> Response:
        """
        Delete an eCMR by ID.

        Args:
            id (UUID): The ID assigned to the eCMR by the eCMR Connector service upon creation.

        Returns:
            Response: The response indicating success or error with status code.
        """
        try:
            # Validate required parameters
            if not id:
                return (
                    jsonify(
                        {
                            "error": "Bad request",
                            "message": "eCMR ID is required",
                        }
                    ),
                    # HTTP status code for bad request
                    400,
                )

            # Call sub-API to delete eCMR by ID
            is_deleted = self.transport_operation_access.delete_ecmr_by_id(id)

            # Check if the deletion was successful
            if is_deleted:
                return (
                    jsonify({"message": "eCMR data deleted successfully"}),
                    204,  # HTTP status code for successful deletion
                )

            # Handle case where the eCMR is not found
            return (
                jsonify(
                    {
                        "error": "Not Found",
                        "message": "eCMR data not found",
                    }
                ),
                404,  # HTTP status code for resource not found
            )

        except Exception as e:
            # Handle unexpected server errors
            return jsonify({"error": "Internal Server Error", "message": str(e)}), 500
