<script lang="ts">

    let query;
    let amountOfCalories;
    let dietType;
    let mealType;
    let files;
    let listOfFoodItems = '';

    async function handleEDAMAMAPI() {

    try{
     let APP_ID = "f0809293";
     let API_KEY = "4c9901ef9b16a44f50887e1926d8a00b";
     const URL = "https://api.edamam.com/api/recipes/v2?type=public&q=" + query + "&app_id=f0809293&app_key=4c9901ef9b16a44f50887e1926d8a00b&diet=" + dietType + "&calories=" + amountOfCalories + "&mealType=" + mealType;
     const response = await fetch(URL);
     const data = await response.json();
     console.log(data);

     document.querySelector("#content").innerHTML = "";

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

    }

    catch(err){

        document.querySelector("#content").innerHTML = `<h3 class="card-text">Recipes unavailable</h3>`;

    }

   }

   async function calorieTracker(){

       //try{
       const URLCalories = "https://api.edamam.com/api/nutrition-data?app_id=c5d32486&app_key=edd240211b6512dcb06d0ee3069929d3	&ingr=" + listOfFoodItems
       const response = await fetch(URLCalories);
       const data = await response.json();
       console.log(data);

       if(data.calories!=0){
       document.querySelector("#calorietracker").innerHTML = `<h3 class="card-text">Calories in Kcal: ${data.calories}</h3>`;
       }

       else{
       document.querySelector("#calorietracker").innerHTML = `<h3 class="card-text">Calories unavailable</h3>`;
       }

       //}catch(err){

       //   document.querySelector("#calorietracker").innerHTML = "Calories is undefined"

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
    <h2 class="my-4">Diet Plan</h2>

    <div class="col-12 col-md-6">
        <form on:submit|preventDefault={handleEDAMAMAPI}>
            <div class="mb-3">
                <input class="form-control" type="text" id="query" placeholder="query" bind:value={query} required/>
            </div>
            <div class="mb-3">
                <input class="form-control" type="text" id="amountOfCalories" placeholder="amount of calories in kcal" bind:value={amountOfCalories} required/>
            </div>
            <div class="mb-3">
            <h5 class="my-4">Diet Type</h5>
            <select bind:value={dietType} id="dietType" required>
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
            <select bind:value={mealType} id="mealType" required>
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
    </div><br>
    <div id="content" class="row"></div><br>

</div>

<br>

<div class="p-3 mb-2 bg-light text-dark rounded shadow-sm animated-background">
  <h2 class="my-4">Calorie tracker</h2>
  <form on:submit|preventDefault={calorieTracker}>
       <label for="listOfFoodItems">Enter the food items here</label>
       <div class="mb-3">
           <input class="form-control" type="text" id="listOfFoodItems" placeholder="Enter the food item" bind:value={listOfFoodItems} required/>
       </div>
       <button class="btn btn-primary" type="submit">Fetch the amount of calories intaken</button>
  </form>
  <br>
  <div id="calorietracker"></div>
</div>

<br>

<a href="/mainpage/calorieHistory/"><button class="btn btn-primary"  type="submit">See your Calorie History</button></a><br><br>

<br>