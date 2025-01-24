# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ToolExecuteParams"]


class ToolExecuteParams(TypedDict, total=False):
    args: Required[object]

    resourceid: str

    thread_id: Annotated[str, PropertyInfo(alias="threadId")]
