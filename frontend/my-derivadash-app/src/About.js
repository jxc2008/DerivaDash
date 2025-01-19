import React from "react"
import "./About.css"

const developers = [
  {
    name: "Joseph Cheng",
    role: "Lead Developer",
    bio: "Joseph is passionate about mathematics and web development. He specializes in creating interactive educational tools.",
  },
  {
    name: "Himesh Nasaka",
    role: "UI/UX Designer",
    bio: "Himesh has a keen eye for design and user experience. He ensures that DerivaDash is both functional and visually appealing.",
  },
]

function About() {
  return (
    <div className="about-container">
      <h2>About DerivaDash</h2>
      <p className="about-description">
        DerivaDash is an interactive platform designed to help students master calculus through quick-fire practice. Our
        goal is to make learning derivatives and integrals both challenging and fun.
      </p>
      <h3>Meet the Team</h3>
      <div className="developers-grid">
        {developers.map((dev, index) => (
          <div key={index} className="developer-card">
            <h4>{dev.name}</h4>
            <p className="developer-role">{dev.role}</p>
            <p className="developer-bio">{dev.bio}</p>
          </div>
        ))}
      </div>
    </div>
  )
}

export default About

