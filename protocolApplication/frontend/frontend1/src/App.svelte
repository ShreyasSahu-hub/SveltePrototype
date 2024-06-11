<!-- src/App.svelte -->
<script>
  import Router from 'svelte-spa-router'; // importing the Router component from the svelte library called svelte-spa-router to map the URL path to the svelte files
  import routes from './routes'; // importing the variable called routes from the file called routes.js that stores the URL path, svelte files mapping in the same directory
  //import 'bootstrap/dist/css/bootstrap.min.css';
</script>

<Router {routes} /> <!-- The Router component takes the routes variable as the arguement input as part of its syntax. -->