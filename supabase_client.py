"""Shared Supabase client instances."""
from supabase import create_client
from config import SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_SVC_KEY

# Anon client — used for auth (login, signup)
anon_client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

# Service client — used for DB reads/writes server-side
svc_client = create_client(SUPABASE_URL, SUPABASE_SVC_KEY)
