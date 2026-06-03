from devhub.app import create_app
from devhub.extensions import db
from devhub.services.planning_queue import PlanningQueue, queue_summary

app = create_app()
with app.app_context():
    q = db.session.get(PlanningQueue, 1)
    summary = queue_summary(q)
    print(f"Queue: {summary['name']}")
    for item in summary['items'][:5]:
        print(f"  Item {item['sort_order']}: {item['title']} ({item['item_type']}) - {item['status']} | Approval: {item['approval_state']}")
