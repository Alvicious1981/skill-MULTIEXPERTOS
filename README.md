# 🧠 Antigravity V9.5 Orchestrator - MULTIEXPERTOS

Este repositorio contiene la infraestructura avanzada para la **Orquestación Agéntica** en entornos Google Antigravity V9.5. Implementa un sistema de múltiples expertos especializados capaces de colaborar de forma autónoma bajo la supervisión de un Agente Manager.

## 🚀 Descripción del Proyecto

El objetivo de este proyecto es dotar al entorno de desarrollo de una **Skill de Convocación de Expertos** (Expert Summoning Skill). Esta habilidad permite descomponer tareas complejas y delegarlas a roles específicos con mandatos y herramientas dedicadas.

## 🏗️ Arquitectura de Roles (V9.5 Matrix)

El sistema opera bajo una jerarquía de roles diseñada para maximizar la eficiencia y la seguridad:

| ID | Rol | Misión Principal |
| :--- | :--- | :--- |
| **00** | **MANAGER** | Estrategia, asignación de recursos y delegación. |
| **01** | **AUDITOR** | Seguridad, análisis STRIDE y validación de vulnerabilidades. |
| **02** | **ARCHITECT** | Diseño de sistemas, especificaciones técnicas y tech stack. |
| **03** | **DEVOPS** | Infraestructura, CI/CD y despliegue. |
| **04** | **DOCS** | Documentación técnica y referencia de API. |
| **05** | **QA** | Pruebas E2E, Unitarias e Ingeniería del Caos. |
| **06** | **DB_EXPERT** | Esquemas de base de datos y optimización SQL. |
| **07** | **UI/UX** | Diseño de interfaz, experiencia de usuario y accesibilidad. |
| **08** | **API_ENGINEER** | Lógica de backend e integración de microservicios. |
| **09** | **MOBILE** | Implementación de clientes móviles. |
| **10** | **DATA_SCIENTIST** | Análisis de datos y modelos de ML. |

## 🛠️ Estructura del Repositorio

- `.agent/skills/antigravity-orchestrator/`: Contiene la lógica semántica y disparadores de la skill.
  - `SKILL.md`: Definición del cerebro de orquestación.
  - `rules.md`: Reglas operativas y protocolos de debate.
  - `scripts/`: Scripts deterministas como `orchestrator.py`.
- `setup_antigravity.md`: Guía maestra detallada sobre el paradigma agéntico 2026.
- `project-state.json`: Registro persistente del progreso y fases del proyecto.

## 📋 Protocolos Críticos

### 1. Consejo de Expertos (Council of Experts)
Para tareas con **Complejidad > 8** o riesgos de seguridad, el Manager convoca simultáneamente al **ARCHITECT (02)** y al **AUDITOR (01)** para un proceso de debate y consenso antes de la implementación.

### 2. Mock First (Desacoplamiento)
Se prioriza la creación de mocks antes de la integración con servicios reales (Stripe, AWS, Supabase) para garantizar la velocidad de desarrollo en las fases iniciales.

### 3. Protocolo "The Healer" (Sanador)
Ante errores de ejecución, el sistema activa automáticamente un análisis de causa raíz antes de reportar al usuario, intentando auto-corregir problemas comunes.

## 🚦 Cómo Empezar

1.  **Explorar Skills**: Usa `find-skills` para que Antigravity indexe las nuevas capacidades.
2.  **Solicitar Planificación**: Inicia una tarea con "Planifica el proyecto..." para activar al Manager (Rol 00).
3.  **Monitorear Estado**: El archivo `project-state.json` reflejará el avance de cada experto.

---
*Generado por Antigravity V9 - 2026*
