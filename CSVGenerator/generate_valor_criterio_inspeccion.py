import pandas as pd

# Load the excel or csv files
areas = pd.read_csv("AreaCriterioInspeccion_Version2.csv")  # or pd.read_excel(...)
opciones = pd.read_csv("OpcionCriterioInspeccion_Version2.csv")
valores = pd.read_csv("ValorCriterioInspeccion_Version2.csv")  # This may be empty or partial

# Prepare a dataframe with all possible combinations
all_criterios = opciones['CriterioInspeccionId'].unique()
all_areas = areas['AreaCriterioInspeccionId'].unique()

# Create a list of all combinations (opcion, area, criterio)
combinations = []
for _, op_row in opciones.iterrows():
    for area_id in all_areas:
        combinations.append({
            'OpcionCriterioInspeccionId': op_row['OpcionCriterioInspeccionId'],
            'AreaCriterioInspeccionId': area_id,
            'CriterioInspeccionId': op_row['CriterioInspeccionId'],
            'Activo': op_row['Activo'] if 'Activo' in op_row else True
        })

all_combos_df = pd.DataFrame(combinations)

# Merge with existing values if provided
if not valores.empty:
    # Only merge on the relevant columns
    merged = pd.merge(all_combos_df, valores[['OpcionCriterioInspeccionId', 'AreaCriterioInspeccionId', 'Valor', 'CriterioInspeccionId']], 
                      on=['OpcionCriterioInspeccionId', 'AreaCriterioInspeccionId', 'CriterioInspeccionId'], how='left')
    result = merged
else:
    result = all_combos_df
    result['Valor'] = ""

# Assign sequential ValorCriterioInspeccionId
result = result.reset_index(drop=True)
result['ValorCriterioInspeccionId'] = result.index + 1

# Reorder columns
result = result[['ValorCriterioInspeccionId', 'OpcionCriterioInspeccionId', 'AreaCriterioInspeccionId', 'Valor', 'CriterioInspeccionId', 'Activo']]

# Save to CSV
result.to_csv("ValorCriterioInspeccion_COMPLETO.csv", index=False)

print("ValorCriterioInspeccion_COMPLETO.csv generated successfully.")