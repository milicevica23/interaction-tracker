from dagster import Definitions, load_assets_from_modules

from . import assets

from .dbt import dbt_assets
from .constants import dbt

all_assets = load_assets_from_modules([assets])


defs = Definitions(
    assets= [dbt_assets],
    resources={
        "dbt": dbt,
    },
)
