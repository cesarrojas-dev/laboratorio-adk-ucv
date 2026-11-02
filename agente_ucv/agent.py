"""Mono-agente académico UCV construido con Google ADK."""
from google.adk.agents.llm_agent import Agent
CONCEPTOS = {
    "api": "Una API permite comunicación entre sistemas.",
    "algoritmo": "Un algoritmo es una secuencia de pasos.",
    "base de datos": "Una base de datos almacena información.",
    "framework": "Un framework es una estructura base que facilita desarrollar software.",
    "git": "Git es un sistema de control de versiones que registra los cambios del código.",
    "docker": "Docker empaqueta aplicaciones en contenedores para ejecutarlas igual en cualquier entorno.",
    "ci/cd": "CI/CD automatiza la integración, las pruebas y el despliegue del software.",
    "machine learning": "Machine learning es una rama de la IA donde los sistemas aprenden a partir de datos.",
}
def explicar_concepto(concepto: str) -> dict:
    """Explica un concepto técnico de forma sencilla.
    Args:
        concepto: nombre del concepto a explicar (por ejemplo, "api").
    Returns:
        dict con las claves "status" y "explicacion".
    """
    if not isinstance(concepto, str) or not concepto.strip():
        return {
            "status": "error",
            "explicacion": "Debes ingresar un concepto válido.",
        }

    clave = concepto.lower().strip()
    if clave in CONCEPTOS:
        return {"status": "success", "explicacion": CONCEPTOS[clave]}

    return {"status": "not_found", "explicacion": "Concepto no registrado."}


def calcular_promedio(numeros: list[float]) -> dict:
    """Calcula el promedio de una lista de números.

    Args:
        numeros: lista de valores numéricos.

    Returns:
        dict con las claves "status" y "promedio" (o "mensaje" si hay error).
    """
    if not isinstance(numeros, list) or len(numeros) == 0:
        return {"status": "error", "mensaje": "Debes enviar una lista no vacía de números."}

    for n in numeros:
        if isinstance(n, bool) or not isinstance(n, (int, float)):
            return {"status": "error", "mensaje": "Todos los valores deben ser numéricos."}

    return {"status": "success", "promedio": sum(numeros) / len(numeros)}


root_agent = Agent(
    model="gemini-3.1-flash-lite",
    name="agente_ucv",
    description="Agente académico UCV",
    instruction="""
    Eres un asistente académico.
    Responde en español.
    Usa lenguaje simple.
    Usa la herramienta explicar_concepto para definiciones técnicas
    y calcular_promedio cuando el usuario pida un promedio.
    """,
    tools=[explicar_concepto, calcular_promedio],
)
