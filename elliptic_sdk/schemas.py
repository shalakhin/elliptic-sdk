import uuid
from datetime import datetime
from typing import Any
from typing import List
from pydantic import BaseModel
from pydantic import Field
from .enums import LegacyWalletTypeEnum
from .enums import LegacyWalletPayloadTypeEnum


class LegacyWalletSubject(BaseModel):
    type: LegacyWalletTypeEnum = Field(default=LegacyWalletTypeEnum.ADDRESS)
    asset: str
    blockchain: str
    hash: str

    class Config:
        use_enum_values = True


class LegacyWalletPayload(BaseModel):
    subject: LegacyWalletSubject
    type: LegacyWalletPayloadTypeEnum = Field(
        default=LegacyWalletPayloadTypeEnum.WALLET_EXPOSURE)
    customer_reference: str

    class Config:
        use_enum_values = True


class AnalysedBy(BaseModel):
    id: uuid.UUID
    type: str


class ClusterEntity(BaseModel):
    name: str
    category: str
    actor_id: int
    is_primary_entity: bool
    is_vasp: Any
    is_after_sanction_date: bool


class Customer(BaseModel):
    reference: str


class LegacyWalletResponse(BaseModel):
    analysed_by: AnalysedBy
    cluster_entities: List[ClusterEntity]
    id: uuid.UUID
    subject: LegacyWalletSubject
    type: LegacyWalletPayloadTypeEnum
    customer: Customer
    created_at: datetime
    updated_at: datetime
    analysed_at: datetime
    process_status: str
    process_status_id: int
    workflow_status_id: int
    workflow_status: str
    error: str | None
    team_id: uuid.UUID
    asset_tier: str
    risk_score: float | None
