import React from "react"
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom"
import Game from "./Game"
import Home from "./Home"
import About from "./About"
import Learn from "./Learn"
import "./App.css"
import { DarkModeProvider, useDarkMode } from "./contexts/DarkModeContext"
import { Moon, Sun } from "lucide-react"
import { Logo } from "./components/Logo"

function DarkModeToggle() {
  const { darkMode, toggleDarkMode } = useDarkMode()
  return (
    <button
      onClick={toggleDarkMode}
      className="fixed top-4 right-4 p-2 rounded-full bg-gray-200 dark:bg-gray-800 z-50"
      aria-label="Toggle dark mode"
    >
      {darkMode ? <Sun className="w-6 h-6" /> : <Moon className="w-6 h-6" />}
    </button>
  )
}

function AppContent() {
  const { darkMode } = useDarkMode()
  return (
    <div className={darkMode ? "dark" : ""}>
      <div className="min-h-screen bg-white dark:bg-gray-900 transition-colors duration-300">
        <div className="container mx-auto px-4 py-8">
          <Link to="/" className="title-link">
            <h1>DerivaDash</h1>
          </Link>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/game" element={<Game />} />
            <Route path="/about" element={<About />} />
            <Route path="/learn" element={<Learn />} />
          </Routes>
        </div>
      </div>
      <DarkModeToggle />
    </div>
  )
}

function App() {
  return (
    <DarkModeProvider>
      <Router>
        <AppContent />
      </Router>
    </DarkModeProvider>
  )
}

export default App

