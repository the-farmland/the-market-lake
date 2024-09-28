from fastapi import Request, HTTPException

valid_serial_codes = ["serial-code-1", "serial-code-2"]  # Add your valid serial codes here
verification_codes = {
    "serial-code-1": "verification-code-1",
    "serial-code-2": "verification-code-2"
}

async def is_authenticated_serial(request: Request):
    serial_code = request.headers.get('plus-api-serial-code')
    if serial_code in valid_serial_codes:
        return True
    else:
        raise HTTPException(status_code=403, detail="Invalid or missing serial code")
