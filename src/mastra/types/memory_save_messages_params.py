# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["MemorySaveMessagesParams"]


class MemorySaveMessagesParams(TypedDict, total=False):
    messages: Required[Iterable[object]]
