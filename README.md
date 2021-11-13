## fastapi

[FastAPI](https://fastapi.tiangolo.com/) is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
* uses uvicorn as server

### Install

```bash
# Install
pip install fastapi

# uvicorn
pip install "uvicorn[standard]"
```
### Run

```bash
# since I am running in a asdf environment I have to add python
python -m uvicorn main:app --reload

# others could run it straigth or install uvicorn in their .basrc
uvicorn main:app --reload

# main: the file main.py (the Python "module").
# app: the object created inside of main.py with the line app = FastAPI().
# --reload: make the server restart after code changes. Only use for development.
```

* Api is available under http://127.0.0.1:8000/
* swagger api http://127.0.0.1:8000/docs
  * openapi json http://127.0.0.1:8000/openapi.json
* redoc http://127.0.0.1:8000/redoc






   

