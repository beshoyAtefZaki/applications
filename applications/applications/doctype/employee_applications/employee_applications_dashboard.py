from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
                'heatmap': False,		
		'fieldname': 'application',
		'transactions': [
			{
				'label': _('Financial Entry'),
				'items': ['Journal Entry']
			},


		] }
