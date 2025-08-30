from __future__ import annotations

from langchain_core.documents import Document

from data_utils import Movie
from retrieval import config


def create_docs_to_embedd(movies: list[Movie], config: config.RetrievalExpsConfig) -> list[Document]:
    """
    Convierte una lista de objetos `Movie` a una lista the objetos `Document`(usada por Langchain).
    En esta función se decide que parte de los datos será usado como embeddings y que parte como metadata.
    """
    movies_as_docs = []
    for movie in movies:
        content = config.text_to_embed_fn(movie)
        metadata = movie.model_dump()
        doc = Document(page_content=content, metadata=metadata)
        movies_as_docs.append(doc)

    return movies_as_docs


## Posibles funciones para usar como `text_to_embed_fn` en `RetrievalExpsConfig` ##
# retrieval/indexing_pipeline_utils.py

def get_synopsys_txt(movie):
    """
    Esta función toma un objeto 'Movie' y devuelve un texto con la sinopsis
    de la película. Este texto se usará para generar el embedding.
    """
    # Suponiendo que 'movie' tiene un atributo 'synopsis' con la sinopsis de la película
    return movie.synopsis


def get_synopsys_txt(movie: Movie) -> str:
    return movie.synopsis

# def ...
