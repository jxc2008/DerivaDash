import React from "react"
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom"
import Game from "./Game"
import Home from "./Home"
import About from "./About"
import Learn from "./Learn"
import "./App.css"

function App() {
  return (
    <Router>
      <div className="container">
        <Link to="/" className="title-link">
          <h1>DerivaDash</h1>
        </Link>
        <nav>
          <Link to="/" className="nav-button">
            Home
          </Link>
          <Link to="/learn" className="nav-button">
            Learn
          </Link>
          <Link to="/about" className="nav-button">
            About
          </Link>
        </nav>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/game" element={<Game />} />
          <Route path="/about" element={<About />} />
          <Route path="/learn" element={<Learn />} />
        </Routes>
      </div>
    </Router>
  )
}

export default App

