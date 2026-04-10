class ValidationResult:
    """비밀번호 검증 결과를 담는 객체
    
    Attributes:
        is_valid (bool): 비밀번호가 모든 규칙을 통과했는지 여부
        reasons (list): 통과하지 못했을 경우의 실패 원인 목록
    """
    def __init__(self, is_valid: bool, reasons: list):
        self.is_valid = is_valid
        self.reasons = reasons

    def __getitem__(self, item):
        return getattr(self, item)

class ValidationRule:
    """비밀번호 검증 규칙의 기본 인터페이스"""
    def validate(self, password: str, reasons: list):
        """비밀번호를 검증하고 실패 시 reasons 리스트에 원인을 추가합니다."""
        pass

class LengthRule(ValidationRule):
    """비밀번호 최소 길이 검증 규칙"""
    MIN_LENGTH = 8 
    def validate(self, password: str, reasons: list):
        if len(password) < self.MIN_LENGTH:
            reasons.append("TOO_SHORT")

class NumberRule(ValidationRule):
    """비밀번호 내 숫자 포함 여부 검증 규칙"""
    def validate(self, password: str, reasons: list):
        if not any(char.isdigit() for char in password):
            reasons.append("NO_NUMBER")

class UpperCaseRule(ValidationRule):
    """비밀번호 내 대문자 포함 여부 검증 규칙"""
    def validate(self, password: str, reasons: list):
        if not any(char.isupper() for char in password):
            reasons.append("NO_UPPERCASE")

def validate_password(password: str) -> ValidationResult:
    """주어진 비밀번호가 보안 규칙을 모두 만족하는지 검사합니다.

    Strategy 패턴을 사용하여 구성된 여러 규칙(길이, 숫자, 대문자)을 순차적으로 검증합니다.

    Args:
        password (str): 검증할 평문 비밀번호 문자열.

    Returns:
        ValidationResult: 검증 통과 여부(is_valid)와 실패 원인(reasons)을 포함한 객체.
    """
    if password is None:
        return ValidationResult(False, ["IS_NULL"])
    
    reasons = []
    rules = [LengthRule(), NumberRule(), UpperCaseRule()]
    
    for rule in rules:
        rule.validate(password, reasons)
        
    return ValidationResult(len(reasons) == 0, reasons)