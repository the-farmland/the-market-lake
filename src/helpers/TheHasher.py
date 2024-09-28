from fastapi import Request, HTTPException

# Add your valid hash codes here
valid_hash_codes = ["hash-code-1", "hash-code-2"]

hash_verification_codes = {
    "hash-code-1": "hash-verification-code-1",
    "hash-code-2": "hash-verification-code-2"
}

async def is_authenticated_hash(request: Request):
    hash_code = request.headers.get('plus-api-hash-code')
    if hash_code in valid_hash_codes:
        return True
    else:
        raise HTTPException(status_code=403, detail="Invalid or missing hash code")
