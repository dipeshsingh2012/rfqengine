import pytest
from app.services.document_parser import DocumentParser

def test_clean_text_removes_whitespace():
    input_text = "  Hello    \n World  \t "
    assert DocumentParser.clean_text(input_text) == "Hello World"

def test_clean_text_removes_control_chars():
    input_text = "Hello\x00World"
    assert DocumentParser.clean_text(input_text) == "HelloWorld"

def test_extract_metadata():
    content = "Visit https://example.com for more info."
    metadata = DocumentParser.extract_metadata(content)
    assert metadata["word_count"] == 7
    assert metadata["has_links"] is True
