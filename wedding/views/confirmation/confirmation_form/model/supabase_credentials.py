import os

import reflex as rx
from dotenv import load_dotenv

load_dotenv()


class SupabaseCredentials(rx.Base):
    supabase_url: str = os.environ.get("SUPABASE_URL")
    supabase_key: str = os.environ.get("SUPABASE_KEY")
