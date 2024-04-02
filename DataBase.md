Alembic은 SQLAlchemy를 위한 마이그레이션 도구로, 데이터베이스 스키마의 변경 관리를 용이하게 해줍니다.

# Installation
```bash
pip install alembic
```

# Initialize Alembic
initial Alembic in **Root** directory on Project  
create alembic.ini and new directory as alembic which contains setting files and migration scripts

```bash
alembic init alembic
```

# Set DataBase URL
```ini
# alembic.ini
sqlalchemy.url = mysql+pymysql://username:password@localhost/databasename
```
또는, alembic/env.py 파일 내에서 create_engine 호출을 사용하여 프로그래매틱하게 데이터베이스 URL을 설정할 수도 있습니다. 이 방법을 사용하면 환경 변수나 다른 설정 파일에서 URL을 로드하는 등 더 유연한 설정이 가능합니다.

모델 가져오기
env.py 파일에서 target_metadata 변수를 설정하여 Alembic이 데이터베이스 스키마를 올바르게 감지할 수 있도록 합니다. SQLAlchemy 모델을 정의한 파일(예: models.py)을 가져온 후, 해당 파일의 Base 메타데이터 객체를 target_metadata에 할당합니다.

```python
from myapp.models import Base  # 모델을 정의한 모듈 경로로 변경
target_metadata = Base.metadata
```
마이그레이션 생성
데이터베이스 스키마 변경사항이 있을 때, Alembic을 사용해 새 마이그레이션을 생성합니다. -m 플래그는 마이그레이션에 대한 설명을 추가합니다.

detect changes and create new migration file
file wiil be saved in alembic/versions directory
```bash
alembic revision --autogenerate -m "설명"
```

마이그레이션 적용
다음 명령을 사용하여 최신 마이그레이션을 데이터베이스에 적용합니다:

bash
Copy code
alembic upgrade head
head는 마이그레이션 체인에서 가장 최근의 마이그레이션을 가리킵니다. 이 명령은 모든 새 마이그레이션을 순차적으로 데이터베이스에 적용합니다.

마이그레이션 내역 확인
데이터베이스에 적용된 마이그레이션 내역을 확인하고 싶다면, 다음 명령을 사용할 수 있습니다:

bash
Copy code
alembic history
이 명령은 적용된 마이그레이션의 리스트와 함께 각 마이그레이션의 버전 식별자와 설명을 출력합니다.

마이그레이션 되돌리기
특정 마이그레이션으로 되돌리고 싶다면, downgrade 명령을 사용합니다. 예를 들어, 한 단계 되돌리고 싶다면:

bash
Copy code
alembic downgrade -1
위 예제와 같이, -1은 마지막으로 적용된 마이그레이션을 되돌립니다. 특정 마이그레이션 버전으로 되돌리고 싶다면, 해당 버전의 식별자를 사용합니다.

Alembic을 사용하면 데이터베이스 스키마의 버전 관리와 마이그레이션 관리가 용이해져, 여러 개발 환경에서의 일관성 유지 및 변경 사항의 적용과 추적이 효과적으로 이루어질 수 있습니다.
