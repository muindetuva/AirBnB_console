---
name: python-alx-style
description: >
  Load when creating or editing any Python file in an ALX project.
  Enforces shebang line, docstring standards, pycodestyle 2.8.*
  compliance, executable permissions, and correct empty __init__.py
  structure. Overrides general Python conventions where ALX
  requirements differ.
tags:
  - python
  - alx
  - pycodestyle
  - docstrings
---

# Python ALX Style Skill

## Rule 1 — Shebang line
Every .py file must begin with this exact string on line 1:
#!/usr/bin/python3
No variation. Not #!/usr/bin/env python3. Not on line 2. Line 1, exactly.

## Rule 2 — Docstrings
Every module, class, and method must have a docstring.
A docstring must be a complete sentence — subject, verb, enough detail
to explain purpose. A single word or fragment fails the checker.

WRONG:
def save(self):
    """Save."""
    pass

RIGHT:
def save(self):
    """Saves the instance to storage and updates the updated_at timestamp."""
    pass

WRONG:
"""Models package."""

RIGHT:
"""Initialises the models package for the AirBnB console project."""

## Rule 3 — pycodestyle 2.8.*
Code must pass pycodestyle with zero errors. The most common failures:
- Trailing whitespace on any line (E291, E301)
- Missing blank line at end of file (W292)
- Two blank lines before and after top-level class and function definitions (E302)
- One blank line between methods inside a class (E301)
- Maximum line length 79 characters (E501)
- No tabs — 4 spaces only (W191)
- No whitespace before ':' or '(' (E203, E211)

Run after every file: pycodestyle <filename>
Zero errors means zero. One warning fails the checker.

## Rule 4 — Empty __init__.py files
An empty package init file contains exactly two lines and nothing else:
#!/usr/bin/python3
"""<Complete sentence describing what this package initialises.>"""

Do not add imports. Do not add pass. Do not add a blank line between them.

## Rule 5 — File ending
Every .py file must end with exactly one newline character.
Not zero newlines. Not two newlines. One.

## Rule 6 — Executable permission
After creating any .py file, make it executable:
chmod +x <filename>
Verify with: ls -la <filename> — must show -rwxr-xr-x
