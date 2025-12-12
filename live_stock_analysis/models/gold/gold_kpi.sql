SELECT
    stock_name,
    stock_current_price,
    stock_diff_open_prev_close,
    stock_percentage_change,
    stock_prev_close,
    fetched_at_timestamp,
    cast(fetched_at_timestamp as date) as trade_date,
    (stock_current_price - stock_prev_close) / stock_prev_close AS daily_price_change_percentage
FROM (
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY stock_name ORDER BY fetched_at_timestamp DESC) AS rn,

    FROM {{ ref('raw_cleaned') }}

) AS t
WHERE rn = 1
