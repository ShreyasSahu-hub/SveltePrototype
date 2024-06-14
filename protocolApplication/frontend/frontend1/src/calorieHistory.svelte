<script>

    let name = '';
    let director = '';
    let description = '';
    let files;
    let showInvalidMessage = false;



    //This function will fetch all the calories that are consumed by the user and at which date it was consumed

    async function handleSubmit(){



        //The Django endpoint API, which is the URL is called by the GET http method to fetch the calorie consumption details.
        //The credentials field is used to remember the user's username, in order to fetch the calorie consumptions that belongs to the user
        //The API response will be stored in the response variable

        let response = await fetch("/RetrieveCalorieDetails/",{

              method: 'GET',
              credentials: "include"

        })


        //The API response will be converted to the JSON format.

        let data = await response.json()

        console.log(data)


        document.getElementById("content").innerHTML = `
        <h3>This table shows the amount of calories that you consumed at each date</h3>
        <table class="table">
           <tr>
             <th>Amount of calories consumed</th>
             <th>The date the calories has been consumed</th>
           </tr>
           <tbody>
           </tbody>
        </table>
        <br>
        <br>
        <h3>This table shows the total amount of calories at each month</h3>
        <table class="table">
           <tr>
             <th>Month</th>
             <th>Total calorie consumption</th>
           </tr>
           <tbody id="totalCalorie">
           </tbody>
        </table>
        `;

        const calorieSummary = {};

        //The calorie detail is iterated by accessing it on a particular field called calorie_detail_retrieved from the API response.
        //Firstly, the date of the calorie intake will converted to UK date and time format, which is day/month/year hours:minutes:seconds.
        //The HTML p tag is used to display the calorie consumption detail. It will displayed in a white box by adding the predefined bootstrap class called card.
        //The white box size will be 100 pixels by 100 pixels. ALl the HTML elements that are used to present the calorie consumption details are stored inside the div tag that
        //has got the id called content, in order to show the calorie intake details below the form.

        data.calorie_detail_retrieved.forEach(calorie => {

            const date = new Date(calorie.currentdate);

            const day = String(date.getUTCDate()).padStart(2, '0');
            const month = date.toLocaleString('default', { month: 'long' });  // Months are zero-based
            const year = date.getUTCFullYear();

            // Extract the time components
            const hours = String(date.getUTCHours()).padStart(2, '0');
            const minutes = String(date.getUTCMinutes()).padStart(2, '0');
            const seconds = String(date.getUTCSeconds()).padStart(2, '0');

            // Format the date in DD/MM/YYYY format
            const ukDateFormat = `${day}/${month}/${year} ${hours}:${minutes}:${seconds}`;

            const dateString = `month: ${month}   year: ${year}`;

            if (calorieSummary[dateString]) {
                 calorieSummary[dateString] += calorie.amountofcalories;
            } else {
                 calorieSummary[dateString] = calorie.amountofcalories;
            }

            document.querySelector('tbody').innerHTML += `

                  <tr>
                    <td>${calorie.amountofcalories} Kcal</td>
                    <td>${ukDateFormat}</td>
                  </tr>
            `;


        });

        Object.keys(calorieSummary).forEach(date => {
            document.getElementById('totalCalorie').innerHTML += `
                <tr>
                    <td>${date}</td>
                    <td>${calorieSummary[date]} Kcal</td>
                </tr>
            `;
        });

    }
</script>

<head>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet">

<style>

table, th, td {
  border:1px solid black;
}

</style>

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


<!--The form will be positioned at the centre of the web page-->
<!--When the user clicks the button which is called as Fetch all the calorie consumption details at all the dates, the function called handleSubmit and its code will be executed.-->

<centre>

 <form on:submit|preventDefault={handleSubmit} align="center">

   <button class="btn btn-sm btn-primary mt-3 custom-btn" type="submit" >Fetch all the calorie consumption details at all the dates</button><br><br>

   <div class="p-3 mb-2 bg-light text-dark rounded shadow-sm">

   <div id="content"></div>

   </div>

 </form>

</centre>