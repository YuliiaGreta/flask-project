from flask import Flask

# Создаю экземпляр приложения Flask
app = Flask(__name__)

# Определяю маршрут для корневого URL
@app.route('/')
def hello():
    # Возвращаю приветственное сообщение для корневого маршрута
    return "Hello, Flask!"

# Определяю маршрут для URL с параметром <name>
@app.route('/user/<name>')
def user(name):
    # Проверяю, является ли имя "YuliiaH"
    if name == "YuliiaH":
        # Возвращаю персонализированное приветствие для "YuliiaH"
        return f"Hello, {name}! Welcome to your personalized Flask app."
    else:
        # Возвращаю стандартное приветствие для остальных имен
        return f"Hello, {name}!"

# Запускаю приложение Flask в режиме отладки
if __name__ == '__main__':
    app.run(debug=True)