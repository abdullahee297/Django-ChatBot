<<<<<<< HEAD
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "qrcodegenerator.settings")

=======
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "qrcodegenerator.settings")

>>>>>>> ec58928 (Crash Error Solve)
app = get_wsgi_application()