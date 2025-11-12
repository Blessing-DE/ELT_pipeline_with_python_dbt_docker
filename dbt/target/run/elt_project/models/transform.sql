
  
    

  create  table "elt_db"."public"."transform__dbt_tmp"
  
  
    as
  
  (
    -- models/transform.sql


SELECT
    "Year" AS year,
    "Industry_name_NZSIOC" AS industry,
    "Variable_name" AS variable,
    "Variable_category" AS category,
    "Value"::numeric AS value
FROM public.staging_enterprise
WHERE "Value" IS NOT NULL
  AND "Value" ~ '^[0-9]+(\.[0-9]+)?$'
  );
  