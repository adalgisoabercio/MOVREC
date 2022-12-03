import "./Register.css";

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
          <h1>Sign In</h1>
          <input type="email" placeholder="Email or phone number" />
          <input type="password" placeholder="Password" />
          <button className="loginButton">Register</button>
        </form>
      </div>
    </div>
  );
}

