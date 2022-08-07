import React, { Component } from "react";
import Background from "./components/Background";
import Login from "./components/Login";
import './index.css'


const adminUser={
  name : "admin",
  pass : "admin"
}
class App extends Component {
  constructor(){
    super()
    this.state = {
      name : "",
      pass : ""
    }
    this.Login = this.Login.bind(this);

  }


  Login = state=>{
  //  console.log(state)
    if(state.name===adminUser.name &&  state.pass===adminUser.pass){
      this.setState({name:state.name,pass:state.pass})

    }
  }
  Logout=state=>{
    //  console.log(state)
        this.setState({name:"",pass:""})
  
      
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
        {
          (this.state.name!=="")? (<div>
            
                                         <h1>Hello {this.state.name}</h1> 
                                          <button className="btn" onClick={this.Logout}>logout</button>
                                     </div>
                                      ): (<Login Login={this.Login}/>)
        }
      </div>
      </div>




    </div>
  );
  }
}

export default App;
