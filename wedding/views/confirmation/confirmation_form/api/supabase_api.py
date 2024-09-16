from datetime import datetime
from typing import Dict, List

import httpcore
import httpx
from postgrest.base_request_builder import APIResponse
from supabase import Client, create_client

from wedding.views.confirmation.confirmation_form.model import (
    SupabaseCredentials as Credentials,
)


class SupabaseAPI:
    def __init__(
        self, table: str, credentials: Credentials, supabase_column_names: List[str]
    ) -> None:
        self.supabase: Client = create_client(
            supabase_url=credentials.supabase_url,
            supabase_key=credentials.supabase_key,
        )
        self.table = table
        self.field_names = supabase_column_names

    def query_data(
        self, order: str, column_select: str = "*", limit: int = 5
    ) -> APIResponse:
        query = (
            self.supabase.table(self.table)
            .select(column_select)
            .order(order, desc=True)
            .limit(limit)
            .execute()
        )
        if query.data:
            return query
        else:
            return []

    def _construct_data_dict(self, data: Dict[str, str]) -> Dict[str, str]:
        data_dict = {field: data.get(field, None) for field in self.field_names}
        data_dict["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return data_dict

    def insert_data(self, data_to_supabase: Dict[str, str]) -> None:
        try:
            return (
                self.supabase.table(self.table)
                .insert(self._construct_data_dict(data_to_supabase))
                .execute()
            )
        except (httpx.ConnectError, httpcore.ConnectError) as e:
            print(e)
