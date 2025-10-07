from markdown_to_blocks import markdown_to_blocks
from block_types import BlockType, block_to_block_type
from textnode import TextNode, TextType
from textnode_to_htmlnode import text_node_to_html_node
from extract_markdown import text_to_textnodes
from htmlnode import HTMLNode, LeafNode, ParentNode

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    lines = block.split("\n")

    if block_type == BlockType.HEADING:
        level = block.count("#", 0, block.find(" "))
        content = block.lstrip("# ").strip()
        children = text_to_children(content)
        return ParentNode(f"h{level}", children)

    if block_type == BlockType.CODE:
        # Remove the first and last line's triple backticks, preserve all formatting
        code_lines = lines[:]
        if code_lines[0].startswith("```"):
            code_lines = code_lines[1:]
        if code_lines and code_lines[-1].startswith("```"):
            code_lines = code_lines[:-1]
        content = "\n".join(code_lines) + "\n"
        text_node = TextNode(content, TextType.TEXT)
        code_node = text_node_to_html_node(text_node)
        return ParentNode("pre", [ParentNode("code", [code_node])])

    if block_type == BlockType.QUOTE:
        # Preserve newlines between quote lines
        content = "\n".join(line.lstrip("> ").strip() for line in lines if line.strip())
        children = text_to_children(content)
        return ParentNode("blockquote", children)

    if block_type == BlockType.UNORDERED_LIST:
        items = [line.lstrip("- ").strip() for line in lines if line.strip()]
        children = [ParentNode("li", text_to_children(item)) for item in items]
        return ParentNode("ul", children)

    if block_type == BlockType.ORDERED_LIST:
        import re
        items = [re.sub(r"^\d+\. ", "", line).strip() for line in lines if line.strip()]
        children = [ParentNode("li", text_to_children(item)) for item in items]
        return ParentNode("ol", children)

    if block_type == BlockType.PARAGRAPH:
        # Join lines with a space for paragraphs
        content = " ".join(line.strip() for line in lines if line.strip())
        children = text_to_children(content)
        return ParentNode("p", children)

    raise ValueError(f"Unknown block type: {block_type}")

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = [block_to_html_node(block) for block in blocks]
    return ParentNode("div", children)