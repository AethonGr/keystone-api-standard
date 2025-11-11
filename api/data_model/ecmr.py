"""e-CMR data model (v0.1) — aligned 1:1 with the provided e-CMR OpenAPI schema https://git.openlogisticsfoundation.org/wg-electronictransportdocuments/ecmr/ecmr-backend/-/blob/main/openapi.yaml/.

Contact:
  name: Open Logistics Foundation]
  email: info@openlogisticsfoundation.org
  url: https://openlogisticsfoundation.org/
"""

from datetime import datetime
from enum import Enum
from typing import List, Literal, Optional

from .base import HandleBaseModel
from pydantic import Field


class CarrierContactInformation(HandleBaseModel):
    """CarrierContactInformation schema."""

    email: Optional[str] = Field(None, min_length=0, max_length=255)
    carrierPhone: Optional[str] = Field(
        None,
        pattern=r"^(\+|\d)[0-9\s\-().]{0,31}$",
    )
    driverPhone: Optional[str] = Field(
        None,
        pattern=r"^(\+|\d)[0-9\s\-().]{0,31}$",
    )


class CarrierCountryCode(HandleBaseModel):
    """CarrierCountryCode schema."""

    region: Optional[str] = Field(None, min_length=2, max_length=60)
    value: Optional[str] = Field(
        None, min_length=2, max_length=2, pattern=r"^[A-Z]{2}$"
    )


class CarrierInformation(HandleBaseModel):
    """CarrierInformation schema."""

    carrierCompanyName: Optional[str] = None
    carrierDriverName: Optional[str] = Field(None, min_length=2, max_length=60)
    carrierStreet: Optional[str] = Field(None, min_length=2, max_length=255)
    carrierPostcode: Optional[str] = Field(None, min_length=2, max_length=17)
    carrierCity: Optional[str] = Field(None, min_length=2, max_length=60)
    carrierCountryCode: Optional[CarrierCountryCode] = None
    carrierLicensePlate: Optional[str] = Field(None, min_length=2, max_length=30)
    carrierContactInformation: Optional[CarrierContactInformation] = None


class Signature(HandleBaseModel):
    """Signature schema."""

    type: Optional[str] = None
    userName: Optional[str] = None
    userCompany: Optional[str] = None
    userStreet: Optional[str] = None
    userPostCode: Optional[str] = None
    userCity: Optional[str] = None
    userCountry: Optional[str] = None
    timestamp: Optional[datetime] = None
    data: Optional[str] = None


class CarriersReservationsAndObservationsOnTakingOverTheGoods(HandleBaseModel):
    """CarriersReservationsAndObservationsOnTakingOverTheGoods schema."""

    carrierReservationsObservations: Optional[str] = Field(
        None, min_length=2, max_length=512
    )
    senderReservationsObservationsSignature: Optional[Signature] = None


class CashOnDelivery(HandleBaseModel):
    """CashOnDelivery schema."""

    customCashOnDelivery: Optional[float] = Field(None, ge=0, le=999999)


class ConsigneeContactInformation(HandleBaseModel):
    """ConsigneeContactInformation schema."""

    email: Optional[str] = Field(None, min_length=0, max_length=255)
    phone: Optional[str] = Field(
        None,
        pattern=r"^(\+|\d)[0-9\s\-().]{0,31}$",
    )


class ConsigneeCountryCode(HandleBaseModel):
    """ConsigneeCountryCode schema."""

    region: Optional[str] = Field(None, min_length=2, max_length=60)
    value: Optional[str] = Field(
        None, min_length=2, max_length=2, pattern=r"^[A-Z]{2}$"
    )


class ConsigneeInformation(HandleBaseModel):
    """ConsigneeInformation schema."""

    consigneeCompanyName: Optional[str] = None
    consigneePersonName: Optional[str] = Field(None, min_length=2, max_length=60)
    consigneePostcode: Optional[str] = Field(None, min_length=2, max_length=17)
    consigneeCity: Optional[str] = Field(None, min_length=2, max_length=60)
    consigneeCountryCode: Optional[ConsigneeCountryCode] = None
    consigneeStreet: Optional[str] = Field(None, min_length=2, max_length=255)
    consigneeContactInformation: Optional[ConsigneeContactInformation] = None


class CustomCharge(HandleBaseModel):
    """CustomCharge schema."""

    value: Optional[float] = Field(None, ge=0, le=99999)
    currency: Optional[str] = Field(None, min_length=2, max_length=512)
    payer: Optional[Literal["SENDER", "CONSIGNEE"]] = None


class DeliveryOfTheGoods(HandleBaseModel):
    """DeliveryOfTheGoods schema."""

    logisticsLocationCity: Optional[str] = Field(None, min_length=2, max_length=60)
    logisticsLocationOpeningHours: Optional[str] = Field(
        None, min_length=2, max_length=255
    )


class DocumentsHandedToCarrier(HandleBaseModel):
    """DocumentsHandedToCarrier schema."""

    documentsRemarks: Optional[str] = Field(None, min_length=2, max_length=512)


class Established(HandleBaseModel):
    """Established schema."""

    customEstablishedDate: Optional[datetime] = None
    customEstablishedIn: Optional[str] = Field(None, min_length=2, max_length=30)


class GoodsReceived(HandleBaseModel):
    """GoodsReceived schema."""

    confirmedLogisticsLocationName: Optional[str] = Field(
        None, min_length=2, max_length=60
    )
    consigneeReservationsObservations: Optional[str] = Field(
        None, min_length=2, max_length=512
    )
    consigneeSignature: Optional[Signature] = None
    consigneeSignatureDate: Optional[datetime] = None
    consigneeTimeOfArrival: Optional[datetime] = None
    consigneeTimeOfDeparture: Optional[datetime] = None


class GrossWeightInKg(HandleBaseModel):
    """GrossWeightInKg schema."""

    supplyChainConsignmentItemGrossWeight: Optional[float] = Field(None, ge=0, le=99999)


class LogisticsShippingMarksCustomBarcode(HandleBaseModel):
    """LogisticsShippingMarksCustomBarcode schema."""

    barcode: Optional[str] = Field(None, min_length=2, max_length=35)


class MarksAndNos(HandleBaseModel):
    """MarksAndNos schema."""

    logisticsShippingMarksMarking: Optional[str] = Field(
        None, min_length=2, max_length=512
    )
    logisticsShippingMarksCustomBarcodeList: Optional[
        List[LogisticsShippingMarksCustomBarcode]
    ] = Field(None, min_items=0, max_items=32)


class MethodOfPacking(HandleBaseModel):
    """MethodOfPacking schema."""

    logisticsPackageType: Optional[str] = Field(None, min_length=2, max_length=35)


class MultiConsigneeShipment(HandleBaseModel):
    """MultiConsigneeShipment schema."""

    isMultiConsigneeShipment: bool


class NatureOfTheGoods(HandleBaseModel):
    """NatureOfTheGoods schema."""

    transportCargoIdentification: Optional[str] = Field(
        None, min_length=2, max_length=512
    )


class NonContractualPartReservedForTheCarrier(HandleBaseModel):
    """NonContractualPartReservedForTheCarrier schema."""

    nonContractualCarrierRemarks: Optional[str] = Field(
        None, min_length=2, max_length=512
    )


class NumberOfPackages(HandleBaseModel):
    """NumberOfPackages schema."""

    logisticsPackageItemQuantity: Optional[int] = Field(None, ge=0, le=9999)


class OtherUsefulParticulars(HandleBaseModel):
    """OtherUsefulParticulars schema."""

    customParticulars: Optional[str] = Field(None, min_length=2, max_length=512)


class ReferenceIdentificationNumber(HandleBaseModel):
    """ReferenceIdentificationNumber schema."""

    value: Optional[str] = Field(None, min_length=1, max_length=35)


class SenderContactInformation(HandleBaseModel):
    """SenderContactInformation schema."""

    email: Optional[str] = Field(None, min_length=0, max_length=255)
    phone: Optional[str] = Field(
        None,
        pattern=r"^(\+|\d)[0-9\s\-().]{0,31}$",
    )


class SenderCountryCode(HandleBaseModel):
    """SenderCountryCode schema."""

    region: Optional[str] = Field(None, min_length=2, max_length=60)
    value: Optional[str] = Field(
        None, min_length=2, max_length=2, pattern=r"^[A-Z]{2}$"
    )


class SenderInformation(HandleBaseModel):
    """SenderInformation schema."""

    senderCompanyName: Optional[str] = None
    senderPersonName: Optional[str] = Field(None, min_length=2, max_length=60)
    senderStreet: Optional[str] = Field(None, min_length=2, max_length=255)
    senderPostcode: Optional[str] = Field(None, min_length=2, max_length=17)
    senderCity: Optional[str] = Field(None, min_length=2, max_length=60)
    senderCountryCode: Optional[SenderCountryCode] = None
    senderContactInformation: Optional[SenderContactInformation] = None


class SendersInstructions(HandleBaseModel):
    """SendersInstructions schema."""

    transportInstructionsDescription: Optional[str] = Field(
        None, min_length=2, max_length=512
    )


class SpecialAgreementsSenderCarrier(HandleBaseModel):
    """SpecialAgreementsSenderCarrier schema."""

    customSpecialAgreement: Optional[str] = Field(None, min_length=2, max_length=255)


class SuccessiveCarrierContactInformation(HandleBaseModel):
    """SuccessiveCarrierContactInformation schema."""

    email: Optional[str] = Field(None, min_length=0, max_length=255)
    carrierPhone: Optional[str] = Field(
        None,
        pattern=r"^(\+|\d)[0-9\s\-().]{0,31}$",
    )
    driverPhone: Optional[str] = Field(
        None,
        pattern=r"^(\+|\d)[0-9\s\-().]{0,31}$",
    )


class SuccessiveCarrierCountryCode(HandleBaseModel):
    """SuccessiveCarrierCountryCode schema."""

    region: Optional[str] = Field(None, min_length=2, max_length=60)
    value: Optional[str] = Field(
        None, min_length=2, max_length=2, pattern=r"^[A-Z]{2}$"
    )


class SuccessiveCarrierInformation(HandleBaseModel):
    """SuccessiveCarrierInformation schema."""

    successiveCarrierCity: Optional[str] = Field(None, min_length=2, max_length=60)
    successiveCarrierCountryCode: Optional[SuccessiveCarrierCountryCode] = None
    successiveCarrierCompanyName: Optional[str] = None
    successiveCarrierDriverName: Optional[str] = Field(
        None, min_length=2, max_length=60
    )
    successiveCarrierPostcode: Optional[str] = Field(None, min_length=2, max_length=17)
    successiveCarrierStreet: Optional[str] = Field(None, min_length=2, max_length=255)
    successiveCarrierContactInformation: Optional[
        SuccessiveCarrierContactInformation
    ] = None


class TakingOverTheGoods(HandleBaseModel):
    """TakingOverTheGoods schema."""

    takingOverTheGoodsPlace: Optional[str] = Field(None, min_length=2, max_length=60)
    logisticsTimeOfArrivalDateTime: Optional[datetime] = None
    logisticsTimeOfDepartureDateTime: Optional[datetime] = None


class ToBePaidBy(HandleBaseModel):
    """ToBePaidBy schema."""

    customChargeCarriage: Optional[CustomCharge] = None
    customChargeSupplementary: Optional[CustomCharge] = None
    customChargeCustomsDuties: Optional[CustomCharge] = None
    customChargeOther: Optional[CustomCharge] = None


class VolumeInM3(HandleBaseModel):
    """VolumeInM3 schema."""

    supplyChainConsignmentItemGrossVolume: Optional[float] = Field(None, ge=0, le=9999)


class Item(HandleBaseModel):
    """Item schema."""

    marksAndNos: Optional[MarksAndNos] = None
    numberOfPackages: Optional[NumberOfPackages] = None
    methodOfPacking: Optional[MethodOfPacking] = None
    natureOfTheGoods: Optional[NatureOfTheGoods] = None
    grossWeightInKg: Optional[GrossWeightInKg] = None
    volumeInM3: Optional[VolumeInM3] = None


class EcmrConsignment(HandleBaseModel):
    """EcmrConsignment schema."""

    senderInformation: Optional[SenderInformation] = None
    multiConsigneeShipment: Optional[MultiConsigneeShipment] = None
    consigneeInformation: Optional[ConsigneeInformation] = None
    takingOverTheGoods: Optional[TakingOverTheGoods] = None
    deliveryOfTheGoods: Optional[DeliveryOfTheGoods] = None
    sendersInstructions: Optional[SendersInstructions] = None
    carrierInformation: Optional[CarrierInformation] = None
    successiveCarrierInformation: Optional[SuccessiveCarrierInformation] = None
    carriersReservationsAndObservationsOnTakingOverTheGoods: Optional[
        CarriersReservationsAndObservationsOnTakingOverTheGoods
    ] = None
    documentsHandedToCarrier: Optional[DocumentsHandedToCarrier] = None
    itemList: Optional[List[Item]] = None
    specialAgreementsSenderCarrier: Optional[SpecialAgreementsSenderCarrier] = None
    toBePaidBy: Optional[ToBePaidBy] = None
    otherUsefulParticulars: Optional[OtherUsefulParticulars] = None
    cashOnDelivery: Optional[CashOnDelivery] = None
    established: Optional[Established] = None
    goodsReceived: Optional[GoodsReceived] = None
    nonContractualPartReservedForTheCarrier: Optional[
        NonContractualPartReservedForTheCarrier
    ] = None
    referenceIdentificationNumber: Optional[ReferenceIdentificationNumber] = None


class EcmrStatus(str, Enum):
    """Enum for eCMR status."""

    NEW = "NEW"
    LOADING = "LOADING"
    IN_TRANSPORT = "IN_TRANSPORT"
    DELIVERED = "DELIVERED"


class EcmrModel(HandleBaseModel):
    """EcmrModel schema. This is the main model for an eCMR document."""

    ecmrId: Optional[str] = None
    ecmrConsignment: EcmrConsignment
    ecmrStatus: Optional[EcmrStatus] = None

    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    editedAt: Optional[datetime] = None
    editedBy: Optional[str] = None
    originUrl: Optional[str] = None
