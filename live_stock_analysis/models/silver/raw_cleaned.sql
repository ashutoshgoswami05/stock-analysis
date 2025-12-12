


select 

round(stock_current_price,2) as stock_current_price ,
round(stock_diff_open_prev_close,2) as stock_diff_open_prev_close,
round(stock_day_high,2) as stock_day_high,
round(stock_day_low,2) as stock_day_low,
round(stock_day_open,2) as stock_day_open,
round(stock_prev_close,2) as stock_prev_close,
round(stock_percentage_change,2) as stock_percentage_change,
fetched_at_timestamp,
cast(fetched_at_timestamp as date) as trade_date,
greatest(stock_day_high-stock_day_low,abs(stock_day_high-stock_prev_close),abs(stock_day_low-stock_prev_close)) as True_Range,
stock_name,
close_price


from 
(
select *,
LEAD(stock_prev_close) OVER (PARTITION BY stock_name ORDER BY fetched_at_timestamp DESC) AS close_price   

from {{ ref('raw_ingestion') }}

)