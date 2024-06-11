<script>

    let queryForVideos = '';

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
  <h2 class="my-4">Find exercise videos</h2>
  <div class="col-12 col-md-6">
     <form on:submit|preventDefault={handleVideos}>
         <label for="queryForVideos">Enter the exercise videos that you want:</label>
         <div class="mb-3">
             <input class="form-control" type="text" id="queryForVideos" placeholder="query" bind:value={queryForVideos}/>
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


