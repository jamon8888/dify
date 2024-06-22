from typing import Optional

from pydantic import BaseModel, Field, PositiveInt


class OracleConfigs(BaseModel):
    """
    ORACLE configs
    """

    ORACLE_HOST: Optional[str] = Field(
        description='ORACLE host',
        default=None,
    )

    ORACLE_PORT: Optional[PositiveInt] = Field(
        description='ORACLE port',
        default=None,
    )

    ORACLE_USER: Optional[str] = Field(
        description='ORACLE user',
        default=None,
    )

    ORACLE_PASSWORD: Optional[str] = Field(
        description='ORACLE password',
        default=None,
    )

    ORACLE_DATABASE: Optional[str] = Field(
        description='ORACLE database',
        default=None,
    )