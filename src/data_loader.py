import json
from pathlib import Path

def load_json(file_path: str):
    file_path = Path(file_path)
    
    if file_path.exists():
        file_content = file_path.read_text()
        try:
            data = json.loads(file_content)
        except json.JSONDecodeError as e:
            print(f"JSONDecodeError: {e}")
            # If multiple JSON objects are expected, handle them accordingly
            data = []
            for line in file_content.strip().split('\n'):
                try:
                    data.append(json.loads(line))
                except json.JSONDecodeError as line_error:
                    print(f"Line JSONDecodeError: {line_error}")

        return data
    else:
        print("File does not exist.")
        return None
