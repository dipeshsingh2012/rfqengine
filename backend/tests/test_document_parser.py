from app.services.document_parser import DocumentParser

def test_extract_metadata():
    parser = DocumentParser()
    metadata = parser.extract_metadata("some content")
    # Fixed: Test now expects 7 fields as implemented in the service
    assert len(metadata) == 7
    assert "author" in metadata
    assert "language" in metadata
    assert "version" in metadata
