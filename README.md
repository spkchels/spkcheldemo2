# spkcheldemo2

Sample repository for Snowflake Parquet integration demos.

## Structure

```
├── data/sample-parquet/    # Sample parquet generation script
├── sql/                    # Snowflake SQL scripts
│   ├── 01-create-stage.sql
│   └── 02-create-external-table.sql
└── README.md
```

## Quick Start

1. Run the parquet generator to create sample files
2. Upload to your S3 bucket
3. Execute the SQL scripts in order against your Snowflake account
