# FastAPI

# INSTALLATION
to set virtual environment for fastapi

```bash
python -m venv fastapienv
```
activate venv

```bash
source fastapienv/Scripts/activate
```
install package

```bash
pip install fastapi
```
install uvicorn for fastapi web server

```bash
pip install "uvicorn[standard]"
```

[standard] includes additional dependencies: `websockets`, `httptools`, `unloop`

to link the fastapi to the database

```bash
pip install sqlalchemy
```

# INDEX

- [Request](/Request/main.py)
- [Validation](/Validation/main.py)
  - [Http Status Codes](/Validation/Status-Codes.md)
- [DataBase](/DataBase)