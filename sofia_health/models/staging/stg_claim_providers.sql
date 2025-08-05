{{ config(materialized='view') }}

with source as (
    select * from {{ source('public', 'claim_providers') }}
),

renamed as (
    select
        claim_id,
        provider_id,
        trim(provider_role) as provider_role
    from source
)

select * from renamed
