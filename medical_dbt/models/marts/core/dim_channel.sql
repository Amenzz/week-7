

select distinct
  channel_id,
  split_part(filename, '.', 1) as channel_name
from {{ ref('stg_telegram_messages') }}
