import React, { Component  } from "react";
import LoginPage from "./Page/LoginPage/LoginPage";


import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";




class App extends Component {
  
  render(){
    return (

      <div className="App">
        <Router>
            <Routes>
              <Route path="/" element={<LoginPage/>}/>
            </Routes>

        </Router>

    </div>
  );
  }
}

export default App;
