# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mastra import Mastra, AsyncMastra

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSyncs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_execute(self, client: Mastra) -> None:
        sync = client.syncs.execute(
            sync_id="syncId",
        )
        assert sync is None

    @parametrize
    def test_method_execute_with_all_params(self, client: Mastra) -> None:
        sync = client.syncs.execute(
            sync_id="syncId",
            input={},
        )
        assert sync is None

    @parametrize
    def test_raw_response_execute(self, client: Mastra) -> None:
        response = client.syncs.with_raw_response.execute(
            sync_id="syncId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert sync is None

    @parametrize
    def test_streaming_response_execute(self, client: Mastra) -> None:
        with client.syncs.with_streaming_response.execute(
            sync_id="syncId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert sync is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_execute(self, client: Mastra) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sync_id` but received ''"):
            client.syncs.with_raw_response.execute(
                sync_id="",
            )


class TestAsyncSyncs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_execute(self, async_client: AsyncMastra) -> None:
        sync = await async_client.syncs.execute(
            sync_id="syncId",
        )
        assert sync is None

    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncMastra) -> None:
        sync = await async_client.syncs.execute(
            sync_id="syncId",
            input={},
        )
        assert sync is None

    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncMastra) -> None:
        response = await async_client.syncs.with_raw_response.execute(
            sync_id="syncId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert sync is None

    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncMastra) -> None:
        async with async_client.syncs.with_streaming_response.execute(
            sync_id="syncId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert sync is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_execute(self, async_client: AsyncMastra) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sync_id` but received ''"):
            await async_client.syncs.with_raw_response.execute(
                sync_id="",
            )
