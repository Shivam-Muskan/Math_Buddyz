<script lang="ts">
	import Header from '$lib/Header.svelte';
	type matrixData = {
		name: string;
		rows: number;
		columns: number;
		matrix: [];
		identity: [];
	};
	let matrices: matrixData[] = [];
</script>

<Header heading="Matrix Calculator" />
