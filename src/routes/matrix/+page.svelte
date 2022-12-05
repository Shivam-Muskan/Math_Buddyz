<script lang="ts">
	import Header from '$lib/Components/Header.svelte';
	import toast from 'svelte-french-toast';
	import { fade, slide } from 'svelte/transition';
	import MatrixView from '$lib/Components/Matrix/MatrixView.svelte';

	let newMatrixAddBtn = false;
	let disableBtn = {
		A: {
			transpose: false,
			determinant: false,
			inverse: false
		}
	};
	let matrixInverse: Record<string, []> = {};

	let matrixTranspose: Record<string, []> = {};

	let matrices: Record<string, unknown> = {
		A: 'empty',
		B: 'empty',
		C: 'empty',
		D: 'empty',
		E: 'empty',
		F: 'empty',
		G: 'empty',
		H: 'empty',
		I: 'empty',
		J: 'empty',
		K: 'empty',
		L: 'empty',
		M: 'empty',
		O: 'empty',
		P: 'empty',
		Q: 'empty',
		R: 'empty',
		S: 'empty',
		T: 'empty',
		U: 'empty',
		V: 'empty',
		W: 'empty',
		X: 'empty',
		Y: 'empty',
		Z: 'empty'
	};

	const newMatrix = async () => {
		const keyWithValue = Object.keys(matrices).find((key) => matrices[key] === 'empty');

		if (keyWithValue) {
			matrices[keyWithValue] = {
				name: keyWithValue.toString(),
				rows: 3,
				columns: 5,
				determinant: 1,
				matrix: [
					[1, 0, 1, 0, 4],
					[1, 0, 1, 0, 4],
					[1, 0, 1, 0, 4]
				]
			};

			disableBtn[keyWithValue] = {
				transpose: false,
				determinant: false,
				inverse: false
			};
		} else toast.error("You can't add more matrix");

		newMatrixAddBtn = false;
	};

	const numberOfRows = (event, matrixKey) => {
		if ('' === event.target.value) return;
		const matrixDict = matrices[matrixKey];
		matrixDict.rows = parseInt(event.target.value);
		if (matrixDict.matrix.length < matrixDict.rows) {
			let newRowsToBeAdded = [];
			for (let i = 1; i <= matrixDict.rows - matrixDict.matrix.length; i++) {
				newRowsToBeAdded.push(new Array(matrixDict.columns).fill(0));
			}
			matrixDict.matrix = [...matrixDict.matrix, ...newRowsToBeAdded];
		} else if (matrixDict.matrix.length > matrixDict.rows) {
			matrixDict.matrix = matrixDict.matrix.slice(0, matrixDict.rows);
		}
		matrices[matrixKey] = matrixDict;
	};

	const numberOfColumns = (event, matrixKey) => {
		if ('' === event.target.value) return;
		const matrixDict = matrices[matrixKey];
		let newColumns = parseInt(event.target.value);
		if (matrixDict.matrix[0].length < newColumns) {
			for (let i = 0; i < matrixDict.rows; i++) {
				const newColumnsData = new Array(newColumns).fill(0);
				matrixDict.matrix[i].push(...newColumnsData);
			}
		} else if (matrixDict.matrix[0].length > newColumns) {
			for (let i = 0; i < matrixDict.rows; i++) {
				matrixDict.matrix[i] = matrixDict.matrix[i].slice(0, newColumns);
			}
		}
		matrixDict.columns = newColumns;
		matrices[matrixKey] = matrixDict;
	};

	const removeMatrix = (matrixKey) => {
		if (matrixTranspose.hasOwnProperty(matrixKey)) {
			const { [matrixKey.toString()]: deleteAble, ...newMatrixTranspose } = matrixTranspose;
			matrixTranspose = newMatrixTranspose;
		}

		if (matrixInverse.hasOwnProperty(matrixKey)) {
			const { [matrixKey.toString()]: deleteAble, ...newMatricesInverse } = matrixInverse;
			matrixTranspose = newMatricesInverse;
		}

		matrices[matrixKey] = 'empty';
	};

	const determinant = async (matrixKey) => {
		disableBtn[matrixKey].determinant = true;
		toast.success('Easier said then done.');
		await new Promise((r) => setTimeout(r, 2000));
		disableBtn[matrixKey].determinant = false;
	};

	const transpose = async (matrixKey) => {
		disableBtn[matrixKey].transpose = true;
		const currentMatrixDict = matrices[matrixKey];
		let transposeMatrix = [];
		for (let c = 0; c < currentMatrixDict.columns; c++) {
			let newTransposeMatrixRow = [];
			for (let r = 0; r < currentMatrixDict.rows; r++) {
				newTransposeMatrixRow.push(currentMatrixDict.matrix[r][c]);
			}
			transposeMatrix.push(newTransposeMatrixRow);
			newTransposeMatrixRow = [];
		}
		matrixTranspose[matrixKey] = transposeMatrix;
		toast.success('Easier said then done.');
		disableBtn[matrixKey].transpose = false;
	};

	const inverse = async (matrixKey) => {
		disableBtn[matrixKey].inverse = true;
		toast.success('Easier said then done.');
		await new Promise((r) => setTimeout(r, 2000));
		disableBtn[matrixKey].inverse = false;
	};
</script>

<Header heading="Matrix Calculator" />

<section id="matrixEditor" class="py-5">
	<div class="grid grid-cols-3">
		<button
			type="button"
			on:click={newMatrix}
			disabled={newMatrixAddBtn}
			class="col-start-2 mx-auto inline-flex items-center justify-center px-6 py-3 text-sm font-semibold leading-5 text-white transition-all duration-200 bg-indigo-600 border border-transparent rounded-md focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-600 hover:bg-indigo-500"
		>
			<svg
				xmlns="http://www.w3.org/2000/svg"
				fill="none"
				viewBox="0 0 24 24"
				stroke-width="1.5"
				stroke="currentColor"
				class="w-6 h-6 mr-2"
			>
				<path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
			</svg>

			New Matrix
		</button>
	</div>
	<div class="px-4 mx-auto sm:px-6 lg:px-8 max-w-7xl">
		<div
			class="grid max-w-fit mx-auto grid-cols-1 mt-12 gap-y-12 md:grid-cols-4 gap-x-8 sm:mt-16 justify-between justify-items-start"
		>
			{#each Object.keys(matrices) as matrixKey}
				{#if matrices[matrixKey] !== 'empty'}
					<div class="flex-col flex justify-center items-center " transition:fade>
						<div class="flex flex-row space-x-10 items-center inline-flex justify-center">
							<span class="text-xl font-bold mb-1">
								Matrix {matrices[matrixKey].name}
							</span>
							<button
								type="button"
								on:click={removeMatrix(matrixKey)}
								disabled={newMatrixAddBtn}
								class="inline-flex group items-center justify-center px-2 py-1 text-sm leading-5 text-white transition-all duration-200 bg-red-600 border border-transparent rounded-md focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-600 hover:bg-red-500"
							>
								<svg
									xmlns="http://www.w3.org/2000/svg"
									fill="none"
									viewBox="0 0 24 24"
									stroke-width="1.5"
									stroke="currentColor"
									class="w-5 h-5 mr-2 motion-safe:group-hover:animate-pulse"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0"
									/>
								</svg>
								{matrices[matrixKey].name}
							</button>
						</div>
						<div class="flex flex-row space-x-2">
							<span>
								Rows:
								<input
									class="mx-auto my-3 w-7 px-2 rounded text-center"
									type="number"
									on:input={numberOfRows(event, matrixKey)}
									value={matrices[matrixKey].rows}
								/>
							</span>
							<span>
								Columns:
								<input
									class="mx-auto my-3 w-7 px-2 rounded text-center"
									type="number"
									on:input={numberOfColumns(event, matrixKey)}
									value={matrices[matrixKey].columns}
								/>
							</span>
						</div>
						<div class="border-x border-x-gray-900 px-3 rounded-lg">
							{#each Array(matrices[matrixKey].rows) as _, row}
								<div class="space-x-1 p-0 mx-0">
									{#each Array(matrices[matrixKey].columns) as _, column}
										<input
											class="mx-auto my-3 w-7 px-2 rounded text-center"
											type="number"
											bind:value={matrices[matrixKey].matrix[row][column]}
											required
										/>
									{/each}
								</div>
							{/each}
						</div>

						<div class="flex flex-col space-y-3 mt-5 mx-auto">
							<button
								type="button"
								on:click={determinant(matrixKey)}
								disabled={disableBtn[matrixKey].determinant}
								class="{disableBtn[matrixKey].determinant
									? 'cursor-not-allowed'
									: ''} inline-flex items-center justify-center px-6 py-3 text-sm font-semibold leading-5 text-white transition-all duration-200 bg-indigo-600 border border-transparent rounded-md focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-600 hover:bg-indigo-500"
							>
								<svg
									xmlns="http://www.w3.org/2000/svg"
									fill="none"
									viewBox="0 0 24 24"
									stroke-width="1.5"
									stroke="currentColor"
									class="w-6 h-6 mr-2"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										d="M15.75 15.75V18m-7.5-6.75h.008v.008H8.25v-.008zm0 2.25h.008v.008H8.25V13.5zm0 2.25h.008v.008H8.25v-.008zm0 2.25h.008v.008H8.25V18zm2.498-6.75h.007v.008h-.007v-.008zm0 2.25h.007v.008h-.007V13.5zm0 2.25h.007v.008h-.007v-.008zm0 2.25h.007v.008h-.007V18zm2.504-6.75h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V13.5zm0 2.25h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V18zm2.498-6.75h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V13.5zM8.25 6h7.5v2.25h-7.5V6zM12 2.25c-1.892 0-3.758.11-5.593.322C5.307 2.7 4.5 3.65 4.5 4.757V19.5a2.25 2.25 0 002.25 2.25h10.5a2.25 2.25 0 002.25-2.25V4.757c0-1.108-.806-2.057-1.907-2.185A48.507 48.507 0 0012 2.25z"
									/>
								</svg>

								Find Determinant
							</button>
							<button
								type="button"
								on:click={transpose(matrixKey)}
								disabled={disableBtn[matrixKey].transpose}
								class="inline-flex items-center justify-center px-6 py-3 text-sm font-semibold leading-5 text-white transition-all duration-200 bg-indigo-600 border border-transparent rounded-md focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-600 hover:bg-indigo-500"
							>
								<svg
									xmlns="http://www.w3.org/2000/svg"
									fill="none"
									viewBox="0 0 24 24"
									stroke-width="1.5"
									stroke="currentColor"
									class="w-6 h-6 mr-2"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										d="M3 7.5L7.5 3m0 0L12 7.5M7.5 3v13.5m13.5 0L16.5 21m0 0L12 16.5m4.5 4.5V7.5"
									/>
								</svg>

								Calculate Transpose
							</button>
							<button
								type="button"
								on:click={inverse(matrixKey)}
								disabled={disableBtn[matrixKey].inverse}
								class="inline-flex items-center justify-center px-6 py-3 text-sm font-semibold leading-5 text-white transition-all duration-200 bg-indigo-600 border border-transparent rounded-md focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-600 hover:bg-indigo-500"
							>
								<svg
									xmlns="http://www.w3.org/2000/svg"
									fill="none"
									viewBox="0 0 24 24"
									stroke-width="1.5"
									stroke="currentColor"
									class="w-6 h-6 mr-2"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										d="M19.5 12c0-1.232-.046-2.453-.138-3.662a4.006 4.006 0 00-3.7-3.7 48.678 48.678 0 00-7.324 0 4.006 4.006 0 00-3.7 3.7c-.017.22-.032.441-.046.662M19.5 12l3-3m-3 3l-3-3m-12 3c0 1.232.046 2.453.138 3.662a4.006 4.006 0 003.7 3.7 48.656 48.656 0 007.324 0 4.006 4.006 0 003.7-3.7c.017-.22.032-.441.046-.662M4.5 12l3 3m-3-3l-3 3"
									/>
								</svg>
								Calculate Inverse
							</button>
						</div>
					</div>
				{/if}
			{/each}
		</div>
	</div>
</section>

{#if Object.keys(matrixTranspose).length}
	<section id="matrixViewer" class="py-5">
		<div class="grid grid-cols-3" transition:fade>
			<div
				class="col-start-2 mx-auto inline-flex items-center justify-center px-6 py-3 text-sm font-semibold leading-5 text-white transition-all duration-200 bg-fuchsia-600 border border-transparent rounded-md"
			>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 24 24"
					stroke-width="1.5"
					stroke="currentColor"
					class="w-5 h-5 mr-2"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						d="M3 7.5L7.5 3m0 0L12 7.5M7.5 3v13.5m13.5 0L16.5 21m0 0L12 16.5m4.5 4.5V7.5"
					/>
				</svg>

				Calculated Transposes
			</div>
		</div>

		<div class="px-4 mx-auto sm:px-6 lg:px-8 max-w-7xl">
			<div
				transition:slide
				class="grid max-w-fit mx-auto grid-cols-1 mt-12 gap-y-12 md:grid-cols-4 gap-x-10 sm:mt-16 justify-between justify-items-start"
			>
				{#each Object.keys(matrices) as matrixKey}
					{#if matrixTranspose.hasOwnProperty(matrixKey)}
						<div class="flex-col flex justify-center items-center " transition:fade>
							<div class="flex flex-row space-x-10 items-center inline-flex justify-center">
								<span class="text-xl font-bold mb-1">
									Matrix {matrices[matrixKey].name}
								</span>
								<button
									type="button"
									class="inline-flex group items-center justify-center px-2 py-1 text-sm leading-5 text-white transition-all duration-200 bg-fuchsia-600 border border-transparent rounded-md"
								>
									<svg
										xmlns="http://www.w3.org/2000/svg"
										fill="none"
										viewBox="0 0 24 24"
										stroke-width="1.5"
										stroke="currentColor"
										class="w-5 h-5 mr-2"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											d="M3 7.5L7.5 3m0 0L12 7.5M7.5 3v13.5m13.5 0L16.5 21m0 0L12 16.5m4.5 4.5V7.5"
										/>
									</svg>
									{matrices[matrixKey].name}
								</button>
							</div>
							<div class="flex flex-row space-x-2">
								<span>
									Rows:
									<input
										class="mx-auto my-3 w-7 px-2 rounded text-center bg-white"
										type="number"
										disabled
										value={matrixTranspose[matrixKey].length}
									/>
								</span>
								<span>
									Columns:
									<input
										class="mx-auto my-3 w-7 px-2 rounded text-center bg-white"
										type="number"
										disabled
										value={matrixTranspose[matrixKey][0].length}
									/>
								</span>
							</div>
							<MatrixView
								rows={matrixTranspose[matrixKey].length}
								columns={matrixTranspose[matrixKey][0].length}
								matrix={matrixTranspose[matrixKey]}
							/>
						</div>
					{/if}
				{/each}
			</div>
		</div>
	</section>
{/if}
