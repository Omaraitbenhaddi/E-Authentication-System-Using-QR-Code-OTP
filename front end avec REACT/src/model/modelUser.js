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

export default loginUser;
