import "./Login.css";
import Google from "./google.png";

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
            New? <b>Sign up now.</b>
          </span>
          <button className="loginButton-google">
            <img src={Google} width="23" height="23" alt="cam"/>Sign In Using Google</button>
        </form>
      </div>
    </div>
  );
}

