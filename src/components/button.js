import React from "react";


const AddButtons = function ({name, onclick, color, id, toggle}){
    return(
        <button className={color} onClick={onclick} data-id={id} data-toggle={toggle}>{name}</button>
        
    );

}
export default AddButtons