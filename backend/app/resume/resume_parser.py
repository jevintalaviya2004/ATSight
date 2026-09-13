from app.parsers.document_parser import extract_text
from app.resume.contact_extractor import extract_contact_information
from app.resume.content_extractor import (
    extract_achievements,
    extract_education,
    extract_experience,
    extract_projects,
    extract_skills,
)
from app.resume.section_detector import split_into_sections


def parse_resume(file_path: str) -> dict:
    """Parse a resume document into structured data."""

    text = extract_text(file_path)

    sections = split_into_sections(text)

    resume = {
        "contact": extract_contact_information(sections["contact"]),
        "experience": extract_experience(sections["experience"]),
        "education": extract_education(sections["education"]),
        "projects": extract_projects(sections["projects"]),
        "skills": extract_skills(sections["skills"]),
        "achievements": extract_achievements(sections["achievements"]),
    }

    return resume