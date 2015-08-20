# Django React Redux Universal Hot Example
---

This is a starter boiler plate app I've put together using [Django](https://djangoproject.com) and
[Erik Rasmussen's example](https://github.com/erikras/react-redux-universal-hot-example)

## Installation

```
cd frontend
npm install

cd ../backend
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements/development.txt
```

## Running Dev Server

```
cd frontend
npm run dev

# in different terminal
cd backend
./manage.py runserver_plus
```

## Building and Running Production Server

```
cd frontend
npm run build
npm run start
```
