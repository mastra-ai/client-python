# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mastra import Mastra, AsyncMastra

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestThreads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Mastra) -> None:
        thread = client.memory.threads.create()
        assert thread is None

    @parametrize
    def test_raw_response_create(self, client: Mastra) -> None:
        response = client.memory.threads.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert thread is None

    @parametrize
    def test_streaming_response_create(self, client: Mastra) -> None:
        with client.memory.threads.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert thread is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Mastra) -> None:
        thread = client.memory.threads.retrieve(
            "threadId",
        )
        assert thread is None

    @parametrize
    def test_raw_response_retrieve(self, client: Mastra) -> None:
        response = client.memory.threads.with_raw_response.retrieve(
            "threadId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert thread is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Mastra) -> None:
        with client.memory.threads.with_streaming_response.retrieve(
            "threadId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert thread is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Mastra) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.memory.threads.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Mastra) -> None:
        thread = client.memory.threads.list()
        assert thread is None

    @parametrize
    def test_raw_response_list(self, client: Mastra) -> None:
        response = client.memory.threads.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert thread is None

    @parametrize
    def test_streaming_response_list(self, client: Mastra) -> None:
        with client.memory.threads.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert thread is None

        assert cast(Any, response.is_closed) is True


class TestAsyncThreads:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMastra) -> None:
        thread = await async_client.memory.threads.create()
        assert thread is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMastra) -> None:
        response = await async_client.memory.threads.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert thread is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMastra) -> None:
        async with async_client.memory.threads.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert thread is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMastra) -> None:
        thread = await async_client.memory.threads.retrieve(
            "threadId",
        )
        assert thread is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMastra) -> None:
        response = await async_client.memory.threads.with_raw_response.retrieve(
            "threadId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert thread is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMastra) -> None:
        async with async_client.memory.threads.with_streaming_response.retrieve(
            "threadId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert thread is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMastra) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.memory.threads.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncMastra) -> None:
        thread = await async_client.memory.threads.list()
        assert thread is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMastra) -> None:
        response = await async_client.memory.threads.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert thread is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMastra) -> None:
        async with async_client.memory.threads.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert thread is None

        assert cast(Any, response.is_closed) is True
