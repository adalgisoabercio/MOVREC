// Importing the Main Page of Web Applications
import Home from "./Pages/Home";
import MovieMedia from "./Pages/MovieMedia";
import Login from "./Pages/Login";
import Register from "./Pages/Register";

//  Implementing the React-Router-Dom for Routing the Files
import { BrowserRouter, Routes, Route } from "react-router-dom";
function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
        </Routes>
        <Routes>
          <Route path="/Movie" element={<MovieMedia />} />
        </Routes>
        <Routes>
          <Route path="/Login" element={<Login />} />
        </Routes>
        <Routes>
          <Route path="/Register" element={<Register />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
