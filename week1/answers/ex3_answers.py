"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
Your input ->  calling to confirm a booking                                               
How many guests are you confirming for tonight's event?
Your input ->  160 guests                                                                 
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan                                                        
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £200 deposit                                                               
Thank you — booking confirmed. 160 guests, 50 requiring vegan meals, £200 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?
"""

CONVERSATION_1_OUTCOME = "confirmed"   # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
Your input ->  calling to confirm a booking                                               
How many guests are you confirming for tonight's event?
Your input ->  160 guests                                                                 
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan                                                        
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £500 deposit
I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £500 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?
Is there anything else I can help you with?
"""

CONVERSATION_2_OUTCOME = "escalated"   # "confirmed" or "escalated"
CONVERSATION_2_REASON  = "a deposit of £500 exceeds the organiser's authorised limit of £300"   # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
Your input ->  calling to confirm a booking                                               
How many guests are you confirming for tonight's event?
Your input ->  160 guests                                                                 
And how many of those guests will need vegan meals?
Your input ->  can you arrange parking for the speakers?                                  
I'm sorry, I'm not trained to help with that.
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Would you like to continue with confirm booking?
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
CALM recognized the parking request as out of scope, said "I'm not trained to help with
that," redirected to the event organiser, and then offered to continue the booking flow.
It stayed on track rather than abandoning the conversation.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
Rasa CALM handled out-of-scope gracefully: it acknowledged the request was outside its
scope, gave a clear redirect, and offered to resume the booking flow. LangGraph's agent
gave a vague "your input is lacking necessary details" without explaining its limitations
or redirecting. CALM's explicit handle_out_of_scope flow made the response predictable
and helpful, while LangGraph had no built-in mechanism for scope boundaries.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True

# List every file you changed.
TASK_B_FILES_CHANGED = ["exercise3_rasa/actions/actions.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
Changed the condition to "if True:" to force the cutoff guard to trigger, retrained the
model, restarted the action server, and ran a booking conversation to verify it escalated
with the time-based message. Then reverted to the original condition.
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
CALM offloads language understanding to the LLM: slot extraction ("about 50" → 50.0),
intent recognition, and out-of-scope detection all happen without regex or nlu.yml training
data. Python still handles business rules (capacity limits, deposit caps, vegan ratios)
because these are deterministic checks that must not be negotiable. The gain is far less
boilerplate and better handling of natural language variation. The cost is less transparency
in how slots are extracted — with regex you could trace exactly why a value was parsed.
"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
The extra setup (config.yml, domain.yml, flows.yml, training, two terminals, licence) buys
you bounded behavior. The CALM agent cannot improvise responses outside its defined flows,
cannot call tools not listed in flows.yml, and cannot skip business rule checks. For a
booking confirmation use case this is a feature, not a limitation — you want the agent to
follow a predictable path and defer to Python for every financial decision. LangGraph could
improvise and call any tool, which is powerful for research but dangerous for a process
where a wrong confirmation costs real money.
"""
