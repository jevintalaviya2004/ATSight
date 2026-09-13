import re


EMAIL_PATTERN = re.compile(
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
)

PHONE_PATTERN = re.compile(
    r"(?<!\d)(?:\+?\d[\d\s().-]{7,}\d)(?!\d)"
)

LINKEDIN_PATTERN = re.compile(
    r"(?:https?://)?(?:www\.)?linkedin\.com/in/[A-Za-z0-9_-]+",
    re.IGNORECASE,
)

GITHUB_PATTERN = re.compile(
    r"(?:https?://)?(?:www\.)?github\.com/[A-Za-z0-9_-]+",
    re.IGNORECASE,
)


def extract_contact_information(lines: list[str]) -> dict[str, str | None]:
    """Extract contact information from resume lines."""

    contact = {
        "name": None,
        "email": None,
        "phone": None,
        "linkedin": None,
        "github": None,
    }

    for line in lines:
        if contact["email"] is None:
            match = EMAIL_PATTERN.search(line)
            if match:
                contact["email"] = match.group(0)

        if contact["phone"] is None:
            match = PHONE_PATTERN.search(line)
            if match:
                contact["phone"] = match.group(0).strip()

        if contact["linkedin"] is None:
            match = LINKEDIN_PATTERN.search(line)
            if match:
                contact["linkedin"] = match.group(0)

        if contact["github"] is None:
            match = GITHUB_PATTERN.search(line)
            if match:
                contact["github"] = match.group(0)

    # Basic name detection:
    # Usually the first meaningful line before contact details.
    for line in lines:
        cleaned = line.strip()

        if not cleaned:
            continue

        if (
            EMAIL_PATTERN.search(cleaned)
            or PHONE_PATTERN.search(cleaned)
            or LINKEDIN_PATTERN.search(cleaned)
            or GITHUB_PATTERN.search(cleaned)
        ):
            continue

        if len(cleaned.split()) <= 5:
            contact["name"] = cleaned
            break

    return contact