# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import memory_thread_update_params, memory_thread_tool_result_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .context_window import (
    ContextWindowResource,
    AsyncContextWindowResource,
    ContextWindowResourceWithRawResponse,
    AsyncContextWindowResourceWithRawResponse,
    ContextWindowResourceWithStreamingResponse,
    AsyncContextWindowResourceWithStreamingResponse,
)

__all__ = ["MemoryThreadsResource", "AsyncMemoryThreadsResource"]


class MemoryThreadsResource(SyncAPIResource):
    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def context_window(self) -> ContextWindowResource:
        return ContextWindowResource(self._client)

    @cached_property
    def with_raw_response(self) -> MemoryThreadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/mastra-python#accessing-raw-response-data-eg-headers
        """
        return MemoryThreadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MemoryThreadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/mastra-python#with_streaming_response
        """
        return MemoryThreadsResourceWithStreamingResponse(self)

    def update(
        self,
        thread_id: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Update a thread

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/api/memory/threads/{thread_id}",
            body=maybe_transform(body, memory_thread_update_params.MemoryThreadUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete(
        self,
        thread_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a thread

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/memory/threads/{thread_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def tool_result(
        self,
        thread_id: str,
        *,
        result_id: str,
        tool_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Get tool execution result for a thread

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/api/memory/threads/{thread_id}/tool-result",
            body=maybe_transform(
                {
                    "result_id": result_id,
                    "tool_id": tool_id,
                },
                memory_thread_tool_result_params.MemoryThreadToolResultParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMemoryThreadsResource(AsyncAPIResource):
    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def context_window(self) -> AsyncContextWindowResource:
        return AsyncContextWindowResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMemoryThreadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/mastra-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMemoryThreadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMemoryThreadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/mastra-python#with_streaming_response
        """
        return AsyncMemoryThreadsResourceWithStreamingResponse(self)

    async def update(
        self,
        thread_id: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Update a thread

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/api/memory/threads/{thread_id}",
            body=await async_maybe_transform(body, memory_thread_update_params.MemoryThreadUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete(
        self,
        thread_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a thread

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/memory/threads/{thread_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def tool_result(
        self,
        thread_id: str,
        *,
        result_id: str,
        tool_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Get tool execution result for a thread

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/api/memory/threads/{thread_id}/tool-result",
            body=await async_maybe_transform(
                {
                    "result_id": result_id,
                    "tool_id": tool_id,
                },
                memory_thread_tool_result_params.MemoryThreadToolResultParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class MemoryThreadsResourceWithRawResponse:
    def __init__(self, memory_threads: MemoryThreadsResource) -> None:
        self._memory_threads = memory_threads

        self.update = to_raw_response_wrapper(
            memory_threads.update,
        )
        self.delete = to_raw_response_wrapper(
            memory_threads.delete,
        )
        self.tool_result = to_raw_response_wrapper(
            memory_threads.tool_result,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._memory_threads.messages)

    @cached_property
    def context_window(self) -> ContextWindowResourceWithRawResponse:
        return ContextWindowResourceWithRawResponse(self._memory_threads.context_window)


class AsyncMemoryThreadsResourceWithRawResponse:
    def __init__(self, memory_threads: AsyncMemoryThreadsResource) -> None:
        self._memory_threads = memory_threads

        self.update = async_to_raw_response_wrapper(
            memory_threads.update,
        )
        self.delete = async_to_raw_response_wrapper(
            memory_threads.delete,
        )
        self.tool_result = async_to_raw_response_wrapper(
            memory_threads.tool_result,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._memory_threads.messages)

    @cached_property
    def context_window(self) -> AsyncContextWindowResourceWithRawResponse:
        return AsyncContextWindowResourceWithRawResponse(self._memory_threads.context_window)


class MemoryThreadsResourceWithStreamingResponse:
    def __init__(self, memory_threads: MemoryThreadsResource) -> None:
        self._memory_threads = memory_threads

        self.update = to_streamed_response_wrapper(
            memory_threads.update,
        )
        self.delete = to_streamed_response_wrapper(
            memory_threads.delete,
        )
        self.tool_result = to_streamed_response_wrapper(
            memory_threads.tool_result,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._memory_threads.messages)

    @cached_property
    def context_window(self) -> ContextWindowResourceWithStreamingResponse:
        return ContextWindowResourceWithStreamingResponse(self._memory_threads.context_window)


class AsyncMemoryThreadsResourceWithStreamingResponse:
    def __init__(self, memory_threads: AsyncMemoryThreadsResource) -> None:
        self._memory_threads = memory_threads

        self.update = async_to_streamed_response_wrapper(
            memory_threads.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            memory_threads.delete,
        )
        self.tool_result = async_to_streamed_response_wrapper(
            memory_threads.tool_result,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._memory_threads.messages)

    @cached_property
    def context_window(self) -> AsyncContextWindowResourceWithStreamingResponse:
        return AsyncContextWindowResourceWithStreamingResponse(self._memory_threads.context_window)
