# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mastra_client_py import MastraClient, AsyncMastraClient

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: MastraClient) -> None:
        status = client.memory.status.retrieve()
        assert status is None

    @parametrize
    def test_raw_response_retrieve(self, client: MastraClient) -> None:
        response = client.memory.status.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert status is None

    @parametrize
    def test_streaming_response_retrieve(self, client: MastraClient) -> None:
        with client.memory.status.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert status is None

        assert cast(Any, response.is_closed) is True


class TestAsyncStatus:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMastraClient) -> None:
        status = await async_client.memory.status.retrieve()
        assert status is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMastraClient) -> None:
        response = await async_client.memory.status.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert status is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMastraClient) -> None:
        async with async_client.memory.status.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert status is None

        assert cast(Any, response.is_closed) is True
