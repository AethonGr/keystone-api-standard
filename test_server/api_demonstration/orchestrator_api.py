"""
This module defines the KEYSTONE API Standard, which serves as the foundation
for managing transport operation data.

The `OrchestratorAPI` class integrates with sub-APIs (TransportOperationAPI, VehicleAPI, and DriverAPI)
to provide endpoints for creating, retrieving, updating, and deleting transport
operation data.
"""

from uuid import UUID

from flask import Response

from .entities import DriverAPI, OrganizationAPI, TransportOperationAPI, VehicleAPI


class OrchestratorAPI:
    """
    Centralized API class for managing transport operation data.

    This class integrates with the TransportOperationAPI, VehicleAPI, and DriverAPI classes
    to provide a unified interface for managing transport operations, vehicles, and drivers.

    It includes methods for adding, retrieving, updating, and deleting data related to
    transport operations, vehicles, and drivers.
    """

    def __init__(self):
        """
        Initialize the OrchestratorAPI class, which integrates with the TransportOperationAPI,
        VehicleAPI, and DriverAPI classes.

        Args:
            None

        Returns:
            None
        """
        # Initialize sub-APIs for transport operations
        self.transport_operation_api = TransportOperationAPI()
        # Initialize sub-APIs for vehicles and drivers
        self.vehicle_api = VehicleAPI()
        # Initialize sub-APIs for drivers
        self.driver_api = DriverAPI()
        # Initialize sub-APIs for organizations
        self.organization_api = OrganizationAPI()

    # Delegate transport operation endpoints
    def add_transport_operation(self) -> Response:
        """
        Add a new transport operation.

        Args:
            None

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.add_transport_operation()

    def get_transport_operation(self) -> Response:
        """
        Retrieve all ongoing transport operations.

        Args:
            None

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.get_transport_operation()

    def get_transport_operation_by_id(self, transportOperationId: int) -> Response:
        """
        Retrieve a transport operation by its ID.

        Args:
            transportOperationId (int): The ID of the transport operation.

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.get_transport_operation_by_id(
            transportOperationId
        )

    def update_transport_operation_by_id(self, transportOperationId: int) -> Response:
        """
        Update a transport operation by its ID.

        Args:
            transportOperationId (int): The ID of the transport operation.

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.update_transport_operation_by_id(
            transportOperationId
        )

    def delete_transport_operation_by_id(self, transportOperationId: int) -> Response:
        """
        Delete a transport operation by its ID.

        Args:
            transportOperationId (int): The ID of the transport operation.

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.delete_transport_operation_by_id(
            transportOperationId
        )

    def get_schedule_by_transport_operation_id(
        self, transportOperationId: int
    ) -> Response:
        """
        Retrieve the schedule of a transport operation by its ID.

        Args:
            transportOperationId (int): The ID of the transport operation.

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.get_schedule_by_transport_operation_id(
            transportOperationId
        )

    def update_schedule_by_transport_operation_id(
        self, transportOperationId: int
    ) -> Response:
        """
        Update the schedule of a transport operation by its ID.

        Args:
            transportOperationId (int): The ID of the transport operation.

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.update_schedule_by_transport_operation_id(
            transportOperationId
        )

    def get_phase_by_transport_operation_id(
        self, transportOperationId: int
    ) -> Response:
        """
        Retrieve the phase of a transport operation by its ID.

        Args:
            transportOperationId (int): The ID of the transport operation.

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.get_phase_by_transport_operation_id(
            transportOperationId
        )

    def append_phase_by_transport_operation_id(
        self, transportOperationId: int
    ) -> Response:
        """
        Append a phase to a transport operation by its ID.

        Args:
            transportOperationId (int): The ID of the transport operation.

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.append_phase_by_transport_operation_id(
            transportOperationId
        )

    def get_phase_by_transport_operation_id_and_phase_id(
        self, transportOperationId: int, phaseId: int
    ) -> Response:
        """
        Retrieve a phase of a transport operation by its ID and phase ID.

        Args:
            transportOperationId (int): The ID of the transport operation.
            phaseId (int): The ID of the phase.

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.get_phase_by_transport_operation_id_and_phase_id(
            transportOperationId, phaseId
        )

    def update_phase_by_transport_operation_id_and_phase_id(
        self, transportOperationId: int, phaseId: int
    ) -> Response:
        """
        Update a phase of a transport operation by its ID and phase ID.

        Args:
            transportOperationId (int): The ID of the transport operation.
            phaseId (int): The ID of the phase.

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.update_phase_by_transport_operation_id_and_phase_id(
            transportOperationId, phaseId
        )

    def get_document_by_transport_operation_id(
        self, transportOperationId: int
    ) -> Response:
        """
        Retrieve a document of a transport operation by its ID.

        Args:
            transportOperationId (int): The ID of the transport operation.

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.get_document_by_transport_operation_id(
            transportOperationId
        )

    def append_document_by_transport_operation_id(
        self, transportOperationId: int
    ) -> Response:
        """
        Append a document to a transport operation by its ID.

        Args:
            transportOperationId (int): The ID of the transport operation.

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.append_document_by_transport_operation_id(
            transportOperationId
        )

    def get_document_by_transport_operation_id_and_reference_code(
        self, transportOperationId: int, referenceCode: str
    ) -> Response:
        """
        Retrieve a document of a transport operation by its ID and reference code.

        Args:
            transportOperationId (int): The ID of the transport operation.
            referenceCode (str): The reference code of the document.

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.get_document_by_transport_operation_id_and_reference_code(
            transportOperationId, referenceCode
        )

    def update_document_by_transport_operation_id_and_reference_code(
        self, transportOperationId: int, referenceCode: str
    ) -> Response:
        """
        Update a document of a transport operation by its ID and reference code.

        Args:
            transportOperationId (int): The ID of the transport operation.
            referenceCode (str): The reference code of the document.

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.update_document_by_transport_operation_id_and_reference_code(
            transportOperationId, referenceCode
        )

    def delete_document_by_transport_operation_id_and_reference_code(
        self, transportOperationId: int, referenceCode: str
    ) -> Response:
        """
        Delete a document of a transport operation by its ID and reference code.

        Args:
            transportOperationId (int): The ID of the transport operation.
            referenceCode (str): The reference code of the document.

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.delete_document_by_transport_operation_id_and_reference_code(
            transportOperationId, referenceCode
        )

    def get_transport_operation_by_plate_number(
        self, countryCode: str, plateNumber: str
    ) -> Response:
        """
        Retrieve a transport operation by its plate number.

        Args:
            countryCode (str): The country code of the plate number.
            plateNumber (str): The plate number of the vehicle.

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.get_transport_operation_by_plate_number(
            countryCode, plateNumber
        )

    def get_schedule_by_plate_number(
        self, countryCode: str, plateNumber: str
    ) -> Response:
        """
        Retrieve the schedule of a transport operation by its plate number.

        Args:
            countryCode (str): The country code of the plate number.
            plateNumber (str): The plate number of the vehicle.

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.get_schedule_by_plate_number(
            countryCode, plateNumber
        )

    def get_phase_by_plate_number(self, countryCode: str, plateNumber: str) -> Response:
        """
        Retrieve the phase of a transport operation by its plate number.

        Args:
            countryCode (str): The country code of the plate number.
            plateNumber (str): The plate number of the vehicle.

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.get_phase_by_plate_number(
            countryCode, plateNumber
        )

    def get_phase_by_plate_number_and_phase_id(
        self, countryCode: str, plateNumber: str, phaseId: int
    ) -> Response:
        """
        Retrieve a phase of a transport operation by its plate number and phase ID.

        Args:
            countryCode (str): The country code of the plate number.
            plateNumber (str): The plate number of the vehicle.
            phaseId (int): The ID of the phase.

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.get_phase_by_plate_number_and_phase_id(
            countryCode, plateNumber, phaseId
        )

    def get_document_by_plate_number(
        self, countryCode: str, plateNumber: str
    ) -> Response:
        """
        Retrieve a document of a transport operation by its plate number.

        Args:
            countryCode (str): The country code of the plate number.
            plateNumber (str): The plate number of the vehicle.

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.get_document_by_plate_number(
            countryCode, plateNumber
        )

    def get_document_by_plate_number_and_reference_code(
        self, countryCode: str, plateNumber: str, referenceCode: str
    ) -> Response:
        """
        Retrieve a document of a transport operation by its plate number and reference code.

        Args:
            countryCode (str): The country code of the plate number.
            plateNumber (str): The plate number of the vehicle.
            referenceCode (str): The reference code of the document.

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.get_document_by_plate_number_and_reference_code(
            countryCode, plateNumber, referenceCode
        )

    def get_location(self) -> Response:
        """
        Retrieve all locations related to transport operations.

        Args:
            None

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.get_location()

    def get_location_by_mode(self, mode: str) -> Response:
        """
        Retrieve locations related to transport operations by location mode.

        Args:
            mode (str): The mode of location.

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.get_location_by_mode(mode)

    def add_ecmr(self) -> Response:
        """
        Add eCMR data.

        Args:
            None

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.add_ecmr()

    def get_ecmr_by_id(self, id: UUID) -> Response:
        """
        Retrieve specrific eCMR data.

        Args:
            id (UUID): The ID assigned to the eCMR by the eCMR Connector service upon creation.

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.get_ecmr_by_id(id)

    def update_ecmr_by_id(self, id: UUID) -> Response:
        """
        Update eCMR data by ID.

        Args:
            id (UUID): The ID assigned to the eCMR by the eCMR Connector service upon creation.

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.update_ecmr_by_id(id)

    def delete_ecmr_by_id(self, id: UUID) -> Response:
        """
        Delete an eCMR by ID.

        Args:
            id (UUID): The ID assigned to the eCMR by the eCMR Connector service upon creation.

        Returns:
            Response: The response from the TransportOperationAPI.
        """
        return self.transport_operation_api.delete_ecmr_by_id(id)

    # Delegate vehicle endpoints
    def add_vehicle(self) -> Response:
        """
        Add a new vehicle.

        Args:
            None

        Returns:
            Response: The response from the VehicleAPI.
        """
        return self.vehicle_api.add_vehicle()

    def get_vehicle(self) -> Response:
        """
        Retrieve all vehicles.

        Args:
            None

        Returns:
            Response: The response from the VehicleAPI.
        """
        return self.vehicle_api.get_vehicle()

    def get_vehicle_by_plate_number(
        self, countryCode: str, plateNumber: str
    ) -> Response:
        """
        Retrieve a vehicle by its plate number.

        Args:
            countryCode (str): The country code of the plate number.
            plateNumber (str): The plate number of the vehicle.

        Returns:
            Response: The response from the VehicleAPI.
        """
        return self.vehicle_api.get_vehicle_by_plate_number(countryCode, plateNumber)

    def update_vehicle_by_plate_number(
        self, countryCode: str, plateNumber: str
    ) -> Response:
        """
        Update a vehicle by its plate number.

        Args:
            countryCode (str): The country code of the plate number.
            plateNumber (str): The plate number of the vehicle.

        Returns:
            Response: The response from the VehicleAPI.
        """
        return self.vehicle_api.update_vehicle_by_plate_number(countryCode, plateNumber)

    def delete_vehicle_by_plate_number(
        self, countryCode: str, plateNumber: str
    ) -> Response:
        """
        Delete a vehicle by its plate number.

        Args:
            countryCode (str): The country code of the plate number.
            plateNumber (str): The plate number of the vehicle.

        Returns:
            Response: The response from the VehicleAPI.
        """
        return self.vehicle_api.delete_vehicle_by_plate_number(countryCode, plateNumber)

    def get_geolocation_by_plate_number(
        self, countryCode: str, plateNumber: str
    ) -> Response:
        """
        Retrieve the geolocation of a vehicle by its plate number.

        Args:
            countryCode (str): The country code of the plate number.
            plateNumber (str): The plate number of the vehicle.

        Returns:
            Response: The response from the VehicleAPI.
        """
        return self.vehicle_api.get_geolocation_by_plate_number(
            countryCode, plateNumber
        )

    def append_geolocation_by_plate_number(
        self, countryCode: str, plateNumber: str
    ) -> Response:
        """
        Append a geolocation to a vehicle by its plate number.

        Args:
            countryCode (str): The country code of the plate number.
            plateNumber (str): The plate number of the vehicle.

        Returns:
            Response: The response from the VehicleAPI.
        """
        return self.vehicle_api.append_geolocation_by_plate_number(
            countryCode, plateNumber
        )

    def get_owner_by_plate_number(self, countryCode: str, plateNumber: str) -> Response:
        """
        Retrieve the owner of a vehicle by its plate number.

        Args:
            countryCode (str): The country code of the plate number.
            plateNumber (str): The plate number of the vehicle.

        Returns:
            Response: The response from the VehicleAPI.
        """
        return self.vehicle_api.get_owner_by_plate_number(countryCode, plateNumber)

    def get_insurance_by_plate_number(
        self, countryCode: str, plateNumber: str
    ) -> Response:
        """
        Retrieve the insurance of a vehicle by its plate number.

        Args:
            countryCode (str): The country code of the plate number.
            plateNumber (str): The plate number of the vehicle.

        Returns:
            Response: The response from the VehicleAPI.
        """
        return self.vehicle_api.get_insurance_by_plate_number(countryCode, plateNumber)

    def get_insurance_by_plate_number_and_insurance_id(
        self, countryCode: str, plateNumber: str, insuranceId: int
    ) -> Response:
        """
        Retrieve the insurance of a vehicle by its plate number and insurance ID.

        Args:
            countryCode (str): The country code of the plate number.
            plateNumber (str): The plate number of the vehicle.
            insuranceId (int): The ID of the insurance.

        Returns:
            Response: The response from the VehicleAPI.
        """
        return self.vehicle_api.get_insurance_by_plate_number_and_insurance_id(
            countryCode, plateNumber, insuranceId
        )

    def get_revision_by_plate_number(
        self, countryCode: str, plateNumber: str
    ) -> Response:
        """
        Retrieve the revision of a vehicle by its plate number.

        Args:
            countryCode (str): The country code of the plate number.
            plateNumber (str): The plate number of the vehicle.

        Returns:
            Response: The response from the VehicleAPI.
        """
        return self.vehicle_api.get_revision_by_plate_number(countryCode, plateNumber)

    def get_revision_by_plate_number_and_revision_id(
        self, countryCode: str, plateNumber: str, revisionId: int
    ) -> Response:
        """
        Retrieve the revision of a vehicle by its plate number and revision ID.

        Args:
            countryCode (str): The country code of the plate number.
            plateNumber (str): The plate number of the vehicle.
            revisionId (int): The ID of the revision.

        Returns:
            Response: The response from the VehicleAPI.
        """
        return self.vehicle_api.get_revision_by_plate_number_and_revision_id(
            countryCode, plateNumber, revisionId
        )

    # Delegate driver endpoints
    def add_driver(self) -> Response:
        """
        Add a new driver.

        Args:
            None

        Returns:
            Response: The response from the DriverAPI.
        """
        return self.driver_api.add_driver()

    def get_driver(self) -> Response:
        """
        Retrieve all drivers.

        Args:
            None

        Returns:
            Response: The response from the DriverAPI.
        """
        return self.driver_api.get_driver()

    def get_driver_by_vat(self, countryCode: str, vat: str) -> Response:
        """
        Retrieve a driver by their VAT number.

        Args:
            countryCode (str): The country code of the VAT number.
            vat (str): The VAT number of the driver.

        Returns:
            Response: The response from the DriverAPI.
        """
        return self.driver_api.get_driver_by_vat(countryCode, vat)

    def update_driver_by_vat(self, countryCode: str, vat: str) -> Response:
        """
        Update a driver by their VAT number.

        Args:
            countryCode (str): The country code of the VAT number.
            vat (str): The VAT number of the driver.

        Returns:
            Response: The response from the DriverAPI.
        """
        return self.driver_api.update_driver_by_vat(countryCode, vat)

    def delete_driver_by_vat(self, countryCode: str, vat: str) -> Response:
        """
        Delete a driver by their VAT number.

        Args:
            countryCode (str): The country code of the VAT number.
            vat (str): The VAT number of the driver.

        Returns:
            Response: The response from the DriverAPI.
        """
        return self.driver_api.delete_driver_by_vat(countryCode, vat)

    def get_license_by_vat(self, countryCode: str, vat: str) -> Response:
        """
        Retrieve the license of a driver by their VAT number.

        Args:
            countryCode (str): The country code of the VAT number.
            vat (str): The VAT number of the driver.

        Returns:
            Response: The response from the DriverAPI.
        """
        return self.driver_api.get_license_by_vat(countryCode, vat)

    def get_traffic_violation_by_vat(self, countryCode: str, vat: str) -> Response:
        """
        Retrieve the traffic violations of a driver by their VAT number.

        Args:
            countryCode (str): The country code of the VAT number.
            vat (str): The VAT number of the driver.

        Returns:
            Response: The response from the DriverAPI.
        """
        return self.driver_api.get_traffic_violation_by_vat(countryCode, vat)

    def get_traffic_violation_by_vat_and_traffic_violation_id(
        self, countryCode: str, vat: str, trafficViolationId: int
    ) -> Response:
        """
        Retrieve a traffic violation of a driver by their VAT number and traffic violation ID.

        Args:
            countryCode (str): The country code of the VAT number.
            vat (str): The VAT number of the driver.
            trafficViolationId (int): The ID of the traffic violation.

        Returns:
            Response: The response from the DriverAPI.
        """
        return self.driver_api.get_traffic_violation_by_vat_and_traffic_violation_id(
            countryCode, vat, trafficViolationId
        )

    def get_tachograph_card_by_vat(self, countryCode: str, vat: str) -> Response:
        """
        Retrieve the tachograph card of a driver by their VAT number.

        Args:
            countryCode (str): The country code of the VAT number.
            vat (str): The VAT number of the driver.

        Returns:
            Response: The response from the DriverAPI.
        """
        return self.driver_api.get_tachograph_card_by_vat(countryCode, vat)

    def get_tachograph_card_by_vat_and_tachograph_card_id(
        self, countryCode: str, vat: str, tachographCardId: str
    ) -> Response:
        """
        Retrieve a tachograph card of a driver by their VAT number and tachograph card ID.

        Args:
            countryCode (str): The country code of the VAT number.
            vat (str): The VAT number of the driver.
            tachographCardId (str): The ID of the tachograph card.

        Returns:
            Response: The response from the DriverAPI.
        """
        return self.driver_api.get_tachograph_card_by_vat_and_tachograph_card_id(
            countryCode, vat, tachographCardId
        )

    # Delegate organization endpoints
    def add_organization(self) -> Response:
        """
        Add a new organization.

        Args:
            None

        Returns:
            Response: The response from the OrganizationAPI.
        """
        return self.organization_api.add_organization()

    def get_organization(self) -> Response:
        """
        Retrieve all organizations.

        Args:
            None

        Returns:
            Response: The response from the OrganizationAPI.
        """
        return self.organization_api.get_organization()

    def get_organization_by_id(self, organizationId: int) -> Response:
        """
        Retrieve an organization by its ID.

        Args:
            organizationId (int): The ID of the organization.

        Returns:
            Response: The response from the OrganizationAPI.
        """
        return self.organization_api.get_organization_by_id(organizationId)

    def update_organization_by_id(self, organizationId: int) -> Response:
        """
        Update an organization by its ID.

        Args:
            organizationId (int): The ID of the organization.

        Returns:
            Response: The response from the OrganizationAPI.
        """
        return self.organization_api.update_organization_by_id(organizationId)

    def delete_organization_by_id(self, organizationId: int) -> Response:
        """
        Delete an organization by its ID.

        Args:
            organizationId (int): The ID of the organization.

        Returns:
            Response: The response from the OrganizationAPI.
        """
        return self.organization_api.delete_organization_by_id(organizationId)
