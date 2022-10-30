import React, { useState  } from "react";
import Background from "../../components/Background";
import '../../index.css'
import logoutUser from "../../components/logout";





function HomePage(){
      const [email,emailState]=useState("")
      const [password,passwordState]=useState("")
      const [error,errorState]=useState("")
      const [token,tokenState]=useState("")

      const Logout=state=>{
        //  console.log(state)
            logoutUser(token)
            emailState("")
            passwordState("")
            errorState("")
            tokenState("")
      
          
        }
      


    return (
        <div>

  <div className="wrapper">
    <div className="wave"></div>
  </div>
  <div className="container">

    <Background name="{email}" />

    <div className="login-container">
      <div>

        <h1>Hello {email}</h1>
        <button className="btn" onClick="{Logout}">logout</button>
      </div>
    </div>
  </div>

</div>
  );
    }


export default HomePage;
