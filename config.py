import os

SUPABASE_URL      = os.environ['SUPABASE_URL']
SUPABASE_ANON_KEY = os.environ['SUPABASE_ANON_KEY']
SUPABASE_SVC_KEY  = os.environ['SUPABASE_SERVICE_KEY']
ANTHROPIC_KEY     = os.environ.get('ANTHROPIC_API_KEY', '')
SECRET_KEY        = os.environ.get('FLASK_SECRET_KEY', 'dev-secret-change-me')
