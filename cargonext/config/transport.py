from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Transactions"),
			"items": [
					{
							"type": "doctype",
							"name": "Transport Order"
					},
					{
							"type": "doctype",
							"name": "Dispatch"
					},
					{
							"type": "doctype",
							"name": "Other Jobs"
					},
			]
		},
		{
			"label": _("Fleet Management"),
			"items": [
					{
							"type": "doctype",
							"name": "Transport Vehicle"
					},
					{
							"type": "doctype",
							"name": "Trip Ticket"
					},
					{
							"type": "doctype",
							"name": "Vehicle Expense"
					},
			]
		},
		{
			"label": _("Masters"),
			"items": [
					{
							"type": "doctype",
							"name": "Transport Company"
					},
					{
							"type": "doctype",
							"name": "Service Provider"
					},
					{
							"type": "doctype",
							"name": "Transport Driver"
					},
					{
							"type": "doctype",
							"name": "Transport Job Service"
					},
					{
							"type": "doctype",
							"name": "Vehicle Make"
					},
					{
							"type": "doctype",
							"name": "Vehicle Model"
					},
			]
		},
		{
			"label": _("Billing and Maintenance"),
			"items": [
					{
							"type": "doctype",
							"name": "Transport Billing"
					},
					{
							"type": "doctype",
							"name": "Repair Request"
					},
					{
							"type": "doctype",
							"name": "Tool Count"
					},
					{
							"type": "doctype",
							"name": "Adjustment"
					},
			]
		},
		{
			"label": _("Setup"),
			"items": [
					{
							"type": "doctype",
							"name": "Transport Settings"
					},			
					{
							"type": "doctype",
							"name": "Transport Reference Type"
					},
					{
							"type": "doctype",
							"name": "Transport Job Type"
					},
					{
							"type": "doctype",
							"name": "Drop Mode"
					},
					{
							"type": "doctype",
							"name": "Transport Driver Group"
					},
					{
							"type": "doctype",
							"name": "Free Waitinng Time"
					},
					{
							"type": "doctype",
							"name": ""
					},
			]
		},
		{
			"label": _("Reports"),
			"items": [
					{
							"type": "report",
							"name": "Job History Report"
					},
					{
							"type": "report",
							"name": "Stock Balances Report"
					},
					{
							"type": "report",
							"name": "Stock Expiry Report"
					},
					{
							"type": "report",
							"name": "Stock Movement Report"
					},
					{
							"type": "report",
							"name": "Stock Ledger"
					},
					{
							"type": "report",
							"name": "Stock Transaction History"
					},
					{
							"type": "report",
							"name": "Unbilled Transactions Report"
					},
					{
							"type": "report",
							"name": "Warehouse Empty Locations Report"
					},
					{
							"type": "report",
							"name": "Inventory Variance Report"
					},
					{
							"type": "report",
							"name": "Product Listing"
					},
			]
		},
	]
