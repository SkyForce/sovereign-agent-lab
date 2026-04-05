"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
All three conditions (PLAIN, XML, SANDWICH) returned correct answers. The 70B model
handled every format without errors. Notably, PLAIN returned Haymarket Vaults (found
mid-list) while XML and SANDWICH both returned The Albanach (the first matching venue).
This suggests XML/SANDWICH formatting triggered a top-down scan that stopped at the
first valid match, while PLAIN may have processed differently. Regardless, all answers
satisfied every constraint — the signal-to-noise ratio was too high for format to matter.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
Both distractors satisfy 2 of 3 constraints, but The Holyrood Arms is harder because
its first two checks pass (capacity=160 exactly equals the required 160, vegan=yes)
making it look like a perfect match. A model that skims rather than evaluating all three
constraints will likely stop there and miss status=full.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
Part C ran the 8B model with distractors. All three conditions were correct but unlike
the 70B model (which returned The Albanach in XML/SANDWICH), the 8B model always returned
The Haymarket Vaults — a mid-list answer. This suggests the smaller model scanned the
full list rather than stopping at the first match, hinting at different attention patterns
even when the final answer is correct. To see outright failures, a longer context or
weaker model would be needed.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most when the signal-to-noise ratio is low — long contexts,
many near-miss distractors, ambiguous constraints, or weaker models. In those conditions,
structural cues like XML tags and sandwich prompting help the attention mechanism locate
the relevant information. With short, clean data and strong models the effect vanishes,
but real-world agent prompts rarely stay short and clean, so building good formatting
habits early prevents hard-to-debug failures later.
"""
