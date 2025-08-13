from fastapi import APIRouter, UploadFile, File, HTTPException
import backend.routes.metrics_store as store

router = APIRouter()

@router.post("/api/v1/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        store.metrics_store["uploaded_files"].append(file.filename)
        return {"status": "success", "filename": file.filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
