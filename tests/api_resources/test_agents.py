# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mastra_client_py import MastraClient, AsyncMastraClient

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: MastraClient) -> None:
        agent = client.agents.retrieve(
            "agentId",
        )
        assert agent is None

    @parametrize
    def test_raw_response_retrieve(self, client: MastraClient) -> None:
        response = client.agents.with_raw_response.retrieve(
            "agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert agent is None

    @parametrize
    def test_streaming_response_retrieve(self, client: MastraClient) -> None:
        with client.agents.with_streaming_response.retrieve(
            "agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: MastraClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: MastraClient) -> None:
        agent = client.agents.list()
        assert agent is None

    @parametrize
    def test_raw_response_list(self, client: MastraClient) -> None:
        response = client.agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert agent is None

    @parametrize
    def test_streaming_response_list(self, client: MastraClient) -> None:
        with client.agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_generate(self, client: MastraClient) -> None:
        agent = client.agents.generate(
            agent_id="agentId",
            messages=[{}],
        )
        assert agent is None

    @parametrize
    def test_method_generate_with_all_params(self, client: MastraClient) -> None:
        agent = client.agents.generate(
            agent_id="agentId",
            messages=[{}],
            output={},
            resourceid="resourceid",
            thread_id="threadId",
        )
        assert agent is None

    @parametrize
    def test_raw_response_generate(self, client: MastraClient) -> None:
        response = client.agents.with_raw_response.generate(
            agent_id="agentId",
            messages=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert agent is None

    @parametrize
    def test_streaming_response_generate(self, client: MastraClient) -> None:
        with client.agents.with_streaming_response.generate(
            agent_id="agentId",
            messages=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_generate(self, client: MastraClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.generate(
                agent_id="",
                messages=[{}],
            )

    @parametrize
    def test_method_stream(self, client: MastraClient) -> None:
        agent = client.agents.stream(
            agent_id="agentId",
            messages=[{}],
        )
        assert_matches_type(str, agent, path=["response"])

    @parametrize
    def test_method_stream_with_all_params(self, client: MastraClient) -> None:
        agent = client.agents.stream(
            agent_id="agentId",
            messages=[{}],
            output={},
            resourceid="resourceid",
            thread_id="threadId",
        )
        assert_matches_type(str, agent, path=["response"])

    @parametrize
    def test_raw_response_stream(self, client: MastraClient) -> None:
        response = client.agents.with_raw_response.stream(
            agent_id="agentId",
            messages=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(str, agent, path=["response"])

    @parametrize
    def test_streaming_response_stream(self, client: MastraClient) -> None:
        with client.agents.with_streaming_response.stream(
            agent_id="agentId",
            messages=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(str, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_stream(self, client: MastraClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.stream(
                agent_id="",
                messages=[{}],
            )


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMastraClient) -> None:
        agent = await async_client.agents.retrieve(
            "agentId",
        )
        assert agent is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMastraClient) -> None:
        response = await async_client.agents.with_raw_response.retrieve(
            "agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert agent is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMastraClient) -> None:
        async with async_client.agents.with_streaming_response.retrieve(
            "agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMastraClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncMastraClient) -> None:
        agent = await async_client.agents.list()
        assert agent is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMastraClient) -> None:
        response = await async_client.agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert agent is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMastraClient) -> None:
        async with async_client.agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_generate(self, async_client: AsyncMastraClient) -> None:
        agent = await async_client.agents.generate(
            agent_id="agentId",
            messages=[{}],
        )
        assert agent is None

    @parametrize
    async def test_method_generate_with_all_params(self, async_client: AsyncMastraClient) -> None:
        agent = await async_client.agents.generate(
            agent_id="agentId",
            messages=[{}],
            output={},
            resourceid="resourceid",
            thread_id="threadId",
        )
        assert agent is None

    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncMastraClient) -> None:
        response = await async_client.agents.with_raw_response.generate(
            agent_id="agentId",
            messages=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert agent is None

    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncMastraClient) -> None:
        async with async_client.agents.with_streaming_response.generate(
            agent_id="agentId",
            messages=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_generate(self, async_client: AsyncMastraClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.generate(
                agent_id="",
                messages=[{}],
            )

    @parametrize
    async def test_method_stream(self, async_client: AsyncMastraClient) -> None:
        agent = await async_client.agents.stream(
            agent_id="agentId",
            messages=[{}],
        )
        assert_matches_type(str, agent, path=["response"])

    @parametrize
    async def test_method_stream_with_all_params(self, async_client: AsyncMastraClient) -> None:
        agent = await async_client.agents.stream(
            agent_id="agentId",
            messages=[{}],
            output={},
            resourceid="resourceid",
            thread_id="threadId",
        )
        assert_matches_type(str, agent, path=["response"])

    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncMastraClient) -> None:
        response = await async_client.agents.with_raw_response.stream(
            agent_id="agentId",
            messages=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(str, agent, path=["response"])

    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncMastraClient) -> None:
        async with async_client.agents.with_streaming_response.stream(
            agent_id="agentId",
            messages=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(str, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_stream(self, async_client: AsyncMastraClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.stream(
                agent_id="",
                messages=[{}],
            )
