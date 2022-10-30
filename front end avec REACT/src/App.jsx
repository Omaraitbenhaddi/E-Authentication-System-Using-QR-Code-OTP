import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import LoginPage from "./Page/LoginPage/LoginPage";
import HomePage from "./Page/LoginPage/HomePage"



function App(){
  
    return (

      <div className="App">

    <Router>
      <Routes>
      <Route path="/" element={<LoginPage/>}/>
      <Route path="/home/" element={<HomePage/>}/>

        </Routes>
    </Router>

    </div>
  );
}

export default App;
