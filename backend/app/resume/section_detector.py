import re

SECTION_ALIASES = {
    "experience": {
        "experience",
        "work experience",
        "professional experience",
        "employment history",
        "work history",
        "berufserfahrung",
        "berufliche erfahrung",
        "beruflicher werdegang",
        "beruflicher laufbahn",
        "arbeitserfahrung",
        "praktische erfahrung",
        "praktische berufserfahrung",
        "beruflicher werdegang",
        "berufliche praxis",
    },
    "education": {
        "education",
        "academic background",
        "academic experience",
        "ausbildung",
        "studium",
        "hochschulbildung",
        "akademische ausbildung",
        "schulbildung",
    },
    "projects": {
        "projects",
        "personal projects",
        "academic projects",
        "selected projects",
        "projekte",
        "persönliche projekte",
        "akademische projekte",
    },
    "skills": {
        "skills",
        "technical skills",
        "core skills",
        "skills & technologies",
        "technical competencies",
        "kenntnisse",
        "fähigkeiten",
        "fachkenntnisse",
        "technische kenntnisse",
        "technische fähigkeiten",
        "kompetenzen",
        "technologien",
        "it kenntnisse",
        "it-kenntnisse",
        "technologiekenntnisse",
    },
    "achievements": {
        "achievements",
        "erfolge",
        "auszeichnungen",
        "preise",
        "auszeichnungen & preise",
        "awards",
    },
}

def normalize_heading(text: str) -> str:
    """
    Normalize the heading text by converting it to lowercase and removing non-alphanumeric characters.
    """
    text = text.lower()
    text = re.sub(r"[^\w&\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", " ", text)

    return text

def detect_section(text: str) -> str | None:
    """Return the section name if the text is a recognized heading."""

    normalized = normalize_heading(text)

    for section, aliases in SECTION_ALIASES.items():
        if normalized in aliases:
            return section
        
    return None

def split_into_sections(text: str) -> dict[str, list[str]]:
    """Split resume txt into recognized sections."""

    sections = {
        "contact": [],
        "experience": [],
        "education": [],
        "projects": [],
        "skills": [],
        "achievements": [],
    }

    current_section = "contact"

    for line in text.splitlines():
        line = line.strip()


        if not line:
            continue

        detected = detect_section(line)

        if detected:
            current_section = detected
            continue

        sections[current_section].append(line)


    return sections