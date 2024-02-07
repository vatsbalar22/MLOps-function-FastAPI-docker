# function-docker

[![Python application test with Github Actions](https://github.com/vatsbalar22/function-docker/actions/workflows/main.yml/badge.svg)](https://github.com/vatsbalar22/function-docker/actions/workflows/main.yml)

## to call microservice 

'''bash
curl -X 'POST' \
  'https://congenial-cod-jj5qxq5vggqr2pvxw-8080.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'

'''