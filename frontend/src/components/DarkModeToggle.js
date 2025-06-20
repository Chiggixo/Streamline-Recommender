import React from "react";

function DarkModeToggle({ darkMode, toggle }) {
  return (
    <div style={{ position: "fixed", bottom: "10px", right: "20px" }}>
      <label style={{ fontSize: "0.9rem" }}>
        <input type="checkbox" checked={darkMode} onChange={toggle} /> 🌙 Dark Mode
      </label>
    </div>
  );
}

export default DarkModeToggle;
