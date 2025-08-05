{{ config(materialized='view') }}

with source as (
    select * from {{ source('public', 'providers') }}
),

renamed as (
    select
        provider_id,
        trim(provider_name) as provider_name,
        trim(provider_type) as provider_type,
        trim(specialty) as specialty,
        trim(cedula_profesional) as cedula_profesional,
        trim(tax_id) as tax_id,
        trim(street_address) as street_address,
        trim(city) as city,
        trim(state) as state,
        trim(zip_code) as zip_code,
        trim(phone) as phone,
        trim(email) as email,
        trim(network_tier) as network_tier,
        cast(contract_start_date as date) as contract_start_date,
        cast(contract_end_date as date) as contract_end_date,
        cast(is_accepting_patients as boolean) as is_accepting_patients,
        cast(quality_rating as numeric) as quality_rating
    from source
)

select * from renamed
