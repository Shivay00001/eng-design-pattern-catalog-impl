from typing import Any, Dict

# --- Singleton ---
class SingletonMeta(type):
    _instances: Dict[Any, Any] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self):
        self.status = "Connected"
    
    def query(self, sql):
        return f"Executing {sql}"

# --- Factory Method ---
class Serializer:
    def serialize(self, data):
        raise NotImplementedError

class JsonSerializer(Serializer):
    def serialize(self, data):
        return f"{{ 'data': '{data}' }}"

class XMLSerializer(Serializer):
    def serialize(self, data):
        return f"<data>{data}</data>"

class SerializerFactory:
    @staticmethod
    def get_serializer(format_type):
        if format_type == "json":
            return JsonSerializer()
        elif format_type == "xml":
            return XMLSerializer()
        raise ValueError("Unknown format")
