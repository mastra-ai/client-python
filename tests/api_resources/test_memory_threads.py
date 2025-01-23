# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mastra import Mastra, AsyncMastra

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMemoryThreads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Mastra) -> None:
        memory_thread = client.memory_threads.update(
            thread_id="threadId",
            body={},
        )
        assert memory_thread is None

    @parametrize
    def test_raw_response_update(self, client: Mastra) -> None:
        response = client.memory_threads.with_raw_response.update(
            thread_id="threadId",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory_thread = response.parse()
        assert memory_thread is None

    @parametrize
    def test_streaming_response_update(self, client: Mastra) -> None:
        with client.memory_threads.with_streaming_response.update(
            thread_id="threadId",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory_thread = response.parse()
            assert memory_thread is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Mastra) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.memory_threads.with_raw_response.update(
                thread_id="",
                body={},
            )

    @parametrize
    def test_method_delete(self, client: Mastra) -> None:
        memory_thread = client.memory_threads.delete(
            "threadId",
        )
        assert memory_thread is None

    @parametrize
    def test_raw_response_delete(self, client: Mastra) -> None:
        response = client.memory_threads.with_raw_response.delete(
            "threadId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory_thread = response.parse()
        assert memory_thread is None

    @parametrize
    def test_streaming_response_delete(self, client: Mastra) -> None:
        with client.memory_threads.with_streaming_response.delete(
            "threadId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory_thread = response.parse()
            assert memory_thread is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Mastra) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.memory_threads.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_tool_result(self, client: Mastra) -> None:
        memory_thread = client.memory_threads.tool_result(
            thread_id="threadId",
            result_id="resultId",
            tool_id="toolId",
        )
        assert memory_thread is None

    @parametrize
    def test_raw_response_tool_result(self, client: Mastra) -> None:
        response = client.memory_threads.with_raw_response.tool_result(
            thread_id="threadId",
            result_id="resultId",
            tool_id="toolId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory_thread = response.parse()
        assert memory_thread is None

    @parametrize
    def test_streaming_response_tool_result(self, client: Mastra) -> None:
        with client.memory_threads.with_streaming_response.tool_result(
            thread_id="threadId",
            result_id="resultId",
            tool_id="toolId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory_thread = response.parse()
            assert memory_thread is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_tool_result(self, client: Mastra) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.memory_threads.with_raw_response.tool_result(
                thread_id="",
                result_id="resultId",
                tool_id="toolId",
            )


class TestAsyncMemoryThreads:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncMastra) -> None:
        memory_thread = await async_client.memory_threads.update(
            thread_id="threadId",
            body={},
        )
        assert memory_thread is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMastra) -> None:
        response = await async_client.memory_threads.with_raw_response.update(
            thread_id="threadId",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory_thread = await response.parse()
        assert memory_thread is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMastra) -> None:
        async with async_client.memory_threads.with_streaming_response.update(
            thread_id="threadId",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory_thread = await response.parse()
            assert memory_thread is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncMastra) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.memory_threads.with_raw_response.update(
                thread_id="",
                body={},
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncMastra) -> None:
        memory_thread = await async_client.memory_threads.delete(
            "threadId",
        )
        assert memory_thread is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMastra) -> None:
        response = await async_client.memory_threads.with_raw_response.delete(
            "threadId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory_thread = await response.parse()
        assert memory_thread is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMastra) -> None:
        async with async_client.memory_threads.with_streaming_response.delete(
            "threadId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory_thread = await response.parse()
            assert memory_thread is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMastra) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.memory_threads.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_tool_result(self, async_client: AsyncMastra) -> None:
        memory_thread = await async_client.memory_threads.tool_result(
            thread_id="threadId",
            result_id="resultId",
            tool_id="toolId",
        )
        assert memory_thread is None

    @parametrize
    async def test_raw_response_tool_result(self, async_client: AsyncMastra) -> None:
        response = await async_client.memory_threads.with_raw_response.tool_result(
            thread_id="threadId",
            result_id="resultId",
            tool_id="toolId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory_thread = await response.parse()
        assert memory_thread is None

    @parametrize
    async def test_streaming_response_tool_result(self, async_client: AsyncMastra) -> None:
        async with async_client.memory_threads.with_streaming_response.tool_result(
            thread_id="threadId",
            result_id="resultId",
            tool_id="toolId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory_thread = await response.parse()
            assert memory_thread is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_tool_result(self, async_client: AsyncMastra) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.memory_threads.with_raw_response.tool_result(
                thread_id="",
                result_id="resultId",
                tool_id="toolId",
            )
