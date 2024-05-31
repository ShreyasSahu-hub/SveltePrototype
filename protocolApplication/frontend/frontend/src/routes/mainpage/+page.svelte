<script lang="ts">
    import {TaskStore} from '../../task-store'
    import {onMount} from 'svelte'
    import {goto} from '$app/navigation';

    let taskDiv = '';

    async function fetchTask() {
       /*
       if (!$TaskStore.length){
         const endpoint = "http://localhost:8000/api/tasks/"
         const response = await fetch(endpoint)
         const data = await response.json()
         //console.log(data)
         TaskStore.set(data)
       }
       */

       // Append new tasks

       //var username=document.cookie;

       //console.log(username)

       let taskDiv = document.createElement('div');
       taskDiv.className = 'col-12 col-sm-6 col-md-4';
       taskDiv.id = "taskholder"

       let response1 = await fetch("http://localhost:8000/TaskFetched/",{

            method: 'GET',
            credentials: "include"

       })

       var b= await response1.json()

       console.log(b.taskDetail)

       taskdetail = b.taskDetail;

       console.log(taskdetail);

       const start = performance.now();

       b.taskDetail.forEach(task => {

            taskDiv.innerHTML += `
                <div id="${task.id}" class="card w-100 h-100">
                    <img class="card-img-top" style="height: 300px; object-fit: cover" src="${task.image}" alt="Task">
                    <div class="card-body d-flex flex-column justify-content-between gap-4">
                        <div>
                            <h5 class="card-title">${task.name}</h5>
                            <p class="card-text">ID: ${task.id}</p>
                            <p class="card-text">Starting date by ${task.date}</p>
                            <p class="card-text">Starting time by ${task.startTime}</p>
                            <p class="card-text">Amount of time by ${task.amountOfTime}</p>
                            <p class="card-text">The Description of the task ${task.descriptionOfTheTask}</p>
                        </div>
                    </div>
                </div>
            `;

       //document.body.appendChild(taskDiv);

       })

       taskDiv.style.visibility = "hidden";

       if(document.body.contains(document.getElementById("taskholder"))){

          document.body.removeChild(document.getElementById("taskholder"));

       }

       document.body.appendChild(taskDiv);

       const end = performance.now();

       console.log(`DOM fetching time took ${end - start} milliseconds.`);

       /*
       $TaskStore.forEach(task => {
            taskDiv.innerHTML += `
                <div id="${task.id}" style="display: none; height: 100px;" class="card w-100 h-100">
                    <img class="card-img-top" style="height: 300px; object-fit: cover" src="${task.image}" alt="Task">
                    <div class="card-body d-flex flex-column justify-content-between gap-4">
                        <div>
                            <h5 class="card-title">${task.name}</h5>
                            <p class="card-text">ID: {task.id}</p>
                            <p class="card-text">Starting date by ${task.date}</p>
                            <p class="card-text">Starting time by ${task.startTime}</p>
                            <p class="card-text">Amount of time by ${task.amountOfTime}</p>
                            <p class="card-text">The Description of the task ${task.descriptionOfTheTask}</p>
                        </div>
                    </div>
                </div>
            `;

       document.body.appendChild(taskDiv);
       });

       */

       console.log(document)

       //document.body.removeChild(taskDiv);

       console.log(document.getElementById("7"))

    }

    let name = '';
    let name1 = '';
    let date = '';
    let startTime = '';
    let amountOfTime = '';
    let descriptionOfTheTask = '';
    let query;
    let amountOfCalories;
    let dietType;
    let mealType;
    let files;
    let showInvalidMessage = false;
    let showTaskList = false;
    let id;
    let idimage;
    let deleteid;
    let errorMessage = '';
    let errorMessageForDelete = '';
    let queryForVideos = '';
    let listOfFoodItems = '';
    let taskdetail = [];

    async function handleSubmit(){
        //const endpoint = 'http://localhost:8000/api/tasks/'
        const a = 'http://localhost:8000/TaskInsert/'
        let data = new FormData()
        data.append('name', name)
        data.append('date', date)
        data.append('startTime', startTime)
        data.append('amountOfTime', amountOfTime)
        data.append('descriptionOfTheTask',descriptionOfTheTask)
        data.append('image', files[0])

        let response = await fetch(a,{

            method: 'POST',
            credentials: "include",
            body:data

        })

        var b= await response.json()

        console.log(b.task_detail[0].id)

        let element = document.getElementById('taskholder');

        console.log(element);

        if(element){
           console.log('Element with id "taskholder" exists.');
        }

        else{

           let taskDiv = document.createElement('div');
           taskDiv.className = 'col-12 col-sm-6 col-md-4';
           taskDiv.id = "taskholder"
           //taskDiv.innerHTML = ``;
           taskDiv.innerHTML = ``;

           document.body.appendChild(taskDiv);

        }

        const start = performance.now();

        document.getElementById("taskholder").innerHTML +=`
             <div id="${b.task_detail[0].id}" style="display: none; height: 100px;" class="card w-100 h-100">
              <img class="card-img-top" style="height: 300px; object-fit: cover" src="${b.task_detail[0].image}" alt="Task">
              <div>
               <h5 class="card-title">${name}</h5>
               <p class="card-text">ID: {b.task_detail[0].id}</p>
               <p class="card-text">Starting date by ${date}</p>
               <p class="card-text">Starting time by ${startTime}</p>
               <p class="card-text">Amount of time by ${amountOfTime}</p>
               <p class="card-text">The Description of the task ${descriptionOfTheTask}</p>
              </div>
             </div>
            </div>
        `;

        const end = performance.now();

        console.log(`DOM insertion time took ${end - start} milliseconds.`);

        /*
        fetch(endpoint, {method: 'POST', body: data}).then(response => response.json()).then(data => {
            TaskStore.update(prev => [...prev, data]),
            console.log(data.id)

            document.getElementById("taskholder").innerHTML +=`
             <div id="${data.id}" style="display: none; height: 100px;" class="card w-100 h-100">
              <img class="card-img-top" style="height: 300px; object-fit: cover" src="${data.image}" alt="Task">
              <div>
               <h5 class="card-title">${name}</h5>
               <p class="card-text">ID: {task.id}</p>
               <p class="card-text">Starting date by ${date}</p>
               <p class="card-text">Starting time by ${startTime}</p>
               <p class="card-text">Amount of time by ${amountOfTime}</p>
               <p class="card-text">The Description of the task ${descriptionOfTheTask}</p>
              </div>
             </div>
            </div>
        `;
        console.log(document)

        })

        */

        console.log(document)

        goto('/mainpage/')
    }

    async function handleDelete(deleteid){

        errorMessageForDelete = '';

        /*
        const taskchecker = $TaskStore.find(task => task.id ==deleteid);

        if(!taskchecker){
            errorMessageForDelete = 'Invalid task ID. Please enter a valid ID.';
            return;
        }
        */

        let response = await fetch("http://localhost:8000/TaskDelete/",{

           method: 'POST',
           credentials: "include",
           body: JSON.stringify({
                task_id: deleteid,
           })
        })

        /*
        if(response.status!=200){
            errorMessageForDelete = 'Invalid task ID. Please enter a valid ID.';
            return;
        }

        else{
        */

        taskdetail = taskdetail.filter(task => task.id !== deleteid);

        const start = performance.now();
        document.getElementById(deleteid).innerHTML = ``;
        const end = performance.now();

        console.log(`DOM deletion time took ${end - start} milliseconds.`);

        /*
        }
        */

        /*
        const endpoint = `http://localhost:8000/api/tasks/${deleteid}`
        fetch(endpoint, {method: 'DELETE'}).then(response => {
            if (response.status == 204) {
                TaskStore.update(prev => prev.filter(task => task.id != deleteid))
            }
        })
        */

        //document.getElementById(deleteid).innerHTML = ``;

        console.log(document)

    }

    async function handleUpdate(){

        //id = data.id

        //console.log(`${id}`);

        //console.log(taskDiv);

        errorMessage = '';
        //const taskchecker = $TaskStore.find(task => task.id ==id);

        //if(!taskchecker){
        //    errorMessage = 'Invalid task ID. Please enter a valid ID.';
        //    return;
        //}

        //const endpoint = `http://localhost:8000/api/tasks/${id}/`
        let data = new FormData()
        data.append('id', id)
        data.append('name', name1)
        data.append('date', date)
        data.append('startTime', startTime)
        data.append('amountOfTime', amountOfTime)
        data.append('descriptionOfTheTask', descriptionOfTheTask)

        //if (files) {
        data.append('image', files[0])
        //}

        console.log(files)

        let response = await fetch("http://localhost:8000/TaskUpdate/",{

           method: 'POST',
           credentials: "include",
           body: data

        })

        if(response.status!=200){
            errorMessage = 'Invalid task ID. Please enter a valid ID.';
            return;
        }

        else{

        let b= await response.json()

        console.log(b)

        console.log(files)

        const start = performance.now();

        document.getElementById(id).innerHTML = `
            <div class="card-body d-flex flex-column justify-content-between gap-4">
              <img class="card-img-top" style="height: 300px; object-fit: cover" src="${b.update_task[0].image}" alt="Task">
              <div>
               <h5 class="card-title">${name1}</h5>
               <p class="card-text">ID: ${id}</p>
               <p class="card-text">Starting date by ${date}</p>
               <p class="card-text">Starting time by ${startTime}</p>
               <p class="card-text">Amount of time by ${amountOfTime}</p>
               <p class="card-text">The Description of the task ${descriptionOfTheTask}</p>
              </div>
            </div>
        `;

         const end = performance.now()

         console.log(`DOM updating time took ${end - start} milliseconds.`);

        /*

        fetch(endpoint, {method: 'PUT', body: data}).then(response => response.json()).then(data => {
            TaskStore.update(prev => {
                let updatedTasks = $TaskStore.slice()
                let index = updatedTasks.findIndex(task => task.id == id)
                updatedTasks[index] = data
                return updatedTasks
            })
        })

        let taskimageURL = {}

        taskimageURL = $TaskStore.find(task => task.id == id)

        document.getElementById(id).innerHTML = `
            <div class="card-body d-flex flex-column justify-content-between gap-4">
              <img class="card-img-top" style="height: 300px; object-fit: cover" src="${taskimageURL.image}" alt="Task">
              <div>
               <h5 class="card-title">${name}</h5>
               <p class="card-text">Starting date by ${date}</p>
               <p class="card-text">Starting time by ${startTime}</p>
               <p class="card-text">Amount of time by ${amountOfTime}</p>
               <p class="card-text">The Description of the task ${descriptionOfTheTask}</p>
              </div>
            </div>
        `;

         */

        console.log(document)

        }

        /*
        let task = {}

        if ($TaskStore.length) {
            task = $TaskStore.find(task => task.id == id)
        } else {
            const endpoint = `http://localhost:8000/api/tasks/${id}/`
            let response = await fetch(endpoint)
            if (response.status == 200) {
                task = await response.json()
            } else {
                task = null;
            }
        }
        ({name, date, startTime, amountOfTime, descriptionOfTheTask} = task)
        */

    }

    async function handleVideos(){

        document.getElementById("returnedVideos").innerHTML = ``;

        console.log(queryForVideos)

        fetch('https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=5&q=' + queryForVideos + '&type=video&key=AIzaSyA20OFgpO9qgwShY_S5PBzh3_Uw2-o3v4k')
        .then(result => result.json())
        .then(data=>{
           console.log(data)
           data.items.forEach(a => {
               document.getElementById("returnedVideos").innerHTML += `
               <p class="card-text">
               <a href="https://www.youtube.com/watch?v=${a.id.videoId}" class="yt-=video">
                   <img src="${a.snippet.thumbnails.high.url}"/>
                   <h3>${a.snippet.title}</h3>
               </a>
               </p><br><br>
               `
           })
        })

    }

    async function calorieTracker(){

       //try{
       const URLCalories = "https://api.edamam.com/api/nutrition-data?app_id=c5d32486&app_key=edd240211b6512dcb06d0ee3069929d3	&ingr=" + listOfFoodItems
       const response = await fetch(URLCalories);
       const data = await response.json();
       console.log(data);
       document.querySelector("#calorietracker").innerHTML = `<h3 class="card-text">Calories in Kcal: ${data.calories}</h3>`;
       //}

       //catch(err){

       //   document.querySelector("#calorietracker").innerHTML = err.message;

       //}

       if(data.calories!=0){

         var today = new Date();
         var dd = String(today.getDate()).padStart(2,'0');
         var mm = String(today.getMonth()+1).padStart(2,'0');
         var yyyy = today.getFullYear();

         var today = `${dd}/${mm}/${yyyy}`

         var fd = new FormData();
         fd.append('listoffooditems', data.calories)
         fd.append('dateinserted', today)
         let response1 = await fetch("http://localhost:8000/CalorieTracker/",{
            method: 'POST',
            credentials: "include",
            body: fd
         })

       }

    }

    function settingTheVariableToTrue(){

       showTaskList = true;

    }


    async function handleEDAMAMAPI() {
     let APP_ID = "f0809293";
     let API_KEY = "4c9901ef9b16a44f50887e1926d8a00b";
     const URL = "https://api.edamam.com/api/recipes/v2?type=public&q=" + query + "&app_id=f0809293&app_key=4c9901ef9b16a44f50887e1926d8a00b&diet=" + dietType + "&calories=" + amountOfCalories + "&mealType=" + mealType;
     const response = await fetch(URL);
     const data = await response.json();
     console.log(data);

     document.querySelector("#content").innerHTML = "";

     for (let i = 0; i < data.hits.length; i++) {
        for (let j = 0; j < data.hits[i].recipe.dishType.length; j++) {
            document.querySelector("#content").innerHTML += `
            <div class="card" style="width: 18rem;">
                <img src="${data.hits[i].recipe.image}" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">${data.hits[i].recipe.label}</h5>
                    <p class="card-text">Source: ${data.hits[i].recipe.source}</p>
                    <p class="card-text">Meal Type: ${data.hits[i].recipe.mealType}</p>
                    <p class="card-text">Diet Type: ${data.hits[i].recipe.dietLabels}</p>
                    <p class="card-text">Calories in Kcal: ${Math.round(data.hits[i].recipe.calories)} kcal</p>
                    <p style="background-color: powderblue;" class="card-text">Here are the list of health labels to prevent your food allergies if you have any: ${data.hits[i].recipe.healthLabels}</p>
                    <a href="${data.hits[i].recipe.url}" class="btn btn-primary">Click here to find more information about that recipe</a>
                </div>
            </div>
            `;
            break;
        }
     }
   }



</script>

<style>

@keyframes gradientAnimation {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}

.animated-background {
    background: linear-gradient(270deg, #ff7e5f, #feb47b);
    background-size: 400% 400%;
    animation: gradientAnimation 15s ease infinite;
}

</style>

<div class="p-3 mb-2 bg-light text-dark rounded shadow-sm animated-background">

    <br><h2 class="my-4">Add a Task</h2><br>

    <div class="col-12 col-md-6">
        <form on:submit|preventDefault={handleSubmit}>
            <div class="mb-3">
                <legend for="name1">Enter the name of the task</legend><br>
                <input class="form-control" type="text" placeholder="name" id="name1" name="name1" bind:value={name} required/>
            </div>
            <div class="mb-3">
                <legend for="date">Enter the date to start the task</legend><br>
                <input class="form-control" type="date" placeholder="date" id="date1" name="date" bind:value={date} required/>
            </div>
            <div class="mb-3">
                <legend for="time">Enter the time to start the task</legend><br>
                <input class="form-control" type="time" placeholder="start Time" id="startTime1" name="startTime" bind:value={startTime} required/>
            </div>
            <div class="mb-3">
                <legend for="amountOfTime">Enter the amount of time to spend the task</legend><br>
                <input class="form-control" type="time" placeholder="Amount of to spend" id="amountOfTime1" name="amountOfTime" bind:value={amountOfTime} required/>
            </div>
            <div class="mb-3">
                <legend for="descriptionOfTheTask">Write the description of the task</legend><br>
                <input class="form-control" type="text" placeholder="description of the task" id="descriptionOfTheTask1" name="descriptionOfTheTask" bind:value={descriptionOfTheTask} required/>
            </div>
            <div class="mb-3">
                <legend for="uploadingTheImage">Upload the image</legend><br>
                <input class="form-control" type="file" id="image" name="filename" bind:files required/>
            </div>
            <button class="btn btn-primary" type="submit">Submit</button>
        </form>
    </div>

</div>

<br>

<div class="p-3 mb-2 bg-light text-dark rounded shadow-sm animated-background">

    <form on:submit|preventDefault={fetchTask}>

      <button class="btn btn-primary" type="submit">Fetch the tasks</button>

    </form>
    <br>

    <h2 class="my-4">Task List</h2>
    <div class="my-4 row">
        {#each taskdetail as task}
        <div class="col-12 col-sm-6 col-md-4">
            <div class="card w-100 h-100">
                <img class="card-img-top" style="height: 300px; object-fit: cover"
                    src={task.image}
                    alt="Task">
                <div class="card-body d-flex flex-column justify-content-between gap-4">
					<div>
                        <h5 class="card-title">{task.name}</h5>
                        <p class="card-text">ID: {task.id}</p>
                        <p class="card-text">Starting date by {task.date}</p>
                        <p class="card-text">Starting time by {task.startTime}</p>
                        <p class="card-text">Amount of time by {task.amountOfTime}</p>
                        <p class="card-text">The Description of the task {task.descriptionOfTheTask}</p>
                    </div>
                    <div>
                        <!--<a href="/mainpage/{task.id}" class="btn btn-primary">View</a>-->

                        <a href="/mainpage/{task.id}/update" class="btn btn-primary">Update</a>

                        <button on:click = {() => handleDelete(task.id)} class="btn btn-danger ml-2">
                            Delete
                        </button>

					</div>
                </div>
            </div>
        </div>
        {/each}
    </div>
</div>
<br>

<!--
<div class="p-3 mb-2 bg-light text-dark rounded shadow-sm animated-background">
    <h2 class="my-4">Diet Plan</h2>

    <div class="col-12 col-md-6">
        <form on:submit|preventDefault={handleEDAMAMAPI}>
            <div class="mb-3">
                <input class="form-control" type="text" placeholder="query" bind:value={query} required/>
            </div>
            <div class="mb-3">
                <input class="form-control" type="text" placeholder="amount of calories in kcal" bind:value={amountOfCalories} required/>
            </div>
            <div class="mb-3">
            <h5 class="my-4">Diet Type</h5>
            <select bind:value={dietType} required>
              <option value="balance">Balance</option>
              <option value="high-fiber">High-Fiber</option>
              <option value="high-protein">High-Protein</option>
              <option value="low-carb">Low-Carb</option>
              <option value="low-fat">Low-Fat</option>
              <option value="low-sodium">Low-Sodium</option>
            </select>
            </div>
            <div class="mb-3">
            <h5 class="mb-4">Meal Type</h5>
            <select bind:value={mealType} required>
              <option value="breakfast">Breakfast</option>
              <option value="brunch">Brunch</option>
              <option value="lunch">Lunch</option>
              <option value="dinner">Dinner</option>
              <option value="snack">Snack</option>
              <option value="teatime">TeaTime</option>
            </select>
            </div>
            <button class="btn btn-primary" type="submit">Submit</button>
        </form>
    </div>
    <div id="content"></div>

</div>

<br>
-->

<!--
<div class="p-3 mb-2 bg-light text-dark rounded shadow-sm animated-background">

    <h2 class="my-4">Update a Task</h2>

    <div class="col-12 col-md-6">
        <form on:submit|preventDefault={handleUpdate}>
            <div class="mb-3">
                <legend for="name">Enter the name of the task</legend><br>
                <input class="form-control" type="text" placeholder="name" bind:value={name1} required/>
            </div>
            <div class="mb-3">
                <legend for="date">Enter the date to start the task</legend><br>
                <input class="form-control" type="date" placeholder="date" bind:value={date} required/>
            </div>
            <div class="mb-3">
                <input class="form-control" type="time" placeholder="start Time" bind:value={startTime} required/>
            </div>
            <div class="mb-3">
                <input class="form-control" type="time" placeholder="Amount of to spend" bind:value={amountOfTime} required/>
            </div>
            <div class="mb-3">
                <input class="form-control" type="text" placeholder="description of the task" bind:value={descriptionOfTheTask} required/>
            </div>
            <div class="mb-3">
                <input class="form-control" type="file" bind:files required/>
            </div>

            <button class="btn btn-primary" type="submit">Submit</button>
        </form>
    </div>

</div>

<br>
-->
<!--
<div class="p-3 mb-2 bg-light text-dark rounded shadow-sm animated-background">

   <h2 class="my-4">Delete a Task</h2>

   <div class="col-12 col-md-6">

      <form on:submit|preventDefault={handleDelete}>
         <div class="mb-3">
             <input class="form-control" type="number" placeholder="Type the id" bind:value={deleteid}/>
             {#if errorMessageForDelete}
               <p class="text-danger">{errorMessageForDelete}</p>
             {/if}
         </div>

         <button class="btn btn-primary" type="submit">Delete</button>
      </form>
   </div>

</div>
-->

<!--
<br>

<div class="p-3 mb-2 bg-light text-dark rounded shadow-sm animated-background">
  <h2 class="my-4">Find exercise videos</h2>
  <div class="col-12 col-md-6">
     <form on:submit|preventDefault={handleVideos}>
      <label>Enter the exercise videos that you want:</label>
         <div class="mb-3">
             <input class="form-control" type="text" placeholder="query" bind:value={queryForVideos}/>
         </div>
         <button class="btn btn-primary" type="submit">Fetch videos</button>
     </form>
  </div>
  <br>
  <br>
</div>

<div>
   <div class="card-body d-flex flex-column justify-content-between gap-4">
        <div id="returnedVideos" class="row">
        </div>
   </div>
</div>

<br>
-->

<!--
<div class="p-3 mb-2 bg-light text-dark rounded shadow-sm animated-background">
  <h2 class="my-4">Calorie tracker</h2>
  <form on:submit|preventDefault={calorieTracker}>
    <label>Enter the food items here</label>
       <div class="mb-3">
           <input class="form-control" type="text" placeholder="Enter the food item" bind:value={listOfFoodItems}/>
       </div>
       <button class="btn btn-primary" type="submit">Fetch the amount of calories intaken</button>
  </form>
  <br>
  <div id="calorietracker"></div>
</div>

<br>

<a href="/mainpage/calorieHistory/"><button class="btn btn-primary"  type="submit">See your Calorie History</button></a><br><br>

<br>
-->
