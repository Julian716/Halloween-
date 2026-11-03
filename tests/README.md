# Pruebas unitarias

Desde la carpeta principal del proyecto, instala las dependencias y ejecuta:

```sh
python -m pip install -r requirements.txt
python -m pytest tests -v
```

Las pruebas usan `pytest`, incluido en `requirements.txt`. No requieren
un servidor MySQL ni variables de entorno: la consulta de monstruos se simula
con la fixture `monkeypatch` de pytest.

`test_app.py` contiene dos pruebas:

- `test_index_displays_monsters`: comprueba que la página principal responde
  con estado 200 y muestra el nombre y el poder de un monstruo.
- `test_index_fails_intentionally`: espera un estado 404 aunque la página
  devuelve 200. Falla a propósito para demostrar el bloqueo del despliegue.

GitHub Actions ejecuta todas las pruebas en el trabajo `check`. El trabajo
`deploy` depende de que `check` termine correctamente. Si cualquier prueba
falla, no se llama al hook de Render. Para habilitar de nuevo el despliegue,
corrige la expectativa de la prueba intencional a 200 o elimina esa prueba.

Para ejecutar las pruebas en local, utiliza `python -m pytest` desde la carpeta
del proyecto.
