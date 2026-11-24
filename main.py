import os

PARTS = [
    "I asked my agent to roast itself; ",
    "it opened a spreadsheet, ",
    "ranked its failures by severity, and asked me to approve the ranking.",
]


def assemble_text():
    return "".join(PARTS)


os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(assemble_text())
