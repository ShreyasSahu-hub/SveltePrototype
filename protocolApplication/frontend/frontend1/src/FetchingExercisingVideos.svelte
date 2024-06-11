<script>

    let queryForVideos = '';         //This variable is created to store the user's input for searching video



    //This javascript function retrieves the youtube videos based on the user's input

    async function handleVideos(){



        //This intialize the HTML elements for the div tag with the id of "returnedVideos" to an empty string

        document.getElementById("returnedVideos").innerHTML = ``;

        console.log(queryForVideos)



        // The 5 videos are fetch using the fetching function. It calls the specified URL to join the queryForVideos variable to the query parameters, which is denoted by q.
        // Whatever result is returned from the URL, is converted to the JSON format. Next, the id field of each videos are fetched from the returned result to display the link of the video to the user, using the anchor tag.
        // The url field for the image is also fetched from the results to display the video's image using the img tag.
        // The title field of each video is fetched to display the title of the videos using the h3 tag.
        // The HTML tags that displays details of each videos are stored in the div tag that has got an id called returnedVideos. That div tag displays all the video's details in rows.
        // That div tag is coded down to the script that is written <div id="returnedVideos" class="row">. It uses the predefined class called row, which is imported by Bootstrap to display the videos one row at a time.


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
    width: 30%;
    margin: 0 auto;
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

.form-control {
    display: block;
    margin: 0 auto; /* This will center the input horizontally */
    position: centre;
    width:400px;
}
</style>



<!--The link tag refers to the bootstrap library by connecting to its URL that is specified in the href component.-->
<!--It allows to import necessary predefined classes to add style to the navigation bar and to the form to fetch Youtube videos.-->

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


<!--This is the HTML tags that are used to develop the form to search and fetch exercising videos.-->
<!--The bind:value syntax is used to store the user input to the queryForVideos variable.-->
<!--As soon as the user clicks the button called Fetch videos, the handleVideos function is called, which is implemented above.-->
<!--The predefined bootstrap class called "p-3 mb-2 bg-light text-dark rounded shadow-sm animated-background" is used to make the background of the form to have animation-->
<br>
<br>
<div class="p-3 mb-2 bg-light text-dark rounded shadow-sm animated-background">
  <h2 class="my-5">Find exercise videos</h2>
  <div>
     <form on:submit|preventDefault={handleVideos}>
         <h5 for="queryForVideos">Enter the exercise videos that you want:</h5>
         <div class="mb-3">
             <input class="form-control" type="text" id="queryForVideos" placeholder="query" bind:value={queryForVideos}/>
         </div>
         <br>
         <div class="center-container">
         <button class="btn btn-primary" type="submit">Fetch videos</button>
         </div>
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


