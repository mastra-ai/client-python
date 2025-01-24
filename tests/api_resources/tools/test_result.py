# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mastra_client_py import MastraClient, AsyncMastraClient

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResult:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: MastraClient) -> None:
        result = client.tools.result.retrieve(
            result_id="resultId",
            tool_id="toolId",
        )
        assert result is None

    @parametrize
    def test_raw_response_retrieve(self, client: MastraClient) -> None:
        response = client.tools.result.with_raw_response.retrieve(
            result_id="resultId",
            tool_id="toolId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = response.parse()
        assert result is None

    @parametrize
    def test_streaming_response_retrieve(self, client: MastraClient) -> None:
        with client.tools.result.with_streaming_response.retrieve(
            result_id="resultId",
            tool_id="toolId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = response.parse()
            assert result is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: MastraClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.tools.result.with_raw_response.retrieve(
                result_id="resultId",
                tool_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `result_id` but received ''"):
            client.tools.result.with_raw_response.retrieve(
                result_id="",
                tool_id="toolId",
            )


class TestAsyncResult:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMastraClient) -> None:
        result = await async_client.tools.result.retrieve(
            result_id="resultId",
            tool_id="toolId",
        )
        assert result is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMastraClient) -> None:
        response = await async_client.tools.result.with_raw_response.retrieve(
            result_id="resultId",
            tool_id="toolId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = await response.parse()
        assert result is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMastraClient) -> None:
        async with async_client.tools.result.with_streaming_response.retrieve(
            result_id="resultId",
            tool_id="toolId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = await response.parse()
            assert result is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMastraClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.tools.result.with_raw_response.retrieve(
                result_id="resultId",
                tool_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `result_id` but received ''"):
            await async_client.tools.result.with_raw_response.retrieve(
                result_id="",
                tool_id="toolId",
            )
