# BookBot

BookBot is a command-line tool that analyzes text files and generates statistics about word and character frequency. It's perfect for examining the composition of books, documents, or any large text files.

## Features

- **Word Count**: Calculates the total number of words in a document
- **Character Frequency Analysis**: Counts the occurrence of each character and displays alphabetic characters sorted by frequency
- **File-based Analysis**: Works with any text file provided as input
- **Clear Output Formatting**: Displays results in an organized, easy-to-read format

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ghurstird/bookbot.git
cd bookbot
```

2. No additional dependencies are required - this project uses only Python standard library.

## Usage

Run BookBot by providing the path to a text file:

```bash
python3 main.py <path_to_book>
```

### Example

```bash
python3 main.py books/frankenstein.txt
```

This will output:
- The book's file path
- Total word count
- Character frequency count (alphabetic characters only, sorted by frequency)

### Error Handling

- If no file path is provided, the program will display a usage message
- If the specified file cannot be found, an error message will be displayed

## Project Structure

- `main.py` - Main entry point for the application
- `stats.py` - Contains functions for text analysis (word count, character count, sorting)
- `books/` - Directory containing sample text files for analysis

## How It Works

1. **main.py** reads the specified text file
2. **stats.py** functions process the text:
   - `get_word_count()` - Splits text by whitespace and counts words
   - `get_char_count()` - Counts occurrences of each character (case-insensitive)
   - `get_sorted_list()` - Sorts characters by frequency in descending order
3. Results are formatted and displayed to the user

## Sample Books

The `books/` directory includes classic literature texts:
- `frankenstein.txt` - Frankenstein by Mary Shelley
- `mobydick.txt` - Moby Dick by Herman Melville
- `prideandprejudice.txt` - Pride and Prejudice by Jane Austen

## About

BookBot is a [Boot.dev](https://www.boot.dev) project, created as an introduction to Python programming and command-line applications.