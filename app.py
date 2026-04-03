from flask import Flask, render_template, request
from validator import validate_password

app = Flask(__name__)

# 프로필 데이터 (유지)
PROFILE = {
    "name": "장성욱",
    "tagline": "Computer Science Student & Developer",
    "description": "경북대학교 컴퓨터학부 학생으로, 다양한 분야의 프로젝트를 경험하고 있습니다. GPU 공유 시스템, GStreamer 비디오 처리 등 실무 중심의 프로젝트를 진행했습니다.",
    "education": "경북대학교 컴퓨터학부",
    "interests": "Backend Development, System Programming, AI",
    "goals": "성능과 효율성을 고려한 시스템 개발자가 되는 것",
    "email": "your.email@example.com",
    "github": "https://github.com/SungWookJang8440",
    "github_username": "SungWookJang8440",
}

# 프로젝트 데이터 (유지)
PROJECTS = [
    {
        "title": "GStreamer Video Analyzer",
        "description": "축구 경기 영상에서 태클 장면을 자동으로 감지하고 분석하는 비디오 처리 시스템.",
        "tech_stack": ["C", "GStreamer",],
        "emoji": "⚽",
        "github": "https://github.com/video-ai-2025/summer2025-team1",
        "demo": None
    },
    {
        "title": "MLOPS_Image_Clustering",
        "description": "MLOPS 이미지 클러스터링",
        "tech_stack": ["Node.js", "Docker", "python"],
        "emoji": "🧮",
        "github": "https://github.com/sang-hash/data-model",
        "demo": None
    }
]

@app.route("/")
def index():
    # ✨ 리팩토링: Data Clumps 해결! 
    # 파이썬의 언패킹(**) 연산자를 사용해 9개의 변수를 1줄로 우아하게 전달합니다.
    return render_template("index.html", **PROFILE, projects=PROJECTS)

@app.route("/profile")
def profile():
    # ✨ 리팩토링: Duplicated Code 해결!
    return render_template("index.html", **PROFILE, projects=PROJECTS)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        pwd = request.form.get('pw')
        result = validate_password(pwd)
        
        if result["is_valid"]:
            return f"입력하신 비밀번호는 아주 안전합니다! (서버 검증 통과) <br><br><a href='/register'>다시 테스트하기</a>"
        else:
            return f"비밀번호 검증 실패!<br>원인: {result['reasons']} <br><br><a href='/register'>돌아가기</a>"
    else:
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