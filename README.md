# Unit Converter

Project url: https://roadmap.sh/projects/unit-converter

A web app to convert between different units of measurement.

## Setup

Clone or download this repo
Have Python 3.6+ installed

## Usage

- Rename `.env_dist` to `.env`
- Add your secret key to the SECRET_KEY variable.  You can create a key with the `secrets` library.
```python
>>> import secrets
>>> secrets.token_hex(16)
'f93998e306275a5cb098bc5bac9712cd'  # Copy this and set it as SECRET_KEY
```

- Run the app
```shell
# With uv
uv run app.py

# With Flask
flask --app app run
```
