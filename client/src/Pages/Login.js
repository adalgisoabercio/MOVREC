import "./Style/Login.css";
import Google from "../Assets/google.png";
import { Link } from "react-router-dom";

export default function Login() {
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
          <h1>Sign In</h1>
          <input type="email" placeholder="Email or phone number" />
          <input type="password" placeholder="Password" />
          <button className="loginButton">Sign In</button>
          <span>
            <Link to="/Register">
              New? <b>Sign up now.</b>
            </Link>
          </span>
          <button className="loginButton-google">
            <img src={Google} width="23" height="23" alt="cam" />
            Sign In Using Google
          </button>
        </form>
      </div>
    </div>
  );
}
