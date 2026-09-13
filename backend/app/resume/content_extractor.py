import re


def clean_lines(lines: list[str]) -> list[str]:
    """Remove empty lines and normalize whitespace."""

    cleaned = []

    for line in lines:
        line = re.sub(r"\s+", " ", line).strip()

        if line:
            cleaned.append(line)

    return cleaned


def extract_experience(lines: list[str]) -> list[dict]:
    """Return cleaned experience entries."""

    lines = clean_lines(lines)

    if not lines:
        return []

    return [
        {
            "description": line
        }
        for line in lines
    ]


def extract_education(lines: list[str]) -> list[dict]:
    """Return cleaned education entries."""

    lines = clean_lines(lines)

    if not lines:
        return []

    return [
        {
            "description": line
        }
        for line in lines
    ]


def extract_projects(lines: list[str]) -> list[dict]:
    """Return cleaned project entries."""

    lines = clean_lines(lines)

    if not lines:
        return []

    return [
        {
            "description": line
        }
        for line in lines
    ]


def extract_skills(lines: list[str]) -> list[str]:
    """Return cleaned skill names."""

    return clean_lines(lines)

def extract_achievements(lines: list[str]) -> list[dict]:
    """Return cleaned achievement entries."""

    lines = clean_lines(lines)

    if not lines:
        return []

    return [
        {
            "description": line
        }
        for line in lines
    ]