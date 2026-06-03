from devhub.app import create_app
from devhub.extensions import db
from devhub.models import Project
from devhub.services.planning_queue import create_docs_driven_queue
from pathlib import Path

app = create_app()
with app.app_context():
    project = Project.query.filter_by(slug='workforce-backup').first()
    if not project:
        project = Project.query.first()
    
    source_path = "/home/workspace/Workforce-Docs/planning/HN3T_MASTER_PLAN.md"
    source_text = Path(source_path).read_text()
    
    queue = create_docs_driven_queue(
        project_id=project.id,
        source_text=source_text,
        name="HN3T Master Plan Queue",
        description="Auto-generated from HN3T_MASTER_PLAN.md",
        source_path=source_path
    )
    print(f"Created queue: {queue.name} (ID: {queue.id})")
    print(f"Items: {len(queue.items)}")
