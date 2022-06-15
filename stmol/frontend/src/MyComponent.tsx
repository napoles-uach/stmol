import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"

//import 3dmol from 3dmol
//import $3Dmol from "3dmol"
//import {$3Dmol} from "3dmol"


class MyComponent extends StreamlitComponentBase<any> {
  public render = (): ReactNode => {

    const title = this.props.args["title"]
    const subtitle = this.props.args["subtitle"]
    const body = this.props.args["body"]
    const link = this.props.args["link"]
    const color = this.props.args["color"]
    const Chemiscope = require("chemiscope")

    

 
/*    return (
      <span>
        <h1>{title}</h1>
        <h2>'3dmol'</h2>
        <h2>{subtitle}</h2>
        <p>{body}</p>
        <a href={link}>{link}</a>
        <script src="https://3Dmol.org/build/3Dmol-min.js" async></script>     
        <div style={{height: "400px", width: "400px", position: "relative"}} className='viewer_3Dmoljs' data-pdb='2POR' data-backgroundcolor='0xffffff' data-style='stick' ></div>
        
      </span>
      
    ) */

    return (
      
    
      <span>
        <h1>{title}</h1>
        <h2>{subtitle}</h2>
        <p>{body}</p>
        <a href={link}>{link}</a>


        <script src="https://3Dmol.org/build/3Dmol-min.js" async></script>
     

        <div style={{height: "400px", width: "400px", position: "relative"}} className='viewer_3Dmoljs' data-pdb='2POR' data-backgroundcolor="red" data-style='stick' >
        

      

        </div>

        

      </span>
    )

  }


}

export default withStreamlitConnection(MyComponent)
