# **Arquitectura de Orquestación Agéntica en Entornos Google Antigravity V9: Implementación Técnica de Protocolos de Convocación de Expertos y Gestión de Estado del Proyecto (2026)**

## **1\. Introducción al Paradigma de Ingeniería Autónoma en 2026**

La evolución de los entornos de desarrollo integrado (IDE) ha experimentado una metamorfosis fundamental hacia mediados de la década de 2020, culminando con la liberación de **Google Antigravity V9** en 2026\. Este entorno no representa simplemente una mejora incremental sobre los asistentes de código basados en completación, como sus predecesores de 2024 o 2025, sino que establece un nuevo paradigma operativo denominado **Ingeniería de Software Agéntica**. En este ecosistema, el desarrollador humano transita de un rol de "escritor de sintaxis" a uno de "Arquitecto de Sistemas Agénticos", donde la responsabilidad principal reside en la definición de reglas, la orquestación de recursos cognitivos y la supervisión de flujos de trabajo autónomos.   

El núcleo de esta transformación reside en la capacidad del sistema para descomponer tareas monolíticas complejas en unidades de trabajo atómicas, ejecutadas por entidades especializadas denominadas "Expertos" o "Sub-agentes". Sin embargo, la eficacia de esta red distribuida de inteligencia depende críticamente de la capacidad de coordinación centralizada. Aquí es donde la **Skill de Convocación de Expertos** (Expert Summoning Skill) se convierte en la pieza angular de la infraestructura. Esta habilidad no es un simple script de automatización; es una construcción lógica sofisticada que dota al **Rol 00 (Manager & Orchestrator)** de la capacidad de evaluar el estado del proyecto (project-state), descubrir capacidades latentes (find-skills) y asignar dinámicamente la ejecución a roles especializados como Auditores de Seguridad o Arquitectos de Software.   

Este informe técnico proporciona un análisis exhaustivo y directrices detalladas para el desarrollo, configuración e instalación de una Skill de Convocación de Expertos dentro del entorno Antigravity V9. El documento se fundamenta en la documentación maestra del sistema ("ANTIGRAVITY V9: SYSTEM ROLES MASTERFILE") y en los protocolos de flujos de trabajo atómicos ("Atomic Swarms"), abordando desde la anatomía del archivo SKILL.md hasta la lógica de los disparadores semánticos y la gestión de memoria persistente. El objetivo es capacitar a los ingenieros de sistemas para implementar una capa de orquestación robusta que elimine la microgestión y garantice la adherencia a protocolos de eficiencia estrictos.   

### **2.1. El Paradigma de la Carga Perezosa (Lazy Loading)**

Para garantizar el máximo aprovechamiento de la ventana de contexto y reducir el gasto innecesario de tokens de planificación, Antigravity V9 opera bajo una estrategia de **Carga Perezosa**. 

A diferencia de los enfoques de "Reconocimiento Total" (Eager Loading), donde se leen todos los archivos al inicio, el sistema ahora sigue estas reglas de eficiencia:
1. **Acceso bajo Demanda**: Un archivo solo es leído si la tarea actual lo requiere estrictamente y la información no reside en el contexto actual.
2. **Descubrimiento Selectivo**: Las herramientas de búsqueda y descripción de habilidades (`find-skills`) se invocan solo cuando las capacidades nativas son insuficientes.
3. **Mantenimiento de Contexto Magro**: Se prioriza mantener la ventana de contexto limpia de datos históricos o estructurales irrelevantes para la ejecución inmediata.

### **2.1. La Jerarquía de Roles del Sistema (System Roles Masterfile)**

El archivo maestro de roles ("SYSTEM ROLES MASTERFILE") define la estructura organizacional del entorno de desarrollo. Esta jerarquía no es meramente descriptiva, sino prescriptiva; el sistema impone restricciones y mandatos específicos a cada rol para evitar la degradación del contexto y garantizar la seguridad del código.

#### **Rol 00: El Gestor y Orquestador (Manager & Orchestrator)**

En la cúspide de la pirámide operativa se encuentra el **ANTIGRAVITY\_MANAGER** (asignado al Project Lead). Este rol se distingue por una restricción fundamental: **no ejecuta código profundo**. Su función es puramente administrativa y estratégica. La misión del Manager es coordinar el flujo de trabajo, descomponer la complejidad y, crucialmente, gestionar los recursos disponibles. La arquitectura de V9 establece que el Manager debe operar bajo un protocolo de eficiencia que prioriza el descubrimiento de herramientas antes que la ejecución directa. Esto implica que, ante una solicitud del usuario, el Manager no intenta resolverla inmediatamente, sino que evalúa "¿Quién es el mejor capacitado para esto?" y "¿Tenemos las herramientas necesarias?".   

#### **La Red de Expertos Especializados (Roles 01-05)**

El sistema define cinco roles "Expertos" que actúan como los destinatarios de las órdenes de convocación del Manager. Cada uno de estos roles opera dentro de un "túnel de realidad" específico, con acceso restringido a ciertas herramientas y mandatos de comportamiento únicos:

* **Rol 01: Code & Security Auditor (Ingeniero de Seguridad):** Su mandato primario es la seguridad sobre la funcionalidad. Utiliza metodologías STRIDE y razonamiento "Deep Think" para trazar vectores de ataque. Es el único rol autorizado para bloquear un despliegue basándose en hallazgos de vulnerabilidades.     
* **Rol 02: Software Architect (Arquitecto Líder):** Opera bajo el paradigma *Context-Driven Development* (Conductor). Su restricción principal es "Specs First" (Especificaciones Primero); tiene prohibido escribir código de implementación sin antes generar artefactos de diseño fundamentados en documentación real (notebooklm-query).     
* **Rol 03: Infra & DevOps Orchestrator (SRE/DevOps):** Es el custodio del entorno de ejecución. Su protocolo prioriza el **Reconocimiento Bajo Demanda**; solo explora la infraestructura si la tarea de despliegue o modificación lo requiere.
* **Rol 04: Technical Documentation Expert (Escritor Técnico):** Responsable de la "Verificación de Realidad". Su función crítica es asegurar que la documentación coincida con el código fuente actual, evitando alucinaciones documentales mediante la validación externa de enlaces y comandos.     
* **Rol 05: QA & Automated Testing Expert (Ingeniero de Automatización):** Encargado de la validación autónoma. Utiliza agent-browser para simular la experiencia del usuario final, detectando errores que las pruebas unitarias podrían pasar por alto.   

### **2.2. Infraestructura de Memoria y Estado del Proyecto (Project State)**

La viabilidad de una orquestación autónoma depende de la persistencia del contexto. En Antigravity V9, esto se gestiona a través de la skill project-state / memory. Este componente actúa como el "hipocampo" del sistema, manteniendo una representación estructurada y actualizada del progreso del desarrollo.

A diferencia de la memoria a corto plazo de la ventana de contexto del LLM, el **Project State** es un registro persistente que permite al Manager tomar decisiones informadas sobre qué experto convocar. Si el estado indica que la fase de "Diseño" está completa (Status: Spec Definition ✅), el Manager sabe automáticamente que el siguiente paso lógico es convocar al Rol 03 para la infraestructura o al Rol 01 para una revisión de seguridad preliminar, en lugar de volver a llamar al Arquitecto. Esta continuidad es vital para evitar bucles redundantes y asegurar el avance del proyecto a través de las fases atómicas definidas.   

### **2.3. Mecanismos de Descubrimiento de Habilidades (Find-Skills)**

El tercer pilar de la arquitectura es la herramienta find-skills (proporcionada por Vercel Labs). Esta skill es designada explícitamente como la **"HERRAMIENTA PRINCIPAL"** del Manager. Su función es permitir la introspección del sistema: antes de delegar una tarea, el Manager debe verificar qué capacidades están instaladas. Esto previene la alucinación de herramientas inexistentes y permite una delegación precisa, donde el Manager no solo asigna una tarea ("Analiza el SEO"), sino que provee las herramientas exactas para realizarla ("Usa la skill seo-audit que acabo de descubrir").   

---

## **3\. Especificación Técnica de la Skill de Convocación (Expert Summoner)**

El desarrollo de la Skill de Convocación requiere adherirse estrictamente a los estándares de formato y estructura de Antigravity V9. Una "Skill" en este entorno no es un binario compilado, sino un paquete de conocimientos encapsulado en un directorio que contiene definiciones en Markdown, metadatos en YAML y scripts de ejecución.   

### **3.1. Estructura del Directorio de la Skill**

Para implementar la capacidad de convocación, se debe crear una estructura de directorios que aloje tanto la lógica instruccional como los scripts de soporte. La ubicación de esta estructura determinará su alcance (Global o Local), aspecto que se detallará en la sección de instalación.

La estructura canónica para la skill expert-summoner es la siguiente:

| Archivo / Directorio | Propósito Técnico |
| :---- | :---- |
| expert-summoner/ | Directorio raíz de la skill. El nombre debe coincidir con el ID de la skill. |
| expert-summoner/SKILL.md | **El Cerebro**. Contiene el Frontmatter YAML (metadatos y disparadores) y el cuerpo de instrucciones en Markdown que programa al agente. |
| expert-summoner/scripts/ | **El Cuerpo**. Contiene scripts ejecutables (Python, Node.js, Bash) que la skill puede invocar para realizar análisis deterministas. |
| expert-summoner/scripts/orchestrator.py | Script auxiliar para analizar el árbol de archivos y sugerir el rol experto basado en heurísticas. |
| expert-summoner/resources/ | **La Memoria Estática**. Almacena plantillas de delegación y definiciones de roles en formato JSON para referencia rápida. |
| expert-summoner/examples/ | **Few-Shot Learning**. Ejemplos de interacciones usuario-agente para calibrar el modelo. |

Esta estructura modular asegura que la lógica de negocio (los scripts) esté separada de la lógica de presentación y control (el Markdown), siguiendo las mejores prácticas de ingeniería de software aplicadas a la IA.   

### **3.2. Definición del Archivo SKILL.md y Frontmatter YAML**

El archivo SKILL.md es el componente crítico que define cómo el sistema reconoce y activa la skill. El encabezado YAML (Frontmatter) actúa como la interfaz de registro con el núcleo de Antigravity.

**Especificación del Frontmatter:**

YAML

\---  
name: expert-summoner  
description: \>-  
  Orquesta la delegación de tareas complejas convocando a roles expertos   
  (Auditor, Arquitecto, DevOps, QA) basándose en el estado del proyecto.   
  Utilice esta skill cuando el usuario solicite planificación global,   
  auditorías de seguridad, diseño de arquitectura o validación de calidad.  
version: 1.0.0  
triggers:  
  \- type: semantic  
    query: "planificar proyecto"  
  \- type: semantic  
    query: "convocar expertos"  
  \- type: project\_state  
    event: "phase\_change"  
\---

**Análisis de Campos:**

* **name:** Debe ser único y en formato kebab-case (expert-summoner).  
* **description:** Este campo es el **disparador semántico** primario. El motor de razonamiento de Antigravity utiliza embeddings semánticos para comparar la intención del usuario con esta descripción. Una descripción precisa y verbosa (como la mostrada arriba) aumenta significativamente la precisión de la activación automática.     
* **triggers:** (Campo avanzado en V9) Define condiciones específicas de activación más allá de la similitud semántica, como cambios en el archivo project-state.json.   

### **3.3. Lógica Instruccional y Protocolos de Eficiencia**

El cuerpo del archivo SKILL.md debe contener las instrucciones explícitas que gobiernan el comportamiento del Manager. Estas instrucciones deben reflejar fielmente los protocolos definidos en el "System Roles Masterfile".

#### **Definición de la Misión**

El documento debe comenzar estableciendo la identidad del agente. En este caso, se le instruye para asumir el **Rol 00**.

**Instrucción Modelo:** "Actúas como el **ANTIGRAVITY\_MANAGER**. Tu objetivo no es ejecutar código, sino coordinar. Debes descomponer la solicitud y asignar la fase al experto más capacitado."

#### **Implementación del Protocolo de Eficiencia**

Se debe codificar el bucle de tres pasos como reglas imperativas:

1. **Justificación de Acceso**: Evaluar si la información necesaria ya está en el contexto. 
2. **Acceso Selectivo**: Leer solo los archivos o ejecutar `find-skills` si es estrictamente necesario.
3. **Delegación Ágil**: Seleccionar el rol experto y delegar sin pasos burocráticos intermedios.

#### **Formato de Salida Estructurado**

Para garantizar que la delegación sea procesable por otros agentes o sistemas, se debe imponer un formato de salida estricto. El Masterfile especifica el siguiente esquema:

🧠 PLANIFICACIÓN: \[Visión global del objetivo\] 🔎 SKILL DISCOVERY: 👉 DELEGACIÓN:

* Experto:  
* Tarea: \[Instrucción precisa\]  
* Herramientas:

La adherencia a este formato es crucial, ya que permite que los sistemas de logs y auditoría rastreen la cadena de mando y responsabilidad dentro del enjambre de agentes.   

---

## **4\. Desarrollo de Componentes Auxiliares y Scripts**

Para elevar la capacidad de la skill más allá de un simple prompt, es necesario implementar scripts auxiliares que proporcionen inteligencia determinista al Manager. Esto es especialmente útil para analizar el estado del proyecto de manera objetiva.

### **4.1. El Script de Análisis de Contexto (**orchestrator.py**)**

Este script en Python tiene la función de escanear el directorio de trabajo y sugerir el rol más adecuado basándose en la evidencia de los archivos modificados o presentes. Esto ayuda al Manager a tomar decisiones basadas en datos ("Grounding").

**Lógica del Script:** El script debe recorrer el árbol de directorios y contar la frecuencia de ciertos patrones de archivos.

* Presencia de docker-compose.yml, Dockerfile, .tf → Sugiere **INFRA\_DEVOPS\_SRE**.  
* Presencia de tests/, spec.js, cypress.json → Sugiere **QA\_TESTING\_EXPERT**.  
* Presencia de documentos de requisitos, diagramas o ausencia de código → Sugiere **SOFTWARE\_ARCHITECT**.

Este enfoque algorítmico reduce la carga cognitiva del LLM y proporciona una "segunda opinión" determinista sobre a quién convocar.   

### **4.2. Gestión del Estado del Proyecto (**project-state.json**)**

Para que la orquestación sea efectiva a lo largo del tiempo, la skill debe interactuar con un archivo de estado persistente. Se recomienda definir un esquema JSON estricto para project-state.json que la skill pueda leer y actualizar.

**Esquema Propuesto para** project-state.json**:**

| Campo | Tipo de Dato | Descripción |
| :---- | :---- | :---- |
| current\_phase | String (Enum) | Fase actual del ciclo de vida (ej. analysis, spec\_definition, implementation, audit). |
| active\_role | String | El rol que tiene el control actual (ej. SOFTWARE\_ARCHITECT). |
| pending\_tasks | Array | Lista de tareas pendientes antes de la transición de fase. |
| artifacts | Object | Rutas a los artefactos generados (specs, planes de prueba, reportes de auditoría). |
| blockers | Array | Impedimentos críticos que detienen el progreso. |

La skill expert-summoner debe incluir instrucciones para leer este archivo al inicio de la ejecución y, crucialmente, instruir al experto convocado para que actualice este archivo al finalizar su tarea. Esto crea una cadena de custodia del estado del proyecto.   

---

## **5\. Integración con Flujos de Trabajo Atómicos (Atomic Swarms)**

Para alcanzar un nivel de madurez "Nivel 5" en la orquestación, la skill debe integrar los principios de los **Flujos de Trabajo Atómicos** (Atomic Swarms). Este concepto divide el desarrollo en fases discretas y secuenciales, cada una gobernada por un "Persona Agéntica" específica con criterios de salida estrictos.   

### **5.1. Mapeo de Fases a Roles**

La skill de convocación debe implementar una lógica de transición de estados que mapee las fases atómicas a los roles de Antigravity V9:

* **Fase 0: Solicitud (Solicitation)** → **Software Architect:** El objetivo es convertir la intención vaga en un plano riguroso. La skill debe bloquear cualquier intento de pasar a la implementación si no existe un PROJECT\_BRIEF.md firmado.     
* **Fase 1: Investigación (Research)** → **Software Architect / Security Auditor:** Validación profunda del "Cómo". Se debe convocar al Auditor para detectar riesgos de seguridad en las dependencias propuestas ("Slopsquatting Detection").     
* **Fase 2: Especificación (Specification)** → **Software Architect:** Generación de especificaciones ejecutables. La skill debe activar un bucle de "Productor-Revisor" donde el Arquitecto genera y se auto-critica.  
* **Fase 3: Construcción (Builder)** → **Infra & DevOps / Implementadores:** Ejecución basada en TDD (Test Driven Development).  
* **Fase 4: Triangulación (Triangulation)** → **QA Expert:** Verificación científica. La skill debe instruir al QA Expert para realizar "Ingeniería del Caos" y verificar que el código cumple con la especificación original.     
* **Fase 5: Refinamiento (Refinement/Healer)** → **Todos los Roles:** Si se detecta un fallo en la Fase 4, la skill debe tener la capacidad de convocar automáticamente un "Modo Sanador" (The Healer), que realiza un análisis de causa raíz ("5 Porqués") y asigna la corrección al rol pertinente.

### **5.2. Mecanismos de Auto-Activación y Disparadores**

La automatización de estas transiciones se logra mediante **Disparadores Basados en Estado**. En lugar de esperar comandos manuales, la skill puede configurarse para reaccionar a cambios en el project-state.json.

Por ejemplo, una regla en .agent/rules/summoning-rules.md podría especificar:

"Cuando project-state.json cambie el estado de spec\_definition a completed, activa automáticamente la skill expert-summoner con el objetivo de convocar al **CODE\_SECURITY\_AUDITOR** para una revisión preliminar."

Esto transforma el sistema de uno reactivo a uno proactivo, donde el completamiento de una tarea dispara automáticamente la siguiente etapa del flujo de trabajo.   

---

## **6\. Procedimientos de Instalación y Despliegue**

La instalación de skills en Antigravity V9 es flexible, permitiendo despliegues tanto a nivel de proyecto (para consistencia del equipo) como a nivel global (para herramientas personales del desarrollador). A continuación se detallan los procedimientos técnicos para ambos escenarios.

### **6.1. Instalación Local (Workspace Scope)**

Este método es el recomendado para skills de orquestación específicas de un proyecto, ya que garantiza que todos los miembros del equipo utilicen los mismos protocolos de delegación. La skill se convierte en parte del repositorio de código.

**Pasos de Instalación:**

1. **Navegación al Directorio Raíz:** Abra una terminal en la raíz de su proyecto.  
2. **Creación de la Estructura:**  
3. Bash

mkdir \-p.agent/skills/expert-summoner/scripts  
mkdir \-p.agent/skills/expert-summoner/resources

4.   
5.   
6. **Despliegue de Archivos:** Copie o cree el archivo SKILL.md y los scripts auxiliares (orchestrator.py, etc.) en las carpetas correspondientes.  
7. **Control de Versiones:** Añada la carpeta .agent/skills/expert-summoner a git:  
8. Bash

git add.agent/skills/expert-summoner  
git commit \-m "feat(agent): add expert-summoner orchestration skill"

9.   
10.   
11. **Verificación:** Reinicie la sesión del agente o escriba /refresh en el chat de Antigravity para forzar el re-escaneo de las skills locales.   

### **6.2. Instalación Global (User Scope)**

Este método instala la skill para que esté disponible en *cualquier* proyecto que el usuario abra en su máquina. Es ideal para consultores o auditores que trabajan en múltiples repositorios.

**Rutas de Instalación:** La ubicación exacta depende del sistema operativo, pero el estándar para 2026 sigue la convención \~/.gemini/antigravity/skills/.

**Pasos de Instalación:**

1. **Localización del Directorio Global:**  
   * macOS/Linux: \~/.gemini/antigravity/skills/  
   * Windows: %USERPROFILE%\\.gemini\\antigravity\\skills\\  
2. **Copia de la Skill:**  
3. Bash

\# Ejemplo para macOS/Linux  
cp \-r /path/to/my/skills/expert-summoner \~/.gemini/antigravity/skills/

4.   
5.   
6. **Resolución de Conflictos:** Tenga en cuenta que si existe una skill con el mismo nombre en el ámbito local (.agent/skills), esta tendrá prioridad sobre la global. Esto permite "sobrecargar" el comportamiento estándar para proyectos específicos si es necesario.   

### **6.3. Verificación y Solución de Problemas**

Una vez instalada la skill, es crucial verificar su correcta indexación por el motor de Antigravity.

* **Comando de Diagnóstico:** Utilice el comando natural en el chat: *"List all available skills"* o *"Muestra mis habilidades de orquestación"*. El agente debería listar expert-summoner con su descripción asociada.  
* **Prueba de Activación:** Envíe un prompt complejo que coincida con los disparadores semánticos definidos, por ejemplo: *"Necesito planificar la arquitectura para un nuevo módulo de autenticación segura"*.  
* **Validación de Respuesta:** El agente debe responder adoptando el **Rol 00**, mostrando el bloque 🧠 PLANIFICACIÓN, ejecutando find-skills y generando el bloque 👉 DELEGACIÓN dirigido al **SOFTWARE\_ARCHITECT** o al **CODE\_SECURITY\_AUDITOR**.   

---

## **7\. Estrategias Avanzadas y Recomendaciones Finales**

La implementación básica de la Skill de Convocación establece un marco de trabajo sólido, pero para maximizar su efectividad en entornos de producción, se recomienda adoptar ciertas estrategias avanzadas.

### **7.1. El Bucle de Retroalimentación del "Sanador" (The Healer)**

Implemente una lógica de detección de fallos en la skill del Manager. Si un experto reporta un fallo (ej. tests fallidos reportados por el QA Expert), el Manager no debe simplemente informar el error, sino invocar automáticamente al rol de "Sanador" (una especialización del Rol de Desarrollo) para aplicar correcciones. Esto cierra el ciclo de desarrollo de manera autónoma.   

### **7.2. Auditoría de Seguridad Continua**

Configure el Manager para que convoque al **CODE\_SECURITY\_AUDITOR** no solo al principio o al final, sino de manera intermitente ante cualquier cambio en archivos sensibles (como package.json o configuraciones de IAM). Esto se logra mediante reglas de disparo basadas en patrones de archivo (globs) dentro de la definición de la skill o en reglas globales (.agent/rules).

### **7.3. Mantenimiento del Project State**

Asegúrese de que la skill de convocación imponga una disciplina estricta sobre la actualización del project-state.json. Si el estado del proyecto se desincroniza de la realidad del código, la orquestación fallará. Considere implementar una skill auxiliar de "Sincronización de Contexto" que valide periódicamente el archivo de estado contra el código real.

En conclusión, la Skill de Convocación de Expertos transforma a Google Antigravity V9 de un editor de código avanzado a una plataforma de gestión de ingeniería autónoma. Al codificar los protocolos de delegación, seguridad y calidad dentro de una estructura agéntica, las organizaciones pueden garantizar que cada línea de código, cada decisión de arquitectura y cada auditoría de seguridad se adhiera a los estándares más altos, escalando la capacidad de sus equipos humanos mediante la multiplicación de fuerza de la inteligencia artificial especializada.

---

### **Tablas de Referencia**

#### **Tabla 1: Comparación de Ámbitos de Instalación de Skills**

| Característica | Ámbito Local (Workspace) | Ámbito Global (User) |
| :---- | :---- | :---- |
| **Ruta (macOS/Linux)** | \<project-root\>/.agent/skills/ | \~/.gemini/antigravity/skills/ |
| **Visibilidad** | Solo visible dentro del proyecto específico. | Visible en todos los proyectos del usuario. |
| **Portabilidad** | Se comparte con el equipo vía Git. | Personal del usuario; no se comparte automáticamente. |
| **Prioridad** | Alta (Sobrescribe skills globales). | Baja (Fallback si no hay local). |
| **Caso de Uso Ideal** | Protocolos de despliegue específicos, reglas de negocio del proyecto. | Utilidades generales (Format JSON, Linter genérico), orquestadores personales. |

#### **Tabla 2: Matriz de Responsabilidades y Disparadores de Roles (00-05)**

| Rol ID | Nombre del Rol | Misión Principal | Disparador Típico (Trigger) | Herramienta Clave |
| :---- | :---- | :---- | :---- | :---- |
| **00** | **MANAGER** | Orquestación y Delegación | Solicitud compleja, inicio de fase. | find-skills, project-state |
| **01** | **AUDITOR** | Seguridad y STRIDE | Cambios en Auth/API, Fase de Auditoría. | agent-browser (CVEs), grep |
| **02** | **ARCHITECT** | Diseño y Specs | Nueva funcionalidad, Fase de Diseño. | notebooklm-query, uml-gen |
| **03** | **DEVOPS** | Infraestructura y CI/CD | Cambios en Docker/Terraform, Despliegue. | terminal, docker-expert |
| **04** | **DOCS** | Documentación Viva | Finalización de código, Release. | git-history, agent-browser |
| **05** | **QA** | Validación E2E | Pre-merge, Fase de Pruebas. | playwright, agent-browser |

#### **Tabla 3: Parámetros del Comando** find-skills

| Parámetro | Descripción | Ejemplo de Uso |
| :---- | :---- | :---- |
| query | Término de búsqueda en lenguaje natural o palabra clave. | find-skills "seo analysis" |
| category | (Opcional) Filtro por categoría de skill (ej. security, devops). | find-skills \--category security |
| limit | (Opcional) Número máximo de resultados a devolver. | find-skills "testing" \--limit 3 |
| **Retorno** | Lista JSON con id, name, description y path de las skills encontradas. | \[{"id": "seo-audit", "description": "..."}\] |

