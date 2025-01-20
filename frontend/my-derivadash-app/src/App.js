import React from "react"
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom"
import Game from "./components/Game"
import Home from "./components/Home"
import About from "./components/About"
import Learn from "./components/Learn"
import "./App.css"
import { DarkModeProvider, useDarkMode } from "./contexts/DarkModeContext"
import { Moon, Sun } from "lucide-react"
import { Logo } from "./components/Logo"

function DarkModeToggle() {
  const { darkMode, toggleDarkMode } = useDarkMode()
  return (
    <button
      onClick={toggleDarkMode}
      className="fixed top-4 right-4 p-2 rounded-full bg-gray-200 dark:bg-gray-800 hover:bg-gray-300 dark:hover:bg-gray-700 transition-colors"
      aria-label="Toggle dark mode"
    >
      {darkMode ? (
        <Sun className="w-5 h-5 text-gray-800 dark:text-gray-200" />
      ) : (
        <Moon className="w-5 h-5 text-gray-800 dark:text-gray-200" />
      )}
    </button>
  )
}

function AppContent() {
  const { darkMode } = useDarkMode()
  return (
    <div className={`container ${darkMode ? "dark" : ""}`}>
      <Link to="/" className="title-link flex items-center gap-4">
        <Logo />
        <h1>DerivaDash</h1>
      </Link>
      <DarkModeToggle />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/game" element={<Game />} />
        <Route path="/about" element={<About />} />
        <Route path="/learn" element={<Learn />} />
      </Routes>
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

