<script lang="ts">
    import {onMount} from 'svelte'      //importing the onMount function from the svelte library, where the web page directly displays the available visual components

    let taskDiv = '';                   //This is a variable called taskDiv, which is initialized to an empty string for now. Later, when the fetchTask function is called when the user clicks the button called "Fetch the tasks"

    let taskdetail = [];

    async function fetchTask() {       //As soon as the user clicks the "Fetch the tasks" button, this function gets called.



       let taskDiv = document.createElement('div');           //A HTML element called div is created in the DOM tree and gets stored in the taskDiv variable
       taskDiv.className = 'col-12 col-sm-6 col-md-4';         //The css class of that div element is set 'col-12 col-sm-6 col-md-4', which is a predefined bootstrap css class that displays the task details which covers 4 columns of its container
       taskDiv.id = "taskholder";                              //The id the div element is set to a value called taskholder



       //A variable called response1 is created that calls the Django endpoint fetch URL with the http GET method to retrieve the task details that are stored in the database. It waits for the results to be returned from the URL by using the await keyword.
       //The credentials field is set to the include value, allows the website to return the task details that belongs to the user by storing the user's username, which uniquely identifies the users.



       let response1 = await fetch("/TaskFetched/",{

            method: 'GET',
            credentials: "include"

       })

       //Once the Django endpoint fetch URL returns the task details, it gets converted to a JSON format,
       //which is one type of data format that is structures the data into a dictionary data structure.
       //It gets stored in the b variable.

       var b= await response1.json()



       //It prints the JSON formatted task details into the console in the built-in inspect section that is provided by Google.
       //This is necessary to check if the fetchTask function returns the expected outcome

       console.log(b.taskDetail)



       //The b variable has got a taskDetail field and it gets accessed by the . notation. Then it gets stored in the taskdetail varaible.

       taskdetail = b.taskDetail;



       //It gets printed into the console to double check, if the field is accessed perfected or not.

       console.log(taskdetail);



       //This iterates all the nested fields inside the taskDetail fields and integrate it with the HTML elements. Then it gets stored in the div element which is defined by the taskDive variable.

       b.taskDetail.forEach(task => {

            //The HTML elements below displays the task details into cards where the details are displayed on white boxes which looks like cards, where the width and the height takes up to 100 pixels.
            //The card's size can be adjusted when the user changes the browser's size.

            taskDiv.innerHTML += `
                <div id="${task.id}" class="card w-100 h-100" style="display: none;>
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

       })

       taskDiv.style.visibility = "hidden";



       //This if statement prevents the task details to be displayed again on the screen every time the user clicks the fetch button

       if(document.body.contains(document.getElementById("taskholder"))){

          document.body.removeChild(document.getElementById("taskholder"));

       }



       //Whatever HTML elements that are contained in the div element gets added as a child node to the DOM tree.

       document.body.appendChild(taskDiv);




       //The start variable is created and it cannot be changed due to the const keyword. It stores the start time at which the HTML elements with the task details are fetched from the div element

       const start = performance.now();


       //This where the document is printed on the screen to see the fetched HTML elements.

       console.log(document.getElementById("taskholder"));



       //It records the finishing time after the HTML elements with the task details are inserted to the DOM.

       const end = performance.now();



       console.log(document)



       //The time taken for the DOM to fetch the HTML elements with the task details
       console.log(`DOM fetching time took ${end - start} milliseconds.`);


    }


    onMount(fetchTask);

    //These are the variables initialised to store whatever data that the user has inserted into the form.

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
    //let taskdetail = [];



    //This function inserts task details that the user has typed into the add task form, by storing it into the database via Django insertion endpoint URL.

    async function handleSubmit(){



        //This endpoint variable cannot be changed due to the const keyword and it stores the Django URL for task detail insertion.

        const endpoint = '/TaskInsert/'



        //The instance of the form data is created in order to store what task details that the user has inserted in the add task form

        let data = new FormData()



        //This is where all the task details that the user has typed are stored into the corresponding fields on the first argument,
        //which are name, date, startTime
        //amountOfTime, descriptionOfTheTask, and image.

        data.append('name', name)
        data.append('date', date)
        data.append('startTime', startTime)
        data.append('amountOfTime', amountOfTime)
        data.append('descriptionOfTheTask',descriptionOfTheTask)
        data.append('image', files[0])



        //The Django endpoint URL is called by using the http POST request.
        //Whatever the user has typed and whatever image that the user inserted are stored in the data variable.
        //The fetch function returns the inserted task details

        let response = await fetch(endpoint,{

            method: 'POST',
            credentials: "include",
            body:data

        })



        //The inserted task details are converted into the JSON format.

        var b= await response.json()



        //This checks if the div element with the id called taskholder exists or not. If not then create a div element with that id and add it to the DOM tree.

        let element = document.getElementById('taskholder');

        console.log(element);

        if(element){
           console.log('Element with id "taskholder" exists.');
        }

        else{

           let taskDiv = document.createElement('div');
           taskDiv.className = 'col-12 col-sm-6 col-md-4';
           taskDiv.id = "taskholder"
           taskDiv.innerHTML = ``;

           document.body.appendChild(taskDiv);

        }



        //This records the starting time to insert HTML elements with the user defined task details into the DOM tree.

        const start = performance.now();



        //The user defined task details are integrated with the HTML elements that has got css card style, which are defined by the bootstrap library.

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



        //It records the finishing time where the HTML elements with task details are inserted to the DOM tree.

        const end = performance.now();



        //The time taken to insert HTML elements with task details is calculated below.

        console.log(`DOM insertion time took ${end - start} milliseconds.`);

        console.log(document)

        await fetchTask();
    }



    //This function deletes the task details. The deleteid is a placeholder that stores the current id of the task that the delete button is in

    async function handleDelete(deleteid){



        //The Django endpoint URL for task detail deletion, by using the POST http request
        //The deleteid parameter is stored to the task_id field, in order for the function that is mapped to the endpoint URL in the view.py file to receive the task id,
        //in order to remove the task details.
        //The JSON.stringify method converts the task_id variable to task id mapping to a JSON format, so that the corresponding function can access the task id easily.

        let response = await fetch("/TaskDelete/",{

           method: 'POST',
           credentials: "include",
           body: JSON.stringify({
                task_id: deleteid,
           })
        })


        taskdetail = taskdetail.filter(task => task.id !== deleteid);


        //It records the starting time where the HTML elements with task details to delete.

        const start = performance.now();
        document.getElementById(deleteid).innerHTML = ``;



        //It records the ending time where the HTML elements with task details to delete.

        const end = performance.now();




        //This calculates the time taken to delete the HTML elements that corresponds to the deleted task details.

        console.log(`DOM deletion time took ${end - start} milliseconds.`);

        console.log(document)

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

.button-container {
     display: flex;
     justify-content: center; /* Horizontally center the button */
     align-items: center;    /* Vertically center the button if needed */
     height: 50px;
}
</style>



<!-- The link HTML tag refers to the bootstrap library where predefined classes are imported to style the navbar with its corresponding style-->

<head>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet">

</head>



<!--This is where the forms are developed on the main page-->

<!-- The on:submit|preventDefault={} notation on the form tag is where the once the user submits the form with their desired details the javascript functions -->

<!-- that are defined above are called and its defined code gets executed.

<!-- The bind:value syntax stores whatever text that the user typed in the text fields or in the multiple choice fields to the variables specified in the curly braces. -->

<!-- The bind:files syntax stores the image URL path that the user has downloaded-->

<!-- The anchor tag which is denoted by <a> creates a link the to the URL which is defined in the href field, which leads you to that URL once you click the link.-->

<!-- Its mapping to the specific webpage is defined in the router.js file -->

<!-- This is the HTML structure to build the navigation bar -->

<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="/#/mainpage">Navbar</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
            <li class="nav-item">
                <a class="nav-link" href="/#/CalorieTracker">Calorie Tracker</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="/#/FetchingExercisingVideos">Fetching exercise videos</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="/#/automatedTesting">testing</a>
            </li>
        </ul>
      </div>
    </div>
</nav>



<!-- This is the HTML element to develop the add task form -->

<div class="p-5 mb-4 bg-light text-dark rounded shadow-sm animated-background">

        <form method="POST" enctype="multiple/form-data" on:submit|preventDefault={handleSubmit}>
            <br><h2 class="form-title">Add a Task</h2><br>
            <div class="row">
            <div class="col">
                <legend for="name1">Enter the name of the task</legend><br>
                <input class="form-control" type="text" placeholder="name" id="name1" name="name1" bind:value={name} required/>
            </div>
            <div class="col">
                <legend for="date">Enter the date to start the task</legend><br>
                <input class="form-control" type="date" placeholder="date" id="date1" name="date" bind:value={date} required/>
            </div>
            </div>
            <div class="row">
            <div class="col">
                <legend for="time">Enter the time to start the task</legend><br>
                <input class="form-control" type="time" placeholder="start Time" id="startTime1" name="startTime" bind:value={startTime} required/>
            </div>
            <div class="col">
                <legend for="amountOfTime">Enter the amount of time to spend the task</legend><br>
                <input class="form-control" type="time" placeholder="Amount of to spend" id="amountOfTime1" name="amountOfTime" bind:value={amountOfTime} required/>
            </div>
            </div>
            <div class="row">
            <div class="col">
                <legend for="descriptionOfTheTask">Write the description of the task</legend><br>
                <input class="form-control" type="text" placeholder="description of the task" id="descriptionOfTheTask1" name="descriptionOfTheTask" bind:value={descriptionOfTheTask} required/>
            </div>
            <div class="col">
                <legend for="uploadingTheImage">Upload the image</legend><br>
                <input class="form-control" type="file" id="image" name="filename" bind:files required/>
            </div>
            </div>
            <br>
            <div class="button-container">
            <button class="btn btn-primary" type="submit">Submit</button>
            </div><br>
        </form>

</div>

<br>



<!-- This is the HTML element to develop the Task List form -->

<div class="p-3 mb-2 bg-light text-dark rounded shadow-sm animated-background">

    <h2 class="my-4">Task List</h2>



    <!-- It iterates all the task details that is stored in the taskdetail variable and displays it as card one at a time. -->

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
                        <p class="card-text">Amount of time by {(task.amountOfTime).split(":")[0]} hours and {(task.amountOfTime).split(":")[1]} minutes</p>
                        <p class="card-text">The Description of the task {task.descriptionOfTheTask}</p>
                    </div>
                    <div>

                        <a href="/#/mainpage/{task.id}" class="btn btn-primary">Update</a>



                        <!-- This is where delete button is created. Once the user clicks this button then task id gets passed to the javascript handleDelete function-->

                        <!-- It defined above. -->

                        <!-- That function gets called and its code gets executed -->

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
