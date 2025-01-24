# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mastra_client_py import MastraClient, AsyncMastraClient

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestThreads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: MastraClient) -> None:
        thread = client.memory.threads.create()
        assert thread is None

    @parametrize
    def test_raw_response_create(self, client: MastraClient) -> None:
        response = client.memory.threads.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert thread is None

    @parametrize
    def test_streaming_response_create(self, client: MastraClient) -> None:
        with client.memory.threads.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert thread is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: MastraClient) -> None:
        thread = client.memory.threads.retrieve(
            "threadId",
        )
        assert thread is None

    @parametrize
    def test_raw_response_retrieve(self, client: MastraClient) -> None:
        response = client.memory.threads.with_raw_response.retrieve(
            "threadId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert thread is None

    @parametrize
    def test_streaming_response_retrieve(self, client: MastraClient) -> None:
        with client.memory.threads.with_streaming_response.retrieve(
            "threadId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert thread is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: MastraClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.memory.threads.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: MastraClient) -> None:
        thread = client.memory.threads.update(
            thread_id="threadId",
            body={},
        )
        assert thread is None

    @parametrize
    def test_raw_response_update(self, client: MastraClient) -> None:
        response = client.memory.threads.with_raw_response.update(
            thread_id="threadId",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert thread is None

    @parametrize
    def test_streaming_response_update(self, client: MastraClient) -> None:
        with client.memory.threads.with_streaming_response.update(
            thread_id="threadId",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert thread is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: MastraClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.memory.threads.with_raw_response.update(
                thread_id="",
                body={},
            )

    @parametrize
    def test_method_list(self, client: MastraClient) -> None:
        thread = client.memory.threads.list()
        assert thread is None

    @parametrize
    def test_raw_response_list(self, client: MastraClient) -> None:
        response = client.memory.threads.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert thread is None

    @parametrize
    def test_streaming_response_list(self, client: MastraClient) -> None:
        with client.memory.threads.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert thread is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: MastraClient) -> None:
        thread = client.memory.threads.delete(
            "threadId",
        )
        assert thread is None

    @parametrize
    def test_raw_response_delete(self, client: MastraClient) -> None:
        response = client.memory.threads.with_raw_response.delete(
            "threadId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert thread is None

    @parametrize
    def test_streaming_response_delete(self, client: MastraClient) -> None:
        with client.memory.threads.with_streaming_response.delete(
            "threadId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert thread is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: MastraClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.memory.threads.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_context_window(self, client: MastraClient) -> None:
        thread = client.memory.threads.context_window(
            "threadId",
        )
        assert thread is None

    @parametrize
    def test_raw_response_context_window(self, client: MastraClient) -> None:
        response = client.memory.threads.with_raw_response.context_window(
            "threadId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert thread is None

    @parametrize
    def test_streaming_response_context_window(self, client: MastraClient) -> None:
        with client.memory.threads.with_streaming_response.context_window(
            "threadId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert thread is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_context_window(self, client: MastraClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.memory.threads.with_raw_response.context_window(
                "",
            )

    @parametrize
    def test_method_tool_result(self, client: MastraClient) -> None:
        thread = client.memory.threads.tool_result(
            thread_id="threadId",
            result_id="resultId",
            tool_id="toolId",
        )
        assert thread is None

    @parametrize
    def test_raw_response_tool_result(self, client: MastraClient) -> None:
        response = client.memory.threads.with_raw_response.tool_result(
            thread_id="threadId",
            result_id="resultId",
            tool_id="toolId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert thread is None

    @parametrize
    def test_streaming_response_tool_result(self, client: MastraClient) -> None:
        with client.memory.threads.with_streaming_response.tool_result(
            thread_id="threadId",
            result_id="resultId",
            tool_id="toolId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert thread is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_tool_result(self, client: MastraClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.memory.threads.with_raw_response.tool_result(
                thread_id="",
                result_id="resultId",
                tool_id="toolId",
            )


class TestAsyncThreads:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMastraClient) -> None:
        thread = await async_client.memory.threads.create()
        assert thread is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMastraClient) -> None:
        response = await async_client.memory.threads.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert thread is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMastraClient) -> None:
        async with async_client.memory.threads.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert thread is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMastraClient) -> None:
        thread = await async_client.memory.threads.retrieve(
            "threadId",
        )
        assert thread is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMastraClient) -> None:
        response = await async_client.memory.threads.with_raw_response.retrieve(
            "threadId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert thread is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMastraClient) -> None:
        async with async_client.memory.threads.with_streaming_response.retrieve(
            "threadId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert thread is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMastraClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.memory.threads.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncMastraClient) -> None:
        thread = await async_client.memory.threads.update(
            thread_id="threadId",
            body={},
        )
        assert thread is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMastraClient) -> None:
        response = await async_client.memory.threads.with_raw_response.update(
            thread_id="threadId",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert thread is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMastraClient) -> None:
        async with async_client.memory.threads.with_streaming_response.update(
            thread_id="threadId",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert thread is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncMastraClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.memory.threads.with_raw_response.update(
                thread_id="",
                body={},
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncMastraClient) -> None:
        thread = await async_client.memory.threads.list()
        assert thread is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMastraClient) -> None:
        response = await async_client.memory.threads.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert thread is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMastraClient) -> None:
        async with async_client.memory.threads.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert thread is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncMastraClient) -> None:
        thread = await async_client.memory.threads.delete(
            "threadId",
        )
        assert thread is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMastraClient) -> None:
        response = await async_client.memory.threads.with_raw_response.delete(
            "threadId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert thread is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMastraClient) -> None:
        async with async_client.memory.threads.with_streaming_response.delete(
            "threadId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert thread is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMastraClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.memory.threads.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_context_window(self, async_client: AsyncMastraClient) -> None:
        thread = await async_client.memory.threads.context_window(
            "threadId",
        )
        assert thread is None

    @parametrize
    async def test_raw_response_context_window(self, async_client: AsyncMastraClient) -> None:
        response = await async_client.memory.threads.with_raw_response.context_window(
            "threadId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert thread is None

    @parametrize
    async def test_streaming_response_context_window(self, async_client: AsyncMastraClient) -> None:
        async with async_client.memory.threads.with_streaming_response.context_window(
            "threadId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert thread is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_context_window(self, async_client: AsyncMastraClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.memory.threads.with_raw_response.context_window(
                "",
            )

    @parametrize
    async def test_method_tool_result(self, async_client: AsyncMastraClient) -> None:
        thread = await async_client.memory.threads.tool_result(
            thread_id="threadId",
            result_id="resultId",
            tool_id="toolId",
        )
        assert thread is None

    @parametrize
    async def test_raw_response_tool_result(self, async_client: AsyncMastraClient) -> None:
        response = await async_client.memory.threads.with_raw_response.tool_result(
            thread_id="threadId",
            result_id="resultId",
            tool_id="toolId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert thread is None

    @parametrize
    async def test_streaming_response_tool_result(self, async_client: AsyncMastraClient) -> None:
        async with async_client.memory.threads.with_streaming_response.tool_result(
            thread_id="threadId",
            result_id="resultId",
            tool_id="toolId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert thread is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_tool_result(self, async_client: AsyncMastraClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.memory.threads.with_raw_response.tool_result(
                thread_id="",
                result_id="resultId",
                tool_id="toolId",
            )
