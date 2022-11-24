<script>
	import '../app.css';
	import Navigation from './Navigation.svelte';
	import { Toaster } from 'svelte-french-toast';
</script>

<div class="bg-gray-100	min-h-screen">
	<Toaster />
	<Navigation />
	<slot />
</div>
