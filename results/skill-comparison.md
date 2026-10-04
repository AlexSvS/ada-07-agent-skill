# Skill comparison
|        Dimensiones       |                                                                                                    Mi skill                                                                                                   |                                                                   Skill profesional                                                                   |                                                               Conclusión                                                              |
|:------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------:|
| Trigger / routing        | Está orientado a identificar cuándo una solicitud corresponde a una revisión de Pull Request, especialmente para evaluar si está lista para revisión/aprobación humana.                                       | Está orientado a una revisión de calidad de código mediante cinco ejes: correctness, readability, architecture, security y performance.               | Complementarios: mi skill tiene un routing más enfocado en PR readiness; el profesional en code quality.                              |
| Scope / boundaries       | Define un alcance amplio sobre el PR: requisitos, criterios de aceptación, especificación, tareas, implementación, tests y trazabilidad. También distingue problemas obligatorios, recomendados y opcionales. | Se concentra más en la calidad técnica del cambio: código, arquitectura, seguridad, rendimiento y mantenibilidad.                                     | Mi skill tiene límites de proceso más claros, mientras que el profesional profundiza más en la calidad técnica.                       |
| Workflow depth           | Sigue una secuencia de contexto → requirements/AC → evidencia de tests → findings → open questions → verdict. Está muy alineado con el ciclo SDD.                                                             | Utiliza gates de calidad, sizing/cohesión, evaluación de cinco ejes, findings por severidad, remedios estructurales, verification story y checklist.  | El profesional tiene mayor profundidad de revisión técnica, mientras que mi skill tiene mejor integración con el flujo SDD.           |
| Correctness              | Evalúa si los requisitos nuevos están respaldados por SPEC, TASKS, implementación y tests. Detectó la regresión de __version__.                                                                               | Evalúa directamente si el cambio funciona y si rompe comportamiento existente. Detectó el mismo test fallido y la ausencia de tests para FR-07–FR-09. | Empate en los problemas encontrados; el profesional lo formula como un quality gate técnico más explícito.                            |
| Architecture             | Da mucho peso a la consistencia REQUIREMENTS → SPEC → TASKS → Implementation → Test → Traceability.                                                                                                           | Interpreta la arquitectura también desde el desacoplamiento, cohesión y consistencia del cambio, pero incorpora el SDD como parte de la arquitectura. | Mi skill es más fuerte en trazabilidad SDD; el profesional tiene una visión arquitectónica más general.                               |
| Security                 | No es uno de sus ejes principales; la revisión se concentra principalmente en requirements, trazabilidad y readiness.                                                                                         | Tiene un eje específico de Security. Considera validación de entrada, posibles inyecciones, datos externos, autenticación y límites de confianza.     | Ventaja clara del skill profesional para revisiones de seguridad.                                                                     |
| Performance              | No constituye un eje central de la evaluación. Puede detectar problemas si afectan requisitos o tests, pero no realiza un análisis específico.                                                                | Tiene un eje dedicado a performance y relaciona FR-08 con el costo potencial de ordenar resultados y con NFR-01.                                      | Ventaja del profesional, aunque parte del análisis de performance/pagination parece algo excesivo para este CLI local.                |
| Tests / verification     | Usa los tests como evidencia de readiness: ejecuta pytest, identifica regresiones y verifica si existen pruebas para los nuevos requisitos.                                                                   | Además de revisar tests, incorpora una verification story y gates de tests/build/manual verification/spec alignment/traceability.                     | El profesional tiene un modelo de verificación más completo; mi skill está más enfocado en evidencia suficiente para aprobar el PR.   |
| Severity model           | Utiliza MUST FIX → SHOULD FIX → OPTIONAL, con findings RF-01–RF-05.                                                                                                                                           | Utiliza Critical → Required → Consider → Nit.                                                                                                         | Ambos permiten priorización. El profesional ofrece una jerarquía más granular, mientras que mi modelo es más sencillo y accionable.   |
| Human review             | Termina explícitamente con “NOT READY FOR HUMAN REVIEW / APPROVAL” y plantea preguntas abiertas que requieren decisión humana.                                                                                | Termina con “REQUEST CHANGES (BLOCKED)” y también identifica decisiones que requieren intervención humana.                                            | Ambos preservan el juicio humano. Mi skill separa mejor las preguntas abiertas; el profesional hace más fuerte el gate de aprobación. |
| References / composition | Integra varios artefactos del proyecto: AGENTS.md, REQUIREMENTS.md, SPEC.md, TASKS.md, implementación, tests y docs/traceability.md.                                                                          | Combina contexto del PR con cinco dimensiones de calidad y una estructura de findings/remedios/verificación.                                          | Mi skill compone mejor información específica del proyecto; el profesional compone mejor criterios generales de calidad de software.  |
| Reusability              | Muy reutilizable para proyectos que utilizan SDD/specifications y PRs, pero algunas evaluaciones dependen de estructuras como SPEC/TASKS/traceability.                                                        | Más reutilizable entre diferentes proyectos porque sus cinco ejes son aplicables incluso sin SDD.                                                     | El profesional es más generalizable; mi skill es más especializado y útil cuando existe un workflow SDD.                              |

# Professional Skill Study — ADA-07
## Source
Repository: https://github.com/addyosmani/agent-skills
Skill: code-review-and-quality
Version / commit: 1401c8b8030e023baeebb31781a6653fe8e93026
Installed path: "C:\Users\Alex\Documents\agy2-projects\ada-07-agent-skill\.agents\skills\code-review-and-quality\SKILL.md"
## Why this skill was selected
The skill was selected because it provides a professional, structured approach to code review based on five quality dimensions: correctness, readability, architecture, security, and performance. It was useful for comparing a general professional code-review workflow against my own reviewing-pull-requests skill, which focuses more strongly on PR readiness, requirements, and SDD traceability.

## Anatomy observations
The skill is structured around:
- An executive summary and approval verdict.
- Quality gates based on five review axes.
- PR sizing and cohesion analysis.
- Findings classified as Critical, Required, Consider, and Nit.
- Structural remedies and recommended actions.
- A verification story covering tests, build, manual verification, specification alignment, and traceability.
- A final review checklist and summary.

Its main strength is combining technical code-quality analysis with a clear REQUEST CHANGES / APPROVE decision model.

## Execution
PR / diff reviewed: PR #1 — "New requirements added" (update-branch → master) in AlexSvS/ada-05-spec-driven-feature
Prompt used: 
"Review this pull request using the code-review-and-quality skill. Analyze correctness, readability, architecture, security, and performance, identify blocking findings, verify tests and specification alignment, and provide a final approval verdict."

Artifacts produced:
professional-skill-review.md

## Findings unique to the professional skill
1. Dedicated security and performance analysis. The professional skill explicitly evaluated input-validation risks, potential over-sanitization of international names/emails, and the possible performance impact of deterministic sorting.
2. Five-axis quality gates and structural review. It evaluated PR sizing/cohesion and provided structural remedies such as separating the requirements/specification work from the version-related test change.
## Findings unique to my skill
1. Stronger SDD traceability analysis. My skill explicitly followed the lifecycle Requirement → Acceptance Criterion → Task → Implementation → Test → Traceability, identifying that FR-07–FR-09 were not propagated through the required artifacts.
2. PR-readiness and human-review gate. My skill emphasized whether the PR was ready to move to human review, using MUST FIX / SHOULD FIX / OPTIONAL and explicitly concluding that the PR was not ready for human review/approval.
