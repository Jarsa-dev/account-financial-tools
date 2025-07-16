# Copyright 2018, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class AccountFullReconcile(models.Model):
    _inherit = "account.full.reconcile"

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for rec in records:
            if not rec.exchange_move_id:
                continue
            invoice_moves = rec.reconciled_line_ids.filtered(
                lambda line: line.account_id.reconcile
                and line.journal_id.type in ["sale", "purchase"]
                and line.move_id.move_type in ["in_invoice", "out_invoice"]
            ).mapped("move_id")
            invoice_moves.write(
                {
                    "exchange_move_id": rec.exchange_move_id.id,
                }
            )
        return records
