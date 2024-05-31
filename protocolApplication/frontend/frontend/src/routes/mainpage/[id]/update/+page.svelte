<script lang="ts">
    //import {TaskStore} from '../../../../task-store'
    import {goto} from '$app/navigation'
    import {onMount} from 'svelte'

    let name = '';
    let date = '';
    let startTime = '';
    let amountOfTime = '';
    let descriptionOfTheTask = '';
    let files;
    let showInvalidMessage = false;
    export let data;
    let id;

    async function handleSubmit(){

        /*
        const endpoint = `http://localhost:8000/api/tasks/${id}/`
        let data = new FormData()
        data.append('name', name)
        data.append('date', date)
        data.append('startTime', startTime)
        data.append('amountOfTime', amountOfTime)
        data.append('descriptionOfTheTask', descriptionOfTheTask)

        //if (files) {
            data.append('image', files[0])
        //}

        fetch(endpoint, {method: 'PUT', body: data}).then(response => response.json()).then(data => {
            TaskStore.update(prev => {
                let updatedTasks = $TaskStore.slice()
                let index = updatedTasks.findIndex(task => task.id == data.id)
                updatedTasks[index] = data
                return updatedTasks
            })
        })
        */

        //id = data.id

        let data = new FormData()
        data.append('id', id)
        data.append('name', name)
        data.append('date', date)
        data.append('startTime', startTime)
        data.append('amountOfTime', amountOfTime)
        data.append('descriptionOfTheTask', descriptionOfTheTask)
        data.append('image', files[0])

        let response = await fetch("http://localhost:8000/TaskUpdate/",{

           method: 'POST',
           credentials: "include",
           body: data

        })

        goto('/mainpage/')
    }

    onMount(async function() {
        id = data.id

        /*
        let task = {}

        if ($TaskStore.length) {
            task = $TaskStore.find(task => task.id == id)
        } else {
            const endpoint = `http://localhost:8000/api/tasks/${data.id}/`
            let response = await fetch(endpoint)
            if (response.status == 200) {
                task = await response.json()
            } else {
                task = null;
            }
        }
        ({name, date, startTime, amountOfTime, descriptionOfTheTask} = task)
        */
    })

</script>


<div>

    <h2 class="my-4">Update a Task</h2>

    <div class="col-12 col-md-6">
        <form on:submit|preventDefault={handleSubmit}>
            <div class="mb-3">
                <legend for="name">Enter the name of the task</legend><br>
                <input class="form-control" type="text" id="name1" placeholder="name" bind:value={name}/>
            </div>
            <div class="mb-3">
                <legend for="date">Enter the date to start the task</legend><br>
                <input class="form-control" type="date" id="date1" placeholder="date" bind:value={date}/>
            </div>
            <div class="mb-3">
                <legend for="time">Enter the time to start the task</legend><br>
                <input class="form-control" type="time" id="startTime1" placeholder="start Time" bind:value={startTime}/>
            </div>
            <div class="mb-3">
                <legend for="amountOfTime">Enter the amount of time to spend the task</legend><br>
                <input class="form-control" type="time" id="amountOfTime1" placeholder="Amount of to spend" bind:value={amountOfTime}/>
            </div>
            <div class="mb-3">
                <legend for="descriptionOfTheTask">Write the description of the task</legend><br>
                <input class="form-control" type="text" id="descriptionOfTheTask1" placeholder="description of the task" bind:value={descriptionOfTheTask}/>
            </div>
            <div class="mb-3">
                <legend for="uploadingTheImage">Upload the image</legend><br>
                <input class="form-control" id="image" type="file" bind:files/>
            </div>

            <button class="btn btn-primary" type="submit">Submit</button>
        </form>
    </div>

</div>