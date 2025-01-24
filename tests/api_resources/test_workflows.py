# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mastra_client_py import MastraClient, AsyncMastraClient

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkflows:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: MastraClient) -> None:
        workflow = client.workflows.retrieve(
            "workflowId",
        )
        assert workflow is None

    @parametrize
    def test_raw_response_retrieve(self, client: MastraClient) -> None:
        response = client.workflows.with_raw_response.retrieve(
            "workflowId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert workflow is None

    @parametrize
    def test_streaming_response_retrieve(self, client: MastraClient) -> None:
        with client.workflows.with_streaming_response.retrieve(
            "workflowId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert workflow is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: MastraClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            client.workflows.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: MastraClient) -> None:
        workflow = client.workflows.list()
        assert workflow is None

    @parametrize
    def test_raw_response_list(self, client: MastraClient) -> None:
        response = client.workflows.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert workflow is None

    @parametrize
    def test_streaming_response_list(self, client: MastraClient) -> None:
        with client.workflows.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert workflow is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_execute(self, client: MastraClient) -> None:
        workflow = client.workflows.execute(
            workflow_id="workflowId",
        )
        assert workflow is None

    @parametrize
    def test_method_execute_with_all_params(self, client: MastraClient) -> None:
        workflow = client.workflows.execute(
            workflow_id="workflowId",
            input={},
        )
        assert workflow is None

    @parametrize
    def test_raw_response_execute(self, client: MastraClient) -> None:
        response = client.workflows.with_raw_response.execute(
            workflow_id="workflowId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert workflow is None

    @parametrize
    def test_streaming_response_execute(self, client: MastraClient) -> None:
        with client.workflows.with_streaming_response.execute(
            workflow_id="workflowId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert workflow is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_execute(self, client: MastraClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            client.workflows.with_raw_response.execute(
                workflow_id="",
            )


class TestAsyncWorkflows:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMastraClient) -> None:
        workflow = await async_client.workflows.retrieve(
            "workflowId",
        )
        assert workflow is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMastraClient) -> None:
        response = await async_client.workflows.with_raw_response.retrieve(
            "workflowId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert workflow is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMastraClient) -> None:
        async with async_client.workflows.with_streaming_response.retrieve(
            "workflowId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert workflow is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMastraClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            await async_client.workflows.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncMastraClient) -> None:
        workflow = await async_client.workflows.list()
        assert workflow is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMastraClient) -> None:
        response = await async_client.workflows.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert workflow is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMastraClient) -> None:
        async with async_client.workflows.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert workflow is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_execute(self, async_client: AsyncMastraClient) -> None:
        workflow = await async_client.workflows.execute(
            workflow_id="workflowId",
        )
        assert workflow is None

    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncMastraClient) -> None:
        workflow = await async_client.workflows.execute(
            workflow_id="workflowId",
            input={},
        )
        assert workflow is None

    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncMastraClient) -> None:
        response = await async_client.workflows.with_raw_response.execute(
            workflow_id="workflowId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert workflow is None

    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncMastraClient) -> None:
        async with async_client.workflows.with_streaming_response.execute(
            workflow_id="workflowId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert workflow is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_execute(self, async_client: AsyncMastraClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            await async_client.workflows.with_raw_response.execute(
                workflow_id="",
            )
