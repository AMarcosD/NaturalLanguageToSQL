## ESTE ARCHIVO SOLO CORRESPONDE A DOCUMENTACION DEL PASO A PASO MIENTRAS SE REALIZABA EL DESARROLLO

BDD PostgreSQL 
1 - Descargar e instalar PostgreSQL (v15)
2 - Creamos BDD sofia_health
3 - Creamos usuario para DBT con un grant 
    CREATE USER dbt_user WITH PASSWORD 'dbt_pass';
    GRANT ALL PRIVILEGES ON DATABASE sofia_health TO dbt_user;
    GRANT USAGE ON SCHEMA public TO dbt_user;
    GRANT CREATE ON SCHEMA public TO dbt_user;


DBT
1 - Creamos VENV para aislar depencencias (Buenas prácticas)
    python -m venv venv 
    .\venv\Scripts\activate
2 - instalacion dbt-postgres (pip install dbt-postgres) (posee conector con postgres)
3 - Creamos proyecto y estructura (dbt init sofia_health)
    [
        host (hostname for the instance): localhost
        port [5432]: 5433
        user (dev username): dbt_user
        pass (dev password): 
        dbname (default database that dbt will build objects in): sofia_health
        schema (default schema that dbt will build objects in): public
        threads (1 or more) [1]: 4
    ]

DATA -> PostgreSQL
1 - Creamos Bases de datos en postgres 
-- Tabla: patients
CREATE TABLE patients (
    patient_id TEXT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    maternal_surname TEXT,
    date_of_birth DATE,
    gender TEXT,
    curp TEXT,
    street_address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    email TEXT,
    plan_name TEXT,
    plan_code TEXT,
    policy_number TEXT,
    group_id TEXT,
    enrollment_date DATE,
    is_active BOOLEAN,
    annual_deductible NUMERIC,
    annual_out_of_pocket_max NUMERIC
);

-- Tabla: providers
CREATE TABLE providers (
    provider_id TEXT PRIMARY KEY,
    provider_name TEXT,
    provider_type TEXT,
    specialty TEXT,
    cedula_profesional TEXT,
    tax_id TEXT,
    street_address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    phone TEXT,
    email TEXT,
    network_tier TEXT,
    contract_start_date DATE,
    contract_end_date DATE,
    is_accepting_patients BOOLEAN,
    quality_rating NUMERIC
);

-- Tabla: claims
CREATE TABLE claims (
    claim_id TEXT PRIMARY KEY,
    patient_id TEXT,
    service_date DATE,
    claim_submitted_date DATE,
    claim_type TEXT,
    place_of_service TEXT,
    diagnosis_codes TEXT,
    diagnosis_descriptions TEXT,
    procedure_codes TEXT,
    procedure_descriptions TEXT,
    billed_amount NUMERIC,
    allowed_amount NUMERIC,
    deductible_amount NUMERIC,
    coinsurance_amount NUMERIC,
    copay_amount NUMERIC,
    insurance_paid_amount NUMERIC,
    patient_responsibility NUMERIC,
    claim_status TEXT,
    denial_reason TEXT,
    is_in_network BOOLEAN,
    network_tier TEXT,
    prior_auth_number TEXT,
    processed_date DATE,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

-- Tabla: claim_providers
CREATE TABLE claim_providers (
    claim_id TEXT,
    provider_id TEXT,
    provider_role TEXT,
    PRIMARY KEY (claim_id, provider_id),
    FOREIGN KEY (claim_id) REFERENCES claims(claim_id),
    FOREIGN KEY (provider_id) REFERENCES providers(provider_id)
);
COPY patients FROM 'C:\\Users\\marco\\Desktop\\desafio_sofia\\data\\patients.csv' DELIMITER ',' CSV HEADER;
COPY providers FROM 'C:\\Users\\marco\\Desktop\\desafio_sofia\\data\\providers.csv' DELIMITER ',' CSV HEADER;
COPY claims FROM 'C:\\Users\\marco\\Desktop\\desafio_sofia\\data\\claims.csv' DELIMITER ',' CSV HEADER;
COPY claim_providers FROM 'C:\\Users\\marco\\Desktop\\desafio_sofia\\data\\claim_providers.csv' DELIMITER ',' CSV HEADER;

4 - Alimentamos models/staging/schema.yml con los sources y la metadata de las tablas de forma detallada para luego ser consumida por LLM
5 - Creamos las vistas (models/staging/stg_*)
5 - dbt docs generate (sitio estatico con documentacion)
    dbt docs serve (servidor local con la documentacion)
6 - Generamos archivo ask_claims.py e instalamos las siguientes librerias google-generativeai psycopg2-binary python-dotenv
7 - Necesitamos un resumen del schema para reducir costos. Se generó un script (generate_schema_summary.py)
8 - A partir de 
