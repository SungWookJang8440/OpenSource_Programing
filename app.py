from flask import Flask, request
from validator import validate_password  # 우리가 TADD로 만든 함수 임포트!

app = Flask(__name__)

# --- 기존 코드 유지 ---
@app.route("/")
def index():
    return "Welcome to My Development Journal API"

@app.route("/profile")
def profile():
    return "이름 : 장성욱<br>학력 : 경북대학교 컴퓨터학부"

@app.route("/skills")
def skills():
    return "Python"

@app.route("/register")
def register():
    # URL 파라미터로 비밀번호를 입력받습니다 (예: ?pw=Abc1234)
    pwd = request.args.get('pw')
    
    if not pwd:
        return "비밀번호를 입력해주세요. (예시 주소: /register?pw=자신의비밀번호)"
    
    # TADD로 안전성이 보장된 함수로 검증!
    result = validate_password(pwd)
    
    if result["is_valid"]:
        return f"입력하신 '{pwd}'는 아주 안전한 비밀번호입니다! (회원가입 통과)"
    else:
        # 실패한 이유(reasons)를 클라이언트(화면)에 보여줍니다.
        return f"비밀번호 검증 실패!<br>원인: {result['reasons']}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)