"""Generate sample parquet files for demo purposes."""
import pyarrow as pa
import pyarrow.parquet as pq
import random
from datetime import datetime, timedelta

def generate_sample_data(num_rows=10000):
    """Generate sample transaction data."""
    base_date = datetime(2024, 1, 1)
    
    data = {
        'transaction_id': list(range(1, num_rows + 1)),
        'customer_id': [random.randint(1000, 9999) for _ in range(num_rows)],
        'amount': [round(random.uniform(1.0, 5000.0), 2) for _ in range(num_rows)],
        'currency': [random.choice(['AUD', 'USD', 'GBP', 'EUR']) for _ in range(num_rows)],
        'transaction_date': [(base_date + timedelta(days=random.randint(0, 365))).isoformat() for _ in range(num_rows)],
        'category': [random.choice(['retail', 'online', 'atm', 'transfer', 'payment']) for _ in range(num_rows)],
        'status': [random.choice(['approved', 'declined', 'pending']) for _ in range(num_rows)],
    }
    
    table = pa.table(data)
    return table

if __name__ == '__main__':
    for i in range(3):
        table = generate_sample_data(num_rows=10000)
        filename = f'transactions_batch_{i:03d}.snappy.parquet'
        pq.write_table(table, filename, compression='snappy')
        print(f'Generated: {filename} ({table.num_rows} rows)')
