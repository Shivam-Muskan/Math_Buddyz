<script lang="ts">
	export let rows: number;
	export let columns: number;
	export let matrix: [];
</script>

<div class="border-x border-x-gray-900 px-3 rounded-lg">
	<form>
		{#each Array(rows) as _, row}
			<div class="space-x-1 p-0 mx-0">
				{#each Array(columns) as _, column}
					<input
						class="mx-auto my-3 w-7 px-2 rounded text-center bg-fuchsia-500 text-gray-50"
						type="number"
						bind:value={matrix[row][column]}
						disabled
					/>
				{/each}
			</div>
		{/each}
	</form>
</div>
