# retrieval/retrieval_pipeline_utils.py

import re
def clean_query_txt(query: str) -> str:
  """
    Esta función toma la query de entrada y la limpia para su posterior procesamiento.
    Puede incluir eliminación de caracteres especiales, conversión a minúsculas, etc.
    """
    query = query.lower()  # Convertir a minúsculas
    query = re.sub(r'[^a-zA-Z0-9\s]', '', query)  # Eliminar caracteres no alfanuméricos
    return query
