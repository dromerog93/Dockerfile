import argparse
import re
from pathlib import Path

def extract_fields(dockerfile_path):
    tool_name = dockerfile_path.parent.name
    base_image = version = category = subcategory = description = source = "NA"
    entrypoint = ""  # Inicializado vacío
    cmd_raw = ""

    with open(dockerfile_path, 'r', encoding='utf-8') as f:
        for line in f:
            line_strip = line.strip()

            if line_strip.startswith("FROM "):
                base_image = line_strip.split("FROM ")[-1]
            if 'LABEL version=' in line:
                version_match = re.search(r'version="?([\w\.\-\_]+)"?', line)
                if version_match:
                    version = version_match.group(1)
            if 'LABEL bioinfo.category=' in line:
                match = re.search(r'bioinfo.category="(.*?)"', line)
                if match:
                    category = match.group(1)
            if 'LABEL bioinfo.subcategory=' in line:
                match = re.search(r'bioinfo.subcategory="(.*?)"', line)
                if match:
                    subcategory = match.group(1)
            if 'LABEL description=' in line:
                match = re.search(r'description="(.*?)"', line)
                if match:
                    description = match.group(1)
            if 'LABEL source=' in line:
                match = re.search(r'source="(.*?)"', line)
                if match:
                    source = match.group(1)
            if line_strip.startswith("ENTRYPOINT"):
                entrypoint_clean = line_strip.replace("ENTRYPOINT", "").strip()
                entrypoint_clean = entrypoint_clean.strip("[]").replace('"', '').replace("'", "").strip()
                entrypoint = " ".join(entrypoint_clean.split(",")) if entrypoint_clean else ""
            if line_strip.startswith("CMD"):
                cmd_raw = line_strip.replace("CMD", "").strip()

    if not entrypoint and cmd_raw:
        cleaned_cmd = cmd_raw.strip("[]").replace('"', '').replace("'", "").strip()
        cleaned_cmd = " ".join(cleaned_cmd.split(","))
        entrypoint = f"CMD: {cleaned_cmd}"

    return [tool_name, category, subcategory, version, base_image, description, entrypoint, source]

def generate_table(input_dir: str, output_file: str):
    root = Path(input_dir)
    output_path = Path(output_file)
    file_exists = output_path.exists()
    
    header = ["Tool", "Category", "Subcategory", "Version", "Base Image", "Description", "Entry point", "Documentation"]
    rows = []

    for dockerfile_path in root.rglob("Dockerfile*"):
        rows.append(extract_fields(dockerfile_path))

    mode = 'a' if file_exists else 'w'
    with open(output_file, mode, encoding='utf-8') as out:
        if not file_exists:
            out.write("\t".join(header) + "\n")
        for row in rows:
            out.write("\t".join(row) + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate tabulated tool summary from Dockerfiles.")
    parser.add_argument('--input', required=True, help='Input directory with Dockerfiles')
    parser.add_argument('--output', default='tools_summary.txt', help='Output TXT file')

    args = parser.parse_args()
    generate_table(args.input, args.output)

