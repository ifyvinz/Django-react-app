import React from "react";
//import { Button } from "react-bootstrap";
//import Form from 'react-bootstrap/Form';
import AddButtons from './button.js'
//import { useState, useEffect } from 'react';

const Task = ({task, onclick, onChange}) =>{
   
  return (
       
    <div >
               
      <div ><span><strong>{task.title}</strong> by @{task.author} on {task.timestamp}</span>
      <p>{task.description}</p>
      <div className="Delete">
        </div>
         <AddButtons name="Delete"  color={"btn btn-danger"} id={task.id} onclick={onclick}/> 
         <div className="form-check form-switch">
            <input className="form-check-input" type="checkbox" role="switch" id="custom-switch" data-id={task.id} onChange={onChange} />
            <label className="form-check-label" data-for="flexSwitchCheckDefault">Complete</label>
          
         </div>
        
        </div>
     </div>
   );
        
}

export default Task;