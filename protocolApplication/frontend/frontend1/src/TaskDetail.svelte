<script lang="ts">
    import {pop} from "svelte-spa-router"          //importing the pop function from the svelte library called svelte-spa-router
    import {onMount} from 'svelte'               //importing the onMount function from the svelte library, where the web page directly displays the available visual components


    //These variables will store a value once the user has entered something in the updated task form

    let name = '';              //created a name variable to store the updated task name
    let date = '';              //created a date variable to store the updated date to start the task
    let startTime = '';            //created a startTime variable to store the time to start the updated task
    let amountOfTime = '';               //created a amountOfTime variable to store the amount of time to spend on the updated task
    let descriptionOfTheTask = '';            //created a descriptionOfTheTask variable to store the description of the updated description
    let files;           //created a files variable to store the Image URL path
    let showInvalidMessage = false;      //created a showInvalidMessage variable to store
    export let params;        //This variable stores the parameters of the current URL
    let id;         //This variable stores the task's id to locate which task to update


    //This javascript function is called as soon as the user clicks the submit button

    async function handleSubmit(){


        //An instance of the FormData object is create to store whatever the user has entered to its corresponding variables.
        //The corresponding variables are on the first arguement of the append function, which are id, name, date, startTime, amountOfTime, descriptionOfTheTask, and image.


        let data = new FormData()
        data.append('id', id)
        data.append('name', name)
        data.append('date', date)
        data.append('startTime', startTime)
        data.append('amountOfTime', amountOfTime)
        data.append('descriptionOfTheTask', descriptionOfTheTask)
        data.append('image', files[0])




        //The fetch function is called to pass the user inputs that are stored in the data variable above and stores it to the body field to pass the user inputs to the
        //python function that is mapped to the specific Django endpoint URL that is defined in url.py file in the MasterProject folder.
        //That python function will update the task details for the corresponding task's id
        //It uses the POST http method to update the task details
        //The credentials field stores the user's username to update the task that belongs to the user by comparing the username.



        let response = await fetch("/TaskUpdate/",{

           method: 'POST',
           credentials: "include",
           body: data

        })

        let data1 = await response.json()

        //console.log(data1.update_taskdetail.id)

        const start = performance.now();

        document.getElementById(data1.update_task[0].id).innerHTML = `
            <div class="card-body d-flex flex-column justify-content-between gap-4" style="display: none;>
              <img class="card-img-top" style="height: 300px; object-fit: cover" src="${data1.update_task[0].image}" alt="Task">
              <div>
               <h5 class="card-title">${data1.update_task[0].name}</h5>
               <p class="card-text">Starting date by ${data1.update_task[0].date}</p>
               <p class="card-text">Starting time by ${data1.update_task[0].startTime}</p>
               <p class="card-text">Amount of time by ${data1.update_task[0].amountOfTime}</p>
               <p class="card-text">The Description of the task ${data1.update_task[0].descriptionOfTheTask}</p>
              </div>
            </div>
        `;

        const end = performance.now();

        console.log(`DOM updating time took ${end - start} milliseconds.`);

        console.log(document)


        //This pop function automatically redirects to the previous page which is the main page.

        pop();

    }



    //The onMount function immediately extracts the id field from the URL parameter and scrolls up to the top of the webpage as soon as the user
    //Visits the update page, using the scrollIntoView() function on the root of the DOM, because that is where the webpage starts.

    onMount(async function() {
        id = params.id;
        document.body.scrollIntoView();
    })

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

<!-- The link HTML tag refers to the bootstrap library in the specified URL to import necessary css classes to style the navigation bar components-->
<!-- and the form to update the task's details-->



<head>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet">

</head>




<!--This is the HTML tags to develop the navigation bar which is placed on the top of the web page-->
<!--The anchor tags are used to link the text inside these tags and link it to the URL path specified in the href field-->
<!-- The link redirects the user to the webpage that is corresponded to the specified URL path-->



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





<!--This is the HTML tags to develop the form to update the task's details.-->
<!--Once the user has filled in the form and submit the updated the task details, then the javascript function called handleSubmit is called
<!--to update the task details in the database. It's explained earlier on how it does it.-->
<!--input tag displays the form field fo the user to input. The bind:value svelte syntax stores the variable that are in the curly braces-->
<!--The variables are specified earlier. The id field helps to locate the form fields to enter values for automated testing.-->



<div>

<div class="p-5 mb-4 bg-light text-dark rounded shadow-sm animated-background">

    <h2 class="my-4">Update a Task</h2>

    <div>
        <form on:submit|preventDefault={handleSubmit}>
            <div class="row">
            <div class="col">
                <legend for="name">Enter the name of the task</legend><br>
                <input class="form-control" type="text" id="name1" placeholder="name" bind:value={name}/>
            </div>
            <div class="col">
                <legend for="date">Enter the date to start the task</legend><br>
                <input class="form-control" type="date" id="date1" placeholder="date" bind:value={date}/>
            </div>
            </div>
            <div class="row">
            <div class="col">
                <legend for="time">Enter the time to start the task</legend><br>
                <input class="form-control" type="time" id="startTime1" placeholder="start Time" bind:value={startTime}/>
            </div>
            <div class="col">
                <legend for="amountOfTime">Enter the amount of time to spend the task</legend><br>
                <input class="form-control" type="time" id="amountOfTime1" placeholder="Amount of to spend" bind:value={amountOfTime}/>
            </div>
            </div>
            <div class="row">
            <div class="col">
                <legend for="descriptionOfTheTask">Write the description of the task</legend><br>
                <input class="form-control" type="text" id="descriptionOfTheTask1" placeholder="description of the task" bind:value={descriptionOfTheTask}/>
            </div>
            <div class="col">
                <legend for="uploadingTheImage">Upload the image</legend><br>
                <input class="form-control" id="image" type="file" bind:files/>
            </div>
            </div><br>
            <div class="button-container">
            <button class="btn btn-primary" type="submit">Submit</button>
            </div>
        </form>
    </div>
</div>
</div>