import os
os.system('PYTHONPATH=webapp/ gunicorn -w 4 -b 0.0.0.0:5001 webservice')
