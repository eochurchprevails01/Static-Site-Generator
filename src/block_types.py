from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if not block:
        return BlockType.PARAGRAPH
    
    lines = block.split("\n")
    
    # Heading: starts with 1-6 # followed by space
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    # Code: starts with ``` and ends with ```
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    # Quote: every line starts with >
    if all(line.startswith(">") for line in lines if line):
        return BlockType.QUOTE
    
    # Unordered list: every line starts with - followed by space
    if all(line.startswith("- ") for line in lines if line):
        return BlockType.UNORDERED_LIST
    
    # Ordered list: every line starts with number. (e.g., 1., 2.)
    if all(line.strip() for line in lines):  # Ensure no empty lines
        numbered = True
        for i, line in enumerate(lines, 1):
            if not line.startswith(f"{i}. "):
                numbered = False
                break
        if numbered:
            return BlockType.ORDERED_LIST
    
    # Default: paragraph
    return BlockType.PARAGRAPH