import React, { useState  } from "react";
import Background from "../../components/Background";
import Login from "../../components/Login"
import '../../index.css'
import logoutUser from "../../components/logout";
import ImageProfile from "../../components/ImageProfile";
import QrScanner from 'qr-scanner';
import DemendeValidateUser from "../../components/DemendeValidationOtp";
import ValiderOtp from "../../components/ValiderOtp";






function LoginPage()  {

  const [email,emailState]=useState("")
  const [error,errorState]=useState("")
  const [token,tokenState]=useState("")
  const [result, setResult] = useState("")
  const [Valid, setValid] = useState(false)
  const [send, setsend] = useState(false)
  let otp
  const [ValFinal, setValFinal] = useState("")

  const ValiderOTP = async (e)=>{
    e.preventDefault();
    const response= await ValiderOtp({
      email: email,
      otp:otp,

  },token)
  if(response.detail==="otp matched kindly process to save password"){
    setValFinal(response.detail)}
  }


  const sendOTP =async (e)=>{
    e.preventDefault();

    const response= await DemendeValidateUser({
      email: email,

  },token)
  console.log(response)
  setsend(true)

  }



  const submitQr =()=>{
    const date = new Date();
    let s =date.getFullYear()+":"+date.getMonth()+":"+date.getDay()+":"+date.getHours()
    //+":"+date.getMinutes()+":"+date.getSeconds() 
    console.log(email+s)
    console.log(result)
    if(email+s===result){
          setValid(true)
    }
    console.log(Valid)
  }


  const Readcode=(e)=>{
    const file = e.target.files[0];
    if (!file) {
        return;
    }
    QrScanner.scanImage(file, { returnDetailedScanResult: true })
        .then(result => setResult(result.data))
        .catch(e => console.log(e));

  }


 


  const Loginfunc = (email_,token_,resp)=>{
    if(token_!==undefined){
      emailState(email_)
      tokenState(token_)



    }
    else{
      console.log(resp[0])
      errorState(resp[0])

    }

  }

  const Logout=state=>{
        logoutUser(token)
        emailState("")
        errorState("")
        tokenState("")
  
      
    }

    return (

      <div >


    <div className="wrapper">
  <div className="wave"></div>
    </div>
    {
      (token!=="")? (<ImageProfile Logout_={Logout} />):(<></>)
    } 

    <div className="container">


      <Background token={token}/>






      <div className="login-container">
        {
          (token!=="")? (
                              (Valid===false)?((
                              <div>
                                <h1>Hello {email}</h1> 
                                <input type="file" onChange={(e)=>Readcode(e)} ></input>
                                 <input type="submit" className="btn" value="Submit" onClick={submitQr} / >
                              </div>
                                 
                                 ))
                                 :
                                 
                                 (
                                  


                                  (send===false)?(
                                    <form method="post" onSubmit={sendOTP} >
                                    <h1>Hello {email}</h1> 
                                    <button  className="btn" >send Otp </button>
                                    </form>
 
                                    )
                                  
                                  
                                  :(
                                  (

                                    (ValFinal==="")?(


                                    <form method="post" onSubmit={ValiderOTP} >
                                    <h1>Hello </h1> 
                                    <input type="text" onChange={e=>otp=e.target.value} />
                                    <input type="submit" className="btn" value="validate Otp"  / >
                                    </form>):(<>Good job { ValFinal }</>)
                                            )
                                    


                                  
                                  
                                  )
                                  )
                                        





                                      ): (<Login Loginfunc={Loginfunc} error={error} errorState={errorState}
                                         emailState={emailState} email={email} tokenState={tokenState} token={token}  />)
        }
                              </div>
      </div>
     



    </div>
  );
}

export default LoginPage;
