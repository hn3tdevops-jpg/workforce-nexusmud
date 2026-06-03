import os
import re

def fix_file(path):
    with open(path, 'r') as f:
        content = f.read()
    
    original_content = content
    
    # Identify import style
    has_from_datetime_datetime = re.search(r'from datetime import datetime', content)
    has_import_datetime = re.search(r'^import datetime$', content, re.MULTILINE)
    
    if has_from_datetime_datetime:
        # Ensure UTC is imported
        if not re.search(r'from datetime import .*UTC', content):
            content = re.sub(r'from datetime import datetime', 'from datetime import datetime, UTC', content)
        
        # Replace calls
        content = content.replace('datetime.utcnow()', 'datetime.now(UTC)')
        # Replace callable references (like in SQLAlchemy defaults)
        # We use a lambda to keep it a callable
        content = re.sub(r'(?<!\.)datetime\.utcnow(?!\()', 'lambda: datetime.now(UTC)', content)
        
    elif has_import_datetime:
        # Replace calls
        content = content.replace('datetime.datetime.utcnow()', 'datetime.datetime.now(datetime.UTC)')
        # Replace callable references
        content = re.sub(r'datetime\.datetime\.utcnow(?!\()', 'lambda: datetime.datetime.now(datetime.UTC)', content)
        
    if content != original_content:
        with open(path, 'w') as f:
            f.write(content)
        return True
    return False

def main():
    base_dir = '/home/workspace/workforce-dev'
    count = 0
    for root, dirs, files in os.walk(base_dir):
        if '.venv' in dirs:
            dirs.remove('.venv')
        for file in files:
            if file.endswith('.py'):
                path = os.path.join(root, file)
                if fix_file(path):
                    print(f"Fixed: {path}")
                    count += 1
    print(f"Total files fixed: {count}")

if __name__ == '__main__':
    main()
