import React, { Component } from 'react'

const loginUser = async (credentiel)=>{
    const response = await fetch("http://127.0.0.1:8000/api/login/",{
        method: 'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body:  JSON.stringify(credentiel)
    });
    return await response.json();
}
class Login extends Component {
    constructor(){
        super()
        this.state = {
            email : "",
            password : "",
            token:"",
        }
        this.submit = this.submit.bind(this);
    }

    submit =async (e)=>{
        e.preventDefault();
        const response= await loginUser({
            email: this.state.email,
            password:this.state.password

        })
        if(response.token !== "")
                this.state.token = response.token
        this.props.Login(this.state);

    }



    
  render(){
    return (
          
          <form  onSubmit={this.submit} method="post">
                    <h2 className="title">Login </h2>
                    <p><span className='error'>{this.props.error}</span></p>
    
                    <div className="input-div one focus">

                        <div className="i">
                            <i className="fas fa-user"></i>
                        </div>

                        <div>
                         {/*     <label  htmlFor="user">email</label> */}

                            <input type="text"
                                    id='email'
                                    className="input"
                                    placeholder='Usename'
                                    onChange={e=>this.setState({email : e.target.value})}
                                    value={this.state.email}
                            
                            />

                        </div>

                    </div>
    
    
                    <div className="input-div two ">

                        <div className="i">
                            <i className="fas fa-lock"></i>
                        </div>

                        <div>

                            <input type="password"
                            id='password'
                            className="input"
                            placeholder='password'
                            onChange={e=>this.setState({password:e.target.value})}
                            value={this.state.password}
                            />
                                  {/*  <label  htmlFor="pass">password </label>*/}
                        </div>
                    </div>
    
    
                    <a href="index.html">Forgot password?</a>
                    <input type="submit" className="btn" value="Login"/>
    
    
                </form>
    
      )
  }
}

export default Login