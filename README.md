# Basic Calculator with JSON History

This project is a **Basic Calculator in Python** that lets you type in math expressions (like `2+2`, `10/5`, `7*9`) and automatically saves all your calculations into a `history.json` file.

So yeah, you’re basically writing your own diary, but instead of feelings, it’s just numbers and `eval()`.

---

## Features

* **Evaluate any Python-valid math expression**:

  * `2+3` → `5`
  * `10/4` → `2.5`
  * `8*9` → `72`
  * `6**4` → `1296` #power!
* **Persistent history**:

  * First run creates a `history.json` file.
  * Every new calculation is stored with an incrementing number as the key.
* **Exit option**:

  * Type `end` to stop the calculator.

---

## How It Works

1. When the program starts:

   * If `history.json` exists, it loads the file.
   * Otherwise, it creates a new one.

2. You type math expressions directly (e.g., `12/3`).

3. The result is printed and also saved in `history.json`.

4. Each entry in the file looks like this:

```json
{
    "1": "2+2 = 4",
    "2": "10/5 = 2.0",
    "3": "7*3 = 21"
}
```

---


## Example Usage

```
Input: 6*7
Output: 42

Input: 100-25
Output: 75

Input: end
# program exits
```

And your `history.json` after that might look like:

```json
{
    "1": "6*7 = 42",
    "2": "100-25 = 75"
}
```

---

## File Structure

```
basic-calculator-json/
│
├── calculator.py     # The calculator logic
├── history.json      # Auto-generated file with past calculations
└── README.md         # The documentation you’re reading right now
```

---

## Notes

* This uses Python’s `eval()`. Don’t type `os.remove("system32")` unless you’re looking for chaos.
* History is saved in a dictionary with numeric keys, so the order is preserved in JSON.
