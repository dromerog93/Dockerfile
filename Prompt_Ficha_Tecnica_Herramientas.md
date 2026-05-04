# 🧭 Prompt para generar una ficha técnica de herramienta bioinformática

> ⚠️ Este prompt define la estructura y los contenidos esperados en una ficha técnica para documentar herramientas bioinformáticas integradas en imágenes Docker.  
> Úsalo como guía para describir de forma clara, homogénea y útil cada herramienta.

---

🔹 **Instrucciones generales:**

Genera una ficha técnica detallada de una herramienta bioinformática siguiendo los siguientes campos. Cada campo debe contener información clara y específica:

---

## 📄 Campos obligatorios:

1. **Versión**  
   - Especifica la versión exacta instalada de la herramienta. Usualmente en `ENV VERSION`
   - Ejemplo: `0.20.0`

2. **Categoría**  
   - Define la categoría funcional general.  
   - Ejemplo: `General`, `Preprocesamiento`

3. **Subcategoría**  
   - Clasificación más específica dentro de la categoría.  
   - Ejemplos: `trimming`, `rRNA-filtering`, `read-merging`

4. **Imagen base**  
   - Indica la imagen de sistema utilizada en el Dockerfile.  
   - Ejemplos: Docker con `Ubuntu 22.04` o `Python 3.13-slim` o `Openjdk 11-slim`

5. **Descripción**  
   - Resumen en 1 o 2 frases sobre qué hace la herramienta y en qué contexto se aplica.

6. **Archivos de entrada**  
   - Tipos de archivo que acepta como entrada, con breve descripción del rol de cada uno.

7. **Archivos de salida**  
    - Tipos de archivo que genera como resultado, explicando su utilidad o contenido.

8. **Documentación oficial**  
   - URL directa al repositorio o página de documentación.

9. **Uso básico**  
   - Comando mínimo funcional con un ejemplo realista y sintácticamente correcto.

10. **Parámetros comunes**  
   - Lista de flags/argumentos más utilizados, con breve descripción de cada uno.

---

✅ La ficha debe facilitar tanto la comprensión como la integración en pipelines. Utiliza tablas donde sea útil (por ejemplo, para los parámetros o tipos de archivo), y asegúrate de que los ejemplos de uso estén probados o basados en la documentación oficial más reciente.
