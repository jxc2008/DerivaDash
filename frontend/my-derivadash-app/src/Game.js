import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import { useLocation, Link } from 'react-router-dom';
import './Game.css';

function Game() {
  const location = useLocation();
  const { selectedRules, timeLimit } = location.state || { selectedRules: [], timeLimit: 60 };
  const [problem, setProblem] = useState(null);
  const [userInput, setUserInput] = useState('');
  const [output, setOutput] = useState('');
  const [timeLeft, setTimeLeft] = useState(timeLimit);
  const [isRunning, setIsRunning] = useState(true);
  const [score, setScore] = useState(0);
  const timerRef = useRef(null);

  useEffect(() => {
    if (isRunning) {
      startTimer();
      generateProblem();
    }

    return () => {
      clearInterval(timerRef.current);
    };
  }, [isRunning]);

  const startTimer = () => {
    clearInterval(timerRef.current);
    timerRef.current = setInterval(() => {
      setTimeLeft(prev => {
        if (prev <= 1) {
          clearInterval(timerRef.current);
          setIsRunning(false);
          alert(`Time's up! Your final score is ${score}.`);
          return 0;
        }
        return prev - 1;
      });
    }, 1000);
  };

  const generateProblem = async () => {
    try {
      const result = await callBackend(selectedRules);
      if (result.status === "new_problem") {
        setProblem(result.problem);
        setOutput(`Problem: ${result.problem.function}`);
      }
    } catch (error) {
      setOutput(`Error: ${error.message}`);
      setIsRunning(false);
    }
  };

  const handleInputChange = (e) => {
    setUserInput(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!userInput) return;

    try {
      const result = await callBackend(selectedRules, userInput, problem.derivative || problem.result);
      if (result.status === "incorrect") {
        setOutput(`Incorrect! ${result.message}`);
      } else {
        setScore(prevScore => prevScore + 1);
        setOutput("Correct! New problem incoming...");
        setUserInput('');
        if (isRunning) {
          setTimeout(() => generateProblem(), 1000);
        }
      }
    } catch (error) {
      setOutput(`Error: ${error.message}`);
      setIsRunning(false);
    }
  };

  return (
    <div className="game-container">
      <div className="score-display">Score: {score}</div>
      <div className="problem-box">
        <Link to="/" className="back-button">Back to Home</Link>
        <h2>Game On!</h2>
        <div id="output">{output}</div>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={userInput}
            onChange={handleInputChange}
            placeholder="Enter your answer"
          />
          <button type="submit">Submit</button>
        </form>
        <div id="time-display">Time Left: {timeLeft}s</div>
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
  const response = await axios.post('http://localhost:5000/random_problem', payload);
  return response.data;
}

export default Game;
