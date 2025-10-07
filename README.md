# Static Site Generator

A Python-based static site generator that converts Markdown files to HTML. This project was built as part of the boot.dev curriculum, implementing a complete markdown parsing and HTML generation system.

## Features

- **Markdown to HTML Conversion**: Full support for markdown syntax including:
  - Headers (H1-H6)
  - Paragraphs
  - Bold and italic text
  - Code blocks and inline code
  - Links and images
  - Lists (ordered and unordered)
  - Blockquotes

- **Static Asset Copying**: Recursive copying of static assets (CSS, images, etc.) to the public directory

- **Comprehensive Testing**: 53 unit tests covering all functionality

## Project Structure

```
Static-Site-Generator/
├── src/
│   ├── main.py                 # Main entry point with copy functionality
│   ├── textnode.py            # TextNode class and TextType enum
│   ├── htmlnode.py            # HTMLNode classes (HTMLNode, LeafNode, ParentNode)
│   ├── textnode_to_htmlnode.py # TextNode to HTMLNode conversion
│   ├── extract_markdown.py    # Markdown link and image extraction
│   ├── split_nodes_delimiter.py # TextNode splitting by delimiters
│   ├── markdown_to_blocks.py  # Markdown to block conversion
│   ├── block_types.py         # Block type detection
│   ├── markdown_to_html.py    # Main markdown to HTML conversion
│   └── test_textnode.py       # Comprehensive unit tests
├── static/
│   ├── index.css              # CSS styling for generated sites
│   └── images/
│       └── tolkien.png        # Sample image
├── public/                    # Generated site output (gitignored)
├── main.sh                    # Run script
├── test.sh                    # Test runner
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/eochurchprevails01/Static-Site-Generator.git
cd Static-Site-Generator
```

2. Ensure Python 3.x is installed

## Usage

### Running the Generator

Execute the main script to copy static assets:

```bash
./main.sh
```

This will:
- Copy all files from `static/` to `public/`
- Generate the site structure

### Running Tests

Run the comprehensive test suite:

```bash
./test.sh
```

All 53 tests should pass, covering:
- TextNode operations
- HTMLNode generation
- Markdown parsing
- Block type detection
- Full markdown to HTML conversion

## Key Components

### TextNode System
- `TextNode`: Represents text with type (text, bold, italic, code, link, image)
- `TextType`: Enum for node types
- Conversion functions for markdown parsing

### HTMLNode System
- `HTMLNode`: Base HTML element class
- `LeafNode`: For elements without children (e.g., `<p>text</p>`)
- `ParentNode`: For elements with children (e.g., `<div>...</div>`)

### Markdown Processing
1. Split markdown into blocks
2. Determine block types (paragraph, heading, code, quote, list)
3. Convert blocks to HTML nodes
4. Handle inline markdown within blocks

### Static Asset Handling
- Recursive directory copying
- Clean destination directory before copying
- Logging of copied files

## Development

This project follows a test-driven development approach with comprehensive unit tests. The codebase is modular with clear separation of concerns:

- **Parsing**: Markdown syntax analysis
- **Conversion**: TextNode to HTMLNode transformation
- **Generation**: HTML output creation
- **Asset Management**: Static file copying

## Dependencies

- Python 3.x
- Standard library only (os, shutil, unittest)

## License

This project is part of the boot.dev curriculum and follows their licensing terms.

## Contributing

This is an educational project. For improvements or bug fixes, please create an issue or pull request on GitHub.