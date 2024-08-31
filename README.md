[![Python application test with Github Actions](https://github.com/MBIANDI/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/MBIANDI/functions-from-zero/actions/workflows/main.yml)

# To call Microservice
Execute this:
 ```bash
curl -X 'POST' \
  'https://expert-trout-4jg65jrvrwvx2q4j7-8080.app.github.dev/docs' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'
 ```

### Build container

` docker build .`
` docker image ls`

### Run container

` docker run -p 8080 93f7dffea261 `

### Invoke

run `invoke.sh`
