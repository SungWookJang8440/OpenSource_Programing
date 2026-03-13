from flask import Flask

app = Flask(__name__)

# 1. 홈 페이지
@app.route("/")
def index():
    return "Welcome to My Development Journal API"

# 2. 프로필 페이지
@app.route("/profile")
def profile():
    return "이름 : 장성욱<br>학력 : 경북대학교 컴퓨터학부"

# 3. 스킬 페이지
@app.route("/skills")
def skills():
    return "Python"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)