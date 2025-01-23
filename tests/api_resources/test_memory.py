# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mastra import Mastra, AsyncMastra

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMemory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_save_messages(self, client: Mastra) -> None:
        memory = client.memory.save_messages(
            messages=[{}],
        )
        assert memory is None

    @parametrize
    def test_raw_response_save_messages(self, client: Mastra) -> None:
        response = client.memory.with_raw_response.save_messages(
            messages=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert memory is None

    @parametrize
    def test_streaming_response_save_messages(self, client: Mastra) -> None:
        with client.memory.with_streaming_response.save_messages(
            messages=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert memory is None

        assert cast(Any, response.is_closed) is True


class TestAsyncMemory:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_save_messages(self, async_client: AsyncMastra) -> None:
        memory = await async_client.memory.save_messages(
            messages=[{}],
        )
        assert memory is None

    @parametrize
    async def test_raw_response_save_messages(self, async_client: AsyncMastra) -> None:
        response = await async_client.memory.with_raw_response.save_messages(
            messages=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert memory is None

    @parametrize
    async def test_streaming_response_save_messages(self, async_client: AsyncMastra) -> None:
        async with async_client.memory.with_streaming_response.save_messages(
            messages=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert memory is None

        assert cast(Any, response.is_closed) is True
