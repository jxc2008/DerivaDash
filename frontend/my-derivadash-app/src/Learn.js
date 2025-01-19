import React from "react"
import "./Learn.css"

function Learn() {
  return (
    <div className="learn-container">
      <h2>Learn Derivatives and Integrals</h2>
      <section>
        <h3>Derivatives</h3>
        <p>Derivatives measure the rate of change of a function. Here are some common rules:</p>
        <ul>
          <li>Power Rule: The derivative of x^n is n * x^(n-1)</li>
          <li>Product Rule: (f * g)' = f' * g + f * g'</li>
          <li>Quotient Rule: (f / g)' = (f' * g - f * g') / g^2</li>
          <li>Chain Rule: (f(g(x)))' = f'(g(x)) * g'(x)</li>
        </ul>
      </section>
      <section>
        <h3>Integrals</h3>
        <p>Integrals are the opposite of derivatives and represent the area under a curve. Some key concepts:</p>
        <ul>
          <li>Indefinite Integrals: ∫ f(x) dx = F(x) + C, where F'(x) = f(x)</li>
          <li>Definite Integrals: ∫[a to b] f(x) dx = F(b) - F(a)</li>
          <li>U-Substitution: Used for integrating composite functions</li>
          <li>Integration by Parts: ∫ u dv = uv - ∫ v du</li>
        </ul>
      </section>
      <p>Practice these concepts in DerivaDash to improve your skills!</p>
    </div>
  )
}

export default Learn

