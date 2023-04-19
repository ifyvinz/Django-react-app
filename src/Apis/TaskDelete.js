//import React from "react";
//import { useState, useEffect } from 'react';


//const [tasks, setTasks] =  useState([])

/*useEffect(() =>{
    fetch(`api/todoList`)
        .then(response => response.json())
        .then(data =>{ 
          setTasks(data.todoList)
        } )
        .catch(error => console.log(error))
},[]);*/

const DeleteTask = async (taskId) =>{
    try{
        const response = await fetch(`api/${taskId}/deleteTask`,{
            method: 'DELETE'
        })
        const data = await response.json()
        return data.tasks
        
    }catch(err){
        console.log(err)
    }
}
export default DeleteTask;