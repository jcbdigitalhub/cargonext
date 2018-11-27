# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Cargonext",
			"color": "blue",
			"icon": "fa fa-ship",
			"type": "module",
			"label": _("Cargonext")
		},
		                {
                        "module_name": "Sea Freight",
                        "color": "blue",
                        "icon": "fa fa-ship",
                        "type": "module",
                        "label": _("Sea Freight")
                },
                {
                        "module_name": "Air Freight",
                        "color": "gray",
                        "icon": "fa fa-plane",
                        "type": "module",
                        "label": _("Air Freight")
                },
                {
                        "module_name": "Customs",
                        "color": "green",
                        "icon": "fa fa-certificate",
                        "type": "module",
                        "label": _("Customs")
                },
		{
			"module_name": "Trucking", 
                        "color": "orange",
                        "icon": "fa fa-truck",
                        "type": "module",
                        "label": _("Trucking")
		},
                {
                        "module_name": "Warehouse",
                        "color": "#DEB887",
                        "icon": "octicon octicon-package",
                        "type": "module",
                        "label": _("Warehouse")
                },
                {
                        "module_name": "CMS Master",
                        "color": "green",
                        "icon": "fa fa-folder-open",
                        "type": "module",
                        "label": _("CMS Master")
                },

	]
