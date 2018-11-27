from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Transactions"),
			"items": [
					{
							"type": "doctype",
							"name": "Warehouse Order"
					},
					{
							"type": "doctype",
							"name": "Receive"
					},
					{
							"type": "doctype",
							"name": "Release"
					},
					{
							"type": "doctype",
							"name": "Picking"
					},
					{
							"type": "doctype",
							"name": "Packing"
					},
					{
							"type": "doctype",
							"name": "Other Jobs"
					},
			]
		},
		{
			"label": _("Billing and Inventory"),
			"items": [
					{
							"type": "doctype",
							"name": "Periodic Billing"
					},
					{
							"type": "doctype",
							"name": "Inventory Count"
					},
					{
							"type": "doctype",
							"name": "Transfers"
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
							"name": "Warehouse Settings"
					},			
					{
							"type": "doctype",
							"name": "Areas"
					},
					{
							"type": "doctype",
							"name": "Carton Group"
					},
					{
							"type": "doctype",
							"name": "Carton Size"
					},
					{
							"type": "doctype",
							"name": "Location Types"
					},
					{
							"type": "doctype",
							"name": "Item"
					},
					{
							"type": "doctype",
							"name": "Locations"
					},
					{
							"type": "doctype",
							"name": "Pick Faces"
					},
					{
							"type": "doctype",
							"name": "Product Styles"
					},
					{
							"type": "doctype",
							"name": "Products"
					},
					{
							"type": "doctype",
							"name": "Warehouse"
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
