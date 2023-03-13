from elastic_db import es, ELASTIC_INDEX


def get_ids_by_string_from_elastic (req:str):
    """Возвращает список id из базы эластика по введенной строке
       Максимум 20 результатов
    """
    resp = es.search(index=f"{ELASTIC_INDEX}", query={
                                                "regexp": {
                                                            "text": {
                                                            "value": f".*{req}.*",
                                                            }
                                                }
    }, size=1500)

    return [int(hint['_id']) for hint in resp['hits']['hits']]