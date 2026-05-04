## 🚀 Prompt extendido para generación de Dockerfile en bioinformática

> Usa este prompt como plantilla actualizada para crear nuevos `Dockerfile` de herramientas bioinformáticas, incorporando casos particulares y variaciones por lenguaje.

---

### 🛠 Instrucciones generales

1. **Imagen base**

   * **C/C++ o shell-based**: `ubuntu:22.04`
   * **Python**: `python:X.Y-slim` (por ejemplo, `python:3.13-slim`)
   * **Java**: `openjdk:11-jre-slim` (o superior según requisito)

2. **Metadata con **\`\`** (en inglés)**

   ```dockerfile
   LABEL maintainer="Daniel Romero-Guzmán <danirg9993@gmail.com>"
   LABEL version="${TOOLNAME}_VERSION"
   LABEL description="<ToolName> - Brief description in English"
   LABEL source="<Repository or documentation URL>"
   LABEL bioinfo.category="<category in English>"
   LABEL bioinfo.subcategory="<subcategory in English>"
   ```

3. **Variables de entorno**

   ```dockerfile
   ENV <TOOLNAME>_VERSION=<exact version>
   ENV DEBIAN_FRONTEND=noninteractive
   ```

   **Nota:** reemplaza `<TOOLNAME>` por el nombre de la herramienta en mayúsculas (por ejemplo, `FASTP_VERSION`, `CUTADAPT_VERSION`). Siempre usa la variable con el nombre exacto de la herramienta.

4. **Instalación y limpieza**

   * Combina dependencias y build en un mismo bloque `RUN`:

     ```dockerfile
     RUN apt-get update -y && \
         apt-get install -y --no-install-recommends <build-packages> && \
         <installation commands> && \
         apt-get purge -y <build-packages> && \
         apt-get autoremove -y && \
         apt-get clean && \
         rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache
     ```
   * **Python tools**:

     ```dockerfile
     RUN pip install --no-cache-dir <package>==${TOOLNAME}_VERSION && \
         rm -rf /root/.cache /tmp/*
     ```

5. **Directorio de trabajo y ejecución**

   ```dockerfile
   WORKDIR /data
   ENTRYPOINT ["<main_command>"]
   ```

   * Para herramientas que necesiten argumentos por defecto editables, usa `CMD` en lugar de `ENTRYPOINT`.

---

### 🐍 Variaciones por lenguaje / tipo de herramienta

* **C/C++ (Make/CMake)**: base `ubuntu:22.04`. Si requiere compilación intensiva, considera multi-stage builds.
* **Python**: base `python:X.Y-slim`, añade `ENV PIP_NO_CACHE_DIR=1`, limpia caches.
* **Java**: base `openjdk:11-jre-slim`, ejecuta JAR con:

  ```dockerfile
  ENTRYPOINT ["sh","-c","java -jar /opt/<tool>/$(<TOOLNAME>_VERSION)/<tool>.jar"]
  ```
* **Binarios precompilados**: solo si compilar no es viable (por errores conocidos), se permite usar binarios directos. Descarga tarball/binary, extrae en `/opt/<tool>`, crea enlace en `/usr/local/bin`.

---

### 🔧 Compilación desde fuente y limpieza estricta

* **Descarga por defecto** con `git clone`:

  ```dockerfile
  git clone --branch v${TOOLNAME}_VERSION https://github.com/org/repo.git
  ```

* **Alternativa** con `wget` si no hay repositorio Git o etiquetas de versión:

  ```dockerfile
  wget <URL>.tar.gz
  ```

* **Instalación mínima**:
  Solo paquetes indispensables como `make`, `gcc`, `cmake`, `g++`, `ca-certificates`, etc.

---

### 🛠️ Elección del sistema de compilación

Antes de compilar, revisa el contenido del repositorio fuente:

| Si contiene...           | Usa...                             |
|--------------------------|-------------------------------------|
| `CMakeLists.txt`         | ✅ CMake (preferido)                |
| `Makefile`               | ✅ GNU Make                         |
| `meson.build`            | ⚠️ Meson + Ninja *(solo si necesario)* |
| `configure` / `autogen.sh` | ⚠️ Autotools *(evitar si es posible)* |

Si el programa proviene de GitHub revisar el lenguaje de programación principal para escoger el compilador correcto: gcc para C, g++ para C++, o cambiar la base de la imagen para python, Java o R.
---

### 🧱 Compilación con **CMake** (convención moderna recomendada)

```dockerfile
RUN apt-get update && apt-get install -y --no-install-recommends \
    git cmake g++ ca-certificates <otros-pkgs> && \
    git clone --branch ${TOOLNAME_VERSION} <repo> /tmp/<tool> && \
    cd /tmp/<tool> && \
    cmake -B build && \
    cmake --build build && \
    cmake --install build --prefix /usr/local && \
    apt-get purge -y git cmake g++ ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache
```

> 🔹 Este método evita el uso de `cd build` y permite un flujo limpio y reproducible.

---

### 🔨 Compilación con **Make**

```dockerfile
RUN apt-get update && apt-get install -y --no-install-recommends \
    git make g++ ca-certificates <otros-pkgs> && \
    git clone --branch ${TOOLNAME_VERSION} <repo> /tmp/<tool> && \
    cd /tmp/<tool> && \
    make && \
    cp <binario> /usr/local/bin/ && \
    apt-get purge -y git make g++ ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache
```

> 🔹 Usa `make` solo si no existe `CMakeLists.txt`. Asegúrate de copiar manualmente los binarios resultantes.

---

### 🎯 Buenas prácticas

* **Tamaño mínimo**: combina pasos, usa `--no-install-recommends`, elimina caches.
* **Reproducibilidad**: fija versiones exactas y usa tags o ramas específicas.
* **Seguridad**: evita paquetes innecesarios, limpia credenciales y caches.
