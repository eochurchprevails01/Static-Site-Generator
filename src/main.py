import os
import shutil
from textnode import TextNode, TextType
from markdown_to_html import markdown_to_html_node, extract_title

def copy_dir(src, dst):
    """
    Recursively copy all contents from src directory to dst directory.
    First deletes all contents of dst to ensure a clean copy.
    """
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.makedirs(dst, exist_ok=True)
    
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
            print(f"Copied file: {src_path} to {dst_path}")
        elif os.path.isdir(src_path):
            copy_dir(src_path, dst_path)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read markdown
    with open(from_path, 'r') as f:
        markdown_content = f.read()
    
    # Read template
    with open(template_path, 'r') as f:
        template_content = f.read()
    
    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    
    # Extract title
    title = extract_title(markdown_content)
    
    # Replace placeholders
    full_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    
    # Ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Write to file
    with open(dest_path, 'w') as f:
        f.write(full_html)

def main():
    # Delete public directory
    if os.path.exists("public"):
        shutil.rmtree("public")
    
    # Copy static files
    copy_dir("static", "public")
    
    # Generate page
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()
