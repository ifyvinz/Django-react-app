
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

const TaskCompleted = async (taskId) =>{
    try{
        const response = await fetch(`api/${taskId}/setCompleted`,{
            method: 'PUT',
            credentials: 'same-origin',
            headers: {
                'Accept': 'application/json',
                'X-CSRFTOKEN':getCookie('csrftoken')
            },
            body: JSON.stringify({
                id: taskId
            })
        })
        const data = await response.json()
        
        return data.tasks
        
    }catch(err){
        console.log(err)
    }
}
export default TaskCompleted;