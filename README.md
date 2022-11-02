# 작업 디렉토리 생성방법

```
./ec 문제링크
```

## 예시

```
./ec https://www.acmicpc.net/problem/1008
./ec https://www.acmicpc.net/problem/1260
```

# 샘플 수정 방법

- `.sample` 디렉토리 내 파일 수정

# STANDARD 문제 구분

- 문제 난이도의 기준이 되는 문제
- 문제제목 앞에 ★ 추가

# Dependency 작성
- project의 현재 의존성 모듈을 `requirements.txt`에 기록
```
pip freeze > requirements.txt
```
# Dependency 설치
- `requirements.txt`의 의존성 모듈 설치
- `-user` 사용시 현재 사용자 계정에만 설치
```
pip install -r ./requirements.txt
pip install -r ./requirements.txt -user
```