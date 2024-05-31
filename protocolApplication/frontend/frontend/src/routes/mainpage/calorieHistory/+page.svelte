<script>
    import {TaskStore} from '../../../task-store'
    //import {goto} from '$app/navigation';

    let name = '';
    let director = '';
    let description = ''
    let files;
    let showInvalidMessage = false;

    //let validFields = () => {
    //    return name.length > 4 && director.length > 4 && description.length > 10
    //}

    //document.getElementById("taskholder").innerHTML = ``;

    async function handleSubmit(){
        //if (!validFields()) {
        //    showInvalidMessage = true;
        //    return
        //}
        //const endpoint = 'http://localhost:8000/api/tasks/'
        //let data = new FormData()
        //data.append('name', name)
        //data.append('director', director)
        //data.append('description', description)
        //data.append('image', files[0])

        let response = await fetch("http://localhost:8000/RetrieveCalorieDetails/",{

              method: 'GET',
              credentials: "include"

        })

        let data = await response.json()

        console.log(data)

        data.calorie_detail_retrieved.forEach(calorie => {

            const date = new Date(calorie.currentdate);

            const day = String(date.getUTCDate()).padStart(2, '0');
            const month = String(date.getUTCMonth() + 1).padStart(2, '0'); // Months are zero-based
            const year = date.getUTCFullYear();

            // Extract the time components
            const hours = String(date.getUTCHours()).padStart(2, '0');
            const minutes = String(date.getUTCMinutes()).padStart(2, '0');
            const seconds = String(date.getUTCSeconds()).padStart(2, '0');

            // Format the date in DD/MM/YYYY format
            const ukDateFormat = `${day}/${month}/${year} ${hours}:${minutes}:${seconds}`;

            document.getElementById("content").innerHTML += `
                <div class="card w-100 h-100">
                    <div class="card-body d-flex flex-column justify-content-between gap-4">
                        <div>
                            <p class="card-text">Amount of Calories Consumed: ${calorie.amountofcalories} Kcal</p>
                            <p class="card-text">Date of the Calories Consumed: ${ukDateFormat}</p>
                        </div>
                    </div>
                </div>
            `;

        });

        //fetch(endpoint, {method: 'POST', body: data}).then(response => response.json()).then(data => {
        //    TaskStore.update(prev => [...prev, data])
        //})

        //goto('/mainpage/')
    }
</script>

 <!--<div class="p-3 mb-2 bg-light text-dark rounded shadow-sm">-->

<centre>

 <form on:submit|preventDefault={handleSubmit} align="center">

   <button class="btn btn-sm btn-primary mt-3 custom-btn" type="submit" >Fetch all the calorie consumption details at all the dates</button><br><br>

   <div class="p-3 mb-2 bg-light text-dark rounded shadow-sm">

   <div id="content"></div>

   </div>

   <!--</div>-->

 </form>

 </centre>