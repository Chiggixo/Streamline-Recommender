import React, { useState } from "react";
import RecommendationForm from "./components/RecommendationForm";
import AdminPanel from "./components/AdminPanel";
import "./App.css";
import logo from "./STREAMLINE-LOGO.png";

// ✅ MUI ThemeProvider
import { ThemeProvider, createTheme } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";

const theme = createTheme(); // default light theme

function App() {
  const [isAdmin, setIsAdmin] = useState(false);
  const [authenticated, setAuthenticated] = useState(false);

  const handleAdminLogin = (username, password) => {
    if (username === "admin" && password === "admin123") {
      setAuthenticated(true);
    } else {
      alert("Invalid admin credentials");
    }
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <div className="App">
        <header className="navbar">
          <div className="nav-left">
            <img src={logo} alt="Company Logo" className="nav-logo" />
            <h1 className="nav-title">Streamline Beauty India Pvt. Ltd.</h1>
          </div>
          <div className="nav-right">
            <button className="admin-btn" onClick={() => setIsAdmin(!isAdmin)}>
              {isAdmin ? "Back to User" : "Admin Login"}
            </button>
          </div>
        </header>

        {/* USER RECOMMENDATION VIEW */}
        {!isAdmin && <RecommendationForm />}

        {/* ADMIN LOGIN VIEW */}
        {isAdmin && !authenticated && (
          <div className="admin-login">
            <h2>Admin Login</h2>
            <input
              type="text"
              placeholder="Username"
              onChange={() => setAuthenticated(false)}
              id="admin-username"
            />
            <input
              type="password"
              placeholder="Password"
              onKeyDown={(e) => {
                if (e.key === "Enter") {
                  handleAdminLogin(
                    document.getElementById("admin-username").value,
                    e.target.value
                  );
                }
              }}
            />
            <button
              onClick={() =>
                handleAdminLogin(
                  document.getElementById("admin-username").value,
                  document.querySelector("input[type='password']").value
                )
              }
            >
              Login
            </button>
          </div>
        )}

        {/* ADMIN PANEL VIEW */}
        {isAdmin && authenticated && <AdminPanel />}
      </div>
    </ThemeProvider>
  );
}

export default App;
