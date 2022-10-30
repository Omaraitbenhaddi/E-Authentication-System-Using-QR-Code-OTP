
const ValiderOtp = async (credentiel,token)=>{
    const response = await fetch("http://127.0.0.1:8000/api/validate_otp/",{
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'Authorization':`Token ${token}`

        },
        body:  JSON.stringify(credentiel)
    });
    return await response.json();
}

export default ValiderOtp