# Lab 5: Static Code Analysis — Issues and Fixes

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Weak MD5 hash | Security | 39 | MD5 is flagged by Bandit as a weak hash. | Replace MD5 with SHA-256 for job card IDs. |
| Shell command injection risk | Security | 61 | subprocess.call uses shell=True with a constructed command. | Replace the shell command with a safer file-copy method. |
| Hardcoded password | Security | 8 | A password is stored directly in the source code. | Remove it if unnecessary, or load it securely from configuration. |
| Mutable default argument | Bug risk | 12 | history=[] is shared between function calls. | Use None as the default and create a new list inside the function. |
| Broad exception handling | Code quality | 23 | Catching Exception can hide unexpected errors. | Catch KeyError specifically. |
| Missing docstrings | Maintainability | Multiple | The module and functions lack documentation. | Add clear module and function docstrings. |
| Non-snake-case names | Style | Multiple | Function names, arguments and variables use inconsistent naming. | Rename them using snake_case. |
| Formatting violations | Style | 7, 43, 49, 77 | Missing whitespace, insufficient blank lines and an overlong line. | Apply Flake8 formatting requirements. |
