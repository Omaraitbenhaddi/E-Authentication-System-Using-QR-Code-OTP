import React, { Component  } from "react";
import Background from "../../components/Background";
import Login from "../../components/Login"
import '../../index.css'
import logoutUser from "../../components/logout";






class LoginPage extends Component {
  constructor(){
    super()
    this.state = {
      email : "",
      password : "",
      error : "",
      token : ""
    }

  }


  Login = state=>{
    if(state.token!==undefined){
      this.setState({email:state.email,password:state.password,token:state.token})


    }
    else{
      this.setState({error:"detaill no match"})
    }

  }
  Logout=state=>{
    //  console.log(state)
        logoutUser(this.state.token)
        this.setState({email:"",password:"",token:"",error:""})
  
      
    }


  render(){
    return (

      <div >


    <div className="wrapper">
  <div className="wave"></div>
    </div>
    <div className="container">

      <Background name={this.state.email}/>



      <div className="login-container">
        {
          (this.state.token!=="")? (<div>
            
                                         <h1>Hello {this.state.email}</h1> 
                                          <button className="btn" onClick={this.Logout}>logout</button>
                                     </div>
                                      ): (<Login Login={this.Login} error={this.state.error}  />)
        }
      </div>
      </div>
     



    </div>
  );
  }
}

export default LoginPage;
