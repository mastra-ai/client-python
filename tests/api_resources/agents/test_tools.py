# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mastra_client_py import MastraClient, AsyncMastraClient

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_execute(self, client: MastraClient) -> None:
        tool = client.agents.tools.execute(
            tool_id="toolId",
            agent_id="agentId",
            args={},
        )
        assert tool is None

    @parametrize
    def test_method_execute_with_all_params(self, client: MastraClient) -> None:
        tool = client.agents.tools.execute(
            tool_id="toolId",
            agent_id="agentId",
            args={},
            resourceid="resourceid",
            thread_id="threadId",
        )
        assert tool is None

    @parametrize
    def test_raw_response_execute(self, client: MastraClient) -> None:
        response = client.agents.tools.with_raw_response.execute(
            tool_id="toolId",
            agent_id="agentId",
            args={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert tool is None

    @parametrize
    def test_streaming_response_execute(self, client: MastraClient) -> None:
        with client.agents.tools.with_streaming_response.execute(
            tool_id="toolId",
            agent_id="agentId",
            args={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert tool is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_execute(self, client: MastraClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.tools.with_raw_response.execute(
                tool_id="toolId",
                agent_id="",
                args={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.agents.tools.with_raw_response.execute(
                tool_id="",
                agent_id="agentId",
                args={},
            )


class TestAsyncTools:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_execute(self, async_client: AsyncMastraClient) -> None:
        tool = await async_client.agents.tools.execute(
            tool_id="toolId",
            agent_id="agentId",
            args={},
        )
        assert tool is None

    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncMastraClient) -> None:
        tool = await async_client.agents.tools.execute(
            tool_id="toolId",
            agent_id="agentId",
            args={},
            resourceid="resourceid",
            thread_id="threadId",
        )
        assert tool is None

    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncMastraClient) -> None:
        response = await async_client.agents.tools.with_raw_response.execute(
            tool_id="toolId",
            agent_id="agentId",
            args={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert tool is None

    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncMastraClient) -> None:
        async with async_client.agents.tools.with_streaming_response.execute(
            tool_id="toolId",
            agent_id="agentId",
            args={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert tool is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_execute(self, async_client: AsyncMastraClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.tools.with_raw_response.execute(
                tool_id="toolId",
                agent_id="",
                args={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.agents.tools.with_raw_response.execute(
                tool_id="",
                agent_id="agentId",
                args={},
            )
