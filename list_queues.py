from devhub.app import create_app
from devhub.extensions import db
from devhub.services.planning_queue import PlanningQueue

app = create_app()
with app.app_context():
    queues = PlanningQueue.query.all()
    for q in queues:
        print(f"ID: {q.id} | Name: {q.name} | Status: {q.status}")
