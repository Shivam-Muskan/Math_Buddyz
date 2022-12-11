<script lang="ts">
	export let rows: number;
	export let columns: number;
	export let matrix: [];
	export let bg: string = 'bg-fuchsia-500';
</script>

<div class="rounded-lg border-x border-x-gray-900 px-3">
	<form>
		{#each Array(rows) as _, row}
			<div class="mx-0 space-x-1 p-0">
				{#each Array(columns) as _, column}
					<input
						class="my-3 w-16 rounded {bg} px-2 py-1 text-center text-gray-50"
						type="number"
						bind:value={matrix[row][column]}
						disabled
					/>
				{/each}
			</div>
		{/each}
	</form>
</div>
