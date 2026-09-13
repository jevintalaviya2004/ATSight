import re


SECTION_ALIASES = {
    "responsibilities": {
        "responsibilities",
        "key responsibilities",
        "job responsibilities",
        "your responsibilities",
        "tasks",
        "duties",
        "aufgaben",
        "tätigkeiten",
        "verantwortlichkeiten",
        "aufgabengebiet",
    },
    "requirements": {
        "requirements",
        "qualifications",
        "job requirements",
        "required qualifications",
        "your profile",
        "profile",
        "anforderungen",
        "qualifikationen",
        "voraussetzungen",
        "anforderungsprofil",
        "ihr profil",
    },
    "education": {
        "education",
        "educational requirements",
        "academic requirements",
        "ausbildung",
        "studium",
        "hochschulbildung",
        "bildung",
    },
    "experience": {
        "experience",
        "work experience",
        "professional experience",
        "required experience",
        "berufserfahrung",
        "berufliche erfahrung",
        "erfahrung",
        "praktische erfahrung",
    },
    "skills": {
        "skills",
        "technical skills",
        "technical competencies",
        "technologies",
        "skills & technologies",
        "kenntnisse",
        "fachkenntnisse",
        "technische kenntnisse",
        "kompetenzen",
        "technologien",
        "it kenntnisse",
        "it-kenntnisse",
    },
}


def normalize_heading(text: str) -> str:
    """Normalize a possible JD section heading."""

    text = text.strip().lower()
    text = re.sub(r"[^\w&\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", " ", text)

    return text


def detect_section(text: str) -> str | None:
    """Return the recognized section name."""

    normalized = normalize_heading(text)

    for section, aliases in SECTION_ALIASES.items():
        if normalized in aliases:
            return section

    return None


def split_into_sections(text: str) -> dict[str, list[str]]:
    """Split a job description into recognized sections."""

    sections = {
        "general": [],
        "responsibilities": [],
        "requirements": [],
        "education": [],
        "experience": [],
        "skills": [],
    }

    current_section = "general"

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