"""
Gunicorn configuration file for InstalAlarm production deployment.
"""
import multiprocessing
import os

# Server socket
bind = os.getenv('GUNICORN_BIND', '127.0.0.1:8000')
backlog = 2048

# Worker processes
workers = int(os.getenv('GUNICORN_WORKERS', multiprocessing.cpu_count() * 2 + 1))
worker_class = os.getenv('GUNICORN_WORKER_CLASS', 'sync')
worker_connections = 1000
timeout = 120
keepalive = 5
max_requests = 1000
max_requests_jitter = 50

# Logging
accesslog = os.getenv('GUNICORN_ACCESS_LOG', '-')  # '-' oznacza stdout
errorlog = os.getenv('GUNICORN_ERROR_LOG', '-')
loglevel = os.getenv('GUNICORN_LOG_LEVEL', 'info')
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# Process naming
proc_name = 'instalalarm'

# Server mechanics
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

# SSL (jeśli używasz bezpośrednio w Gunicorn, zwykle przez Nginx)
# keyfile = None
# certfile = None

