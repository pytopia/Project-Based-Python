import re

def extract_yaml(content):
    pattern = r'```yaml\s*(.*?)\s*```'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(1).strip()
    else:
        return content.strip()
