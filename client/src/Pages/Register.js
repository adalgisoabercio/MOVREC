// Connections and Default Dependencies
import React from 'react'
import axios from 'react-axios'
import Config from '../Config/defaultConfig'

// Styles
import "./Style/Register.css"

export default function Register() {
  return (
    <div className="login">
      <div className="top">
        <div className="wrapper">
          <div className="logo">
            ADP <span>.</span>
          </div>
        </div>
      </div>
      <div className="container">
        <form>
          <h1>Register</h1>
          <input type="text" placeholder="User Name" />
          <input type="number" placeholder="Years Old" />
          <input type="email" placeholder="Email or phone number" />
          <input type="password" placeholder="Password" />
          <button className="loginButton">Register</button>
        </form>
      </div>
    </div>
  );
}

