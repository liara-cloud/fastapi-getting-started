# FastAPI Getting Started
## Installation (Local)
- clone the project:
```
git clone https://github.com/liara-cloud/fastapi-getting-started.git
```

- change directory:
```
cd fastapi-getting-started
```

- install `virtualenv` module:
```
pip install virtualenv
```

- create new virtual environment:
```
python -m venv .venv
```

- activate virtual env:
```
source .venv/Scripts/activate # in Windows: .venv\Scripts\activate
```

- install all dependencies:
```
pip install -r requirements.txt
```

- rename `.env.example` to `.env`
- set Database ENVs in `.env`, for example:
```bash
DB_USER=sa
DB_NAME=my_db
DB_HOST=bromo.liara.cloud
DB_PORT=31858
DB_PASS=yw8FVaUqlvliRFxmcp7VnDUG
```

- run the project:
```
uvicorn sql_app.main:app --reload
```

## Installation (Liara)
- clone the project:
```
git clone https://github.com/liara-cloud/fastapi-getting-started.git
```

- change directory:
```
cd fastapi-getting-started
```

- install Liara/CLI:
```
npm i -g @liara/cli
```

- login to liara:
```
liara login
```

- create a new Docker app:
```
liara app:create
```

- set provided DB_ENVs (on `.env.example` file) into the Liara

- deploy your app on Liara:
```
liara deploy --port 80 --platform docker
```
