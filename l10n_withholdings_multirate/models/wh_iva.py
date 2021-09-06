# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountWhIvaLineTax(models.Model):
    _inherit = 'account.wh.iva.line.tax'

    def converted_amount(self, amount):
        amount_converted = super().converted_amount(amount)
        if self.move_id.use_custom_rate():
            rate = self.move_id.get_custom_rate()
            amount_converted = amount * rate
        return amount_converted


class AccountWhIva(models.Model):
    _inherit = "account.wh.iva"

    @api.model
    def converted_amount(self, line, amount):
        amount_converted = super().converted_amount(line, amount)
        if line.invoice_id.use_custom_rate():
            rate = line.invoice_id.get_custom_rate()
            amount_converted = amount / rate
        return amount_converted
