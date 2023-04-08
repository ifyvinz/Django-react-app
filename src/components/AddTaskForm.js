import React from "react";
//import { Form, FormGroup } from "react-bootstrap";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
//import getCookie from './Apis/SubmitTask';
//import { useState } from 'react';

const TaskForm = ({title, description, onChangeTitle, onChangeDescript, cookies, onSubmit}) =>{
    /*const [task, setTask] = useState({
        title: "",
        description: ""
    })*/

   /*const getCookie = (name) => {
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
  }*/
    
    
   /*const saveTask = (event) =>{
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
    }*/

   /*const updateTitle = (e) =>{
     setTask({
      ...task,
      title: e.target.value
     });
    }

   const updateDescription = (e) =>{
            setTask({
             ...task,
             description: e.target.value
            })
 
         }*/
    //const csrftoken = getCookie('csrftoken');
    //value={cookies}
    return (
        <Form onSubmit={onSubmit}> 
          <Form.Group className="mb-3" controlId="formtoken" >
            <Form.Control type="hidden" name="csrfmiddlewaretoken"  /> {/* Add the CSRF token as a hidden input */} 
          </Form.Group>
          <Form.Group className="mb-3" controlId="formTitle" >
            <Form.Label>Title</Form.Label>
            <Form.Control type="text" name ="title" value = {title} onChange={onChangeTitle} placeholder="Task title" />
          </Form.Group>
          <Form.Group className="mb-3" controlId="formDescription">
            <Form.Label>Description</Form.Label>
            <Form.Control as="textarea" name= "description" value = {description} onChange={onChangeDescript} rows={3} />
          </Form.Group>
          <Form.Check type="switch" id="custom-switch" label="Completed"/>
         <Button variant="primary" type="submit">
           Submit
         </Button>
       </Form>   
    )
}

export default TaskForm;

   