// src/routes.js
//These are where all the svelte files are imported
import MainPage from './MainPage.svelte';
import TaskDetail from './TaskDetail.svelte'; // Create this component to show task details
import CalorieTracker from './CalorieTracker.svelte';
import calorieHistory from './calorieHistory.svelte';
import FetchingExercisingVideos from './FetchingExercisingVideos.svelte';
import automatedTesting from './automatedTesting.svelte';

//This is where all the URL path to svelte files are mapped
const routes = {
  '/mainpage': MainPage,
  '/mainpage/:id/': TaskDetail, // Dynamic route
  '/CalorieTracker': CalorieTracker,
  '/calorieHistory': calorieHistory,
  '/FetchingExercisingVideos': FetchingExercisingVideos,
  '/automatedTesting': automatedTesting,
};


//This makes the URL path to svelte files mapping to be included in the website
export default routes;