# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["ResultResource", "AsyncResultResource"]


class ResultResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResultResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mastra-ai/client-python#accessing-raw-response-data-eg-headers
        """
        return ResultResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResultResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mastra-ai/client-python#with_streaming_response
        """
        return ResultResourceWithStreamingResponse(self)

    def retrieve(
        self,
        result_id: str,
        *,
        tool_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Get tool execution result

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        if not result_id:
            raise ValueError(f"Expected a non-empty value for `result_id` but received {result_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/api/tools/{tool_id}/result/{result_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncResultResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResultResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mastra-ai/client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResultResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResultResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mastra-ai/client-python#with_streaming_response
        """
        return AsyncResultResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        result_id: str,
        *,
        tool_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Get tool execution result

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        if not result_id:
            raise ValueError(f"Expected a non-empty value for `result_id` but received {result_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/api/tools/{tool_id}/result/{result_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ResultResourceWithRawResponse:
    def __init__(self, result: ResultResource) -> None:
        self._result = result

        self.retrieve = to_raw_response_wrapper(
            result.retrieve,
        )


class AsyncResultResourceWithRawResponse:
    def __init__(self, result: AsyncResultResource) -> None:
        self._result = result

        self.retrieve = async_to_raw_response_wrapper(
            result.retrieve,
        )


class ResultResourceWithStreamingResponse:
    def __init__(self, result: ResultResource) -> None:
        self._result = result

        self.retrieve = to_streamed_response_wrapper(
            result.retrieve,
        )


class AsyncResultResourceWithStreamingResponse:
    def __init__(self, result: AsyncResultResource) -> None:
        self._result = result

        self.retrieve = async_to_streamed_response_wrapper(
            result.retrieve,
        )
