"""Index Info Standard Model."""

from typing import Optional

from pydantic import Field, field_validator

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)


class IndexInfoQueryParams(QueryParams):
    """Index Info Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol")
    @classmethod
    def upper_symbol(cls, v: str) -> str:
        """Convert symbol to uppercase."""
        return v.upper()


class IndexInfoData(Data):
    """Index Info Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: str = Field(description="The name of the index.")
    description: Optional[str] = Field(
        description="The short description of the index.", default=None
    )
    methodology: Optional[str] = Field(
        description="URL to the methodology document.", default=None
    )
    factsheet: Optional[str] = Field(
        description="URL to the factsheet document.", default=None
    )
    num_constituents: Optional[int] = Field(
        description="The number of constituents in the index.", default=None
    )
