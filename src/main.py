import os
import shutil
import sys
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

def generate_page(from_path, template_path, dest_path, basepath="/"):
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
    
    # Replace basepath in href and src
    full_html = full_html.replace('href="/', f'href="{basepath}')
    full_html = full_html.replace('src="/', f'src="{basepath}')
    
    # Ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Write to file
    with open(dest_path, 'w') as f:
        f.write(full_html)

def generate_pages_recursive(content_dir, template_path, dest_dir, basepath="/"):
    """
    Recursively generate HTML pages from all index.md files in content_dir
    """
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file == 'index.md':
                # Get relative path from content_dir
                rel_path = os.path.relpath(root, content_dir)
                if rel_path == '.':
                    rel_path = ''
                
                # Source markdown path
                md_path = os.path.join(root, file)
                
                # Destination HTML path
                if rel_path:
                    html_path = os.path.join(dest_dir, rel_path, 'index.html')
                else:
                    html_path = os.path.join(dest_dir, 'index.html')
                
                # Generate the page
                generate_page(md_path, template_path, html_path, basepath)

def main():
    # Get basepath from command line argument
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    
    dest_dir = "docs"  # Build into docs for GitHub Pages
    
    # Delete docs directory
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    
    # Copy static files
    copy_dir("static", dest_dir)
    
    # Generate all pages
    generate_pages_recursive("content", "template.html", dest_dir, basepath)

if __name__ == "__main__":
    main()
