# ValidationResult 클래스 도입 (Primitive Obsession 해결)
class ValidationResult:
    def __init__(self, is_valid: bool, reasons: list):
        self.is_valid = is_valid
        self.reasons = reasons

    # 기존 딕셔너리처럼 접근 가능하게 만들어서 기존 테스트 코드를 수정하지 않도록 함 (호환성 유지)
    def __getitem__(self, item):
        return getattr(self, item)

# Strategy Pattern 도입 (OCP 위반 및 Excessive if/else 해결)
class ValidationRule:
    def validate(self, password: str, reasons: list):
        pass

class LengthRule(ValidationRule):
    MIN_LENGTH = 8 # Magic Number 해결
    def validate(self, password: str, reasons: list):
        if len(password) < self.MIN_LENGTH:
            reasons.append("TOO_SHORT")

class NumberRule(ValidationRule):
    def validate(self, password: str, reasons: list):
        if not any(char.isdigit() for char in password):
            reasons.append("NO_NUMBER")

class UpperCaseRule(ValidationRule):
    def validate(self, password: str, reasons: list):
        if not any(char.isupper() for char in password):
            reasons.append("NO_UPPERCASE")

def validate_password(password: str):
    if password is None:
        return ValidationResult(False, ["IS_NULL"])
    
    reasons = []
    # 규칙들을 리스트에 담아 순회
    rules = [LengthRule(), NumberRule(), UpperCaseRule()]
    
    for rule in rules:
        rule.validate(password, reasons)
        
    return ValidationResult(len(reasons) == 0, reasons)