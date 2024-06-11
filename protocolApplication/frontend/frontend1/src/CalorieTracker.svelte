<script lang="ts">

    let query;               //The variable query is created to store the food item that the user has inputted in the form for the diet plan
    let amountOfCalories;             //The variable amountOfCalories is created to store the desired amount of calories that the user inputted in the form
    let dietType;                     //The dietType variable is created to store whatever diet option is chosen by the user
    let mealType;                     //The mealType variable is created to store whatever meal option is chosen by the user
    let listOfFoodItems = '';               //The listOfFoodItems is created to store the food item and its quantity that is typed from the user. Only one food item and its quantity should be stored. No more than that.



    //This javascript function is where the EDAMAM API is called to provided a list of recipes as part of the diet plan based on the user's diet preferences that was filled in the diet plan form.

    async function handleEDAMAMAPI() {

    try{
     let APP_ID = "f0809293";                                      //This stores the API ID for calling the API
     let API_KEY = "4c9901ef9b16a44f50887e1926d8a00b";             //This stores the API key for calling the API



     //The URL API includes what the user types in the first text field in the form which is stored in the query variable,
     //the API ID, the API key, the diet type option that the user has selected, the amount of desired calories that the user has entered,
     //the meal type option the user has selected. This is manditory for the API to be called, or otherwise it cannot be called




     const URL = "https://api.edamam.com/api/recipes/v2?type=public&q=" + query + "&app_id=f0809293&app_key=4c9901ef9b16a44f50887e1926d8a00b&diet=" + dietType + "&calories=" + amountOfCalories + "&mealType=" + mealType;



     const response = await fetch(URL);                  //The response variable waits for the URL to provide the results based on the user's diet preferences. If the results are provided then it gets stored in the response variable.
     const data = await response.json();                 //The API response is converted to a JSON format and it gets stored in the data variable.
     console.log(data);                                  //The API response gets printed in the console.

     document.querySelector("#content").innerHTML = "";              //The HTML content of the div tag that has the id called content is initialized to an empty string.



     //The for loop iterates the fields of the API response to display the recipes that fits the user's preferences through HTML elements.
     //The h5 tag is used to display the title of the recipe, the p tag is used to display the recipes details in paragraphs,
     //the anchor tag is used to establish the link to the recipe website, and the img tag is used to display the recipe image
     //All of the information about the recipes are stores in a white box which is defined by the bootstrap class called card in the div tag.
     //These HTML tag elements will be stored in the div tag with the id of content, which is stated further in this svelte file.
     //It's coded as <div id="content" class="row">. The result will be displayed row by row.


     for (let i = 0; i < data.hits.length; i++) {
            document.querySelector("#content").innerHTML += `
            <div class="card" style="width: 18rem;">
                <img src="${data.hits[i].recipe.image}" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">${data.hits[i].recipe.label}</h5>
                    <p class="card-text">Source: ${data.hits[i].recipe.source}</p>
                    <p class="card-text">Meal Type: ${data.hits[i].recipe.mealType}</p>
                    <p class="card-text">Diet Type: ${data.hits[i].recipe.dietLabels}</p>
                    <p class="card-text">Calories in Kcal: ${Math.round(data.hits[i].recipe.calories)} kcal</p>
                    <a href="${data.hits[i].recipe.url}" class="btn btn-primary">Click here to find more information about that recipe</a>
                </div>
            </div>
            `;
     }



     //The if statement is captured if there are no recipe based on the user's diet preferences. It will display to the user that there's no available recipe that is personalized to you.

     if(data.hits.length==0){

        document.querySelector("#content").innerHTML = `<h3 class="card-text">Recipes unavailable</h3>`;

     }

    }



    //The try catch syntax will capture the incorrect or missing inputs that the user has typed in the form

    catch(err){

        document.querySelector("#content").innerHTML = `<h3 class="card-text">You have entered an invalid input. Please enter a valid input</h3>`;

    }

   }



   //This javascript function will display how much calories that the user has consumed based on what food item they have entered in the calorie tracker form through the EDAMAM API

   async function calorieTracker(){



       //The API is called through the specified URL that included what food item and its quantity that the user has typed in the text field, which is stored in the listOfFoodItems variable

       const URLCalories = "https://api.edamam.com/api/nutrition-data?app_id=c5d32486&app_key=edd240211b6512dcb06d0ee3069929d3&ingr=" + listOfFoodItems
       const response = await fetch(URLCalories);                //The response variable waits for API to give the amount of calories. Once that is done it stores the amount of calories.
       const data = await response.json();                       //The result from the API is converted to the JSON format.
       console.log(data);



       //The if statement will check if API returned the amount of calories or not. If it's returned then the amount of calories is displayed.
       //If not then it will display a message that says calories unavailable.
       //It will be displayed from the div tag that has the id called calorietracker.

       if(data.calories!=0){
       document.querySelector("#calorietracker").innerHTML = `<h3 class="card-text">Calories in Kcal: ${data.calories}</h3>`;
       }

       else{
       document.querySelector("#calorietracker").innerHTML = `<h3 class="card-text">Calories unavailable</h3>`;
       }



       //This if statement will store the date at which the user typed the food item and its quantities in the form in the database in the correct format.
       //This can happen if the API returned the amount of calories.

       if(data.calories!=0){



         //This captures the current date in the right format.

         var today = new Date();
         var dd = String(today.getDate()).padStart(2,'0');
         var mm = String(today.getMonth()+1).padStart(2,'0');
         var yyyy = today.getFullYear();

         var today = `${dd}/${mm}/${yyyy}`



         //The amount of calories and the current date that the user has typed the food items and its quantities are passed to the python function that is mapped to the Django endpoint URL.
         //called "http://localhost:8000/CalorieTracker/" which is defined in the url.py file in the protocolApplication folder. This is done through the POST http method to store the calories in the database.

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
    width: 75%;
    margin: 0 auto;
}

.vertical-center {
  margin: 0;
  position: absolute;
  top: 50%;
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
}

h2, h5 {
    text-align: center;
}

.mb-3{

    text-align: center;

}

.center-container {
    display: flex;
    justify-content: center;  /* Centers horizontally */
}
</style>

<head>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet">

</head>

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




<!--This is the form for the diet plan. The components inside the curly braces will store the user input to the variables that are declared on the top of this script-->
<!--The required keyword means it's compulsory for the user to fill in the form field-->
<!--The option tag is used to create all the available options that the user can select for the diet type or the meal type-->
<!--Once the user fills in the form and clicks the submit button, the handleEDAMAMAPI function will be called and its code will be executed-->
<!--The id field are included to locate the HTML tag for automated testing-->

<div class="p-3 mb-2 bg-light text-dark rounded shadow-sm animated-background">

    <h2 class="my-4">Diet Plan</h2>

        <form on:submit|preventDefault={handleEDAMAMAPI}>
            <div class="mb-3">
                <h2 class="my-4">Enter the food items</h2>
                <input class="form-control" type="text" id="query" placeholder="query" bind:value={query} required/>
            </div>
            <div class="mb-3">
                <h2 class="my-4">Enter the maximum amount of calories that you want to intake</h2>
                <input class="form-control" type="text" id="amountOfCalories" placeholder="amount of calories in kcal" bind:value={amountOfCalories} required/>
            </div>
            <div class="mb-3">
            <h2 class="my-4">Diet Type</h2>
            <select bind:value={dietType} id="dietType" required>
              <option value="high-fiber">High-Fiber</option>
              <option value="high-protein">High-Protein</option>
              <option value="low-carb">Low-Carb</option>
              <option value="low-fat">Low-Fat</option>
              <option value="low-sodium">Low-Sodium</option>
            </select>
            </div>
            <div class="mb-3">
            <h2 class="mb-4">Meal Type</h2>
            <select bind:value={mealType} id="mealType" required>
              <option value="breakfast">Breakfast</option>
              <option value="brunch">Brunch</option>
              <option value="lunch">Lunch</option>
              <option value="dinner">Dinner</option>
              <option value="snack">Snack</option>
              <option value="teatime">TeaTime</option>
            </select>
            </div>
            <div class="center-container">
            <button class="btn btn-primary" type="submit">Submit</button>
            </div>
        </form>
    <br>
    <div id="content" class="row"></div><br>

</div>

<br>



<!--This is the Calorie tracker form. Whatever food items and its quantity that the user has typed in the text field, it will be stored on the listOfFoodItems variable.-->
<!--Once the user fills in the form and clicks the button called Fetch the amount of calories intake, the calorieTracker javascript function will be called and its code-->
<!--will be executed.-->

<div class="p-3 mb-2 bg-light text-dark rounded shadow-sm animated-background">
  <h2 class="my-4">Calorie tracker</h2>
  <form on:submit|preventDefault={calorieTracker}>
       <h5 for="listOfFoodItems">Enter the food items here</h5>
       <div class="mb-3">
           <input class="form-control" type="text" id="listOfFoodItems" placeholder="Enter the food item" bind:value={listOfFoodItems} required/>
       </div>
       <div class="center-container">
       <button class="btn btn-primary" type="submit">Fetch the amount of calories intaken</button>
       </div>
  </form>
  <br>
  <div id="calorietracker"></div>
</div>

<!--The div tag with the id called calorietracker will return the amount of calories that is contained in the food item that the user has typed in the text field-->

<br>

<!--This is the link that will redirect the user to the web page that will show the user's calorie consumption history-->
<div class="p-3 mb-2 bg-light text-dark rounded shadow-sm animated-background">
<form>
<div class="center-container">
<a href="/#/calorieHistory/"><button class="btn btn-primary" type="submit">See your Calorie History</button></a><br><br>
</div>
</form>
</div>
<br>