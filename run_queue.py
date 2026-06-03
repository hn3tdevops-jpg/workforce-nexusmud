from devhub.app import create_app
from devhub.extensions import db
from devhub.services.planning_queue import PlanningQueue, approve_queue_item, run_next_item

app = create_app()
with app.app_context():
    q = db.session.get(PlanningQueue, 1)
    
    # Approve the first item (gate)
    item1 = q.items[0]
    print(f"Approving item 1: {item1.title}")
    approve_queue_item(item1, approver="Gemini CLI")
    
    # Run the next item
    print("Running next item...")
    result = run_next_item(q)
    print(f"Result: {result.status} - {result.message}")
