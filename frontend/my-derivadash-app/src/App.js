import React from "react"
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom"
import Game from "./Game"
import Home from "./Home"
import About from "./About"
import "./App.css"

function App() {
  return (
    <Router>
      <div className="container">
        <Link to="/" className="title-link">
          <h1>DerivaDash</h1>
        </Link>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/game" element={<Game />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </div>
    </Router>
  )
}

export default App

