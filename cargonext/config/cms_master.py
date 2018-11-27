from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Organizations"),
			"items": [
					{
							"type": "doctype",
							"name": "Customer"
					},
					{
							"type": "doctype",
							"name": "Supplier"
					},
					{
							"type": "doctype",
							"name": "Shipper"
					},
					{
							"type": "doctype",
							"name": "Consignee"
					},
			]
		},
		{
			"label": _("Reference Files"),
			"items": [
					{
							"type": "doctype",
							"name": "Container Type"
					},
					{
							"type": "doctype",
							"name": "Dangerous Goods"
					},
					{
							"type": "doctype",
							"name": "Equipment"
					},
					{
							"type": "doctype",
							"name": "Package Types"
					},
					{
							"type": "doctype",
							"name": "Job Types"
					},
					{
							"type": "doctype",
							"name": "Service Levels"
					},
					{
							"type": "doctype",
							"name": "Vessels"
					},
			]
		},
		{
			"label": _("Tariff and Rates"),
			"items": [
					{
							"type": "doctype",
							"name": "Rate Class"
					},
					{
							"type": "doctype",
							"name": "Quotation Documents"
					},
			]
		},
		{
			"label": _("Locations"),
			"items": [
					{
							"type": "doctype",
							"name": "Countries"
					},
					{
							"type": "doctype",
							"name": "Cities and Towns"
					},
					{
							"type": "doctype",
							"name": "Domestic Zone Sets"
					},
					{
							"type": "doctype",
							"name": "International Zones"
					},
					{
							"type": "doctype",
							"name": "Post Codes"
					},
					{
							"type": "doctype",
							"name": "Time Zones"
					},
					{
							"type": "doctype",
							"name": "Trade Lanes"
					},
					{
							"type": "doctype",
							"name": "Transit Time"
					},
					{
							"type": "doctype",
							"name": "UNLOCO"
					},
			]
		},
		{
			"label": _("Customs"),
			"items": [
					{
							"type": "doctype",
							"name": "Classification Lookup"
					},
					{
							"type": "doctype",
							"name": "Global Codes"
					},
					{
							"type": "doctype",
							"name": "Global Tariffs"
					},
					{
							"type": "doctype",
							"name": "Packs Conversion"
					},
					{
							"type": "doctype",
							"name": "Item"
					},
					{
							"type": "doctype",
							"name": "Time Zones"
					},
					{
							"type": "doctype",
							"name": "Trade Lanes"
					},
					{
							"type": "doctype",
							"name": "Transit Time"
					},
					{
							"type": "doctype",
							"name": "UNLOCO"
					},
			]
		},
		{
			"label": _("Warehouse"),
			"items": [
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
	]
