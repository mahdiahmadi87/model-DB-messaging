# model-DB-messaging

login user:
```bash
curl -X POST http://localhost:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{"username": "user1", "password": "password123"}'
```

get unread messages:
```bash
curl -X GET http://localhost:8000/inbox/unread-messages/ \
-H "Authorization: Bearer <ACCESS-TOKEN>"
```

get unread notifications:
```bash
curl -X GET http://localhost:8000/inbox/unread-notifications/ \
-H "Authorization: Bearer <ACCESS-TOKEN>"
```

refresh token:
```bash
curl -X POST http://localhost:8000/api/token/refresh/ \
-H "Content-Type: application/json" \
-d '{"refresh": "<REFRESH-TOKEN>"}'
```