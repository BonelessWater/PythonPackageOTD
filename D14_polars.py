'''
Day 14, June 21th 2025: 

Welcome to polars.py!

When pandas is too slow and you hate the thought of any other
language, but python polars is the right choice. Built in Rust 
with a Python API, it's designed for speed, memory efficiency, 
and expressive syntax.
'''

import polars as pl

# Create sample DataFrame
df = pl.DataFrame({
    'product': ['A', 'B', 'C'] * 100, 'sales': range(300), 'region': ['North', 'South'] * 150
})

# Basic operations with method chaining
result = (
    df
    .filter(pl.col('sales') > 100)
    .group_by('product')
    .agg([
        pl.col('sales').mean().alias('avg_sales'),
        pl.col('sales').count().alias('count')
    ])
    .sort('avg_sales', descending=True)
)
print("Grouped results:")
print(result)

# Lazy evaluation for performance
lazy_result = (
    df.lazy()
    .with_columns([
        (pl.col('sales') * 0.1).alias('commission'),
        pl.col('sales').rank().over('region').alias('rank')
    ])
    .filter(pl.col('rank') <= 10).collect()  # Execute the query plan
)
print(f"\nTop performers per region: {lazy_result.shape[0]} rows")

# String operations and expressions
text_df = pl.DataFrame({
    'names': ['john doe', 'JANE SMITH', 'bob jones'],
    'emails': ['JOHN@SITE.COM', 'jane@email.org', 'Bob@Test.Net']
})

cleaned = text_df.with_columns([
    pl.col('names').str.to_titlecase(),
    pl.col('emails').str.to_lowercase()
])
print("\nCleaned text:")
print(cleaned)
