{
    "name": "Portal Attendance Sync",
    "version": "18.0.1.0.5",  # Sube la versión para forzar actualización profunda
    "category": "Human Resources",
    "depends": ["hr_attendance", "portal"],
    "data": [
        "security/security.xml",
        "views/portal_templates.xml",
    ],
    "installable": True,
    "license": "LGPL-3",
}
