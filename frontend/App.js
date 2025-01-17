import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const derivativeRules = [
    'constant-rule',
    'power-rule',
    'product-rule',
    'quotient-rule',
    'chain-rule',
  ];
  const integralRules = [
    'constant-function',
    'linear-function',
    'quadratic-function',
    'cubic-function',
    'u-substitution',
    'integration-by-parts',
  ];
  const allRules = [...derivativeRules, ...integralRules];

  // Initialize checkbox states for each rule
  const initialSelected = {};
  allRules.forEach(rule => (initialSelected[rule] = false));

  const [selectedRules, setSelectedRules] = useState(initialSelected);
  const [timeLimit, setTimeLimit] = useState(60);
  const [timeLeft, setTimeLeft] = useState(60);
  const [isRunning, setIsRunning] = useState(false);
  const [correctAnswer, setCorrectAnswer] = useState(null);
  const [output, setOutput] = useState('');
  const timerRef = useRef(null);

  const handleCheckboxChange = (e) => {
    const { id, checked } = e.target;
    setSelectedRules(prev => ({ ...prev, [id]: checked }));
  };

  const handleTimeLimitChange = (e) => {
    setTimeLimit(parseInt(e.target.value));
  };

  const startTimer = () => {
    clearInterval(timerRef.current);
    timerRef.current = setInterval(() => {
      setTimeLeft(prev => {
        if (prev <= 1) {
          clearInterval(timerRef.current);
          setIsRunning(false);
          setOutput("Time's up! Practice session ended.");
          return 0;
        }
        return prev - 1;
      });
    }, 1000);
  };

  const startPractice = async () => {
    const selected = allRules.filter(rule => selectedRules[rule]);
    if (selected.length === 0) {
      setOutput("Please select at least one rule to practice.");
      return;
    }
    if (isRunning) return;

    setIsRunning(true);
    setTimeLeft(timeLimit);
    setOutput('');
    startTimer();
    generateProblem(selected);
  };

  const generateProblem = async (selected) => {
    try {
      const result = await callBackend(selected, null, correctAnswer);
      if (result.status === "new_problem") {
        setCorrectAnswer(result.problem.derivative);
        setOutput(`Problem: ${result.problem.function}`);
        const userInput = prompt("Enter the derivative:");
        if (!userInput) {
          clearInterval(timerRef.current);
          setIsRunning(false);
          return;
        }
        const checkResult = await callBackend(selected, userInput, result.problem.derivative);
        if (checkResult.status === "incorrect") {
          setOutput(`Incorrect! ${checkResult.message}`);
        } else {
          setOutput("Correct! New problem incoming...");
          if (isRunning) {
            setTimeout(() => generateProblem(selected), 1000);
          }
        }
      }
    } catch (error) {
      setOutput(`Error: ${error.message}`);
      clearInterval(timerRef.current);
      setIsRunning(false);
    }
  };

  useEffect(() => {
    return () => {
      clearInterval(timerRef.current);
    };
  }, []);

  return (
    <div className="container">
      <h1>DerivaDash</h1>
      <p className="description">
        Master calculus through quick-fire practice! Solve derivatives and integrals against the clock to build speed and confidence.
      </p>

      <div className="options-container">
        <div className="option-group">
          <div className="option-header">
            <input type="checkbox" id="derivatives" defaultChecked readOnly />
            <label htmlFor="derivatives">Derivatives</label>
          </div>
          <div className="checkbox-group">
            {derivativeRules.map(rule => (
              <div key={rule} className="checkbox-item">
                <input
                  type="checkbox"
                  id={rule}
                  checked={selectedRules[rule]}
                  onChange={handleCheckboxChange}
                />
                <label htmlFor={rule}>{rule.replace('-', ' ')}</label>
              </div>
            ))}
          </div>
        </div>

        <div className="option-group">
          <div className="option-header">
            <input type="checkbox" id="integrals" readOnly />
            <label htmlFor="integrals">Integrals</label>
          </div>
          <div className="checkbox-group">
            {integralRules.map(rule => (
              <div key={rule} className="checkbox-item">
                <input
                  type="checkbox"
                  id={rule}
                  checked={selectedRules[rule]}
                  onChange={handleCheckboxChange}
                />
                <label htmlFor={rule}>{rule.replace('-', ' ')}</label>
              </div>
            ))}
          </div>
        </div>
      </div>

      <div className="controls">
        <select
          id="time-limit"
          value={timeLimit}
          onChange={handleTimeLimitChange}
        >
          <option value="60">60 seconds</option>
          <option value="120">120 seconds</option>
          <option value="180">180 seconds</option>
          <option value="300">300 seconds</option>
        </select>
        <button id="start-practice" onClick={startPractice}>
          Start Practice
        </button>
      </div>

      <div id="output" style={{ marginTop: '20px' }}>{output}</div>
      <div id="time-display" style={{ marginTop: '10px' }}>
        Time Left: {timeLeft}s
      </div>
    </div>
  );
}

// Axios backend call function
async function callBackend(rules, input, answer) {
  const payload = {
    selected_rules: rules,
    user_input: input,
    correct_answer: answer,
  };
  const response = await axios.post('http://localhost:5000/random_derivative', payload);
  return response.data;
}

export default App;
