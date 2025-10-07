import os
import shutil
from textnode import TextNode, TextType

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

def main():
    copy_dir("static", "public")

if __name__ == "__main__":
    main()
