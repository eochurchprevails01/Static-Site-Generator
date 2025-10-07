from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text_parts = node.text.split(delimiter)
        if len(text_parts) % 2 == 0:
            raise ValueError("Invalid Markdown syntax: unmatched delimiter")
        current_text_type = TextType.TEXT
        for part in text_parts:
            if part:
                new_nodes.append(TextNode(part, current_text_type))
            current_text_type = text_type if current_text_type == TextType.TEXT else TextType.TEXT
    return new_nodes

