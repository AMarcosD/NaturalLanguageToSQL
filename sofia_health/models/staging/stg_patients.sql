{{ config(materialized='view') }}

with source as (
    select * from {{ source('public', 'patients') }}
),

renamed as (
    select
        patient_id,
        trim(first_name) as first_name,
        trim(last_name) as last_name,
        trim(maternal_surname) as maternal_surname,
        cast(date_of_birth as date) as date_of_birth,
        gender,
        curp,
        street_address,
        city,
        state,
        zip_code,
        email,
        plan_name,
        plan_code,
        policy_number,
        group_id,
        cast(enrollment_date as date) as enrollment_date,
        cast(is_active as boolean) as is_active,
        cast(annual_deductible as numeric) as annual_deductible,
        cast(annual_out_of_pocket_max as numeric) as annual_out_of_pocket_max
    from source
)

select * from renamed
