"""
WSGI config for team_creator project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'team_creator.settings')

application = get_wsgi_application()

#application = get_wsgi_application()
#application = WhiteNoise(application, root='/team_creator/v_ball/static/files')
#application.add_files('/path/to/more/static/files', prefix='more-files/')
