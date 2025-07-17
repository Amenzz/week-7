

select
  message_id,
  message_date,
  channel_id,
  length(message_text) as message_length,
  has_media
from {{ ref('stg_telegram_messages') }}
