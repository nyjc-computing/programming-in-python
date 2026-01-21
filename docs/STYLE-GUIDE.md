# Style Guide for Programming in Python Lessons

This document collates style decisions for consistency across all lesson notebooks.

## Function References

**Rule:** When referring to functions in text (markdown cells), always include parentheses after the function name.

**Examples:**
- ✅ Correct: `factorial()`, `len()`, `print()`, `append()`, `dict.values()`
- ❌ Incorrect: `factorial`, `len`, `print`

**Rationale:** Parentheses make it immediately clear that we're referring to a function, not a variable or other identifier.

**Application:** This applies to all function references in:
- Explanatory text
- Exercise descriptions
- Summary sections
- Code comments
- Headers (where appropriate)

**IMPORTANT - Only use `()` for actual function references:**

The `()` suffix is ONLY for:
- Built-in Python functions: `print()`, `len()`, `id()`, `type()`, `range()`, `input()`, `abs()`, `max()`, `min()`, etc.
- Methods that are actually called in code: `append()`, `.keys()`, `.values()`, `.items()`, `.split()`, `.startswith()`, etc.
- User-defined functions that were taught earlier in the lesson

---

### Type Names vs. Conversion Functions

**Rule:** Type names (`int`, `float`, `str`, `bool`, `list`, `dict`, `tuple`) do NOT get parentheses when used as nouns describing a type.

| Context | Correct | Incorrect |
|---------|---------|-----------|
| Type as noun | `` `int` ``, `` `float` ``, `` `str` ``, `` `bool` `` | `` `int()` ``, `` `float()` ``, etc. |
| Conversion function | `` `int()` ``, `` `float()` ``, `` `str()` `` | `` `int` ``, `` `float` `` (when referring to calling the function) |

**Examples:**
- ✅ "Convert to an `int`" / "This is a `str`" / "Returns a `bool`"
- ✅ "Use the `int()` function" / "Call `str()` to convert"
- ❌ "Convert to an `int()`" / "This is a `str()`" / "Returns a `bool()`"

**Plural forms:**
- ✅ "`int`s and `float`s" / "string methods" / "`dict` values"
- ❌ "`int()`s" / "`str()`s" / "`float()` values"

---

### Verbs, Nouns, and Common Words

**Rule:** Do NOT add `()` to words that happen to contain function names.

| Correct | Incorrect |
|---------|-----------|
| "minus", "insert", "open" | "min()us", "insert()ed", "open()ing" |
| "values", "keys", "items" | "values()", "keys()", "items()" (when used as nouns, not method calls) |
| "interpreter", "structure" | "int()erpreter", "str()ucture" |
| "print the values" | "print() the values" (when not referring to the function) |

**Gerunds (-ing forms):**
- ✅ "opening a file" / "reading data" / "printing values"
- ❌ "open()ing a file" / "print()ing values"

**Words containing function names:**
- ✅ "lowercase", "structure", "integer", "abstract", "intended"
- ❌ "lower()case", "str()ucture", "int()eger", "abs()tract", "int()ended"

**This requires human judgment** - do NOT use regex for this. Apply manually when reviewing content.

**Note:** In code cells, actual function calls and definitions naturally include parentheses. This rule is primarily for prose.

---

## Summary Sections

**Rule:** Italicize the phrase "(click to reveal)" in summary `<details>` elements.

**Example:**
```html
<summary>What are three requirements for successful recursion? *(click to reveal)*</summary>
```

---

## Jupyter Notebook Tags

All notebooks should have metadata tags applied to cells:

### Markdown cells with headers
- `h1:title-here` - For `#` level headers
- `h2:title-here` - For `##` level headers
- `h3:title-here` - For `###` level headers

Format: `h{level}:kebab-case-title`

### Code cells
- `try:description` - For "try this" code examples
- `exercise:exercise-name` - For exercise cells where students write code

---

## File Naming

- Use underscore format: `lesson_03a.ipynb`
- Not dash format: `lesson-03a.ipynb`

---

## PRIMM Framework Usage

When adding PRIMM scaffolding:
- Use level 3 headers (`###`) under the main section header
- Use HTML `<details>` tags for collapsible content (not markdown syntax)
- Place PRIMM after formal explanations as reinforcement/practice, not before

---

## Content Principles

### Do:
- Use real-world examples (phone numbers, student records, games, emails)
- Keep existing phrasing verbatim where possible
- Add scaffolding, don't replace existing explanations
- Test all code examples
- Maintain active recall summaries

### Don't:
- Use abstract examples like `True and False or True`
- Rewrite entire sections (add, don't replace)
- Remove existing good content
- Make lessons significantly longer
- Break existing cross-references

---

## Last Updated

2025-01-22
