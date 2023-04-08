//import React, { useCallback } from 'react';
import AddButtons from './components/button.js'
import TaskForm from './components/AddTaskForm.js'
import Task from './components/listTask.js';
import DeleteTask from './Apis/TaskDelete.js';
import TaskCompleted from './Apis/CompletedTask.js'
import getCookie from './Apis/SubmitTask';
import { useState, useEffect } from 'react';



const App = () =>{
 const [ToggleAddButton, setToggleAddButton] = useState({toggle: false, })

 const [tasks, setTasks] =  useState([])

 const fetchApiTasks = async()=>{
     try{
      const response = await fetch(`api/todoList`)
      const data = await response.json()
      
      return data.todoList
      
      //.catch(error => console.log(error))
     }catch(error){
        console.log(error)
     }
  } 
     
 
   
  
  useEffect(() =>{
    const fetchTasks = async() =>{
      const getTasks = await fetchApiTasks()
      setTasks(getTasks)
    }
    fetchTasks()

  },[]);
    
 const AddButtonToggle = () =>{
  console.log(typeof(tasks))
      return setToggleAddButton({
        toggle:!ToggleAddButton.toggle
      })
  }
 const HandleDelete =(e) =>{
    const taskId = e.target.dataset.id
    console.log("about to delete")
    const aboutToDelete = async () =>{
      if (window.confirm('Are you sure you want to delete this post?')){
        const allTasks = await DeleteTask(taskId)
        console.log(allTasks)
        setTasks(allTasks)
      }
      
    }
    aboutToDelete()
 }

 const handleCheck =(e) =>{
  const taskId = e.target.dataset.id
  console.log("about to delete")
  const aboutToDelete = async () =>{
 
      const allTasks = await TaskCompleted(taskId)
      console.log(allTasks)
      setTasks(allTasks)
    
    
  }
  aboutToDelete()
}
  
  const [SubmitTask, setSubmitTask] = useState({
    title: "",
    description: ""
  })
  const updateTitle = (e) =>{
    setSubmitTask({
     ...SubmitTask,
     title: e.target.value
    });
   }

  const updateDescription = (e) =>{
    setSubmitTask({
      ...SubmitTask,
        description: e.target.value
      })

  }
  const SubmitTaskRequest  = async (event) =>{
    event.preventDefault()
    const csrftoken = getCookie('csrftoken'); 
    console.log(csrftoken )
    
    let formData = new FormData()
    formData.append('title', SubmitTask.title);
    formData.append('description', SubmitTask.description);
    //formData.append('csrfmiddlewaretoken', csrfToken);
    //Post a message with REST API
    try{
      const response = await fetch('api/newPost', {
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
       const data = await response.json()
       //setTasks([...tasks, data.task])
       setTasks(data.task)
            
        console.log(data.message)
        console.log(data.task)
        console.log(".................Done")
        console.log(tasks.title)
        console.log(tasks.description)
        console.log(data)
        setToggleAddButton({
            toggle: !ToggleAddButton.toggle
    
        })
      }   
  
    catch(err){
      console.log(err)
    }
  }
  
  //<AddButtons name="Add Task"  onclick={AddButtonToggle} color={"btn btn-dark"} toggle={ToggleAddButton}/>
  // <button className='{"btn btn-dark"}' onClick={AddButtonToggle}>{"Add Task"}</button>
  return (
      <main className="container">
           <h1 className="text-white text-uppercase text-center my-4">Todo app</h1>
            <div className="row">
              <div className="col-md-6 col-sm-10 mx-auto p-0">
                <div className="card p-3">
                  <div className="mb-4">
                    <AddButtons name="Add Task"  onclick={AddButtonToggle} color={"btn btn-dark"} toggle={ToggleAddButton}/>
                    <br />
                    <br />
                    {ToggleAddButton.toggle && <TaskForm title={SubmitTask.title} description={SubmitTask.description}
                          onChangeTitle={updateTitle} onChangeDescript={updateDescription}  onSubmit={SubmitTaskRequest} />}
                  </div>
                  
                </div>
                
              </div>
            </div>
            
            { !ToggleAddButton.toggle && tasks.map(task =>{ return <div className="row" key={task.id} >
               <div className={`col-md-6 col-sm-10 mx-auto p-0 ` }>  
                  <div className={`card p-3 ${task.completed ? "reminder" : ""}`}>
                     <div className="mb-4" >
                        
                          <Task  task={task}  onclick={HandleDelete} onChange={handleCheck}/>
                        
                     </div>
                  </div>
               </div>
            </div>})}
       </main>
    );
  }
export default App;