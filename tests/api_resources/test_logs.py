# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mastra import Mastra, AsyncMastra

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Mastra) -> None:
        log = client.logs.retrieve(
            "runId",
        )
        assert log is None

    @parametrize
    def test_raw_response_retrieve(self, client: Mastra) -> None:
        response = client.logs.with_raw_response.retrieve(
            "runId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert log is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Mastra) -> None:
        with client.logs.with_streaming_response.retrieve(
            "runId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert log is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Mastra) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.logs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Mastra) -> None:
        log = client.logs.list()
        assert log is None

    @parametrize
    def test_raw_response_list(self, client: Mastra) -> None:
        response = client.logs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert log is None

    @parametrize
    def test_streaming_response_list(self, client: Mastra) -> None:
        with client.logs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert log is None

        assert cast(Any, response.is_closed) is True


class TestAsyncLogs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMastra) -> None:
        log = await async_client.logs.retrieve(
            "runId",
        )
        assert log is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMastra) -> None:
        response = await async_client.logs.with_raw_response.retrieve(
            "runId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert log is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMastra) -> None:
        async with async_client.logs.with_streaming_response.retrieve(
            "runId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert log is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMastra) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.logs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncMastra) -> None:
        log = await async_client.logs.list()
        assert log is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMastra) -> None:
        response = await async_client.logs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert log is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMastra) -> None:
        async with async_client.logs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert log is None

        assert cast(Any, response.is_closed) is True
