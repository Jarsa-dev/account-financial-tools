# Copyright 2018, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    exchange_move_ids = fields.One2many(
        "account.move",
        "exchange_origin_move_id",
        string="Currency Exchange Difference Moves",
    )
    exchange_origin_move_id = fields.Many2one(
        "account.move",
        string="Origin Exchange Move",
    )

    def action_currency_rate_diference(self):
        return {
            "name": _("Currency Exchange Difference Move"),
            "view_type": "form",
            "view_mode": "form",
            "res_model": "account.move",
            "domain": [("id", "in", self.exchange_move_id.ids)],
            "type": "ir.actions.act_window",
            "context": {"create": False, "delete": False},
        }
