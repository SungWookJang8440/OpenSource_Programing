def validate_password(password):
    if password is None:
        return {"is_valid": False, "reasons": ["IS_NULL"]}
    
    reasons = []
    
    if len(password) < 8:
        reasons.append("TOO_SHORT")
    if not any(char.isdigit() for char in password):
        reasons.append("NO_NUMBER")
    if not any(char.isupper() for char in password):
        reasons.append("NO_UPPERCASE")
        
    return {
        "is_valid": len(reasons) == 0,
        "reasons": reasons
    }