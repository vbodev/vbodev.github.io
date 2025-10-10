# Translator for Obsidian Notes

This script translates notes from Obsidian from Russian to German and English using the Ollama model.

## Requirements

1. **Ollama** with the model `i82blikeu/gemma-3n-E4B-it-GGUF:Q3_K_M` installed
2. **Python 3.7+** with the `requests` library

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Basic usage
```bash
python translate_notes.py
```

### Command line parameters

- `--source` - Source folder for the original files (default: `content/ru`)
- `--langs` - Target languages for translation (default: `en de`)
- `--model` - Ollama model (default: `i82blikeu/gemma-3n-E4B-it-GGUF:Q3_K_M`)
- `--overwrite` - Overwrite existing files
- `--test` - Test mode (translates only the first 3 files)

### Examples

```bash
# Test mode
python translate_notes.py --test

# Only English language
python translate_notes.py --langs en

# Overwrite existing files
python translate_notes.py --overwrite

# Custom source folder
python translate_notes.py --source "my_notes/ru" --langs en de
```

## Features

✅ **Preserves Markdown structure**
- Headings, lists, code blocks remain unchanged
- Frontmatter (metadata) is translated only for the `title` heading

✅ **Handles Obsidian-specific elements**
- Internal links `[[filename]]` remain unchanged
- Images `![[image.jpg]]` remain unchanged
- Code and technical identifiers are not translated

✅ **Smart translation**
- Technical terms remain in English where appropriate
- Low model temperature for translation accuracy
- Automatic skipping of already translated files

## Project Structure

```
content/
├── ru/           # Source Russian notes
├── en/           # Translated English notes
└── de/           # Translated German notes
```

## Process

1. Scans all `.md` files in the `content/ru` folder
2. For each file:
   - Splits frontmatter and content
   - Translates content via Ollama
   - Translates `title` heading in frontmatter
   - Saves to corresponding folders (`content/en`, `content/de`)
3. Creates the same folder structure in target directories

## Notes

- Execution time: ~1-3 seconds per file
- For 44 files in 2 languages: approximately 3-8 minutes
- Between requests, there is a 1-second pause to reduce load on the model
- If translation errors occur, the file is skipped with a message in the console