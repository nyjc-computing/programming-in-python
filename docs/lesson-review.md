# Teaching Materials Review: Programming in Python (Lessons 1-13)

**Reviewed:** 2025-01-21
**Scope:** Lesson flow from 01 to 13
**Reviewer:** AI Assistant (Claude Opus 4.5)

---

## Executive Summary

The course follows a generally logical progression from basic expressions to more advanced concepts. Overall pedagogical approach is sound, with good use of concrete examples and progressive difficulty.

**Key Finding:** Lesson 12 (convenience features) is positioned too late—its content (f-strings, `enumerate()`, tuple unpacking, in-place operators) is used extensively throughout Lessons 6-11 before being formally taught.

---

## Lesson-by-Lesson Analysis

### Lesson 1: Expressions

**Main Topics:**
- Arithmetic operators (+, -, *, /, //, **, %)
- Data types: int, float, bool, str
- Comparison operators
- Type conversions
- String concatenation and repetition
- `print()` and `type()` functions

**Premature Usage Issues:**
- Functions concept used before Lesson 2 — mitigated by "crash course" section (acceptable)
- `not` keyword used but now caveated with note about later coverage (acceptable)
- ~~`.isdecimal()` method referenced~~ — not found in Lesson 1; report was incorrect

**Scaffolding:** Good step-by-step operator exploration, try-it-yourself cells, summary with active recall

---

### Lesson 2: Abstraction

**Main Topics:**
- Function definition (`def`)
- Parameters vs arguments
- Variable scoping (global vs local)
- `return` statement
- Functions vs procedures
- Docstrings
- `help()` function
- `NameError` and `TypeError`
- `len()` function (now with proper summary)

**Scaffolding:**
- **Excellent PRIMM sections** (Predict-Investigate-Make pattern)
- Pythontutor visualization for scoping
- Good foreshadowing of logical operators (Lesson 3b)
- `len()` investigation followed by clear summary of behavior

---

### Lesson 3a: Selection (Part 1)

**Main Topics:**
- `input()` function
- Object methods (`.isdecimal()`)
- `if-else` statements
- Data validation
- `elif` keyword

**Premature Usage Issues:**
- ~~`len()` used without formal teaching~~ — now properly summarized in Lesson 2
- Methods introduced as "Crash course" — unavoidable given extensive string method usage; could be better scaffolded with PRIMM (Predict phase before showing usage)
- ~~`return` used before students fully understand~~ — `return` was covered in Lesson 2 (cell 17)

**Scaffolding:** Progressive validation example, phone number context, negative validation algorithmic pattern

---

### Lesson 3b: Selection (Part 2)

**Main Topics:**
- Logical operators: `and`, `or`, `not`
- Non-evaluative checking (short-circuit evaluation)
- String indexing (positive and negative)
- Boolean logic with non-boolean types

**Premature Usage Issues:**
- String indexing introduced as "Crash course" — could be scaffolded with PRIMM (Predict-Run-Investigate pattern)
- `IndexError` referenced contextually (to show why `.startswith()` is safer than indexing) — formal treatment with exercise in Lesson 5 is appropriate
- Negative indexing introduced with appropriate warning ("their use is generally discouraged")

**Scaffolding:** Builds on Lesson 3a's `validate()` function, progressive logical operator explanation, truth tables, good comparison of methods vs indexing for error handling

---

### Lesson 4: Recursion

**Main Topics:**
- Recursive functions
- Base case requirements
- `RecursionError`
- Trace tables
- Function annotations
- `random` module

**Scaffolding:**
- **Excellent:** Detailed trace table with stacking/unwinding phases
- Python Tutor visualization link
- "Don't recurse in your brain" tip
- Debug output version (`factorial_debug`)

**Note:** Recursion before iteration is unusual pedagogically but intentional—Lesson 5 covers iteration.

---

### Lesson 5: Iteration

**Main Topics:**
- `while` loops
- `for` loops with `range()`
- Indexed vs direct iteration
- String slicing
- `IndexError`

**Premature Usage Issues:**
- String slicing introduced as "Crash course" without sufficient scaffolding
- `len()` used without formal introduction

**Scaffolding:** Compares recursion vs iteration, three requirements for while loops, progressive exercises

---

### Lesson 6a: Data structures - list and tuple

**Main Topics:**
- Lists (creation, indexing, slicing)
- List methods (append, insert, del)
- List operators (+, *)
- `len()`, `sum()`, `min()`, `max()`
- Tuples
- `in` operator

**Premature Usage Issues:**
- **`enumerate()`** used but not taught until Lesson 12
- **f-strings** used extensively but not taught until Lesson 12

**Scaffolding:** Progressive list operations, exercises with hints, mutability explanation

---

### Lesson 6b: Data structures - dict

**Main Topics:**
- Dictionary creation and usage
- Key-value pairs
- Dict methods (get, keys, values, items)
- Dict iteration
- `KeyError`

**Premature Usage Issues:**
- **f-strings** used extensively
- **Tuple unpacking** (`for key, value in...`) not taught until Lesson 12

**Issue:** Cell 22-23 contains duplicate list initialization content from Lesson 6a

**Scaffolding:** Student record example, progressive dict operations, exercises with hints

---

### Lesson 7: Debugging with trace tables

**Main Topics:**
- Trace tables
- Pseudocode
- `pdb` debugger
- `breakpoint()` function

**Premature Usage Issues:**
- `try-except` referenced (taught in Lesson 10)
- `+=` operator used (taught in Lesson 12)

**Scaffolding:** Concrete LCM algorithm example, iteration counting exercise, pseudocode comparison

**Missing:** No Summary section (deviates from pattern)

---

### Lesson 8: Value and Identity

**Main Topics:**
- `==` vs `is` operators
- `id()` function
- Value vs Identity
- Mutable vs Immutable
- Dict/list reference issues

**Scaffolding:**
- **Excellent PRIMM structure** (Predict-Investigate-Make)
- Student records example with identity issue
- Progressive concept building

---

### Lesson 9a: File IO

**Main Topics:**
- `open()` function
- File modes (r, w, a, x)
- `read()`, `readline()`, `readlines()`
- `write()`, `writelines()`
- Escape sequences (`\n`, `\t`)
- `strip()` method
- `with` statement (context managers)
- `split()` and `join()` string methods

**Premature Usage Issues:**
- **f-strings** used throughout

**Scaffolding:** Progressive file operation exploration, task-based learning (Tasks 1-3), refactoring exercise

**Issue:** Summary section is incomplete

---

### Lesson 9b: Files and Directories

**Main Topics:**
- `os` module
- Working directory (`getcwd()`, `chdir()`)
- Absolute vs relative paths
- Directory creation (`mkdir()`, `makedirs()`)
- Path operations (`split()`, `join()`, `dirname()`, `basename()`)
- `os.path` functions

**Premature Usage Issues:**
- **f-strings** used throughout
- **Tuple unpacking** used (`dirname, basename = os.path.split(path)`) without teaching

**Issue:** References non-existent "Lesson 7b" for tuple unpacking

**Missing:** No Summary section, Exercise 2 scaffold incomplete

---

### Lesson 10: Error handling with `try-except`

**Main Topics:**
- `try-except-else-finally`
- `FileNotFoundError`
- `Exception` object
- `ValueError` handling
- Re-raising exceptions

**Premature Usage Issues:**
- **f-strings** used throughout
- Reference error: mentions "Lesson 9 and 10, on Object-Oriented Programming"

**Scaffolding:** Progressive error handling, concrete file error examples, `try-except` vs `if-else` comparison

**Missing:** No Summary section (deviates from pattern)

---

### Lesson 11: Handling CSV files with `csv`

**Main Topics:**
- `csv.reader` and `csv.writer`
- `csv.DictReader` and `csv.DictWriter`
- CSV format rules
- Error handling for CSV

**Premature Usage Issues:**
- **f-strings** used extensively
- **`enumerate()`** used in one example without teaching
- **`.get()` method** used for dictionaries without formal teaching

**Scaffolding:** Investigation sections throughout, progressive exercises (1-5), "Crash course: CSV format rules", troubleshooting section

---

### Lesson 12: Convenience features in Python

**Main Topics:**
- f-strings
- Tuple unpacking
- `enumerate()`
- `zip()`
- `sorted()` and `reversed()`
- In-place operators (`+=`, `-=`, etc.)

**Issue:** Should be taught MUCH earlier—content used throughout Lessons 6-11

**Scaffolding:** Example for each feature, summary with exercises

**Bug:** Cell 6 references undefined `rows` variable (should be `options`)

---

### Lesson 13: Abstraction with Modules

**Main Topics:**
- Modules and `import`
- `__name__ == "__main__"`
- Module aliases
- Code organization

**Premature Usage Issues:**
- Type hints (`list[str]`) used without formal teaching
- `None` type used in return types without formal teaching

**Scaffolding:** Concrete game example, `__name__` explanation, before/after reorganization comparison

---

## Patterns Observed

### Positive Patterns ✅

1. **Jupyter intro** in every lesson
2. **Summary with active recall** in 11/13 lessons (missing: L7, L9b, L10)
3. **PRIMM framework** in Lessons 2, 3a, 8
4. Progressive exercise difficulty
5. Cross-lesson references (mostly accurate)
6. Hints in expandable `<details>` tags
7. Pythontutor links for visualization
8. "Crash course" sections for quick concept introductions

### Negative Patterns ❌

1. **f-strings used throughout** but only taught in Lesson 12
2. **`enumerate()` used** but only taught in Lesson 12
3. **Tuple unpacking used** but only taught in Lesson 12
4. **In-place operators** used but only taught in Lesson 12
5. Missing Summary sections in Lessons 7, 9b, 10
6. Duplicate content between 6a and 6b (cell 22-23)
7. Reference errors ("Lesson 7b", OOP lesson numbers)

---

## Summary Table

| Lesson | Premature Usage | Missing Scaffolding | Inconsistencies | Summary Present |
|--------|-----------------|---------------------|-----------------|-----------------|
| 1 | `not` keyword (caveated), functions (crash course) | None | Report error: `.isdecimal()` not in L1 | Yes |
| 2 | None | `len()` now has summary | Fixed: `type()` parentheses | Yes |
| 3a | Methods (unavoidable, could use PRIMM) | Methods could use Predict phase | ~~return~~ was in L2, ~~len~~ now in L2 | Yes |
| 3b | String indexing (crash course) | Could use PRIMM for indexing | IndexError contextual (formal in L5) | Yes |
| 4 | Recursion before iteration | None | None | Yes |
| 5 | String slicing, `len()` | None | None | Yes |
| 6a | f-strings, `enumerate()` | None | None | Yes |
| 6b | f-strings, tuple unpacking | None | Duplicate content | Yes |
| 7 | `try-except`, `+=` | None | None | **No** |
| 8 | f-strings, `enumerate()`, `.isalpha()` | None | Duplicate content | Yes |
| 9a | f-strings | None | Incomplete summary | Partial |
| 9b | f-strings, tuple unpacking | Exercise 2 incomplete | Wrong reference | **No** |
| 10 | f-strings | None | Wrong reference | **No** |
| 11 | f-strings, `enumerate()`, `.get()` | None | None | Yes |
| 12 | None | None | Bug (rows/options) | Yes |
| 13 | Type hints, `None` | None | Different summary format | Yes |

---

## Recommendations

### Critical (High Priority)

1. **Move Lesson 12 earlier** - Features (f-strings, enumerate, tuple unpacking, in-place operators) should be taught no later than Lesson 5 or 6, as they're used extensively throughout. Suggested placement: After Lesson 5 (Iteration) or as part of Lesson 2 (Abstraction).

2. **Add Summary sections** to Lessons 7, 9b, and 10 for consistency with the course pattern.

3. **Fix Lesson 6a/6b duplication** - Remove duplicate list initialization content from 6b (cells 22-23).

4. **Teach `len()` formally** - Should have dedicated coverage in Lesson 1 or 2, not just in exercises.

5. **Fix reference errors:**
   - L9b: Correct "Lesson 7b" reference
   - L9b/L10: Fix OOP lesson references
   - L12: Fix undefined `rows` variable

### Important (Medium Priority)

6. **Consolidate string methods** - Create dedicated treatment for common string methods (`.isdecimal()`, `.isalpha()`, `.strip()`, `.split()`, `.join()`) rather than "crash courses."

7. **Consolidate string indexing/slicing** - These appear in multiple "crash courses" but could use unified treatment.

8. **Add PRIMM scaffolding** to more lessons - The pattern in Lessons 2, 3a, and 8 works well; consider expanding to other lessons.

9. **Consider splitting Lesson 11** - CSV handling is dense; could benefit from more scaffolding.

10. **Add trace table exercises** to earlier lessons (1-3) for prediction practice.

### Nice to Have (Low Priority)

11. Add bridging sections between all lesson pairs (like Lesson 2 has).

12. Standardize "Crash course" sections - either formalize these or integrate them better.

13. Add more "Predict" sections before code execution to build mental models.

---

## Acceptance Criteria Met

- [x] Reviewed all 13 lessons
- [x] Identified gaps in logical/semantic flow
- [x] Checked scaffolding coverage (PRIMM, trace tables)
- [x] Identified premature concept/syntax usage
- [x] Checked pattern consistency across notebooks
