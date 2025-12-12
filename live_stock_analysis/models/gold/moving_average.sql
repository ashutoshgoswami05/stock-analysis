select
    stock_name,
    stock_current_price,
    stock_diff_open_prev_close,
    stock_percentage_change,
    (stock_current_price - stock_prev_close) / stock_prev_close AS daily_price_change_percentage,
    close_price,
    fetched_at_timestamp,
    cast(fetched_at_timestamp as date) as trade_date,
    sma20,
    14_day_ATR

from (
    select *,
AVG(close_price) OVER (
    PARTITION BY stock_name
    ORDER BY fetched_at_timestamp DESC
    ROWS BETWEEN 19 PRECEDING AND CURRENT ROW
) AS sma20,

AVG(True_Range) OVER (
    PARTITION BY stock_name
    ORDER BY fetched_at_timestamp DESC
    ROWS BETWEEN 13 PRECEDING AND CURRENT ROW
) AS day14_atr

    FROM {{ ref('raw_cleaned') }}
)

    

