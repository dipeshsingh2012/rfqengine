import asyncio
from typing import Any, Dict, List, AsyncGenerator

class DocumentParser:
    """Service for parsing various document formats with memory efficiency."""
    
    async def parse_text_stream(self, content: str) -> AsyncGenerator[Dict[str, Any], None]:
        """Simulates parsing a large text document line by line."""
        lines = content.splitlines()
        for line in lines:
            # Simulate async I/O or heavy processing
            await asyncio.sleep(0) 
            yield {"type": "text_line", "content": line.strip()}

    async def extract_metadata(self, content: str) -> Dict[str, Any]:
        """Extracts metadata from a document string."""
        return {
            "length": len(content),
            "has_content": len(content) > 0
        }
