import os

SETUP = "I asked my agent to roast itself; "
ACTION = "it opened a spreadsheet, "
PAYOFF = "ranked its failures by severity, and asked me to approve the ranking."


def assemble_text():
    return f"{SETUP}{ACTION}{PAYOFF}"


os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(assemble_text())
