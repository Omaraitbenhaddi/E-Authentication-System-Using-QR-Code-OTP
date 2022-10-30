import React from 'react'
import loginUser from '../model/modelUser';

function Login(props) {
    let password



    const submit =async (e)=>{
        let email
        e.preventDefault();
        const response= await loginUser({
            email: props.email,
            password:password

        })
        try{
        if(response.user.email!=="")
                    email=response.user.email
        }
        catch(error){email=""}

        props.Loginfunc(email,response.token,response.detail || [response.password +" password"] );


    }



    
    return (
          
          <form  onSubmit={submit} method="post">
                    <h2 className="title">Login </h2>
                    <p><span className='error'>{props.error}</span></p>
    
                    <div className="input-div one focus">

                        <div className="i">
                            <i className="fas fa-user"></i>
                        </div>

                        <div>
                         {/*     <label  htmlFor="user">email</label> */}

                            <input type="email"
                                    id='email'
                                    className="input"
                                    placeholder='Email'
                                    onChange={e=>props.emailState(e.target.value)}
                                    value={props.email}
                            
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
                            placeholder='Password'
                            onChange={e=>password=e.target.value}
                            value={password}
                            />
                                  {/*  <label  htmlFor="pass">password </label>*/}
                        </div>
                    </div>
    
    
                    <a href="/">Forgot password?</a>
                    <input type="submit" className="btn" value="Login"/>
    
    
                </form>
    
      )
  }


export default Login