import re
from typing import Dict, Any, List

class DocumentParser:
    @staticmethod
    def clean_text(text: str) -> str:
        """Removes excessive whitespace and non-printable characters."""
        if not text:
            return ""
        # Remove control characters and normalize whitespace
        cleaned = re.sub(r"[\x00-\x1F\x7F]", "", text)
        return " ".join(cleaned.split())

    @staticmethod
    def extract_metadata(content: str) -> Dict[str, Any]:
        """Extracts basic metadata from document content."""
        return {
            "length": len(content),
            "word_count": len(content.split()),
            "has_links": bool(re.search(r"https?://", content))
        }
