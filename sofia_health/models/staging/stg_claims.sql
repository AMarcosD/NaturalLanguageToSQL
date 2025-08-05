{{ config(materialized='view') }}

with source as (
    select * from {{ source('public', 'claims') }}
),

renamed as (
    select
        claim_id,
        patient_id,
        cast(service_date as date) as service_date,
        cast(claim_submitted_date as date) as claim_submitted_date,
        trim(claim_type) as claim_type,
        trim(place_of_service) as place_of_service,
        diagnosis_codes,
        diagnosis_descriptions,
        procedure_codes,
        procedure_descriptions,
        cast(billed_amount as numeric) as billed_amount,
        cast(allowed_amount as numeric) as allowed_amount,
        cast(deductible_amount as numeric) as deductible_amount,
        cast(coinsurance_amount as numeric) as coinsurance_amount,
        cast(copay_amount as numeric) as copay_amount,
        cast(insurance_paid_amount as numeric) as insurance_paid_amount,
        cast(patient_responsibility as numeric) as patient_responsibility,
        trim(claim_status) as claim_status,
        trim(denial_reason) as denial_reason,
        cast(is_in_network as boolean) as is_in_network,
        trim(network_tier) as network_tier,
        trim(prior_auth_number) as prior_auth_number,
        cast(processed_date as date) as processed_date
    from source
)

select * from renamed
