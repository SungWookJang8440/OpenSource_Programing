from flask import Flask, request
from validator import validate_password

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to My Development Journal API"

@app.route("/profile")
def profile():
    return "이름 : 장성욱<br>학력 : 경북대학교 컴퓨터학부"

@app.route("/skills")
def skills():
    return "Python"

# --- 🎯 4단계 완벽 대응: 웹 라우트 및 클라이언트 검증 추가 ---
@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 폼에서 입력받은 비밀번호를 가져와 서버 단에서 TADD 로직으로 검증합니다.
        pwd = request.form.get('pw')
        result = validate_password(pwd)
        
        if result["is_valid"]:
            return f"입력하신 비밀번호는 아주 안전합니다! (서버 검증 통과) <br><br><a href='/register'>다시 테스트하기</a>"
        else:
            return f"비밀번호 검증 실패!<br>원인: {result['reasons']} <br><br><a href='/register'>돌아가기</a>"
    else:
        # GET 요청 시 사용자에게 입력 폼을 보여줍니다.
        # HTML5 속성(required, minlength="8")을 통한 client-side verification 적용!
        return '''
            <h3>관리자 회원가입 (비밀번호 검증 테스트)</h3>
            <form method="POST" action="/register">
                <label>비밀번호 입력 : </label>
                <input type="password" name="pw" required minlength="8" placeholder="8자 이상, 대문자/숫자 포함">
                <button type="submit">서버로 전송</button>
            </form>
            <p>※ 클라이언트 검증: 8자 미만 입력 시 브라우저가 자체적으로 경고를 띄웁니다.</p>
        '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)