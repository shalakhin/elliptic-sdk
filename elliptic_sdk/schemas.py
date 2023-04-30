"""Elliptic SDK elliptic_sdk/schemas.py."""
import uuid
from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from .enums import LegacyWalletPayloadTypeEnum, WalletAnalysisSubjectTypeEnum


class LegacyWalletSubject(BaseModel):
    """LegacyWalletSubject schema."""

    asset: str
    type: WalletAnalysisSubjectTypeEnum = Field(
        default=WalletAnalysisSubjectTypeEnum.ADDRESS,
    )
    hash: str
    blockchain: str

    class Config:
        """Config."""

        use_enum_values = True


class LegacyWalletPayload(BaseModel):
    """LegacyWalletPayload schema."""

    subject: LegacyWalletSubject
    type: LegacyWalletPayloadTypeEnum = Field(
        default=LegacyWalletPayloadTypeEnum.WALLET_EXPOSURE,
    )
    customer_reference: str

    class Config:
        """Config."""

        use_enum_values = True


class AnalysedBy(BaseModel):
    """AnalysedBy schema."""

    id: uuid.UUID
    type: str


class ClusterEntity(BaseModel):
    """ClusterEntity schema."""

    name: str
    category: str
    is_primary_entity: bool
    is_vasp: Any
    actor_id: int
    is_after_sanction_date: bool


class Customer(BaseModel):
    """Customer schema."""

    reference: str


class LegacyWalletResponse(BaseModel):
    """LegacyWalletResponse schema."""

    id: uuid.UUID
    type: LegacyWalletPayloadTypeEnum
    subject: LegacyWalletSubject
    customer: Customer
    created_at: datetime
    updated_at: datetime
    analysed_at: datetime
    analysed_by: AnalysedBy
    asset_tier: str
    cluster_entities: list[ClusterEntity]
    team_id: uuid.UUID
    risk_score: float | None
    error: str | None
    workflow_status: str
    workflow_status_id: int
    process_status: str
    process_status_id: int
