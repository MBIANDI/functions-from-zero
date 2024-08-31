[![Python application test with Github Actions](https://github.com/MBIANDI/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/MBIANDI/functions-from-zero/actions/workflows/main.yml)

# To call Microservice
Execute this:
'''bash
curl -X 'POST' \
  'https://noahgift-functions-from-zero-r7g59wcxx6x-8080.githubpreview.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'
'''
