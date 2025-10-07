# Static Site Generator

A Python-based static site generator that converts Markdown files to HTML pages with templates. This project was built as part of the boot.dev curriculum, implementing a complete markdown parsing, HTML generation, and site building system.

## Features

- **Markdown to HTML Conversion**: Full support for markdown syntax including:
  - Headers (H1-H6)
  - Paragraphs
  - Bold and italic text
  - Code blocks and inline code
  - Links and images
  - Lists (ordered and unordered)
  - Blockquotes

- **Page Generation**: Generate complete HTML pages from markdown content using templates
  - Extract titles from H1 headers
  - Apply HTML templates with placeholders
  - Generate full websites with navigation and styling

- **Static Asset Management**: Recursive copying of static assets (CSS, images, etc.) to the public directory

- **Web Server**: Built-in development server for previewing generated sites

- **Comprehensive Testing**: 57 unit tests covering all functionality

## Project Structure

```
Static-Site-Generator/
├── src/
│   ├── main.py                 # Main entry point with site generation
│   ├── textnode.py            # TextNode class and TextType enum
│   ├── htmlnode.py            # HTMLNode classes (HTMLNode, LeafNode, ParentNode)
│   ├── textnode_to_htmlnode.py # TextNode to HTMLNode conversion
│   ├── extract_markdown.py    # Markdown link and image extraction
│   ├── split_nodes_delimiter.py # TextNode splitting by delimiters
│   ├── markdown_to_blocks.py  # Markdown to block conversion
│   ├── block_types.py         # Block type detection
│   ├── markdown_to_html.py    # Main markdown to HTML conversion and title extraction
├── content/
│   └── index.md               # Main page content in markdown
├── static/
│   ├── index.css              # CSS styling for generated sites
│   └── images/
│       └── tolkien.png        # Sample image
├── public/                    # Generated site output (gitignored)
├── template.html              # HTML template for page generation
├── main.sh                    # Run script with web server
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

Execute the main script to generate the complete site and start the development server:

```bash
./main.sh
```

This will:
- Generate HTML pages from markdown content using templates
- Copy all static assets (CSS, images, etc.) to the public directory
- Start a local web server at http://localhost:8888

### Running Tests

Run the comprehensive test suite:

```bash
./test.sh
```

All 57 tests should pass, covering:
- TextNode operations
- HTMLNode generation
- Markdown parsing
- Block type detection
- Title extraction
- Full page generation

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
5. Extract titles from H1 headers

### Page Generation
- `generate_page()`: Converts markdown to HTML pages using templates
- Template system with `{{ Title }}` and `{{ Content }}` placeholders
- Automatic directory creation for output files

### Static Asset Handling
- Recursive directory copying
- Clean destination directory before copying
- Logging of copied files

### Development Server
- Built-in Python HTTP server for local development
- Serves generated site at http://localhost:8888

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