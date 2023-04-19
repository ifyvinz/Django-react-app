//import React from "react";
//import { useState } from 'react';


    /*const [task, setTask] = useState({
        title: "",
        description: ""
    })*/

const getCookie = (name) => {
     let cookieValue = null;
     if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if(cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
export default getCookie;
    
    
/*export const saveTask = (event) =>{
        event.preventDefault()
        const csrftoken = getCookie('csrftoken'); 
        console.log(getCookie('csrftoken'))
        
        let formData = new FormData()
        formData.append('title', task.title);
        formData.append('description', task.description);
        //formData.append('csrfmiddlewaretoken', csrfToken);
        //Post a message with REST API
        fetch('api/newPost', {
            method: 'POST',
            credentials: 'same-origin',
            
            headers: {
                'Accept': 'application/json',
                //'Access-Control-Allow-Credentials': true,
                //'Access-Control-Allow-Origin':'http://localhost:3000',
                'X-CSRFTOKEN':csrftoken
            },
            body: formData
        })
        .then(response => response.json())
        .then(data => {
              console.log(data)
              
        })
        .catch(err => console.log(err))
    }

 export const updateTitle = (e) =>{
     setTask({
      ...task,
      title: e.target.value
     });
    }

export const updateDescription = (e) =>{
            setTask({
             ...task,
             description: e.target.value
            })
        }

*/