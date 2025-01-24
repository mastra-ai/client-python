# System

Methods:

- <code title="get /api">client.system.<a href="./src/mastra_client_py/resources/system.py">retrieve_status</a>() -> None</code>

# Agents

Types:

```python
from mastra_client_py.types import AgentStreamResponse
```

Methods:

- <code title="get /api/agents/{agentId}">client.agents.<a href="./src/mastra_client_py/resources/agents/agents.py">retrieve</a>(agent_id) -> None</code>
- <code title="get /api/agents">client.agents.<a href="./src/mastra_client_py/resources/agents/agents.py">list</a>() -> None</code>
- <code title="post /api/agents/{agentId}/generate">client.agents.<a href="./src/mastra_client_py/resources/agents/agents.py">generate</a>(agent_id, \*\*<a href="src/mastra_client_py/types/agent_generate_params.py">params</a>) -> None</code>
- <code title="post /api/agents/{agentId}/stream">client.agents.<a href="./src/mastra_client_py/resources/agents/agents.py">stream</a>(agent_id, \*\*<a href="src/mastra_client_py/types/agent_stream_params.py">params</a>) -> str</code>

## Tools

Methods:

- <code title="post /api/agents/{agentId}/tools/{toolId}/execute">client.agents.tools.<a href="./src/mastra_client_py/resources/agents/tools.py">execute</a>(tool_id, \*, agent_id, \*\*<a href="src/mastra_client_py/types/agents/tool_execute_params.py">params</a>) -> None</code>

# Memory

Methods:

- <code title="post /api/memory/save-messages">client.memory.<a href="./src/mastra_client_py/resources/memory/memory.py">save_messages</a>(\*\*<a href="src/mastra_client_py/types/memory_save_messages_params.py">params</a>) -> None</code>

## Status

Methods:

- <code title="get /api/memory/status">client.memory.status.<a href="./src/mastra_client_py/resources/memory/status.py">retrieve</a>() -> None</code>

## Threads

Methods:

- <code title="post /api/memory/threads">client.memory.threads.<a href="./src/mastra_client_py/resources/memory/threads/threads.py">create</a>() -> None</code>
- <code title="get /api/memory/threads/{threadId}">client.memory.threads.<a href="./src/mastra_client_py/resources/memory/threads/threads.py">retrieve</a>(thread_id) -> None</code>
- <code title="patch /api/memory/threads/{threadId}">client.memory.threads.<a href="./src/mastra_client_py/resources/memory/threads/threads.py">update</a>(thread_id, \*\*<a href="src/mastra_client_py/types/memory/thread_update_params.py">params</a>) -> None</code>
- <code title="get /api/memory/threads">client.memory.threads.<a href="./src/mastra_client_py/resources/memory/threads/threads.py">list</a>() -> None</code>
- <code title="delete /api/memory/threads/{threadId}">client.memory.threads.<a href="./src/mastra_client_py/resources/memory/threads/threads.py">delete</a>(thread_id) -> None</code>
- <code title="get /api/memory/threads/{threadId}/context-window">client.memory.threads.<a href="./src/mastra_client_py/resources/memory/threads/threads.py">context_window</a>(thread_id) -> None</code>
- <code title="post /api/memory/threads/{threadId}/tool-result">client.memory.threads.<a href="./src/mastra_client_py/resources/memory/threads/threads.py">tool_result</a>(thread_id, \*\*<a href="src/mastra_client_py/types/memory/thread_tool_result_params.py">params</a>) -> None</code>

### Messages

Methods:

- <code title="get /api/memory/threads/{threadId}/messages">client.memory.threads.messages.<a href="./src/mastra_client_py/resources/memory/threads/messages.py">list</a>(thread_id) -> None</code>

# Workflows

Methods:

- <code title="get /api/workflows/{workflowId}">client.workflows.<a href="./src/mastra_client_py/resources/workflows.py">retrieve</a>(workflow_id) -> None</code>
- <code title="get /api/workflows">client.workflows.<a href="./src/mastra_client_py/resources/workflows.py">list</a>() -> None</code>
- <code title="post /api/workflows/{workflowId}/execute">client.workflows.<a href="./src/mastra_client_py/resources/workflows.py">execute</a>(workflow_id, \*\*<a href="src/mastra_client_py/types/workflow_execute_params.py">params</a>) -> None</code>

# Syncs

Methods:

- <code title="post /api/syncs/{syncId}/execute">client.syncs.<a href="./src/mastra_client_py/resources/syncs.py">execute</a>(sync_id, \*\*<a href="src/mastra_client_py/types/sync_execute_params.py">params</a>) -> None</code>

# Logs

Methods:

- <code title="get /api/logs/{runId}">client.logs.<a href="./src/mastra_client_py/resources/logs.py">retrieve</a>(run_id) -> None</code>
- <code title="get /api/logs">client.logs.<a href="./src/mastra_client_py/resources/logs.py">list</a>() -> None</code>

# Tools

Methods:

- <code title="get /api/tools/{toolId}">client.tools.<a href="./src/mastra_client_py/resources/tools/tools.py">retrieve</a>(tool_id) -> None</code>
- <code title="get /api/tools">client.tools.<a href="./src/mastra_client_py/resources/tools/tools.py">list</a>() -> None</code>
- <code title="post /api/tools/{toolId}/execute">client.tools.<a href="./src/mastra_client_py/resources/tools/tools.py">execute</a>(tool_id, \*\*<a href="src/mastra_client_py/types/tool_execute_params.py">params</a>) -> None</code>

## Result

Methods:

- <code title="get /api/tools/{toolId}/result/{resultId}">client.tools.result.<a href="./src/mastra_client_py/resources/tools/result.py">retrieve</a>(result_id, \*, tool_id) -> None</code>
