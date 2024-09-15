from datetime import datetime

def format_value(key, value):
    if isinstance(value, dict):
        return ", ".join(filter(None, value.values()))
    elif isinstance(value, datetime):
        return value.strftime('%b %Y')
    elif isinstance(value, (list, tuple)):
        return ", ".join(map(str, value))
    return str(value)

def schema_to_markdown(data, level=1):
    markdown = ""

    if isinstance(data, dict):
        title = data.get('title', '')
        url = data.get('url', '')
        description = data.get('description', '')

        if title:
            heading = '#' * min(level, 3)  # Limit heading level to 3
            if url:
                markdown += f"{heading} [{title}]({url})\n\n"
            else:
                markdown += f"{heading} {title}\n\n"

        if description:
            markdown += f"{description}\n\n"

        for key, value in data.items():
            if key not in ['title', 'url', 'description']:
                if isinstance(value, (dict, list)):
                    markdown += schema_to_markdown(value, level + 1)
                else:
                    markdown += f"**{key.replace('_', ' ').title()}:** {format_value(key, value)}\n"
        markdown += "\n"

    elif isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                markdown += schema_to_markdown(item, level)
            elif isinstance(item, str):
                markdown += f"- {item}\n"
            else:
                markdown += schema_to_markdown(item, level)
        markdown += "\n"

    elif isinstance(data, str):
        if len(data.split()) > 10:  # Assume it's a long text field
            markdown += f"{data}\n\n"
        else:
            markdown += f"{data}\n\n"

    return markdown
