import argparse
import os
import re
from pathlib import Path
from collections import defaultdict, OrderedDict

def extract_labels(dockerfile_path):
    category, subcategory = None, None
    with open(dockerfile_path, 'r', encoding='utf-8') as f:
        for line in f:
            if 'LABEL bioinfo.category=' in line:
                category_match = re.search(r'bioinfo.category="(.*?)"', line)
                if category_match:
                    category = category_match.group(1).strip().capitalize()
            if 'LABEL bioinfo.subcategory=' in line:
                subcategory_match = re.search(r'bioinfo.subcategory="(.*?)"', line)
                if subcategory_match:
                    subcategory = subcategory_match.group(1).strip()
            if category and subcategory:
                break
    return category or "Uncategorized", subcategory or "unspecified"

def read_dockerfile_content(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().strip()

def generate_markdown(input_dir: str, output_file: str, sorted_output: bool = True):
    root = Path(input_dir)
    group_class = defaultdict if sorted_output else OrderedDict
    data = group_class(lambda: group_class(list))

    for dockerfile_path in root.rglob("Dockerfile*"):
        tool_name = dockerfile_path.parent.name
        category, subcategory = extract_labels(dockerfile_path)
        docker_content = read_dockerfile_content(dockerfile_path)
        if category not in data:
            data[category] = group_class(list)
        if subcategory not in data[category]:
            data[category][subcategory] = []
        data[category][subcategory].append((tool_name, docker_content))

    with open(output_file, 'w', encoding='utf-8') as out:
        out.write("# Bioinformatics Tools\n\n")
        for category in sorted(data) if sorted_output else data:
            out.write(f"## {category}\n\n")
            for subcategory in sorted(data[category]) if sorted_output else data[category]:
                out.write(f"### {subcategory}\n\n")
                for tool_name, content in sorted(data[category][subcategory]) if sorted_output else data[category][subcategory]:
                    out.write(f"#### {tool_name}\n\n")
                    out.write("```dockerfile\n")
                    out.write(content)
                    out.write("\n```\n\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate markdown catalog of Dockerfile tools.")
    parser.add_argument('--input', required=True, help='Input directory with Dockerfiles')
    parser.add_argument('--output', default='bioinfo_tools.md', help='Output markdown file')
    parser.add_argument('--unsorted', action='store_true', help='Preserve insertion order instead of sorting alphabetically')

    args = parser.parse_args()
    generate_markdown(args.input, args.output, sorted_output=not args.unsorted)

