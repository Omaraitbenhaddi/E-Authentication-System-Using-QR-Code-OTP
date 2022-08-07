import React, { Component } from "react";
import Background from "./components/Background";
import Login from "./components/Login";
import './index.css'


const adminUser={
  name : "admin@admin.ma",
  pass : "admin"
}
class App extends Component {
  constructor(){
    super()
    this.user = {
      name : "",
      pass : ""
    }

  }


  Login = state=>{
    console.log(state)

  }


  render(){
    return (

      <div className="App">


    <div class="wrapper">
  <div class="wave"></div>
    </div>
    <div class="container">

      <Background/>
      <div className="login-container">
      <Login Login={this.Login}/>
      </div>
      </div>




    </div>
  );
  }
}

export default App;
