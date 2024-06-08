import time
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to fetch numbers from the provided endpoint based on the type
def fetch_numbers(endpoint):
    try:
        response = requests.get(endpoint)
        data = response.json()
        numbers = data.get('numbers', [])
        return numbers
    except Exception as e:
        print("Error fetching numbers:", e)
        return []

# Function to calculate average of numbers in the window
def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0.0

# Initialize the state
window_size = 10
stored_numbers = []

# Function to maintain window size and update stored numbers
def update_numbers(new_number):
    if len(stored_numbers) < window_size:
        stored_numbers.append(new_number)
    else:
        stored_numbers.pop(0)
        stored_numbers.append(new_number)

@app.route('/numbers/<type>', methods=['GET'])
def process_numbers(type):
    global stored_numbers

    # Map the type to the corresponding endpoint
    endpoints = {
        'primes': 'http://20.244.56.144/test/primes',
        'fibonacci': 'http://20.244.56.144/test/fibo'
    }

    # Fetch numbers from the provided endpoint based on the type
    numbers = fetch_numbers(endpoints.get(type, ''))

    # Update stored numbers and calculate average
    update_numbers(numbers)
    avg = calculate_average(stored_numbers)

    return jsonify({
        "window_prev_state": stored_numbers[:-1],
        "window_curr_state": stored_numbers,
        "numbers": numbers,
        "avg": round(avg, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)
