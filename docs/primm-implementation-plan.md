# PRIMM and Cognitive Scaffolding Implementation Plan

**Created:** 2025-01-21
**Last Updated:** 2025-01-21
**Status:** 🚧 In Progress (Phases 1-2, 4-5 Complete, Phase 3, 6 Pending)
**Objective:** Add PRIMM framework elements and trace tables at major cognitive cliffs identified in the cognitive demand analysis.

---

## Overview of Changes

| Change | Lessons Affected | Cognitive Cliff Addressed |
|--------|------------------|--------------------------|
| Split Lesson 3 | L3 → L3a, L3b | Multiple topics in one lesson (boolean overload) |
| PRIMM: Scoping | L2 | Variable scoping confusion |
| Lesson flow improvements | L2, L3a, L3b, L4 | Bridge paragraphs, summary formatting |
| PRIMM: Single conditions | L3a | Mental model of selection |
| PRIMM: Boolean logic | L3b | Boolean operators & short-circuit evaluation |
| Trace tables | L4 | Recursion mental model |
| PRIMM: Identity bug | L8 | Reference semantics confusion |

---

## Task Breakdown

### Phase 1: Lesson 3 Split ✅ COMPLETE

#### Task 1.1: Create Lesson 3a ✅
- **File:** `lesson_03a.ipynb`
- **Content:** Ends after `if-elif-else` with good programming practices
- **Includes:**
  - Input/output with `input()` function
  - Object methods (`isdecimal()`)
  - `if-else` statements
  - `elif` keyword
  - Phone number validation (2 checks: isdecimal, length)
  - Good programming practices (multi-line code, algorithmic patterns)
  - Summary items 1-3 only
- **Completed:** 2025-01-21
- **Acceptance Criteria:** ✅ All met

#### Task 1.2: Create Lesson 3b ✅
- **File:** `lesson_03b.ipynb`
- **Content:** Starts with `str.startswith()`, introduces logical operators
- **Includes:** `str.startswith()` and `str.endswith()` methods, Logical operators (`and`, `or`, `not`), Non-evaluative checking, String indexing, Boolean logic with non-boolean types, Summary items 4-6
- **Completed:** 2025-01-21
- **Acceptance Criteria:** ✅ All met

#### Task 1.3: Update Lesson References ✅ COMPLETE
- **Files:** L2, L3b, L4
- **Changes:**
  - L2: Added bridge paragraph to L3a (selection)
  - L2: Added note about logical operators (covered in L3b)
  - L3b: Added introduction referencing L3a
  - L4: Will need bridge added (see below)
- **Acceptance Criteria:** ✅ Cross-lesson references updated

---

### Phase 2: PRIMM for Lesson 2 (Scoping) ✅ COMPLETE

#### Task 2.1: Add PRIMM Section After Formal Scoping
- **Location:** `lesson_02.ipynb`, AFTER "#### Caveats" section (after formal scoping explanation)
- **Content:** Game/player_name scenario with predict-investigate-make
- **Structure:**
  - Predict: What happens to player name? (students apply newly learned scoping rules)
  - Run code: Confirm understanding
  - Investigate: Check understanding (details recap rules)
  - Make: How would you fix this? (two approaches: global keyword vs return values)
- **Placement:** PRIMM serves as **reinforcement/practice** AFTER students learn concepts, not before
- **Completed:** 2025-01-21
- **Notes:**
  - PRIMM section uses level 3 headers (###) under "## Variable scoping"
  - Uses HTML in `<details>` tags (not markdown)
  - Game/player_name scenario is concrete and relatable
  - Leads naturally into "Functions vs procedures" section
- **Acceptance Criteria:** ✅ All met

---

### Phase 3: PRIMM for Lesson 3a (Single Conditions) ⏳ PENDING

#### Task 3.1: Add PRIMM Before `if-else` Section
- **Location:** `lesson_03a.ipynb`, before the `if-else` section
- **Content:** Phone number validation step-by-step build
- **Acceptance Criteria:**
  - [ ] Step 1: Empty input check with prediction
  - [ ] Step 2: Digits-only check with prediction
  - [ ] Each prediction uses collapsible details
  - [ ] Builds from simple to complex
  - [ ] Uses real-world phone validation scenario
  - [ ] Maintains existing examples (just adds scaffolding)

**Note:** L3a currently has `if-else` examples but could benefit from PRIMM scaffolding before introducing the syntax.

---

### Phase 4: PRIMM for Lesson 3b (Boolean Logic) 🟡 PARTIAL

#### Task 4.1: Add Introduction to L3b ✅ COMPLETE
- **Location:** `lesson_03b.ipynb`, at start after Jupyter intro
- **Content:** Overview of multi-condition validation needs
- **Completed:** 2025-01-21
- **Acceptance Criteria:** ✅ All met

#### Task 4.2: Add PRIMM for `elif` (Flattening) ❌ REMOVED
- **Status:** elif was covered in L3a, not L3b. This task removed from plan.

#### Task 4.3: Add PRIMM for Boolean Operators ✅ COMPLETE
- **Location:** `lesson_03b.ipynb`
- **Status:** Existing content covers the key concepts
- **What's included:**
  - Shows problem first (nested if structure)
  - Introduces logical operators as solution
  - Troubleshooting examples (`startswith('6' or '8' or '9')` anti-pattern)
  - Non-evaluative checking with hands-on exercise
  - String indexing vs methods comparison
  - All examples are real-world, not abstract `True/False`
- **Acceptance Criteria:** ✅ All met

---

### Phase 5: Trace Tables for Lesson 4 (Recursion) ✅ COMPLETE

#### Task 5.1: Add Trace Table After `factorial()` Example ✅
- **Location:** `lesson_04.ipynb`, after factorial function
- **Insertion Point:** After initial factorial example, before exercises
- **Content:**
  - Real-world re-prompt example (4 calls trace)
  - Factorial trace (first 3 calls only)
  - Unwinding explanation
  - Debug output example with `factorial_debug()`
- **Completed:** 2025-01-21
- **Acceptance Criteria:** ✅ All met
- **Note:** Bridge paragraph was considered but intentionally NOT added — students without programming background won't wonder "why recursion before iteration" until they encounter other tutorials later

---

### Phase 6: PRIMM for Lesson 8 (Identity Bug) ⏳ PENDING

#### Task 6.1: Add PRIMM Before `word_stats()` Bug
- **Location:** `lesson_08.ipynb`, before word_stats function
- **Insertion Point:** At start of lesson, after Jupyter intro
- **Content:** Student records scenario with prediction
- **Acceptance Criteria:**
  - [ ] Concrete scenario (student enrollment data)
  - [ ] Prediction shows expected behavior
  - [ ] Running code reveals surprising result
  - [ ] Investigate with `id()` tracking
  - [ ] Modify shows fix
  - [ ] Leads naturally into existing `word_stats` example
  - [ ] `word_stats` becomes reinforcement, not first exposure

---

## Implementation Order

### Recommended Sequence

1. **Phase 1** (L3 Split) - ✅ Complete
   - Task 1.1: Create L3a
   - Task 1.2: Create L3b
   - Task 1.3: Update references

2. **Phase 2** (L2 PRIMM) - ✅ Complete
   - Task 2.1: Add scoping PRIMM (after formal explanation)

3. **Phase 3** (L3a PRIMM) - ⏳ Pending
   - Task 3.1: Add single-condition PRIMM

4. **Phase 4** (L3b PRIMM) - 🟡 Partial
   - Task 4.1: Add L3b intro ✅
   - Task 4.2: Removed from plan
   - Task 4.3: Boolean PRIMM ✅

5. **Phase 5** (L4 Trace) - ⏳ Pending
   - Task 5.1: Add recursion trace tables + bridge

6. **Phase 6** (L8 PRIMM) - ⏳ Pending
   - Task 6.1: Add identity PRIMM

---

## Testing Checklist

After each phase, verify:

### File Integrity
- [x] All notebooks open without errors
- [x] All code cells run successfully
- [x] No broken internal links (e.g., "see Lesson X for more")
- [x] Summary sections match actual lesson content

### Pedagogical Coherence
- [x] PRIMM sections flow naturally into existing content
- [x] Scaffolding doesn't repeat content unnecessarily
- [x] Examples remain concrete and real-world
- [x] Collapsible details work properly
- [x] Prediction-reveal pattern maintained

### Student Experience
- [x] Clear visual distinction between PRIMM and regular content
- [x] Code examples are runnable and produce expected output
- [x] Hints are genuinely helpful, not just giving answers
- [x] Difficulty progression is maintained

---

## Content Principles

### ✅ DO:
- Use real-world examples (phone numbers, student records, games, emails)
- Keep existing phrasing verbatim where possible
- Add scaffolding, don't replace existing explanations
- Use collapsible `<details>` for reveals
- Test all code examples
- Maintain active recall summaries
- Preserve existing exercise structure

### ❌ DON'T:
- Use abstract examples like `True and False or True`
- Rewrite entire sections (add, don't replace)
- Remove existing good content
- Make lessons significantly longer
- Break existing cross-references

---

## Progress Tracking

| Phase | Task | Status | Notes | Session |
|-------|------|--------|-------|---------|
| 1.1 | Create L3a | ✅ Complete | File created with if-elif-else, good practices, items 1-3 | 2025-01-21 |
| 1.2 | Create L3b | ✅ Complete | File created with logical operators, reordered pedagogically | 2025-01-21 |
| 1.3 | Update references | ✅ Complete | L2 bridge added, logical operators note added, L3b intro added | 2025-01-21 |
| 2.1 | L2 scoping PRIMM | ✅ Complete | Added AFTER formal scoping as reinforcement | 2025-01-21 |
| 3.1 | L3a single-condition PRIMM | ⏳ Pending | | |
| 4.1 | L3b introduction | ✅ Complete | Explains progression from L3a | 2025-01-21 |
| 4.2 | L3b elif PRIMM | ❌ Removed | Content moved to L3a | 2025-01-21 |
| 4.3 | L3b boolean PRIMM | ✅ Complete | Troubleshooting, non-evaluative checking covered | 2025-01-21 |
| 5.1 | L4 recursion trace | ✅ Complete | Phone re-prompt trace, factorial trace (3 calls), debug output added (bridge intentionally omitted) | 2025-01-21 |
| 6.1 | L8 identity PRIMM | ⏳ Pending | | |

**Legend:** ⬜ Not Started | 🟡 In Progress | ✅ Complete | ❌ Blocked | ⏳ Pending

---

## File Location Reference

```
Programming in Python/
├── lesson_01.ipynb
├── lesson_02.ipynb          ✅ Phase 2 COMPLETE (PRIMM added after scoping)
├── lesson_03a.ipynb         ✅ Phase 1.1 COMPLETE
├── lesson_03b.ipynb         ✅ Phase 1.2 COMPLETE
├── lesson_04.ipynb          ⏳ Phase 5 (trace + bridge needed)
├── lesson_05.ipynb
├── lesson_06a.ipynb
├── lesson_06b.ipynb
├── lesson_07.ipynb
├── lesson_08.ipynb          ⏳ Phase 6 (PRIMM needed)
├── lesson_09a.ipynb
├── lesson_09b.ipynb
├── lesson_10.ipynb
├── lesson_11.ipynb
├── lesson_12.ipynb
└── lesson_13.ipynb
```

**Note:** Filenames use underscore format (`lesson_03a.ipynb`) not dash format (`lesson-03a.ipynb`)

---

## Next Session Priorities

1. **Phase 5** - Add bridge and trace tables to L4 (recursion)
   - Add bridge explaining why recursion is taught before iteration
   - Add trace table with phone re-prompt example
   - Add factorial trace (first 3 calls only)
2. **Phase 6** - Add PRIMM to L8 (identity bug)
   - Student records scenario with prediction
   - Investigate with `id()` tracking (if covered by then)
3. **Phase 3** - Consider adding PRIMM to L3a (if time permits)
   - Single-condition scaffolding before if-else

**Estimated time per phase:** 30-45 minutes each

---

## Session Log

### 2025-01-21: Phase 1 (L3 Split) - ✅ Complete

**Completed Tasks:**
- Created `lesson_03a.ipynb` covering:
  - `input()` function and data validation
  - `if-else` and `if-elif-else` statements
  - Phone number validation (isdecimal, length checks only)
  - Good programming practices (multi-line code, algorithmic patterns)
  - Summary items 1-3
- Created `lesson_03b.ipynb` covering:
  - `str.startswith()` and `str.endswith()` methods
  - Problem demonstration (nested if for starting digit check)
  - Logical operators (`and`, `or`, `not`)
  - Non-evaluative checking (short-circuit evaluation)
  - String indexing vs methods
  - Boolean logic with non-boolean types
  - Complete phone validation with logical operators
  - Summary items 4-6
- Applied metadata to both notebooks
- Original `lesson_03.ipynb` deleted and committed

### 2025-01-21: Phase 2 (L2 PRIMM) & Flow Improvements - ✅ Complete

**Completed Tasks:**
- Added PRIMM section to `lesson_02.ipynb` after formal scoping explanation
  - Predict: Game/player_name scenario
  - Investigate: Confirm understanding
  - Make: Two solutions (global keyword vs return values)
- Added L2 → L3a bridge: "## Next: Making decisions with code"
- Added note about logical operators in L2 (covered in L3b)
- Italicized `(click to reveal)` in all summary sections
- Files renamed with leading zeros: lesson_03a.ipynb, lesson_03b.ipynb

### 2025-01-21: Phase 5 (L4 Trace Tables) - ✅ Complete

**Completed Tasks:**
- Added "Understanding recursion with trace tables" section after factorial function
- Phone re-prompt trace table showing 4 calls (3 errors + success)
- Factorial trace table showing stacking (first 3 calls), base case, and unwinding
- Debug example with `factorial_debug()` function that prints call stack with indentation
- Trace section emphasizes "trust the function" approach and explains why full tracing doesn't work
- Bridge paragraph intentionally NOT added — students won't question "why recursion before iteration" until later

**Key Implementation Decisions:**
1. **L3a scope:** Stopped at if-elif-else (not including logical operators)
2. **L3b reordering:** Introduced `str.startswith()` first, then showed nested-if problem, then logical operators
3. **PRIMM placement:** Moved to AFTER formal scoping explanation as reinforcement/practice
4. **Header levels:** PRIMM sections use level 3 (###) under "## Variable scoping"
5. **HTML in details:** Use proper HTML tags in `<details>`, not markdown

### 2025-01-21: Style Guide & Standardisation - ✅ Complete

**Completed Tasks:**
- Created docs/STYLE-GUIDE.md with function naming convention, summary formatting, Jupyter tags, file naming, PRIMM usage, content principles
- Applied function() naming style (with manual corrections after regex issues)
- Updated Python documentation references from 3.7 to 3.13 (4 files)
- Added 2 questions to L4 summary (RecursionError, random.randint)
- Fixed `factorial_debug()` to remove default parameter (not yet introduced)
- Added Jupyter metadata tags to L4 code cells and markdown headers

**Lesson Learned:** Function naming convention requires human judgment - do NOT use regex. Common false positives: "into" → "int()o", "abstract" → "abs()tract", verbs like "write" → "write()".

**Current Progress:**
- Phase 1: ✅ Complete (L3 split, references updated)
- Phase 2: ✅ Complete (L2 PRIMM, lesson flow improvements)
- Phase 4: 🟡 Partial (L3b intro and boolean content exist, elif PRIMM removed)

---

## Related Documents

- [Cognitive Demand Analysis](cognitive-demand-analysis.ipynb) - Analysis that informed these changes
- [Why Students Struggle](why-students-struggle-and-what-actually-helps.md) - Research framework
- Original lesson files in `Programming in Python/` directory
