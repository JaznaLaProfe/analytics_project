def serializar_documento(documento):

    if documento:
        documento["_id"] = str(documento["_id"])

    return documento

def serializar_lista(documentos):

    return [
        serializar_documento(documento)
        for documento in documentos
    ]