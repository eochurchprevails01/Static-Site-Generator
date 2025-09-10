import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_different_text(self):
        node = TextNode("Text one", TextType.TEXT)
        node2 = TextNode("Text two", TextType.TEXT)
        self.assertNotEqual(node, node2)
    
    def test_not_eq_different_type(self):
        node = TextNode("Same Text", TextType.BOLD)
        node2 = TextNode("Same Text", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq_with_url_none(self):
        node = TextNode("Link Text", TextType.LINK, None)
        node2 = TextNode("Link Text", TextType.LINK, None)
        self.assertEqual(node, node2)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p","Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Raw text")
        self.assertEqual(node.to_html(), "Raw text")

    def test_leaf_to_html_no_value_raises_error(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()