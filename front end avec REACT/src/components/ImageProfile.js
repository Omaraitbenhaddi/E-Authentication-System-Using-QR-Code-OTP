import React,{ useState } from 'react'
import Profile from "../img/prof.svg"


function ImageProfile(props) {

    const [open,StateOpen]=useState(false)

  return (
    <>
    <div className='container_pdp'>
        <button onClick={()=>{StateOpen(!open)}} className="button_profile pdp"><img  src={Profile} className="pdp"  alt=""/></button>


    </div>
            <div className={`Dropdownmenu ${open? 'active' : 'inactive'}`}>

            <DropDownItems text="Logout" logout={props.Logout_}/>

        </div>
    </>

  )
}

function DropDownItems(props){
    return(
        <div className='dropDownitem'> 
                <a href='/' onClick={props.logout}>{ props.text }</a>
        </div>
    );
}

export default ImageProfile