#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from calaccess_raw import models
from .base import BaseAdmin


@admin.register(models.CvrSoCd)
class CvrSoCdAdmin(BaseAdmin):
    list_display = ("filing_id", "amend_id", "rpt_date", "filer_naml", "form_type")
    list_filter = ("form_type",)
    date_hierarchy = "rpt_date"


@admin.register(models.Cvr2SoCd)
class Cvr2SoCdAdmin(BaseAdmin):
    list_display = ("filing_id",  "item_cd", "entity_cd", "enty_naml", "form_type",)
    list_filter = ("form_type", "entity_cd", "off_s_h_cd", "item_cd")


@admin.register(models.CvrCampaignDisclosureCd)
class CvrCampaignDisclosureCdAdmin(BaseAdmin):
    list_display = ("filing_id", "rpt_date", "filer_naml", "cmtte_type", "form_type")
    list_filter = ("cmtte_type", "form_type", "entity_cd",)
    date_hierarchy = "rpt_date"


@admin.register(models.Cvr2CampaignDisclosureCd)
class Cvr2CampaignDisclosureCdAdmin(BaseAdmin):
    list_display = ("filing_id", "enty_naml", "form_type")
    list_filter = ("form_type", "entity_cd",)


@admin.register(models.Cvr3VerificationInfoCd)
class Cvr3VerificationInfoCdAdmin(BaseAdmin):
    list_display = ("filing_id", "sig_date", "sig_naml", "form_type")
    list_filter = ("form_type",)
    date_hierarchy = "sig_date"


@admin.register(models.DebtCd)
class DebtCdAdmin(BaseAdmin):
    list_display = (
        "filing_id",
        "expn_code",
        "payee_naml",
        "amt_incur",
        "amt_paid",
    )
    list_filter = ("entity_cd", "expn_code",)


@admin.register(models.ExpnCd)
class ExpnCdAdmin(BaseAdmin):
    list_display = (
        "filing_id",
        "expn_date",
        "cand_naml",
        "payee_naml",
        "form_type",
        "amount",
    )
    list_filter = ("expn_code", "entity_cd", "form_type",)
    date_hierarchy = "expn_date"


@admin.register(models.LoanCd)
class LoanCdAdmin(BaseAdmin):
    list_display = (
        "filing_id",
        "form_type",
        "loan_date1",
        "loan_type",
        "lndr_naml",
        "loan_amt1",
        "loan_amt2",
        "loan_amt3",
        "loan_amt4"
    )
    list_filter = ("loan_type", "entity_cd", "form_type")
    date_hierarchy = "loan_date1"


@admin.register(models.RcptCd)
class RcptCdAdmin(BaseAdmin):
    list_display = (
        "filing_id",
        "form_type",
        "rcpt_date",
        "ctrib_naml",
        "ctrib_emp",
        "ctrib_occ",
        "amount"
    )
    list_filter = (
        "form_type",
        "entity_cd",
    )
    date_hierarchy = "rcpt_date"


@admin.register(models.S401Cd)
class S401CdAdmin(BaseAdmin):
    list_display = (
        "filing_id",
        "form_type",
        "cand_naml",
        "payee_naml",
        "amount",
    )
    list_filter = (
        "rec_type",
        "form_type",
        "office_cd",
        "juris_cd",
        "off_s_h_cd",
        "sup_opp_cd",
    )


@admin.register(models.F495P2Cd)
class F495P2CdAdmin(BaseAdmin):
    list_display = (
        "filing_id",
        "form_type",
        "elect_date",
        "contribamt"
    )
    list_filter = ("rec_type", "form_type",)
    date_hierarchy = "elect_date"


@admin.register(models.S496Cd)
class S496CdAdmin(BaseAdmin):
    list_display = (
        "filing_id",
        "exp_date",
        "expn_dscr",
        "amount"
    )
    list_filter = (
        "rec_type",
        "form_type",
    )
    date_hierarchy = "exp_date"


@admin.register(models.S497Cd)
class S497CdAdmin(BaseAdmin):
    list_display = (
        "filing_id",
    )


@admin.register(models.S498Cd)
class S498CdAdmin(BaseAdmin):
    pass


@admin.register(models.F501502Cd)
class F501502CdAdmin(BaseAdmin):
    pass


@admin.register(models.BallotMeasuresCd)
class BallotMeasuresCdAdmin(BaseAdmin):
    list_display = ("measure_name", "election_date", "jurisdiction")
    list_filter = ("jurisdiction",)
