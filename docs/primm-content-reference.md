# PRIMM Content Reference - Ready to Use

**Purpose:** This document contains all the PRIMM and trace table content ready to copy-paste into lessons.
**Usage:** Reference this during implementation to avoid re-typing.

---

## Table of Contents

1. [Lesson 2: Scoping PRIMM](#lesson-2-scoping-primm)
2. [Lesson 3a: Single-Condition PRIMM](#lesson-3a-single-condition-primm)
3. [Lesson 3b: Introduction](#lesson-3b-introduction)
4. [Lesson 3b: elif PRIMM](#lesson-3b-elif-primm)
5. [Lesson 3b: Boolean Logic PRIMM](#lesson-3b-boolean-logic-primm)
6. [Lesson 4: Recursion Trace Tables](#lesson-4-recursion-trace-tables)
7. [Lesson 8: Identity PRIMM](#lesson-8-identity-primm)

---

## Lesson 2: Scoping PRIMM

**Insertion Point:** `lesson_02.ipynb`, before "## Variable scoping" (before cell #20)

```markdown
### 🤔 Predict: What will happen?

Imagine you're writing a game. You have a variable `player_name` set to "Guest" at the start of your game.

You write a function to ask the player for their name and update it:

```python
# Global variable (outside the function)
player_name = "Guest"

def ask_player_name():
    # Get player input and update the name
    player_name = input("Enter your name: ")
    print(f"Inside function: Welcome, {player_name}!")

# Run the function
ask_player_name()

# What will this print?
print(f"Outside function: player_name is {player_name}")
```

**Before running the code above, predict:**
- What will be printed by the `print()` inside the function?
- What will be printed by the `print()` outside the function?
- Will `player_name` be changed from "Guest" to what the player typed?

<details>
<summary>Write your prediction, then click to reveal what most students expect</summary>

Most students expect:
- Inside function: "Inside function: Welcome, [whatever they typed]!"
- Outside function: "Outside function: player_name is [whatever they typed]!"

They expect the function to CHANGE the global variable.
</details>

<details>
<summary>Now click to see what ACTUALLY happens (and why)</summary>

Actually happens:
- Inside function: "Inside function: Welcome, [whatever they typed]!"
- Outside function: "Outside function: player_name is Guest"

The function prints the new name INSIDE, but the OUTSIDE variable stays as "Guest"!

This is because `player_name = input(...)` creates a NEW local variable inside the function, instead of modifying the global one.
</details>

Now let's see this more clearly:
```

---

## Lesson 3a: Single-Condition PRIMM

**Insertion Point:** `lesson_03a.ipynb`, before "## The `if-else` statement"

```markdown
### 🤔 Predict: Phone number validation step-by-step

You're building a signup form for a mobile app. Users need to enter a valid Singapore phone number.

Let's build this validation step-by-step, starting simple.

**Step 1: Check if user entered anything**

```python
userinput = input('Type a phone number: ')

if not userinput:
    print("Error: Nothing was typed!")
else:
    print(f"You entered: {userinput}")
```

**Before running, predict what will happen if:**
1. User just presses Enter without typing anything
2. User types "91234567"

<details>
<summary>Think about it, then click to reveal</summary>

1. If user presses Enter (empty input):
   - `not userinput` is `True` (empty string is treated as `False`)
   - Prints: "Error: Nothing was typed!"

2. If user types "91234567":
   - `not userinput` is `False`
   - Goes to `else` branch
   - Prints: "You entered: 91234567"
</details>

Now run the code to verify:

```python
# Try it with empty input and with "91234567"
```

**Step 2: Check if it's all numbers**

Phone numbers should only contain digits 0-9. Let's add that check:

```python
userinput = input('Type a phone number: ')

if not userinput:
    print("Error: Nothing was typed!")
elif not userinput.isdecimal():
    print("Error: Phone numbers can only contain digits!")
else:
    print(f"Valid input so far: {userinput}")
```

**Predict what happens if user types:**
1. "9123 4567" (contains a space)
2. "hello" (contains letters)
3. "91234567" (all digits)

<details>
<summary>Think about it, then click to reveal</summary>

1. "9123 4567": `isdecimal()` returns `False` → "Error: Phone numbers can only contain digits!"
2. "hello": `isdecimal()` returns `False` → "Error: Phone numbers can only contain digits!"
3. "91234567": `isdecimal()` returns `True` → "Valid input so far: 91234567"
</details>

Now let's run it and see:
```

---

## Lesson 3b: Introduction

**Insertion Point:** `lesson_03b.ipynb`, at start after Jupyter intro

```markdown
# Lesson 3b: Selection — Multiple Conditions and Boolean Logic

In Lesson 3a, we learned how to check one condition at a time. But real-world validation often needs multiple checks.

For example, a Singapore phone number must pass ALL of these checks:
1. ✅ Something was entered (not empty)
2. ✅ Only digits (no letters or symbols)
3. ✅ Exactly 8 digits
4. ✅ Starts with 6, 8, or 9

Let's build this step-by-step.
```

---

## Lesson 3b: elif PRIMM

**Insertion Point:** `lesson_03b.ipynb`, before showing flattened phone validation

```markdown
### 🔍 Investigate: What's the problem here?

**Question:** Why is this nested code hard to read?

<details>
<summary>Click to reveal</summary>

Look at the indentation! Each `if` is indented further inside the previous one. By the time you reach the success case ("Valid phone number!"), you're 4 levels deep.

Also, notice how the error message "Type digits only" is far from the `isdecimal()` check that triggers it. This makes the code hard to debug.
</details>

### ✏️ Modify: Flatten the structure

Python gives us `elif` (short for "else if") to avoid deep nesting:

```python
userinput = input('Type a phone number: ')

if not userinput:
    print("Nothing was typed")
elif not userinput.isdecimal():
    print("Type digits only")
elif len(userinput) != 8:
    print("Phone number must be 8 digits")
else:
    print("Valid phone number!")
```

**Predict:** What's the advantage of this structure?

<details>
<summary>Click to reveal</summary>

All the checks are at the same indentation level! Each error message appears right next to its check. Much easier to read and debug.

This is called "negative validation" — check for all the error conditions first, then the success case last.
</details>
```

---

## Lesson 3b: Boolean Logic PRIMM

**Insertion Point:** `lesson_03b.ipynb`, in the boolean operators section

```markdown
Here's the wrong way to check if a phone number starts with 6, 8, or 9:

```python
# ❌ WRONG - try this and see what happens
userinput = input('Type a phone number: ')

if not userinput:
    print("Nothing was typed")
elif not userinput.isdecimal():
    print("Type digits only")
elif len(userinput) != 8:
    print("Phone number must be 8 digits")
elif not userinput.startswith('6' or '8' or '9'):  # ← This line!
    print("Phone number must start with 6, 8, or 9")
else:
    print("Valid phone number!")
```

### 🔍 Investigate: Why doesn't this work?

Test it with the phone number "81234567" — it should be valid, but it gets rejected!

<details>
<summary>Click to reveal what's happening</summary>

The expression `'6' or '8' or '9'` doesn't do what you might expect.

In Python, `or` evaluates from left to right and STOPS as soon as it finds a truthy value.

`'6'` is a non-empty string, so it's truthy. Python stops there and returns just `'6'`.

So `userinput.startswith('6' or '8' or '9')` becomes `userinput.startswith('6')`

It only checks if the number starts with 6, not 8 or 9!
</details>

### ✏️ Modify: The correct way

We need to check each condition separately with `or`:

```python
userinput = input('Type a phone number: ')

if not userinput:
    print("Nothing was typed")
elif not userinput.isdecimal():
    print("Type digits only")
elif len(userinput) != 8:
    print("Phone number must be 8 digits")
elif not (
    userinput.startswith("6")
    or userinput.startswith("8")
    or userinput.startswith("9")
):
    print("Phone number must start with 6, 8, or 9")
else:
    print("Valid phone number!")
```

**Now test with "81234567" and "71234567"** — both should work correctly!

### 🧪 Experiment: Understanding `and` vs `or`

**Scenario:** Your app needs to validate an email. It must:
- Contain "@"
- Contain "."

```python
email = input('Type your email: ')

# Option A: Using 'or'
if '@' in email or '.' in email:
    print("Valid email (Option A)")

# Option B: Using 'and'
if '@' in email and '.' in email:
    print("Valid email (Option B)")
```

**Predict:** What's the difference between Option A and Option B?

Test with these inputs:
- "test@" (only @)
- "test." (only .)
- "test@domain.com" (both)

<details>
<summary>Click to reveal the difference</summary>

Option A (`or`): Accepts "test@" OR "test." OR "test@domain.com"
- "test@" → Valid (has @)
- "test." → Valid (has .)
- "test@domain.com" → Valid (has both)

Option B (`and`): Only accepts "test@domain.com"
- "test@" → Invalid (missing .)
- "test." → Invalid (missing @)
- "test@domain.com" → Valid (has both)

For email validation, we need BOTH @ and . → use `and`
</details>
```

---

## Lesson 4: Recursion Trace Tables

**Insertion Point:** `lesson_04.ipynb`, after the `factorial()` example (after cell #7)

```markdown
### 📊 Understanding Recursion: Don't Trace Everything!

When beginners see recursive code, they try to trace through every single call in their head.

**This doesn't work.** You'll get lost after 2-3 calls.

Instead, let's trace just the FIRST FEW calls to understand the pattern, then trust the rest.

#### Real-world example: Re-prompting until valid input

Before `factorial`, let's look at a simpler recursion you already understand — re-prompting for a phone number:

```python
def prompt_valid_phone_number():
    userinput = input('Type a phone number: ')

    # Validation checks (simplified)
    if not userinput.isdecimal():
        print("Type digits only")
        return prompt_valid_phone_number()  # ← Calls itself!
    else:
        return userinput

# This keeps asking until user enters valid input
phone = prompt_valid_phone_number()
print(f"Got valid phone: {phone}")
```

### 📊 Trace: First 2-3 calls only

Let's trace what happens when user types "abc" then "91234567":

| Call | User Input | Check | Action | Returns |
|------|------------|-------|--------|---------|
| 1st | "abc" | Not digits | Print error, call self again | *waits* |
| 2nd | "91234567" | Is digits | Return "91234567" | "91234567" |
| 1st | (unwinds) | Has result now | Return what it got | "91234567" |

**Key insight:** Call 1 PAUSES and waits for Call 2 to finish. When Call 2 returns, Call 1 just passes that result along.

You don't need to imagine 10 calls. Just understand: "Each call waits for the next one to finish."

Now let's apply this to `factorial()`:

#### 📊 Trace: factorial(5) — First 3 calls only

```python
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
```

| Call | `n` value | Condition | Action | Status |
|------|-----------|-----------|--------|--------|
| 1st | 5 | `n > 1` | Calculate `5 * factorial(4)` | *waiting* |
| 2nd | 4 | `n > 1` | Calculate `4 * factorial(3)` | *waiting* |
| 3rd | 3 | `n > 1` | Calculate `3 * factorial(2)` | *waiting* |
| ... | ... | ... | ... | ... |
| Base | 1 | `n <= 1` | Return 1 | ✅ Done! |

Now the calls UNWIND in reverse order:

| Call | Has result | Calculation | Returns |
|------|------------|-------------|---------|
| Base | - | - | 1 |
| n=2 | Got 1 from base | `2 * 1 = 2` | 2 |
| n=3 | Got 2 from n=2 | `3 * 2 = 6` | 6 |
| n=4 | Got 6 from n=3 | `4 * 6 = 24` | 24 |
| n=5 | Got 24 from n=4 | `5 * 24 = 120` | 120 |

**You don't need to trace all 5 calls!** Just understand:
1. Calls stack up (go deeper)
2. Base case returns
3. Results unwind back up

### 🔍 Verify with debug output

Run this to see the actual call order:

```python
def factorial_debug(n, depth=0):
    indent = "  " * depth  # Indent based on call depth
    print(f"{indent}factorial({n}) called")

    if n <= 1:
        print(f"{indent}→ Base case! Returning 1")
        return 1
    else:
        result = n * factorial_debug(n - 1, depth + 1)
        print(f"{indent}→ Returning {result}")
        return result

print("Calling factorial_debug(5):")
factorial_debug(5)
```

Notice how the output indents deeper, then unwinds back!
```

---

## Lesson 8: Identity PRIMM

**Insertion Point:** `lesson_08.ipynb`, before the `word_stats` function (before cell #2)

```markdown
# Lesson 8: Identity and Mutability

So far, we've been working with variables that seem straightforward. But Python has some behaviors that can cause surprising bugs.

Let's start with a real-world scenario.

## 🤔 Predict: Student records processing

You're writing code to process student enrollment data. Each student record needs to track:
- Student name
- Class they're enrolling in
- Enrollment date

Here's a function that's supposed to create a separate record for each student:

```python
def create_student_records(names):
    """Creates a record for each student name"""
    record = {"class": "CS101", "date": "2025-01-21"}  # Common info
    records = []

    for name in names:
        record["name"] = name  # Add student's name
        records.append(record)  # Save the record

    return records

# Test with 3 students
students = ["Alice", "Bob", "Charlie"]
student_records = create_student_records(students)

print("Records created:")
for i, record in enumerate(student_records, 1):
    print(f"{i}. {record}")
```

**Before running, predict what the output will be:**

<details>
<summary>Most students expect...</summary>

Most students expect 3 different records:
```
1. {'name': 'Alice', 'class': 'CS101', 'date': '2025-01-21'}
2. {'name': 'Bob', 'class': 'CS101', 'date': '2025-01-21'}
3. {'name': 'Charlie', 'class': 'CS101', 'date': '2025-01-21'}
```
</details>

### 🔍 Run the code and investigate

Run the code above. **What did you actually get?**

<details>
<summary>Click to reveal what actually happens</summary>

You get the SAME record 3 times:
```
1. {'name': 'Charlie', 'class': 'CS101', 'date': '2025-01-21'}
2. {'name': 'Charlie', 'class': 'CS101', 'date': '2025-01-21'}
3. {'name': 'Charlie', 'class': 'CS101', 'date': '2025-01-21'}
```

All three records show "Charlie" — the last student! The first two names disappeared!
</details>

### 📊 What's going on? Track the identity

Let's add `id()` tracking to see what's happening:

```python
def create_student_records_debug(names):
    record = {"class": "CS101", "date": "2025-01-21"}
    records = []

    for name in names:
        print(f"Processing: {name}")
        print(f"  record id = {id(record)}")
        record["name"] = name
        records.append(record)
        print(f"  appended record with id = {id(records[-1])}")
        print()

    return records

students = ["Alice", "Bob", "Charlie"]
student_records = create_student_records_debug(students)

print("\nFinal records:")
for i, record in enumerate(student_records, 1):
    print(f"{i}. {record}")
```

**What do you notice about the `id()` values?**

<details>
<summary>Click to reveal</summary>

All the IDs are the SAME! We're appending the SAME dictionary 3 times.

Each time we modify `record["name"]`, we're changing the SAME object that's already in the list 3 times!
</details>

### ✏️ Modify: How do we fix this?

We need to create a NEW dictionary for each student:

```python
def create_student_records_fixed(names):
    records = []

    for name in names:
        record = {"class": "CS101", "date": "2025-01-21"}  # NEW dict each time!
        record["name"] = name
        records.append(record)

    return records

students = ["Alice", "Bob", "Charlie"]
student_records = create_student_records_fixed(students)

print("Records created:")
for i, record in enumerate(student_records, 1):
    print(f"{i}. {record}")
    print(f"   id = {id(record)}")  # Each record has different ID now!
```

Now each student gets their own separate record!
```

---

## Usage Notes

### Markdown Cell Format
All PRIMM sections should be in **markdown cells**, not code cells.

### Collapsible Details Pattern
```markdown
<details>
<summary>Click to reveal</summary>

Content here...
</details>
```

### Code Cell Format
All runnable code should be in **code cells** that follow the markdown explanation cells.

### Visual Indicators
- 🤔 Predict = Before running code
- 🔍 Investigate = After seeing surprising result
- ✏️ Modify = Fixing or improving code
- 📊 Trace = Trace table or visualization
- 🧪 Experiment = Trying variations

### Testing Checklist
- [ ] All code runs without errors
- [ ] Predictions are hidden until clicked
- [ ] Examples are real-world, not abstract
- [ ] Scaffolding doesn't repeat existing content
- [ ] Flow is natural, not abrupt
