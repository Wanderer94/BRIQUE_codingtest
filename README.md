# BRIQUE_codingtest

### 1. 가상 환경 생성

프로젝트의 종속성을 관리하기 위해 가상 환경을 생성합니다.

```bash
python -m venv venv
```

### 2. 가상 환경 활성화

- **Windows**:

  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux**:

  ```bash
  source venv/bin/activate
  ```

### 3. 필요한 패키지 설치

`requirements.txt` 파일에 정의된 패키지를 설치합니다.

```bash
pip install -r requirements.txt
```

### 4. 문제별 실행 방법

각 문제는 별도의 폴더에 있으며, 폴더 이름은 `Q01`, `Q02`, 등으로 지정되어 있습니다. 각 폴더에는 `main.py` 파일이 포함되어 있습니다. 다음 명령어를 사용하여 각 문제를 실행할 수 있습니다.

- **문제 1 (폴더: Q01)**:

  ```bash
  cd Q01
  python main.py
  cd ..
  ```

- **문제 2 (폴더: Q02)**:
  서버를 실행하고 나서 클라이언트를 실행해야 합니다. 각 서버는 별도의 터미널에서 실행되어야 하며, 클라이언트도 각 서버에 맞게 실행해야 합니다.

1. **비동기 서버 실행**

   첫 번째 터미널을 열고 비동기 서버를 실행합니다.

   ```bash
   python async_server.py
   ```

2. **비동기 클라이언트 실행**

   두 번째 터미널을 열고 비동기 클라이언트를 실행합니다.

   ```bash
   python async_client.py
   ```

3. **동기 서버 실행**

   세 번째 터미널을 열고 동기 서버를 실행합니다.

   ```bash
   python sync_server.py
   ```

4. **동기 클라이언트 실행**

   네 번째 터미널을 열고 동기 클라이언트를 실행합니다.

   ```bash
   python sync_client.py
   ```

- **문제 3 (폴더: Q03)**:

  ```bash
  cd Q03
  python main.py
  cd ..
  ```

- **문제 4 (폴더: Q04)**:

1. 애플리케이션을 실행합니다. app.py 파일을 사용하여 애플리케이션을 시작합니다.

```bash
cd Q04
python app.py
cd ..
```

2.  애플리케이션이 실행되면 웹 브라우저를 열고 다음 URL로 이동하여 애플리케이션을 확인합니다:

```
http://127.0.0.1:5000/
```

3. 애플리케이션 사용

- **기온과 습도 입력:**
  입력 테이블에 기온과 습도를 입력합니다. 입력 필드를 수정하면 그래프가 자동으로 업데이트됩니다.

- **랜덤화 버튼:**
  "Randomize" 버튼을 클릭하면 기온과 습도의 값이 랜덤으로 생성되며, 표와 그래프가 업데이트됩니다.

- **문제 5 (폴더: Q05)**:

  ```bash
  cd Q05
  python main.py
  cd ..
  ```

- **문제 7 (폴더: Q07)**:

  ```bash
  cd Q07
  python main.py
  cd ..
  ```

### 5. 가상 환경 비활성화

작업이 끝난 후 가상 환경을 비활성화합니다.

```bash
deactivate
```
