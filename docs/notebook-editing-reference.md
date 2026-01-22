# Notebook Editing Reference

Learnings from working with Jupyter notebooks using the NotebookEdit tool.

---

## Workflow Summary

### 1. Initial Read
Always read the notebook first to understand:
- Current cell structure and IDs
- The insertion point (which cell_id to insert before)
- What content exists that needs to be modified

### 2. Insertions

**Finding:** Despite initial concerns about reverse-order insertion, cells appear in the **order the tool calls are made**.

To insert cells BEFORE cell `X`:
```json
{"cell_id": "X", "edit_mode": "insert", "cell_type": "markdown", "new_source": "..."}
```

Insert multiple cells in sequence — first call creates first cell (closest to target), second call creates second cell, etc.

### 3. Deletions

**Finding:** The `edit_mode: "delete"` does NOT work (returns validation error requiring `new_source`).

To remove a cell, use replace with empty string:
```json
{"cell_id": "X", "edit_mode": "replace", "new_source": ""}
```

### 4. Cell ID Tracking After Insertions

**Critical:** After inserting cells, all subsequent cell IDs shift forward.

Example: If you insert 3 cells before cell-10:
- Original cell-10 becomes cell-13
- Original cell-11 becomes cell-14
- etc.

**Workflow:** After inserting, **re-read the notebook** to get updated cell IDs before making further edits to cells after the insertion point.

### 5. Edit Modes Summary

| Mode | Purpose | Required Params |
|------|---------|-----------------|
| `insert` | Add new cell before specified cell_id | `cell_type`, `new_source` |
| `replace` | Replace content of existing cell | `new_source` |
| `delete` | Does NOT work — use replace with empty string instead | N/A |

### 6. Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| Assuming cell IDs remain static | Re-read after insertions |
| Trying to use delete mode | Use replace with empty string |
| Editing wrong cells due to ID shift | Always re-read to verify current IDs |
| Not verifying insertion order | Check the notebook after editing |

### 7. Verification Step

After making edits, re-read the affected section to verify:
- Cells appear in the correct order
- Content is as expected
- No unintended cells remain (e.g., test insertions)

---

## Session Example (Lesson 5 String Slicing PRIMM)

**Task:** Insert 8 PRIMM cells before cell-29, then update surrounding cells.

**Approach:**
1. Read notebook to locate cell-29 (old "Crash course")
2. Insert 8 cells before cell-29 in desired order (Predict → Run → Investigate → Make → Modify → Caveat)
3. Re-read to verify new structure and find shifted cell IDs
4. Replace old cell-29 with new header
5. Replace shifted cells (now at different IDs) with updated content
6. Re-read to verify final structure

**Key observation:** Cells appeared in correct order despite initial confusion about reverse insertion.
