# Bronze Layer - Ingest JSON from ADLS
from pyspark.sql.functions import col, to_date, lower
file_path = "abfss://retail@pocretailsacc.dfs.core.windows.net/bronze/nehamahajan09/azure-retail-project/refs/heads/main/retail_transactions_bronze.parquet"
df_bronze.show()
