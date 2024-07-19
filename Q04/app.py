from flask import Flask, render_template, request, jsonify
import plotly.graph_objs as go
import plotly.io as pio
import random

app = Flask(__name__)

months = ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월']
data = {
    'months': months,
    'temperature': [0.0] * 12,
    'humidity': [0.0] * 12
}

@app.route('/')
def index():
    global data
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['months'], y=data['temperature'], mode='lines+markers', name='Temperature'))
    fig.add_trace(go.Scatter(x=data['months'], y=data['humidity'], mode='lines+markers', name='Humidity'))
    fig.update_layout(title='Monthly Temperature and Humidity', xaxis_title='Month', yaxis_title='Value')
    
    graph_html = pio.to_html(fig, full_html=False)
    return render_template('index.html', graph_html=graph_html, data=data)

@app.route('/update_data', methods=['POST'])
def update_data():
    global data
    temperatures = request.json.get('temperature', [])
    humidities = request.json.get('humidity', [])
    
    data = {
        'months': months,
        'temperature': [round(float(t), 1) for t in temperatures],
        'humidity': [round(float(h), 1) for h in humidities]
    }
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['months'], y=data['temperature'], mode='lines+markers', name='Temperature'))
    fig.add_trace(go.Scatter(x=data['months'], y=data['humidity'], mode='lines+markers', name='Humidity'))
    fig.update_layout(title='Monthly Temperature and Humidity', xaxis_title='Month', yaxis_title='Value')
    
    graph_html = pio.to_html(fig, full_html=False)
    return jsonify({'graph_html': graph_html})

@app.route('/randomize', methods=['POST'])
def randomize():
    global data
    data = {
        'months': months,
        'temperature': [round(random.uniform(15, 30), 1) for _ in range(12)],
        'humidity': [round(random.uniform(40, 60), 1) for _ in range(12)]
    }
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['months'], y=data['temperature'], mode='lines+markers', name='Temperature'))
    fig.add_trace(go.Scatter(x=data['months'], y=data['humidity'], mode='lines+markers', name='Humidity'))
    fig.update_layout(title='Monthly Temperature and Humidity', xaxis_title='Month', yaxis_title='Value')
    
    graph_html = pio.to_html(fig, full_html=False)
    return jsonify({
        'graph_html': graph_html,
        'temperature': data['temperature'],
        'humidity': data['humidity']
    })

if __name__ == '__main__':
    app.run(debug=True)
