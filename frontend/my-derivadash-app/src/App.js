import React, { useState } from 'react';
import Game from './Game';
import './App.css';

function App() {
  const derivativeRules = [
    'constant',
    'power',
    'product',
    'quotient',
    'chain',
  ];
  const integralRules = [
    'constant',
    'linear',
    'quadratic',
    'cubic',
    'u_substitution',
    'integration_by_parts',
  ];
  const allRules = [...derivativeRules, ...integralRules];

  const initialSelected = {};
  allRules.forEach(rule => (initialSelected[rule] = false));

  const [selectedRules, setSelectedRules] = useState(initialSelected);
  const [timeLimit, setTimeLimit] = useState(60);
  const [isGameStarted, setIsGameStarted] = useState(false);

  const handleCheckboxChange = (e) => {
    const { id, checked } = e.target;
    setSelectedRules(prev => ({ ...prev, [id]: checked }));
  };

  const handleTimeLimitChange = (e) => {
    setTimeLimit(parseInt(e.target.value));
  };

  const startGame = () => {
    const selected = allRules.filter(rule => selectedRules[rule]);
    if (selected.length === 0) {
      alert("Please select at least one rule to practice.");
      return;
    }
    setIsGameStarted(true);
  };

  const endGame = (message) => {
    setIsGameStarted(false);
    alert(message);
  };

  return (
    <div className="container">
      <h1>DerivaDash</h1>
      <p className="description">
        Master calculus through quick-fire practice! Solve derivatives and integrals against the clock to build speed and confidence.
      </p>

      {!isGameStarted ? (
        <>
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
                    <label htmlFor={rule}>{rule.replace('_', ' ')}</label>
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
                    <label htmlFor={rule}>{rule.replace('_', ' ')}</label>
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
            <button id="start-practice" onClick={startGame}>
              Start Game
            </button>
          </div>
        </>
      ) : (
        <Game
          selectedRules={Object.keys(selectedRules).filter(rule => selectedRules[rule])}
          timeLimit={timeLimit}
          onEndGame={endGame}
        />
      )}
    </div>
  );
}

export default App;