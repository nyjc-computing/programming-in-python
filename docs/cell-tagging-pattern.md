# Cell Metadata Tagging Pattern

## Purpose

Jupyter notebook cells should be tagged with descriptive metadata for:
- Navigation (jumping to specific sections)
- Filtering (showing/hiding specific cell types)
- Progress tracking (identifying exercises, examples, etc.)

## Tagging Patterns

### Markdown Cells with Headers

Cells starting with a header (`#`, `##`, etc.) get a slugified tag:

| Header Level | Tag Format | Example |
|--------------|------------|---------|
| `#` | `h1:<slug>` | `h1:lesson-2-abstraction` |
| `##` | `h2:<slug>` | `h2:conditional-iteration-with-while-loop` |
| `###` | `h3:<slug>` | `h3:exercise-1` |

**Slugification rules:**
- Convert to lowercase
- Replace spaces with hyphens
- Remove special characters (keep letters, numbers, hyphens)
- Remove leading/trailing non-alphanumeric characters

**Example:**
```markdown
## Conditional iteration with a `while` loop
```
→ Tag: `h2:conditional-iteration-with-while-loop`

**Additional metadata:** For `h1` cells, also add `"h1": "<slug>"` as a separate metadata field.

### Code Cells

Code cells are tagged based on their purpose:

| Purpose | Tag Format | Example |
|---------|------------|---------|
| Exercise | `exercise:<slug>` | `exercise:triangular-sum` |
| Try/Example | `try:<slug>` | `try:range-function` |
| PRIMM Predict | `primm:predict:<slug>` | `primm:predict:slicing-syntax` |
| PRIMM Run | `primm:run:<slug>` | `primm:run:test-predictions` |
| PRIMM Investigate | `primm:investigate:<slug>` | `primm:investigate:slicing-rules` |
| PRIMM Make | `primm:make:<slug>` | `primm:make:substring-rewrite` |
| PRIMM Modify | `primm:modify:<slug>` | `primm:modify:optional-parameters` |
| Example/Demo | `example:<slug>` | `example:factorial-function` |

**Slugification for code cells:**
- Base on the descriptive comment at the top of the cell
- Or infer from the exercise name in preceding markdown
- Use kebab-case (lowercase with hyphens)

### Special Cell Types

| Cell Type | Tag Format | Example |
|-----------|------------|---------|
| Introduction | `intro:<lesson>` | `intro:jupyter` |
| Summary | `summary:<lesson>` | `summary:iteration` |
| Hint | (no tag, use `<details>` collapsible) | — |

## Implementation Workflow

### 1. Read the Notebook

Read the notebook to understand the structure and identify cells needing tags.

### 2. Identify Cells to Tag

| Cell Type | When to Tag |
|-----------|-------------|
| Markdown headers | Always (h1-h3) |
| Exercise code cells | Always |
| Try/example code cells | Always |
| PRIMM cells | Always |
| Blank cells | Never |
| Non-header markdown | Usually not |

### 3. Apply Tags Surgically

**DO NOT** use bash for pattern-based edits (like `sed` across the whole file).

**DO** use Python to surgically target specific cells:

```python
import json
import re

with open('notebook.ipynb', 'r') as f:
    nb = json.load(f)

# Define tags by cell index (0-based)
tags_to_apply = {
    0: ["h2:introduction"],
    1: ["h1:lesson-title"],
    2: ["example:demo-code"],
    5: ["exercise:my-exercise"],
}

for index, tags in tags_to_apply.items():
    if index < len(nb['cells']):
        if 'metadata' not in nb['cells'][index]:
            nb['cells'][index]['metadata'] = {}
        nb['cells'][index]['metadata']['tags'] = tags

with open('notebook.ipynb', 'w') as f:
    json.dump(nb, f, indent=1)
```

**Note:** The `NotebookEdit` tool does NOT support setting metadata.

### 4. Verification

After tagging, verify by:
```bash
grep -A2 '"tags"' notebook.ipynb
```

## Examples

### Example 1: Header Cell

**Cell:**
```markdown
### Exercise 1

Write an iterative function, `triangular_sum(n)`, that takes in a positive integer `n`...
```

**Tag:** `h3:exercise-1`

### Example 2: Exercise Code Cell

**Cell:**
```python
def triangular_sum(n: int) -> int:
    """Write an appropriate docstring"""
    # Write your code here

print(triangular_sum(5))  # Expected: 15
```

**Tag:** `exercise:triangular-sum`

### Example 3: PRIMM Cell

**Cell:**
```python
# Run these to test your predictions
print("hello"[0:2])
print("hello"[1:4])
```

**Tag:** `primm:run:test-slicing-predictions`

## Current Tool Limitations

The `NotebookEdit` tool does NOT support setting metadata. Use:

```bash
# For single cell
jq '.cells[<index>].metadata.tags = ["<tag>"]' notebook.ipynb > tmp.json && mv tmp.json notebook.ipynb

# Or use Python for more complex operations
python -c "
import json
with open('notebook.ipynb') as f:
    nb = json.load(f)
nb['cells'][<index>]['metadata']['tags'] = ['<tag>']
with open('notebook.ipynb', 'w') as f:
    json.dump(nb, f, indent=1)
"
```

**Always backup before editing metadata.**
