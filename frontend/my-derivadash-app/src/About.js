import React from "react"
import "./About.css"
import { Link } from "react-router-dom"
import { Instagram, Linkedin, Github, Mail } from "lucide-react"
import { useDarkMode } from "./contexts/DarkModeContext"

const developers = [
  {
    name: "Joseph Cheng",
    role: "Developer",
    education: "Computer Science and Mathematics Student at New York University",
    bio: "Joe is a passionate problem-solver with a deep love for mathematics and helping students learn. His fascination with quantitative finance and game theory led to the creation of DerivaDash, a project that combines his enthusiasm for education with his technical skills. As a Computer Science and Mathematics student at NYU, Joe is constantly exploring how math and technology can create innovative solutions for real-world challenges. He's especially driven by the idea of making complex mathematical concepts accessible and enjoyable for students through interactive tools like DerivaDash. When he's not coding or tutoring, you might find Joe exploring the vibrant streets of NYC, shooting hoops on the basketball court, or engaged in deep conversations about life's hidden purposes with friends.",
    social: {
      instagram: "https://www.instagram.com/koioseph_/",
      linkedin: "https://www.linkedin.com/in/joseph-cheng-b03886296/",
      github: "https://github.com/jxc2008",
      email: "joseph.x.cheng@gmail.com",
    },
  },
  {
    name: "Himesh Nasaka",
    role: "Developer",
    education: "Electrical Engineering Student at University of Illinois Urbana-Champaign",
    bio: "", // Cleared to allow Himesh to add his own bio
    social: {
      instagram: "https://www.instagram.com/himesh_nasaka/",
      linkedin: "https://linkedin.com/in/hnasaka",
      github: "https://github.com/hnasaka05",
      email: "himeshnas05@gmail.com",
    },
  },
]

function SocialButtons({ social, darkMode }) {
  const iconColor = darkMode ? "#ff4444" : "#4f46e5"
  return (
    <div className="social-buttons">
      <a href={social.instagram} target="_blank" rel="noopener noreferrer" aria-label="Instagram">
        <Instagram color={iconColor} />
      </a>
      <a href={social.linkedin} target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">
        <Linkedin color={iconColor} />
      </a>
      <a href={social.github} target="_blank" rel="noopener noreferrer" aria-label="GitHub">
        <Github color={iconColor} />
      </a>
      <a href={`mailto:${social.email}`} aria-label="Email">
        <Mail color={iconColor} />
      </a>
    </div>
  )
}

function About() {
  const { darkMode } = useDarkMode()
  return (
    <div className="about-container">
      <h2>About DerivaDash</h2>
      <p className="about-description">
        DerivaDash is an interactive platform designed to help students master calculus through quick-fire practice. Our
        goal is to make learning derivatives and integrals both challenging and fun, bridging the gap between
        theoretical knowledge and practical application in mathematics education.
      </p>
      <h3>Meet the Team</h3>
      <div className="developers-grid">
        {developers.map((dev, index) => (
          <div key={index} className="developer-card">
            <h4>{dev.name}</h4>
            <p className="developer-role">{dev.role}</p>
            <p className="developer-education">{dev.education}</p>
            {dev.bio && <p className="developer-bio">{dev.bio}</p>}
            <SocialButtons social={dev.social} darkMode={darkMode} />
          </div>
        ))}
      </div>
      <div className="back-link-container">
        <Link to="/" className="nav-button">
          Back to Home
        </Link>
      </div>
    </div>
  )
}

export default About

