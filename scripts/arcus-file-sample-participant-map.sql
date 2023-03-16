WITH gf_clean AS (
  SELECT
    kf_id,
    REVERSE(
      SUBSTRING(REVERSE(external_id)
        FROM
        1 for strpos(REVERSE(external_id), '/') -1) -- noqa: PRS
    ) AS file_name,
    external_id
  FROM kfpostgres.genomic_file
  WHERE kf_id != 'GF_3FA9M8KQ'
),

kf_data AS (
  SELECT DISTINCT
    p.kf_id AS participant_id,
    b.kf_id AS sample_id,
    gf.kf_id AS genomic_file_id,
    p.external_id AS research_id,
    b.external_sample_id AS sdg_id,
    b.external_aliquot_id AS aliquot_id,
    file_name,
    gf.external_id
  FROM
    kfpostgres.participant AS p
  JOIN kfpostgres.biospecimen AS b
    ON p.kf_id = b.participant_id
  JOIN kfpostgres.biospecimen_genomic_file AS bgf
    ON bgf.biospecimen_id = b.kf_id
  JOIN gf_clean AS gf
    ON gf.kf_id = bgf.genomic_file_id
)

SELECT
  participant_id,
  sample_id,
  genomic_file_id,
  research_id,
  sdg_id,
  aliquot_id,
  af.file_name
FROM
  kf_data AS kf
JOIN youngnm_dev_schema.arcus_files AS af
  ON af.file_name = kf.file_name;
