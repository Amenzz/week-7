

select distinct
  message_date::date as date,
  extract(year from message_date) as year,
  extract(month from message_date) as month,
  extract(day from message_date) as day,
  extract(dow from message_date) as weekday
from {{ ref('stg_telegram_messages') }}
