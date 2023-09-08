from supabase import create_client, Client
from pydantic import BaseModel
from datetime import datetime
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    URL: str
    KEY: str
    model_config: SettingsConfigDict = SettingsConfigDict(
        env_prefix="SUPABASE_",
    )


# Define the FunctionsData model
class FunctionsData(BaseModel):
    id: int
    uuid: str
    function_name: str
    short_name: str
    short_code: str
    description: str
    created_at: datetime
    updated_at: datetime
    is_function: bool


# Define the FunctionsDataManager class
class FunctionsDataManager:
    def __init__(self):
        settings = Settings()
        self.supabase: Client = create_client(settings.URL, settings.KEY)
        self.query = self.supabase.table("functions_data").select("*")

    def get(self, **kwargs):
        for key, value in kwargs.items():
            self.query.filter(key, "eq", value)
        response = self.query.execute()
        if response.data:
            return FunctionsData(**response.data[0])
        else:
            return None

    def filter(self, **kwargs):
        for key, value in kwargs.items():
            self.query.filter(key, "eq", value)
        return self


# Initialize the Supabase client and the FunctionsDataManager
manager = FunctionsDataManager()
