# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import sync_execute_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["SyncsResource", "AsyncSyncsResource"]


class SyncsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SyncsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/mastra-python#accessing-raw-response-data-eg-headers
        """
        return SyncsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SyncsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/mastra-python#with_streaming_response
        """
        return SyncsResourceWithStreamingResponse(self)

    def execute(
        self,
        sync_id: str,
        *,
        input: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Execute a sync

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sync_id:
            raise ValueError(f"Expected a non-empty value for `sync_id` but received {sync_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/api/syncs/{sync_id}/execute",
            body=maybe_transform({"input": input}, sync_execute_params.SyncExecuteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSyncsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSyncsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/mastra-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSyncsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSyncsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/mastra-python#with_streaming_response
        """
        return AsyncSyncsResourceWithStreamingResponse(self)

    async def execute(
        self,
        sync_id: str,
        *,
        input: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Execute a sync

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sync_id:
            raise ValueError(f"Expected a non-empty value for `sync_id` but received {sync_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/api/syncs/{sync_id}/execute",
            body=await async_maybe_transform({"input": input}, sync_execute_params.SyncExecuteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SyncsResourceWithRawResponse:
    def __init__(self, syncs: SyncsResource) -> None:
        self._syncs = syncs

        self.execute = to_raw_response_wrapper(
            syncs.execute,
        )


class AsyncSyncsResourceWithRawResponse:
    def __init__(self, syncs: AsyncSyncsResource) -> None:
        self._syncs = syncs

        self.execute = async_to_raw_response_wrapper(
            syncs.execute,
        )


class SyncsResourceWithStreamingResponse:
    def __init__(self, syncs: SyncsResource) -> None:
        self._syncs = syncs

        self.execute = to_streamed_response_wrapper(
            syncs.execute,
        )


class AsyncSyncsResourceWithStreamingResponse:
    def __init__(self, syncs: AsyncSyncsResource) -> None:
        self._syncs = syncs

        self.execute = async_to_streamed_response_wrapper(
            syncs.execute,
        )
