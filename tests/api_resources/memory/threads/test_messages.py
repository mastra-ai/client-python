# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mastra_client_py import MastraClient, AsyncMastraClient

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: MastraClient) -> None:
        message = client.memory.threads.messages.list(
            "threadId",
        )
        assert message is None

    @parametrize
    def test_raw_response_list(self, client: MastraClient) -> None:
        response = client.memory.threads.messages.with_raw_response.list(
            "threadId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert message is None

    @parametrize
    def test_streaming_response_list(self, client: MastraClient) -> None:
        with client.memory.threads.messages.with_streaming_response.list(
            "threadId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert message is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: MastraClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.memory.threads.messages.with_raw_response.list(
                "",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncMastraClient) -> None:
        message = await async_client.memory.threads.messages.list(
            "threadId",
        )
        assert message is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMastraClient) -> None:
        response = await async_client.memory.threads.messages.with_raw_response.list(
            "threadId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert message is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMastraClient) -> None:
        async with async_client.memory.threads.messages.with_streaming_response.list(
            "threadId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert message is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncMastraClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.memory.threads.messages.with_raw_response.list(
                "",
            )
