import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Game from './Game';
import Home from './Home';
import './App.css';

function App() {
  return (
    <Router>
      <div className="container">
        <h1>DerivaDash</h1>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/game" element={<Game />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;