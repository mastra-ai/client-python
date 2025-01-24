# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import logs, syncs, system, workflows
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.tools import tools
from .resources.agents import agents
from .resources.memory import memory

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "MastraClient",
    "AsyncMastraClient",
    "Client",
    "AsyncClient",
]


class MastraClient(SyncAPIClient):
    system: system.SystemResource
    agents: agents.AgentsResource
    memory: memory.MemoryResource
    workflows: workflows.WorkflowsResource
    syncs: syncs.SyncsResource
    logs: logs.LogsResource
    tools: tools.ToolsResource
    with_raw_response: MastraClientWithRawResponse
    with_streaming_response: MastraClientWithStreamedResponse

    # client options

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous mastraClient client instance."""
        if base_url is None:
            base_url = os.environ.get("MASTRA_CLIENT_BASE_URL")
        if base_url is None:
            base_url = f"http://localhost:4111"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.system = system.SystemResource(self)
        self.agents = agents.AgentsResource(self)
        self.memory = memory.MemoryResource(self)
        self.workflows = workflows.WorkflowsResource(self)
        self.syncs = syncs.SyncsResource(self)
        self.logs = logs.LogsResource(self)
        self.tools = tools.ToolsResource(self)
        self.with_raw_response = MastraClientWithRawResponse(self)
        self.with_streaming_response = MastraClientWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncMastraClient(AsyncAPIClient):
    system: system.AsyncSystemResource
    agents: agents.AsyncAgentsResource
    memory: memory.AsyncMemoryResource
    workflows: workflows.AsyncWorkflowsResource
    syncs: syncs.AsyncSyncsResource
    logs: logs.AsyncLogsResource
    tools: tools.AsyncToolsResource
    with_raw_response: AsyncMastraClientWithRawResponse
    with_streaming_response: AsyncMastraClientWithStreamedResponse

    # client options

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async mastraClient client instance."""
        if base_url is None:
            base_url = os.environ.get("MASTRA_CLIENT_BASE_URL")
        if base_url is None:
            base_url = f"http://localhost:4111"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.system = system.AsyncSystemResource(self)
        self.agents = agents.AsyncAgentsResource(self)
        self.memory = memory.AsyncMemoryResource(self)
        self.workflows = workflows.AsyncWorkflowsResource(self)
        self.syncs = syncs.AsyncSyncsResource(self)
        self.logs = logs.AsyncLogsResource(self)
        self.tools = tools.AsyncToolsResource(self)
        self.with_raw_response = AsyncMastraClientWithRawResponse(self)
        self.with_streaming_response = AsyncMastraClientWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class MastraClientWithRawResponse:
    def __init__(self, client: MastraClient) -> None:
        self.system = system.SystemResourceWithRawResponse(client.system)
        self.agents = agents.AgentsResourceWithRawResponse(client.agents)
        self.memory = memory.MemoryResourceWithRawResponse(client.memory)
        self.workflows = workflows.WorkflowsResourceWithRawResponse(client.workflows)
        self.syncs = syncs.SyncsResourceWithRawResponse(client.syncs)
        self.logs = logs.LogsResourceWithRawResponse(client.logs)
        self.tools = tools.ToolsResourceWithRawResponse(client.tools)


class AsyncMastraClientWithRawResponse:
    def __init__(self, client: AsyncMastraClient) -> None:
        self.system = system.AsyncSystemResourceWithRawResponse(client.system)
        self.agents = agents.AsyncAgentsResourceWithRawResponse(client.agents)
        self.memory = memory.AsyncMemoryResourceWithRawResponse(client.memory)
        self.workflows = workflows.AsyncWorkflowsResourceWithRawResponse(client.workflows)
        self.syncs = syncs.AsyncSyncsResourceWithRawResponse(client.syncs)
        self.logs = logs.AsyncLogsResourceWithRawResponse(client.logs)
        self.tools = tools.AsyncToolsResourceWithRawResponse(client.tools)


class MastraClientWithStreamedResponse:
    def __init__(self, client: MastraClient) -> None:
        self.system = system.SystemResourceWithStreamingResponse(client.system)
        self.agents = agents.AgentsResourceWithStreamingResponse(client.agents)
        self.memory = memory.MemoryResourceWithStreamingResponse(client.memory)
        self.workflows = workflows.WorkflowsResourceWithStreamingResponse(client.workflows)
        self.syncs = syncs.SyncsResourceWithStreamingResponse(client.syncs)
        self.logs = logs.LogsResourceWithStreamingResponse(client.logs)
        self.tools = tools.ToolsResourceWithStreamingResponse(client.tools)


class AsyncMastraClientWithStreamedResponse:
    def __init__(self, client: AsyncMastraClient) -> None:
        self.system = system.AsyncSystemResourceWithStreamingResponse(client.system)
        self.agents = agents.AsyncAgentsResourceWithStreamingResponse(client.agents)
        self.memory = memory.AsyncMemoryResourceWithStreamingResponse(client.memory)
        self.workflows = workflows.AsyncWorkflowsResourceWithStreamingResponse(client.workflows)
        self.syncs = syncs.AsyncSyncsResourceWithStreamingResponse(client.syncs)
        self.logs = logs.AsyncLogsResourceWithStreamingResponse(client.logs)
        self.tools = tools.AsyncToolsResourceWithStreamingResponse(client.tools)


Client = MastraClient

AsyncClient = AsyncMastraClient
