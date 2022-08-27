
const logoutUser = async (token)=>{
    await fetch("http://127.0.0.1:8000/api/logout/",{
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'Authorization':`Token ${token}`
        },
        body:  {}
    });
}

export default logoutUser