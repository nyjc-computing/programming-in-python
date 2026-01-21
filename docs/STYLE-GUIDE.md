# Style Guide for Programming in Python Lessons

This document collates style decisions for consistency across all lesson notebooks.

## Function References

**Rule:** When referring to functions in text (markdown cells), always include parentheses after the function name.

**Examples:**
- ✅ Correct: `factorial()`, `len()`, `print()`
- ❌ Incorrect: `factorial`, `len`, `print`

**Rationale:** Parentheses make it immediately clear that we're referring to a function, not a variable or other identifier.

**Application:** This applies to all function references in:
- Explanatory text
- Exercise descriptions
- Summary sections
- Code comments
- Headers (where appropriate)

**IMPORTANT - Do NOT use regex for this:**
- Don't add `()` to function names used as verbs (e.g., "write a function" not "write() a function")
- Don't add `()` when the function name is part of a larger word (e.g., "integer" not "int()eger")
- Don't add `()` to common words that happen to match function names (e.g., "abstract" not "abs()tract")
- This requires human judgment - apply manually when reviewing content

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

2025-01-21
