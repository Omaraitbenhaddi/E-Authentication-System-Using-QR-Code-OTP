import React, { Component } from 'react'
import bg1 from "../img/bg.svg"


class Background extends Component {
  render(){
    return (
      <div className='tout'>
  
          <div className="img">
              {(this.props.name!="")?(<div></div>):(<img src={bg1} alt=""/>)}
          </div>
      </div>
    )
  }
}

export default Background