select 

data:c::float as stock_current_price,
data:d::float as stock_diff_open_prev_close,
data:h::float as stock_day_high,
data:l::float as stock_day_low,
data:o::float as stock_day_open,
data:pc::float as stock_prev_close,
data:dp::float as stock_percentage_change,
data:fetched_at::timestamp as fetched_at_timestamp,
data:symbol::string as stock_name


from 

{{ source('s3_source', 'STOCK_DATA') }}