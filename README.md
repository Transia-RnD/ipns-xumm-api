# Cloud Build Server

## ADD GOOGLE ENV TO LOCAL ENV

```
export GOOGLE_APPLICATION_CREDENTIALS="$(dirname $(dirname $(pwd)))/env/.env.dev.firestore.json"
```

## Running API

* `cd stack/server` from the base directory
* `poetry install`
* Add the GOOGLE APP & GMAIL APP CREDENTIALS
* Run the service with `poetry run python3 -m server`

`APP_ENV=config.DevelopmentConfig poetry run python3 -m server`

## Testing API

From the project directory, run

```
./test.sh
source .venv/bin/activate \
&& APP_ENV=config.TestConfig poetry run python3 server/test.py \
&& pip3 freeze > requirements.txt
```

## Linting

We enforce linting on the code with flake8. Run with `flake8 common` from the project root.

## Generating Open API

#### [SERVER] PY

`swagger-codegen generate -c server/swagger/config.json -i server/swagger/latest.yaml -l python-flask -o . -Dmodels`


#### [SDK] PY

`swagger-codegen generate -c server/swagger/config.json -i server/swagger/latest.yaml -l typescript-axios -o ../../libs/sdk-ts`