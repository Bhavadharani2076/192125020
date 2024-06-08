import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
    const [data, setData] = useState(null);

    useEffect(() => {
        fetchData('primes'); // Fetch prime numbers initially
    }, []);

    const fetchData = async (type) => {
        try {
            const response = await fetch(`http://127.0.0.1:5000/numbers/${type}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
            });
            const responseData = await response.json();
            setData(responseData);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    return (
        <div className="App">
            <header className="App-header">
                <h1>Average Calculator</h1>
                <div>
                    <button onClick={() => fetchData('primes')}>Fetch Prime Numbers</button>
                    <button onClick={() => fetchData('fibonacci')}>Fetch Fibonacci Numbers</button>
                </div>
                
                </header>
                <main>
                {data && (
                    <>
                        <p>Previous State: {JSON.stringify(data.window_prev_state)}</p>
                        <p>Current State: {JSON.stringify(data.window_curr_state)}</p>
                        <p>Numbers: {JSON.stringify(data.numbers)}</p>
                        <p>Average: {data.avg}</p>
                    </>
                )}
                {!data && <p>Loading...</p>}
                </main>
            
        </div>
    );
}

export default App;
