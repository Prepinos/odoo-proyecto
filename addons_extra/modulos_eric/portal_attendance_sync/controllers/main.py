# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import http
from odoo.http import request


class PortalAttendanceSync(http.Controller):

    @http.route(
        "/portal/attendance/toggle",
        type="http",
        auth="user",
        methods=["POST"],
        website=True,
    )
    def portal_attendance_toggle(self, **post):
        user = request.env.user
        group = "portal_attendance_sync.group_portal_attendance"

        if not (user.has_group(group) and user.employee_id):
            return request.redirect(request.httprequest.referrer or "/my")

        # Ejecución con sudo para evitar restricciones de acceso del portal
        user.employee_id.sudo()._attendance_action_change()

        return request.redirect(request.httprequest.referrer or "/my")


