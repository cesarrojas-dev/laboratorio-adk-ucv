import pytest

from agente_ucv.agent import calcular_promedio, explicar_concepto, root_agent


def test_concepto_existente():
    r = explicar_concepto("API")
    assert r["status"] == "success"
    assert "comunicación" in r["explicacion"]


def test_concepto_con_espacios_y_mayusculas():
    assert explicar_concepto("  Base de Datos ")["status"] == "success"


@pytest.mark.parametrize("c", ["git", "docker", "ci/cd", "framework", "machine learning"])
def test_nuevos_conceptos(c):
    assert explicar_concepto(c)["status"] == "success"


def test_concepto_no_registrado():
    assert explicar_concepto("blockchain")["status"] == "not_found"


@pytest.mark.parametrize("valor", ["", "   ", None, 123])
def test_concepto_invalido(valor):
    assert explicar_concepto(valor)["status"] == "error"


def test_promedio_correcto():
    assert calcular_promedio([10, 20, 30]) == {"status": "success", "promedio": 20}


@pytest.mark.parametrize("valor", [[], "abc", None, [1, "x"], [True, 2]])
def test_promedio_invalido(valor):
    assert calcular_promedio(valor)["status"] == "error"


def test_agente_configurado():
    assert root_agent.name == "agente_ucv"
    assert len(root_agent.tools) == 2
