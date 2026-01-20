import hashlib
import uuid

def convertir_hash(texto):
    sha256 = hashlib.sha256()
    sha256.update(texto.encode('utf-8'))
    return sha256.hexdigest()

def generar_clave():
    clave = uuid.uuid4().hex[:6]
    return clave