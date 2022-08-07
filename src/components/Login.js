import React, { Component } from 'react'

class Login extends Component {
    constructor(){
        super()
        this.state = {
            name : "",
            pass : ""
        }
        this.submit = this.submit.bind(this);
    }

    submit =(e)=>{
        e.preventDefault();
        this.props.Login(this.state);
    }



    
  render(){
    return (
          
          <form  onSubmit={this.submit}>
                    <h2 className="title">Login</h2>
    
                    <div className="input-div one focus">
                        <div className="i">
                            <i className="fas fa-user"></i>
                        </div>
                        <div>
                            <label  htmlFor="user">username</label>
                            <input type="text" id='user' className="input" onChange={e=>this.setState({name : e.target.value})} value={this.state.name}/>
                        </div>
                    </div>
    
    
                    <div className="input-div two ">
                        <div className="i">
                            <i className="fas fa-lock"></i>
                        </div>
                        <div>
                        <input type="password" id='pass' className="input" onChange={e=>this.setState({pass:e.target.value})} value={this.state.pass}/>
                        <label  htmlFor="pass">password </label>
                        </div>
                    </div>
    
    
                    <a href="index.html">Forgot password?</a>
                    <input type="submit" className="btn" value="Login"/>
    
    
                </form>
    
      )
  }
}

export default Login