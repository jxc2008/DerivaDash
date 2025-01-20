import React from "react"
import { useDarkMode } from "../contexts/DarkModeContext"

export function Logo() {
  const { darkMode } = useDarkMode()

  return (
    <div
      className="w-12 h-12 rounded-full flex items-center justify-center"
      style={{
        backgroundColor: "#ff4444",
      }}
    >
      <img
        src="https://hebbkx1anhila5yf.public.blob.vercel-storage.com/image-fxdv2xwPajefUhNTW0bLBKkssHGoAv.png"
        alt="DerivaDash Logo"
        className="w-8 h-8 invert"
      />
    </div>
  )
}

