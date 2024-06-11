//This file is where the app starts
import App from './App.svelte'; // importing the javascript code as an App component from the App.svelte file in the same directory

// Creates an instance of the App component and stores the document.body components from the HTML DOM structure as starting point to include necessary visual HTMl components as the user interacts with the svelte web app. It gets stored in the app variable.
const app = new App({
	target: document.body,
});

export default app; //The export default syntax allows the developers to share the values, functions, or class from the app variable to other parts of the code to different files