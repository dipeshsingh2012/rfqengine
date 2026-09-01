import csv
import io
import re
from typing import Any, AsyncGenerator, Dict, List

class ExportService:
    """
    Service for generating sanitized, memory-efficient CSV streams.
    """

    @staticmethod
    def sanitize_csv_cell(value: Any) -> str:
        """Strip whitespace and escape formula injection characters."""
        val_str = str(value) if value is not None else ""
        cleaned = val_str.strip()
        dangerous_chars = ('=', '+', '-', '@', '\t', '\r')
        if cleaned.startswith(dangerous_chars):
            return f"'{val_str}"
        return val_str

    @staticmethod
    def sanitize_filename(filename: str) -> str:
        """Strictly sanitize filename to prevent path traversal."""
        return re.sub(r"[^a-zA-Z0-9_-]", "", filename)

    async def generate_csv_stream(
        self, 
        rows: List[Dict[str, Any]], 
        headers: List[str]
    ) -> AsyncGenerator[str, None]:
        """
        Memory-efficient streaming generator that yields CSV rows incrementally.
        """
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(headers)
        yield output.getvalue()
        output.seek(0)
        output.truncate(0)

        for row in rows:
            sanitized_row = [self.sanitize_csv_cell(row.get(h, "")) for h in headers]
            writer.writerow(sanitized_row)
            yield output.getvalue()
            output.seek(0)
            output.truncate(0)
