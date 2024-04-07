from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получение данных из формы
        criteria_weights = request.form.getlist('criteria_weights[]', type=float)
        alternative_names = request.form.getlist('alternative_names[]')
        criteria_names = request.form.getlist('criteria_names[]')
        alternative_scores = np.array([request.form.getlist('scores_row_' + str(i) + '[]', type=int) for i in range(len(alternative_names))])

        # Расчет общей полезности каждой альтернативы
        total_utilities = np.dot(alternative_scores, criteria_weights)

        # Подготовка результатов для вывода
        results = dict(zip(alternative_names, total_utilities))
    else:
        # Данные по умолчанию
        criteria_weights = [0.2, 0.15, 0.2, 0.15, 0.15, 0.15]
        alternative_names = ["Солнечная энергия", "Ветровая энергия", "Гидроэнергия", "Биомасса", "Ядерная энергия"]
        criteria_names = ["Экономическая эффективность", "Экологическая устойчивость", "Надежность и доступность", "Гибкость и адаптивность", "Техническая интеграция", "Социальная ответственность и общественное мнение"]
        alternative_scores = [
            [7, 8, 6, 7, 6, 7],
            [6, 7, 8, 6, 7, 6],
            [8, 6, 7, 6, 7, 7],
            [5, 7, 6, 7, 6, 6],
            [9, 6, 8, 5, 7, 8]
        ]
        results = {}

    return render_template('index.html', criteria_weights=criteria_weights, alternative_names=alternative_names, criteria_names=criteria_names, alternative_scores=alternative_scores, results=results)

if __name__ == '__main__':
    app.run(debug=True)
