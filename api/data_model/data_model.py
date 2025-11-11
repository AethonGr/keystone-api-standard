"""
This module defines the data model for transport operation data.

Each class represents a distinct component of the transport data and includes
attributes with appropriate data types, validations, and constraints.
"""

from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import Field, RootModel

from .base import HandleBaseModel
from .ecmr import EcmrModel


class Payload(RootModel):
    """
    Represents additional information.
    """

    # A dictionary to allow any custom key-value pairs for additional information.
    root: Dict[str, Any]


class Coordinates(HandleBaseModel):
    """
    Represents geographical coordinates.
    """

    latitude: float = Field(
        ..., ge=-90, le=90, description="Latitude in Decimal Degrees (DD)."
    )
    longitude: float = Field(
        ..., ge=-180, le=180, description="Longitude in Decimal Degrees (DD)."
    )


class Geolocation(HandleBaseModel):
    """
    Represents geolocation data for a vehicle.
    """

    dateTime: str = Field(
        ...,
        pattern="^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$",
        description="Date and time of the geolocation.",
    )
    coordinates: Coordinates = Field(
        ..., description="Geographical coordinates of the vehicle."
    )


class Mode(Enum):
    """
    Enum representing the mode of the location.
    """

    GENERIC = "GENERIC"
    GATE = "GATE"
    TERMINAL = "TERMINAL"
    PORT = "PORT"
    AIRPORT = "AIRPORT"
    STATION = "STATION"


class Location(HandleBaseModel):
    """
    Represents details about a location.
    """

    id: int = Field(..., ge=1, description="Unique identifier for the location.")
    countryCode: str = Field(
        ..., pattern="^[A-Z]{2,4}$", description="Country code of the location."
    )
    description: str = Field(
        ..., min_length=1, max_length=100, description="Description of the location."
    )
    mode: Mode = Field(..., description="Mode of the location.")
    coordinates: Optional[Coordinates] = Field(
        None, description="Geographical coordinates of the location."
    )


class Owner(HandleBaseModel):
    """
    Represents details of the vehicle owner.
    """

    id: int = Field(..., ge=1, description="Unique identifier for the vehicle owner.")
    name: str = Field(
        ..., min_length=1, max_length=20, description="Name of the vehicle owner."
    )
    vat: Optional[str] = Field(
        None,
        min_length=2,
        max_length=13,
        description="VAT number of the vehicle owner.",
    )
    payload: Optional[Payload] = Field(None, description="Additional information.")


class Insurance(HandleBaseModel):
    """
    Represents details about the vehicle's insurance.
    """

    id: int = Field(..., ge=1, description="Unique identifier for the insurance.")
    name: str = Field(
        ..., min_length=1, max_length=20, description="Name of the insurance company."
    )
    number: str = Field(
        ..., min_length=1, max_length=20, description="Insurance policy number."
    )
    isInsured: bool = Field(
        ..., description="Indicates whether the vehicle is insured."
    )
    activationDate: str = Field(
        ...,
        pattern="^\\d{4}-\\d{2}-\\d{2}$",
        description="Activation date of the insurance.",
    )
    expirationDate: str = Field(
        ...,
        pattern="^\\d{4}-\\d{2}-\\d{2}$",
        description="Expiration date of the insurance.",
    )
    payload: Optional[Payload] = Field(None, description="Additional information.")


class Revision(HandleBaseModel):
    """
    Represents details about the vehicle's revision.
    """

    id: int = Field(..., ge=1, description="Unique identifier for the revision.")
    name: str = Field(
        ..., min_length=1, max_length=20, description="Name of the revision company."
    )
    number: str = Field(
        ..., min_length=1, max_length=20, description="Revision number."
    )
    executionDate: str = Field(
        ...,
        pattern="^\\d{4}-\\d{2}-\\d{2}$",
        description="Execution date of the revision.",
    )
    expirationDate: str = Field(
        ...,
        pattern="^\\d{4}-\\d{2}-\\d{2}$",
        description="Expiration date of the revision.",
    )
    payload: Optional[Payload] = Field(None, description="Additional information.")


class Vehicle(HandleBaseModel):
    """
    Represents details about the vehicle used in the transport operation.
    """

    id: int = Field(..., ge=1, description="Unique identifier for the vehicle.")
    countryCode: str = Field(
        ...,
        pattern="^[A-Z]{2,4}$",
        description="Country code of the vehicle's registration.",
    )
    plateNumber: str = Field(
        ...,
        min_length=1,
        max_length=20,
        description="License plate number of the vehicle.",
    )
    type: Optional[str] = Field(
        None, min_length=1, max_length=20, description="Type of the vehicle."
    )
    model: Optional[str] = Field(
        None, min_length=1, max_length=20, description="Model of the vehicle."
    )
    geolocation: Optional[List[Geolocation]] = Field(
        None, description="Details of the vehicle's geolocation."
    )
    owner: Owner = Field(..., description="Details of the vehicle owner.")
    insurance: List[Insurance] = Field(
        ..., description="List of vehicle's insurance details."
    )
    revision: List[Revision] = Field(
        ..., description="List of vehicle's revision details."
    )


class Type(Enum):
    """
    Enum representing the type of the driver's license.
    """

    AM = "AM"
    A = "A"
    A1 = "A1"
    A2 = "A2"
    B = "B"
    BE = "BE"
    B1 = "B1"
    C1 = "C1"
    C1E = "C1E"
    C = "C"
    CE = "CE"
    D1 = "D1"
    D1E = "D1E"
    D = "D"
    DE = "DE"


class Status(Enum):
    """
    Enum representing the status of the driver's license.
    """

    VALID = "VALID"
    EXPIRED = "EXPIRED"
    SUSPENDED = "SUSPENDED"
    REVOKED = "REVOKED"
    CONFISCATED = "CONFISCATED"
    LOST_STOLEN = "LOST/STOLEN"


class Category(HandleBaseModel):
    """
    Represents a category of the driver's license.
    """

    type: Type = Field(
        ...,
        description="Type of the license category.",
    )
    description: Optional[str] = Field(
        None,
        min_length=1,
        max_length=20,
        description="A description of the vehicle type associated with the license category.",
    )
    issueDate: str = Field(
        ...,
        pattern="^\\d{4}-\\d{2}-\\d{2}$",
        description="Issue date of the license category.",
    )
    expiryDate: str = Field(
        ...,
        pattern="^\\d{4}-\\d{2}-\\d{2}$",
        description="Expiry date of the license category.",
    )
    status: Status = Field(
        ...,
        description="Status of the license category.",
    )
    code95: Optional[str] = Field(
        None,
        min_length=1,
        max_length=20,
        description="Certificate of Professional Competence (CPC) qualification.",
    )


class License(HandleBaseModel):
    """
    Represents details of the driver's license.
    """

    id: str = Field(
        ...,
        pattern="^[A-Z0-9]{1,16}$",
        description="License unique identifier, which could be set as corresponding to the actual EU Licence Number.",
    )
    countryCode: str = Field(
        ..., pattern="^[A-Z]{2,4}$", description="Country code of the driver's license."
    )
    category: List[Category] = Field(..., description="List of license categories.")


class TrafficViolation(HandleBaseModel):
    """
    Represents details of a traffic violation.
    """

    id: int = Field(
        ..., ge=1, description="Unique identifier for the traffic violation."
    )
    description: str = Field(
        ..., min_length=1, max_length=100, description="Description of the violation."
    )
    code: str = Field(
        ..., min_length=1, max_length=20, description="Code of the traffic violation."
    )
    countryCode: str = Field(
        ...,
        pattern="^[A-Z]{2,4}$",
        description="Country code where the violation occurred.",
    )
    fine: Optional[float] = Field(
        None, ge=0, description="Fine amount for the violation."
    )
    paymentDueDate: Optional[str] = Field(
        None,
        pattern="^\\d{4}-\\d{2}-\\d{2}$",
        description="Payment due date for the fine.",
    )
    paymentDate: Optional[str] = Field(
        None,
        pattern="^\\d{4}-\\d{2}-\\d{2}$",
        description="Date when the fine was paid.",
    )
    isPayed: Optional[bool] = Field(None, description="Indicates if the fine is paid.")
    validityPoints: Optional[int] = Field(
        None, ge=0, description="Number of validity points deducted for the violation."
    )
    payload: Optional[Payload] = Field(None, description="Additional information.")


class ExceededTimeLimits(HandleBaseModel):
    """
    Represents details of exceeded time limits.
    """

    type: Optional[str] = Field(
        None, min_length=1, max_length=20, description="Type of time limit exceeded."
    )
    hours: int = Field(..., ge=0, description="Number of hours exceeded.")
    minutes: int = Field(..., ge=0, le=59, description="Number of minutes exceeded.")
    seconds: int = Field(..., ge=0, le=59, description="Number of seconds exceeded.")


class DrivingInterval(HandleBaseModel):
    """
    Represents a driving interval.
    """

    startDateTime: str = Field(
        ...,
        pattern="^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$",
        description="Start date and time of the driving interval.",
    )
    endDateTime: str = Field(
        ...,
        pattern="^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$",
        description="End date and time of the driving interval.",
    )
    etl: Optional[List[ExceededTimeLimits]] = Field(
        None, description="Details of the exceeded time limits."
    )


class TachographCard(HandleBaseModel):
    """
    Represents details of a tachograph card.
    """

    id: str = Field(
        ...,
        pattern="^[A-Z0-9]{1,16}$",
        description="Unique identifier for the tachograph card.",
    )
    drivingInterval: List[DrivingInterval] = Field(
        ..., description="Details of the driving interval."
    )


class Driver(HandleBaseModel):
    """
    Represents details about the driver.
    """

    id: int = Field(..., ge=1, description="Unique identifier for the driver.")
    firstName: str = Field(
        ..., min_length=1, max_length=20, description="First name of the driver."
    )
    lastName: str = Field(
        ..., min_length=1, max_length=20, description="Last name of the driver."
    )
    countryCode: str = Field(
        ...,
        pattern="^[A-Z]{2,4}$",
        description="Country code of the driver's registration.",
    )
    vat: str = Field(
        ..., min_length=2, max_length=13, description="VAT number of the driver."
    )
    license: License = Field(..., description="Details of the driver's license.")
    trafficViolation: Optional[List[TrafficViolation]] = Field(
        None, description="List of drivers's traffic violations."
    )
    tachographCard: Optional[List[TachographCard]] = Field(
        None, description="List of driver's tachograph cards."
    )


class State(Enum):
    """
    Enum representing the state of the phase.
    """

    PLANNING = "PLANNING"
    IN_PROGRESS = "IN_PROGRESS"
    ARRIVED_AT_PICKUP = "ARRIVED_AT_PICKUP"
    ARRIVED_AT_DESTINATION = "ARRIVED_AT_DESTINATION"
    LOADING = "LOADING"
    UNLOADING = "UNLOADING"
    IN_TRANSIT = "IN_TRANSIT"
    COMPLETED = "COMPLETED"
    DELAYED = "DELAYED"
    CANCELED = "CANCELED"


class Phase(HandleBaseModel):
    """
    Represents a phase of the transport operation.
    """

    id: int = Field(..., ge=1, description="Unique identifier for the phase.")
    location: Location = Field(
        ..., description="Details of the location for the phase."
    )
    dateTime: str = Field(
        ...,
        pattern="^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$",
        description="Date and time of the phase.",
    )
    state: State = Field(
        ...,
        description="State of the phase.",
    )
    payload: Optional[Payload] = Field(None, description="Additional information.")


class OrganizationType(Enum):
    """
    Enum representing the type of the organization.
    """

    OPERATOR = "OPERATOR"
    CUSTOMER = "CUSTOMER"


class Organization(HandleBaseModel):
    """
    Represents details about an organization.
    """

    id: int = Field(..., ge=1, description="Unique identifier for the organization.")
    name: str = Field(
        ..., min_length=1, max_length=20, description="Name of the organization."
    )
    countryCode: str = Field(
        ..., pattern="^[A-Z]{2,4}$", description="Country code of the organization."
    )
    type: OrganizationType = Field(..., description="Type of the organization.")
    vat: Optional[str] = Field(
        None, min_length=2, max_length=13, description="VAT number of the organization."
    )
    address: Optional[str] = Field(
        None,
        min_length=1,
        max_length=100,
        description="Address of the organization.",
    )


class Schedule(HandleBaseModel):
    """
    Represents details about the schedule of a transport operation.
    """

    departureDateTime: str = Field(
        ...,
        pattern="^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$",
        description="Planned departure date and time.",
    )
    realDepartureDateTime: Optional[str] = Field(
        None,
        pattern="^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$",
        description="Actual departure date and time.",
    )
    estimatedDateTimeOfArrival: str = Field(
        ...,
        pattern="^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$",
        description="Estimated arrival date and time.",
    )
    realArrivalDateTime: Optional[str] = Field(
        None,
        pattern="^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$",
        description="Actual arrival date and time.",
    )


class Component(HandleBaseModel):
    """
    Represents a component of a load item.
    """

    type: str = Field(
        ..., min_length=1, max_length=20, description="Type of the component."
    )
    description: Optional[str] = Field(
        None, min_length=1, max_length=100, description="Description of the component."
    )
    width: float = Field(..., ge=0, description="Width of the component in cm.")
    height: float = Field(..., ge=0, description="Height of the component in cm.")
    depth: float = Field(..., ge=0, description="Depth of the component in cm.")
    unitary: bool = Field(..., description="Indicates if the component is unitary.")
    um: str = Field(
        ...,
        min_length=1,
        max_length=20,
        description="Unit of measurement for the component.",
    )


class Load(HandleBaseModel):
    """
    Represents an item of load being transported.
    """

    type: str = Field(..., min_length=1, max_length=20, description="Type of the load.")
    description: Optional[str] = Field(
        None, min_length=1, max_length=100, description="Description of the load."
    )
    weight: float = Field(..., ge=0, description="Weight of the load in kilograms.")
    umWeight: str = Field(
        ...,
        min_length=1,
        max_length=20,
        description="Unit of measurement for the weight.",
    )
    component: List[Component] = Field(
        ..., description="List of components of the load."
    )


class Document(HandleBaseModel):
    """
    Represents details about the international consignment notes used for transport operation.
    """

    referenceCode: str = Field(
        ...,
        min_length=1,
        max_length=20,
        description="Unique identifier assigned to international consignment note used for transport operation.",
    )
    senderOrganization: Organization = Field(
        ..., description="Details about the organization that sends the load."
    )
    receiverOrganization: Organization = Field(
        ..., description="Details about the organization that receives the load."
    )
    startingPoint: Location = Field(
        ..., description="Details about the starting point of the transport operation."
    )
    endingPoint: Location = Field(
        ..., description="Details about the ending point of the transport operation."
    )
    load: Load = Field(..., description="Details about the load being transported.")
    report: Optional[str] = Field(
        None,
        description="Proof of transport and delivery terms, along with customs and insurance documentation for cross-border shipments. Must be a PDF file.",
    )
    payload: Optional[Payload] = Field(None, description="Additional information.")


class TransportOperation(HandleBaseModel):
    """
    Represents the transport operation data.
    """

    id: int = Field(
        ..., ge=1, description="Unique identifier for the transport operation."
    )
    operator: Organization = Field(
        ...,
        description="Details about the logistic operator that handles the transport operation.",
    )
    schedule: Schedule = Field(
        ..., description="Details about the date and time regarding the operation."
    )
    driver: Driver = Field(..., description="Details about the driver.")
    vehicle: Vehicle = Field(..., description="Details about the vehicle.")
    phase: Optional[List[Phase]] = Field(
        None, description="List of the operation phases."
    )
    document: Optional[List[Document]] = Field(
        None,
        description="List of international consignment notes used for the transport operation.",
    )
    ecmr: Optional[List[EcmrModel]] = Field(
        None,
        description="List of eCMR documents associated with the transport operation.",
    )
    payload: Optional[Payload] = Field(
        None, description="Additional information about the transport operation."
    )
