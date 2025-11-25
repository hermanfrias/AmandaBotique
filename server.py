from waitress import serve
from AmandaProjecto.wsgi import application  # Cambia 'your_project_name'

serve(application, host='192.168.1.193', port=8000)