from server import mcp

@mcp.resource(uri="operations://list", description="List of operations")
async def newton_api():
    operaciones = {
        "Simplify": "Simplifica expresiones matemáticas a su forma más reducida",
        "Factor": "Factoriza polinomios en sus componentes más simples",
        "Derive": "Calcula la derivada de una función",
        "Integrate": "Calcula la integral indefinida de una función",
        "Find 0's": "Encuentra las raíces o ceros de una función",
        "Find Tangent": "Determina la ecuación de la recta tangente en un punto específico",
        "Area Under Curve": "Calcula el área bajo la curva entre dos límites dados",
        "Cosine": "Calcula el coseno de un ángulo en radianes",
        "Sine": "Calcula el seno de un ángulo en radianes",
        "Tangent": "Calcula la tangente de un ángulo en radianes",
        "Inverse Cosine": "Calcula el arco coseno (función inversa del coseno)",
        "Inverse Sine": "Calcula el arco seno (función inversa del seno)",
        "Inverse Tangent": "Calcula el arco tangente (función inversa de la tangente)",
        "Absolute Value": "Calcula el valor absoluto de un número",
        "Logarithm": "Calcula el logaritmo con una base específica"
    }

    return operaciones