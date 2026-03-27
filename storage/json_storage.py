import json
import os
class JsonStorage:
    """handles JSON file storage operation"""
    def __init__(self, file_path):
        """initialize storage with file path"""
        self.file_path = file_path
    
    def load(self):
        """load data from JSON file"""
        try:
            if not os.path.exists(self.file_path):
                return []
            
            with open(self.file_path, "r") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    return []
            
            return data   
        
        except (json.JSONDecodeError, FileNotFoundError):
            return [] 
    
    def save(self, data):
        """Save data from JSON file"""
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)     
        