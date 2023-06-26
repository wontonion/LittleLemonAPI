# add following code in your settings.py at the project level
# projectname/settings.py

REST_FRAMEWORK={
    'DEFAULT_FILTER_BACKENDS':[
        'rest_framework.filter.OrderingFilter',
        'rest_framework.filter.SearchFilter',
    ],
    'DEAFAULT_AUTHENTICATION_CLASSES':(
        # be careful that here are the normal parenthesess
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS' : 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2
}