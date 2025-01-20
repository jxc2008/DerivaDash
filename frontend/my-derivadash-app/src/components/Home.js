import React, { useState } from "react"
import { useNavigate, Link } from "react-router-dom"
import "../App.css"
import "./Home.css"
import { useDarkMode } from "../contexts/DarkModeContext"

function Home() {
  const { darkMode } = useDarkMode()
  const navigate = useNavigate()
  const derivativeRules = ["constant", "power", "product", "quotient", "chain"]
  const integralRules = ["integer", "linear", "quadratic", "cubic", "u_substitution", "integration_by_parts"]

  const [derivativesChecked, setDerivativesChecked] = useState(true)
  const [integralsChecked, setIntegralsChecked] = useState(false)
  const [selectedRules, setSelectedRules] = useState({
    derivatives: {
      constant: false,
      power: false,
      product: false,
      quotient: false,
      chain: false,
    },
    integrals: {
      integer: false,
      linear: false,
      quadratic: false,
      cubic: false,
      u_substitution: false,
      integration_by_parts: false,
    },
  })
  const [timeLimit, setTimeLimit] = useState(60)

  const handleCheckboxChange = (e, category) => {
    const { id, checked } = e.target
    setSelectedRules((prev) => ({
      ...prev,
      [category]: {
        ...prev[category],
        [id]: checked,
      },
    }))
  }

  const handleDerivativesChange = (e) => {
    setDerivativesChecked(e.target.checked)
    if (!e.target.checked) {
      setSelectedRules((prev) => ({
        ...prev,
        derivatives: Object.fromEntries(Object.keys(prev.derivatives).map((key) => [key, false])),
      }))
    }
  }

  const handleIntegralsChange = (e) => {
    setIntegralsChecked(e.target.checked)
    if (!e.target.checked) {
      setSelectedRules((prev) => ({
        ...prev,
        integrals: Object.fromEntries(Object.keys(prev.integrals).map((key) => [key, false])),
      }))
    }
  }

  const handleTimeLimitChange = (e) => {
    setTimeLimit(Number.parseInt(e.target.value))
  }

  const startGame = () => {
    const selected = [
      ...Object.keys(selectedRules.derivatives).filter((rule) => selectedRules.derivatives[rule]),
      ...Object.keys(selectedRules.integrals).filter((rule) => selectedRules.integrals[rule]),
    ]
    if (selected.length === 0) {
      alert("Please select at least one rule to practice.")
      return
    }
    navigate("/game", { state: { selectedRules: selected, timeLimit } })
  }

  return (
    <div className={`home-container ${darkMode ? "dark" : ""}`}>
      <p className="description">
        Master calculus through quick-fire practice! Solve derivatives and integrals against the clock to build speed
        and confidence.
      </p>

      <div className="options-container">
        <div className="option-group">
          <div className="option-header">
            <input type="checkbox" id="derivatives" checked={derivativesChecked} onChange={handleDerivativesChange} />
            <label htmlFor="derivatives">Derivatives</label>
          </div>
          <div className="checkbox-group">
            {Object.keys(selectedRules.derivatives).map((rule) => (
              <div key={rule} className="checkbox-item">
                <input
                  type="checkbox"
                  id={rule}
                  checked={selectedRules.derivatives[rule]}
                  onChange={(e) => handleCheckboxChange(e, "derivatives")}
                  disabled={!derivativesChecked}
                />
                <label htmlFor={rule}>{rule.replace("_", " ")}</label>
              </div>
            ))}
          </div>
        </div>

        <div className="option-group">
          <div className="option-header">
            <input type="checkbox" id="integrals" checked={integralsChecked} onChange={handleIntegralsChange} />
            <label htmlFor="integrals">Integrals</label>
          </div>
          <div className="checkbox-group">
            {Object.keys(selectedRules.integrals).map((rule) => (
              <div key={rule} className="checkbox-item">
                <input
                  type="checkbox"
                  id={rule}
                  checked={selectedRules.integrals[rule]}
                  onChange={(e) => handleCheckboxChange(e, "integrals")}
                  disabled={!integralsChecked}
                />
                <label htmlFor={rule}>{rule.replace("_", " ")}</label>
              </div>
            ))}
          </div>
        </div>
      </div>

      <div className="controls">
        <select id="time-limit" value={timeLimit} onChange={handleTimeLimitChange}>
          <option value="60">60 seconds</option>
          <option value="120">120 seconds</option>
          <option value="180">180 seconds</option>
          <option value="300">300 seconds</option>
        </select>
        <button id="start-practice" onClick={startGame}>
          Start Game
        </button>
      </div>

      <div className="navigation-buttons">
        <Link to="/learn" className="nav-button">
          Learn
        </Link>
        <Link to="/about" className="nav-button">
          About
        </Link>
      </div>
    </div>
  )
}

export default Home

