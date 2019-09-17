user = {
    "type": "object",
    "required": ["id", "name", "email", "phone", "address", "devices", "contracts", "created_time"],
    "properties": {
        "id": {
            "type": "string"
        },
        "name": {
            "type": "string"
        },
        "email": {
            "type": "string"
        },
        "phone": {
            "type": "string"
        },
        "address": {
            "type": "string"
        },
        "devices": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["sn", "bind_time"],
                "properties": {
                    "sn": {
                        "type": "string"
                    },
                    "bind_time": {
                        "type": "number"
                    }
                }
            }
        },
        "contracts": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "name", "url", "created_time"],
                "properties": {
                    "id": {
                        "type": "string"
                    },
                    "name": {
                        "type": "string"
                    },
                    "url": {
                        "type": "string"
                    },
                    "created_time": {
                        "type": "number"
                    }
                }
            }
        },
        "created_time": {
            "type": "number"
        }
    }
}


