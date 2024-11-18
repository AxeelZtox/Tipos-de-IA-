import nltk
from nltk.chat.util import Chat, reflections
import requests
import ast
import operator

nltk.download('punkt')

def get_weather(city):
    api_key = '4e161ebf917f678bd13d1ab7a6410dad'  
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    params = {'q': city, 'appid': api_key, 'lang': 'es', 'units': 'metric'}
    response = requests.get(base_url, params=params)
    data = response.json()
    if data['cod'] == 200:
        weather_desc = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"{weather_desc} y {temp}°C"
    else:
        return f"No pude obtener el clima para {city}."

# Función para evaluar expresiones matemáticas de forma segura
def safe_eval(expr):
    allowed_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow
    }

    class CalcVisitor(ast.NodeVisitor):
        def visit(self, node):
            if isinstance(node, ast.Expression):
                return self.visit(node.body)
            elif isinstance(node, ast.BinOp):
                if type(node.op) in allowed_operators:
                    return allowed_operators[type(node.op)](
                        self.visit(node.left), self.visit(node.right))
                else:
                    raise ValueError('Operador no permitido')
            elif isinstance(node, ast.Num):
                return node.n
            else:
                raise ValueError('Tipo de expresión no soportado')

    try:
        node = ast.parse(expr, mode='eval')
        visitor = CalcVisitor()
        return visitor.visit(node)
    except:
        return "No pude calcular la expresión."

# Función para procesar la entrada del usuario
def process_input(user_input):
    greetings = ["hola", "buenos días", "buenas tardes", "buenas noches", "hey", "qué tal"]
    friendly_responses = {
        "hola": "¡Hola! :) ¿En qué puedo ayudarte?",
        "buenos días": "¡Buenos días! Espero que tengas un excelente día. :D",
        "buenas tardes": "¡Buenas tardes! :) ¿Cómo va todo?",
        "buenas noches": "¡Buenas noches! Espero que descanses bien. :D",
        "qué tal": "¡Estoy bien, gracias por preguntar! ¿Y tú? :)"
    }
    
    # Reconocer saludos
    if user_input in greetings:
        return friendly_responses.get(user_input, "¡Hola! :) ¿En qué puedo ayudarte?")
    
    # Manejo del clima
    if "clima en" in user_input:
        city = user_input.split("clima en")[1].strip()
        return get_weather(city)
    
    # Manejo de cálculos
    if "calcula" in user_input:
        expression = user_input.split("calcula")[1].strip()
        return f"El resultado es {safe_eval(expression)}"
    
    # Respuesta por defecto
    return "Lo siento, no entiendo tu pregunta. :("

# Main
def main():
    print("=" * 50)
    print("¡Hola! Soy tu asistente virtual".center(50))
    print("Escribe 'adiós' para salir.".center(50))
    print("=" * 50)
    
    while True:
        user_input = input("\nTú: ").lower()
        if user_input in ["adiós", "salir", "hasta luego", "nos vemos"]:
            print("\nAsistente: Adiós, que tengas un buen día. ¡Hasta pronto! :D")
            print("=" * 50)
            break
        response = process_input(user_input)
        print(f"Asistente: {response}")

if __name__ == "__main__":
    main()
