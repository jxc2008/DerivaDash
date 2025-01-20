import React from "react"
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom"
import Game from "./components/Game"
import Home from "./components/Home"
import About from "./components/About"
import Learn from "./components/Learn"
import "./App.css"
import { DarkModeProvider, useDarkMode } from "./contexts/DarkModeContext"
import { Moon, Sun } from "lucide-react"

function DarkModeToggle() {
  const { darkMode, toggleDarkMode } = useDarkMode()
  return (
    <button onClick={toggleDarkMode} className="dark-mode-toggle" aria-label="Toggle dark mode">
      {darkMode ? <Sun className="w-5 h-5" /> : <Moon className="w-5 h-5" />}
    </button>
  )
}

function AppContent() {
  const { darkMode } = useDarkMode()

  React.useEffect(() => {
    if (darkMode) {
      document.body.classList.add("dark")
    } else {
      document.body.classList.remove("dark")
    }
  }, [darkMode])

  return (
    <div className={`container ${darkMode ? "dark" : ""}`}>
      <Link to="/" className="title-link">
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

