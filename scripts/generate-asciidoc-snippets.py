import os
import sys

def generate_snippet_file(variable_name, variable_value):

    """
    Generates a collection of Sublime Text snippet files from a single AsciiDoc attributes file
    """

    prefix = "openshift"
    filename = f"{prefix}_{variable_name.lower()}.sublime-snippet"

    with open(filename, "w") as f:
        content = f"<snippet>\n\t<content>{variable_name}\n</content>\n\t<tabTrigger>{variable_name}</tabTrigger>\n\t<scope>text.asciidoc</scope>\n\t<description>{variable_value.strip()}</description>\n</snippet>"
        f.write(content)

def main(input_filename):
    with open(input_filename) as f:
        for line in f:
            if line.startswith(":"):
                variable_name, variable_value = line.strip().split(":", 2)[1:]
                generate_snippet_file(variable_name, variable_value)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_filename>")
        sys.exit(1)
    input_filename = sys.argv[1]
    main(input_filename)
