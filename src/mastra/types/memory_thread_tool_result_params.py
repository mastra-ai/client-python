# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MemoryThreadToolResultParams"]


class MemoryThreadToolResultParams(TypedDict, total=False):
    result_id: Required[Annotated[str, PropertyInfo(alias="resultId")]]

    tool_id: Required[Annotated[str, PropertyInfo(alias="toolId")]]
