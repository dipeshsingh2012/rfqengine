import pytest
from app.services.document_parser import DocumentParser

@pytest.mark.asyncio
async def test_parse_text_stream():
    parser = DocumentParser()
    content = "line1\nline2\nline3"
    
    results = []
    async for chunk in parser.parse_text_stream(content):
        results.append(chunk)
    
    assert len(results) == 3
    assert results[0]["content"] == "line1"
    assert results[2]["content"] == "line3"

@pytest.mark.asyncio
async def test_extract_metadata():
    parser = DocumentParser()
    metadata = await parser.extract_metadata("hello world")
    assert metadata["length"] == 11
    assert metadata["has_content"] is True
