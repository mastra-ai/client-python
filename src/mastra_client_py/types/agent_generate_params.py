# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentGenerateParams"]


class AgentGenerateParams(TypedDict, total=False):
    messages: Required[Iterable[object]]

    output: object

    resourceid: str

    thread_id: Annotated[str, PropertyInfo(alias="threadId")]
