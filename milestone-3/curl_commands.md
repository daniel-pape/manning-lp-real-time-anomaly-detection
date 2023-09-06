```bash
curl -X 'POST' \
  'http://0.0.0.0:8000/prediction' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "feature_vector": [
    0.0, 1.0
  ],
  "is_score": true
}'
```

```bash
curl -X 'POST' \
  'http://0.0.0.0:8000/prediction' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "feature_vector": [
    0.0, 1.0
  ],
  "is_score": false
}'
```

```bash
curl -X 'GET' \
  'http://0.0.0.0:8000/model_information' \
  -H 'accept: application/json'
```
