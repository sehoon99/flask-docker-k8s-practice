# Flask + Redis 방문자 카운터 앱 (Dockerized)

이 프로젝트는 Docker와 Docker Compose를 사용하여 Flask 웹 애플리케이션과 Redis를 연동한 간단한 방문자 카운터를 구현합니다.

## 🧱 구성

- **Flask**: 웹 서버
- **Redis**: 방문자 수 저장
- **Docker Compose**: 서비스 오케스트레이션

## 🚀 실행 방법

```bash
git clone https://github.com/sehoon99/flask-docker-k8s-practice.git
cd flask-docker-k8s-practice/docker-compose
docker-compose up --build
