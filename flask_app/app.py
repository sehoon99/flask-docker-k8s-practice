from flask import Flask
import redis

app = Flask(__name__)

# Redis에 연결 (컨테이너 이름 기준)
r = redis.Redis(host='redis', port=6379, db=0)

@app.route('/')
def hello():
    count = r.incr('visit_count')  # 방문자 수 증가
    return f"Hello from Dockerized Flask! You are visitor #{count}"

@app.route('/reset')
def reset():
    r.set('visit_count', 0)  # 카운트 초기화
    return "Visitor counter reset to 0."

@app.route('/status')
def status():
    count = r.get('visit_count') or 0
    return f"Current visitor count is: {int(count)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
