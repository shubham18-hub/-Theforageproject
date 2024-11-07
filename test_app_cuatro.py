import pytest
from app_cuatro import app  # Importa la aplicación Dash desde app_cuatro

# Test the basic layout and functionality
def test_layout(dash_duo):
    # Inicia la aplicación usando DashDuo
    dash_duo.start_server(app)

    # Asegura que el título está presente
    assert dash_duo.find_element("h1").text == "Sales per Region"

    # Asegura que la checklist y el gráfico existen
    assert dash_duo.find_element("#yaxis-column") is not None
    assert dash_duo.find_element("#fig") is not None

def test_callback(dash_duo):
    dash_duo.start_server(app)

    # Simula la selección de regiones en la checklist
    checklist = dash_duo.find_element("#yaxis-column")
    assert checklist is not None

    # Espera a que el gráfico se actualice
    dash_duo.wait_for_element("#fig")

    # Verifica que el gráfico actualizado esté presente
    graph = dash_duo.find_element("#fig")
    assert graph is not None