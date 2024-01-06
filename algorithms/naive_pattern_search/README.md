# Naive Pattern Search

## Overview

"Naive Pattern Search" is a collection of Python scripts located in a folder of the same name. The project contains two main scripts: one for counting the occurrences of a specified pattern in a given text, and another for replacing occurrences of a specified pattern in a string with a given substitute. These scripts are useful for basic text processing tasks such as pattern recognition, text cleaning, and data formatting.

## Features

- **Count Pattern Occurrences**: Count the number of times a specified pattern appears in a text.
- **Replace Pattern**: Replace occurrences of a pattern in a string with a specified substitute.
- **Case Sensitivity Option**: Choose whether the pattern replacement is case-sensitive.
- **Text Processing**: Perform basic text processing and data cleaning tasks.

## Script Descriptions

### Pattern Counting Script

`count_pattern(text, pattern)`

- Counts the number of occurrences of a specified pattern in a given text.
- Parameters:
  - `text`: The text in which to search for the pattern.
  - `pattern`: The pattern to count.
- Returns the number of times the pattern occurs in the text.

### Pattern Replacement Script

`replace_pattern(text, pattern, replacement, case_sensitive=True)`

- Replaces occurrences of a specified pattern in a string with a given substitute.
- Parameters:
  - `text`: The text in which to replace the pattern.
  - `pattern`: The pattern to replace.
  - `replacement`: The string to replace the pattern with.
  - `case_sensitive` (optional): Whether the search should be case-sensitive; defaults to `True`.
- Returns the text with the pattern replaced.

## Usage

1. **Pattern Counting Usage:**
   - Define `my_text` and `my_pattern` with the text and pattern you want to analyze.
   - Run the script to count the occurrences of `my_pattern` in `my_text`.
   - Example output will display the total count of the specified pattern.

2. **Pattern Replacement Usage:**
   - Define `text`, `pattern`, `replacement`, and `case_sensitive` (optional) parameters.
   - Run the script with these parameters to replace the specified pattern in the text.
   - Follow the provided example steps (`format_one` through `format_seven`) to see how the script can be used for complex text processing tasks.

*Note: These scripts are designed for simple text processing and are best suited for small-scale, basic pattern searching and replacement tasks.*
