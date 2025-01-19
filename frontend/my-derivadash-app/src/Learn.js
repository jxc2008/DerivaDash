import React from "react"
import "./Learn.css"
import { Link } from "react-router-dom"

function Learn() {
  return (
    <div className="learn-container">
      <h2>How to Solve Derivatives and Integrals</h2>

      <section className="learn-section">
        <h3>Derivatives Made Simple</h3>
        <p className="learn-intro">
          Derivatives help us find how quickly things change. Think of them as finding the slope at any point on a
          curve.
        </p>
        <div className="rule-card">
          <h4>Key Rules to Remember:</h4>
          <ul>
            <li>
              <strong>Power Rule:</strong> When you see x<sup>n</sup>, multiply by the power and reduce the power by 1
              <p className="example">Example: x³ → 3x²</p>
            </li>
            <li>
              <strong>Product Rule:</strong> When multiplying functions, each piece takes turns being differentiated
              <p className="example">Example: (x² × sin x) → (2x × sin x) + (x² × cos x)</p>
            </li>
            <li>
              <strong>Quotient Rule:</strong> For fractions, think "bottom times derivative of top minus top times
              derivative of bottom, all over bottom squared"
              <p className="example">Example: (x/cos x) → (cos x - x sin x) / cos²x</p>
            </li>
            <li>
              <strong>Chain Rule:</strong> Work from the outside in, multiply the derivatives together
              <p className="example">Example: sin(x²) → 2x × cos(x²)</p>
            </li>
          </ul>
        </div>
      </section>

      <section className="learn-section">
        <h3>Understanding Integrals</h3>
        <p className="learn-intro">
          Integrals are like reverse derivatives. They help us find the total amount when we know the rate of change.
        </p>
        <div className="rule-card">
          <h4>Essential Integration Methods:</h4>
          <ul>
            <li>
              <strong>Basic Integration:</strong> Add 1 to the power and divide by the new power
              <p className="example">Example: ∫ x² dx → x³/3 + C</p>
            </li>
            <li>
              <strong>U-Substitution:</strong> Look for a function and its derivative
              <p className="example">Example: ∫ 2x cos(x²) dx → sin(x²) + C</p>
            </li>
            <li>
              <strong>Integration by Parts:</strong> Use when multiplying functions together
              <p className="example">Example: ∫ x sin x dx → -x cos x + ∫ cos x dx</p>
            </li>
          </ul>
        </div>
      </section>

      <div className="practice-prompt">
        <p>Ready to test your knowledge? Try these concepts in practice mode!</p>
        <Link to="/" className="back-link">
          Back to Practice
        </Link>
      </div>
    </div>
  )
}

export default Learn

