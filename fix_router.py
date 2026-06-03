with open("/home/workspace/workforce-backup/apps/api/app/api/router.py", "r") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line.strip() == "from apps.api.app.api.v1.endpoints.notifications import router as notifications_router" or \
       line.strip() == "from apps.api.app.api.v1.endpoints.maintenance import router as maintenance_router" or \
       line.strip() == "app.include_router(maintenance_router, prefix=\"/maintenance\", tags=[\"maintenance\"])" or \
       line.strip() == "app.include_router(notifications_router, prefix=\"/notifications\", tags=[\"notifications\"])":
        continue
    
    new_lines.append(line)
    
    if "from apps.api.app.api.v1.endpoints.messaging import router as messaging_router" in line:
        new_lines.append("    from apps.api.app.api.v1.endpoints.notifications import router as notifications_router\n")
        new_lines.append("    from apps.api.app.api.v1.endpoints.maintenance import router as maintenance_router\n")
    
    if "app.include_router(messaging_router, prefix=\"/messaging\", tags=[\"messaging\"])" in line:
        new_lines.append("    app.include_router(maintenance_router, prefix=\"/maintenance\", tags=[\"maintenance\"])\n")
        new_lines.append("    app.include_router(notifications_router, prefix=\"/notifications\", tags=[\"notifications\"])\n")

with open("/home/workspace/workforce-backup/apps/api/app/api/router.py", "w") as f:
    f.writelines(new_lines)
