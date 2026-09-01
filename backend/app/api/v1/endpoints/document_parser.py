from fastapi import APIRouter, UploadFile, File, HTTPException, status
from typing import Dict, Any

router = APIRouter()

@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload_document(file: UploadFile = File(...)) -> Dict[str, Any]:
    """
    Handles document uploads (CSV, Markdown, etc.).
    Validates file extensions and content.
    """
    allowed_extensions = {".csv", ".md", ".txt", ".pdf"}
    file_ext = file.filename.split(".")[-1].lower()
    
    # Check extension
    if f".{file_ext}" not in allowed_extensions:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported file extension: {file_ext}"
        )

    content = await file.read()
    if not content:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File is empty"
        )

    # Logic for parsing would go here
    return {
        "filename": file.filename,
        "size": len(content),
        "status": "uploaded"
    }
