"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ["search_venues", "get_venue_details"]

QUERY_1_VENUE_NAME    = "none"
QUERY_1_VENUE_ADDRESS = "none"
QUERY_2_FINAL_ANSWER  = "none"

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
Changed The Albanach's status to "full" in mcp_venue_server.py and reran. The output was
identical in both runs because the Llama model output tool calls as JSON text strings
instead of actually invoking them via LangGraph's tool-calling mechanism. No tools were
executed in either run. In principle, only mcp_venue_server.py needed changing — the client
code (exercise4_mcp_client.py) and agent code stayed untouched, which demonstrates the
decoupling benefit of MCP.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 212   # venue_tools.py (directly imported, tightly coupled)
LINES_OF_TOOL_CODE_EX4 = 0     # exercise4_mcp_client.py has zero tool logic — tools discovered dynamically via MCP

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP provides dynamic tool discovery — the client connects, lists available tools, and wraps
them automatically. Adding a new tool to the server requires zero changes in the client.
Multiple clients (LangGraph agent, Rasa action server, any MCP-compatible client) can share
the same tool server, ensuring consistent behavior and a single place to update venue data.
"""

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

WEEK_5_ARCHITECTURE = """
- The MCP venue server provides all tool capabilities (search, booking, weather, flyer generation) as a shared service, so any client can discover and use them without code changes.
- The LangGraph research agent handles open-ended tasks (venue research, comparison, flyer generation) because its flexible ReAct loop can chain tools in any order the model decides.
- The Rasa CALM confirmation agent handles structured phone calls from pub managers because its explicit flows ensure every booking follows the same auditable path with deterministic business rule checks.
- A persistent memory layer (CLAUDE.md or vector store) stores past sessions and booking history so the agent can learn from previous searches and avoid repeating work.
- A planner-executor split (DeepSeek R1 for planning, Llama 70B for execution) separates high-level reasoning from fast tool execution, allowing cost control and better multi-step task decomposition.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
LangGraph is the right agent for research — it needs to improvise, chain tools in
unpredictable orders, and handle open-ended queries like "find the best venue." In Exercise
2 it checked multiple venues, calculated costs, and fetched weather in whatever order the
model decided. Rasa CALM is the right agent for the confirmation call — it follows a fixed
slot-collection flow (guests → vegan count → deposit) and enforces hard business rules in
Python. Swapping them feels wrong because a LangGraph agent on a phone call could skip
the deposit check or hallucinate a confirmation, while a Rasa CALM agent doing research
would be stuck — it can't improvise tool chains or explore options not defined in flows.yml.
Each architecture's strength is the other's weakness.
"""
