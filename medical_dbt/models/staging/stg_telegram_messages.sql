-- models/staging/stg_telegram_messages.sql

with source as (
  select 
    data::jsonb as message_json,
    filename,
    inserted_at
  from raw.telegram_messages
),

cleaned as (
  select
    (message_json ->> 'id')::int as message_id,
    (message_json ->> 'message') as message_text,
    (message_json ->> 'date')::timestamp as message_date,
    (message_json ->> 'peer_id') as channel_id,
    (message_json ->> 'media') is not null as has_media,
    filename,
    inserted_at
  from source
)

select * from cleaned
