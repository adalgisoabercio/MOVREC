// import logo from './logo.svg';
// import leftbar from './components/leftbar.js';
// import './style/App.css';
import Home from './Pages/Home';
import Register from './Pages/Register';
import Login from './Pages/Login';

function App() {
  return (
    // <div className="App">
    //   <header className="App-header">
    //     <img src={logo} className="App-logo" alt="logo" />
    //     <p className = 'text-3xl font-bold underline'>
    //       Edit <code>src/App.js</code> and save to reload.
    //     </p>
    //     <a
    //       className="App-link"
    //       href="https://reactjs.org"
    //       target="_blank"
    //       rel="noopener noreferrer"
    //     >
    //       Learn React
    //     </a>
    //   </header>
    // </div>
    // <div className="App">
    <div>
      {/* <Home /> */}
      <Register />
      {/* <Login /> */}
    </div>
  );
}

export default App;
