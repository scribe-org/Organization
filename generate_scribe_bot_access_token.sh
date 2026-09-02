curl -XPOST https://matrix.org/_matrix/client/v3/login -H 'Content-Type: application/json' -d '{
    "type": "m.login.password",
    "identifier": { "type": "m.id.user", "user": "scribe_bot" },
    "password": "REPLACE_WITH_SCRIBE_BOT_ELEMENT_PASSWORD",
    "device_id": "SCRIBE_CI",
    "initial_device_display_name": "Scribe CI"
}'
