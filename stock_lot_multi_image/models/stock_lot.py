# Copyright (C) 2025 Cetmix OÜ
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class StockLot(models.Model):
    _name = "stock.lot"
    _inherit = ["stock.lot", "base_multi_image.owner"]

    image = fields.Image(compute="_compute_image")

    @api.depends("image_ids")
    def _compute_image(self):
        """
        Compute main image of lots
        """
        for lot in self:
            lot.image = (
                lot.image_ids
                and lot.with_context(bin_size=False).image_ids[0].image_1920
                or False
            )
