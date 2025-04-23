# 🧮 MCP - Model Context Protocol for Newton Mathematics | [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)

**Motor de Contexto de Procesos (MCP)** - Servidor MCP que proporciona una interfaz elegante para realizar operaciones matemáticas avanzadas utilizando la Newton API.

## 🌟 Características Principales

### 🧮 Operaciones Matemáticas
- **Cálculo Avanzado**
  ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) ![REST API](https://img.shields.io/badge/-REST%20API-FF6F00?logo=fastapi&logoColor=white)
  - Integración de funciones
  - Derivación
  - Factorización
  - Simplificación de expresiones
  - Funciones trigonométricas

### 🚀 Características Técnicas
- **Integración MCP**
  - Implementación asíncrona con FastMCP
  - Logging integrado para debugging
  - Manejo robusto de errores

### 📊 Operaciones Disponibles
| Operación | Descripción |
|-----------|-------------|
| Simplify | Simplifica expresiones matemáticas a su forma más reducida |
| Factor | Factoriza polinomios en sus componentes más simples |
| Derive | Calcula la derivada de una función |
| Integrate | Calcula la integral indefinida de una función |
| Find 0's | Encuentra las raíces o ceros de una función |
| Find Tangent | Determina la ecuación de la recta tangente en un punto específico |
| Area Under Curve | Calcula el área bajo la curva entre dos límites dados |
| Cosine | Calcula el coseno de un ángulo en radianes |
| Sine | Calcula el seno de un ángulo en radianes |
| Tangent | Calcula la tangente de un ángulo en radianes |
| Inverse Cosine | Calcula el arco coseno (función inversa del coseno) |
| Inverse Sine | Calcula el arco seno (función inversa del seno) |
| Inverse Tangent | Calcula el arco tangente (función inversa de la tangente) |
| Absolute Value | Calcula el valor absoluto de un número |
| Logarithm | Calcula el logaritmo con una base específica |

## 🛠️ Stack Tecnológico

| Capa | Tecnologías |
|------|-------------|
| **Backend** | Python 3.10+, FastMCP |
| **API** | Newton API |
| **Logging** | MCP Context Logger |

## 🚀 Implementación

### 📋 Prerrequisitos
- ![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB)
- Instalación del paquete MCP
- Conexión a Internet para acceder a Newton API

### ⚡ Inicio Rápido
```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/mcp-math.git
cd mcp-math

# Instalar dependencias
pip install -r requirements.txt

# Iniciar el servidor
python source/main.py
```

### 📝 Ejemplo de Uso
```python
# Realizar una integración
operation = "integrate"
data = "x^2"  # Integrará x^2

# La respuesta incluirá la integral: (1/3)x^3 + C
```

## 🤝 Contribuciones
¡Las contribuciones son bienvenidas! Si tienes ideas para nuevas operaciones matemáticas o mejoras, no dudes en crear un PR.

## 📄 Licencia
Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---
Desarrollado con ❤️ usando MCP y Newton API