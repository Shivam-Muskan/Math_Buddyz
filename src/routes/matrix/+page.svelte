<script lang="ts">
	import Header from '$lib/Components/Header.svelte';
	import toast from 'svelte-french-toast';
	import { fade, slide } from 'svelte/transition';
	import MatrixView from '$lib/Components/Matrix/MatrixView.svelte';
	import API from '$lib/utils/api';
	import Drawer from '$lib/Components/Matrix/Drawer.svelte';

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
				columns: 3,
				determinant: null,
				matrix: [
					[2, 3, 5],
					[9, 8, 7],
					[4, 5, 6]
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
		const currentMatrixDict = matrices[matrixKey];
		const response = await API.post('/matrix_determinant', { matrix: currentMatrixDict.matrix });
		if (response.error) {
			toast.error(response.message);
			disableBtn[matrixKey].determinant = false;
			return;
		}
		currentMatrixDict.determinant = response.result;
		matrices[matrixKey] = currentMatrixDict;
		toast.success(`Easier said then done. It's really a joke for computer to find this kind of thing`);
		disableBtn[matrixKey].determinant = false;
	};

	const transpose = async (matrixKey) => {
		disableBtn[matrixKey].transpose = true;
		const currentMatrixDict = matrices[matrixKey];
		const response = await API.post('/matrix_transpose', { matrix: matrices[matrixKey].matrix });
		if (response.error) {
			toast.error(response.message);
			disableBtn[matrixKey].transpose = false;
			return;
		}
		matrixTranspose[matrixKey] = response.result;
		toast.success('Easier said then done. Look at you doing maths with headache.');
		disableBtn[matrixKey].transpose = false;
	};

	const inverse = async (matrixKey) => {
		disableBtn[matrixKey].inverse = true;
		const currentMatrixDict = matrices[matrixKey];
		const response = await API.post('/matrix_inverse', { matrix: matrices[matrixKey].matrix });
		if (response.error) {
			toast.error(response.message);
			disableBtn[matrixKey].inverse = false;
			return;
		}
		matrices[matrixKey].determinant = response.determinant;
		matrixInverse[matrixKey] = response.result;
		toast.success('Easier said then done. You got the Inverse');
		disableBtn[matrixKey].inverse = false;
	};
	let isOpen = false;
	const handleToggle = () => {
		isOpen = !isOpen;
	};
</script>

<Header heading="Matrix Calculator" />

<section id="matrixEditor" class="py-5">
	<div class="grid grid-cols-3">
		<button
			type="button"
			on:click={newMatrix}
			disabled={newMatrixAddBtn}
			class="col-start-2 mx-auto inline-flex items-center justify-center rounded-md border border-transparent bg-indigo-600 px-6 py-3 text-sm font-semibold leading-5 text-white transition-all duration-200 hover:bg-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-600 focus:ring-offset-2"
		>
			<svg
				xmlns="http://www.w3.org/2000/svg"
				fill="none"
				viewBox="0 0 24 24"
				stroke-width="1.5"
				stroke="currentColor"
				class="mr-2 h-6 w-6"
			>
				<path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
			</svg>

			New Matrix
		</button>
	</div>
	<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
		<div
			class="mx-auto mt-12 grid max-w-fit grid-cols-1 justify-between justify-items-start gap-y-12 gap-x-8 sm:mt-16 md:grid-cols-4"
		>
			{#each Object.keys(matrices) as matrixKey}
				{#if matrices[matrixKey] !== 'empty'}
					<div class="flex flex-col items-center justify-center " transition:fade>
						<div class="flex inline-flex flex-row items-center justify-center space-x-10">
							<span class="mb-1 text-xl font-bold">
								Matrix {matrices[matrixKey].name}
							</span>
							<button
								type="button"
								on:click={removeMatrix(matrixKey)}
								disabled={newMatrixAddBtn}
								class="group inline-flex items-center justify-center rounded-md border border-transparent bg-red-600 px-2 py-1 text-sm leading-5 text-white transition-all duration-200 hover:bg-red-500 focus:outline-none focus:ring-2 focus:ring-red-600 focus:ring-offset-2"
							>
								<svg
									xmlns="http://www.w3.org/2000/svg"
									fill="none"
									viewBox="0 0 24 24"
									stroke-width="1.5"
									stroke="currentColor"
									class="mr-2 h-5 w-5 motion-safe:group-hover:animate-pulse"
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
									class="mx-auto my-3 w-7 rounded px-2 text-center"
									type="number"
									on:input={numberOfRows(event, matrixKey)}
									value={matrices[matrixKey].rows}
								/>
							</span>
							<span>
								Columns:
								<input
									class="mx-auto my-3 w-7 rounded px-2 text-center"
									type="number"
									on:input={numberOfColumns(event, matrixKey)}
									value={matrices[matrixKey].columns}
								/>
							</span>
						</div>
						<div class="rounded-lg border-x border-x-gray-900 px-3">
							{#each Array(matrices[matrixKey].rows) as _, row}
								<div class="mx-0 space-x-1 p-0">
									{#each Array(matrices[matrixKey].columns) as _, column}
										<input
											class="mx-auto my-3 w-16 rounded px-2 py-1 text-center"
											type="number"
											bind:value={matrices[matrixKey].matrix[row][column]}
											required
										/>
									{/each}
								</div>
							{/each}
						</div>

						<div class="mx-auto mt-5 flex flex-col space-y-3">
							<button
								type="button"
								on:click={determinant(matrixKey)}
								disabled={disableBtn[matrixKey].determinant}
								class="{disableBtn[matrixKey].determinant
									? 'cursor-not-allowed'
									: ''} inline-flex items-center justify-center rounded-md border border-transparent bg-indigo-600 px-6 py-3 text-sm font-semibold leading-5 text-white transition-all duration-200 hover:bg-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-600 focus:ring-offset-2"
							>
								<svg
									xmlns="http://www.w3.org/2000/svg"
									fill="none"
									viewBox="0 0 24 24"
									stroke-width="1.5"
									stroke="currentColor"
									class="mr-2 h-6 w-6"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										d="M15.75 15.75V18m-7.5-6.75h.008v.008H8.25v-.008zm0 2.25h.008v.008H8.25V13.5zm0 2.25h.008v.008H8.25v-.008zm0 2.25h.008v.008H8.25V18zm2.498-6.75h.007v.008h-.007v-.008zm0 2.25h.007v.008h-.007V13.5zm0 2.25h.007v.008h-.007v-.008zm0 2.25h.007v.008h-.007V18zm2.504-6.75h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V13.5zm0 2.25h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V18zm2.498-6.75h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V13.5zM8.25 6h7.5v2.25h-7.5V6zM12 2.25c-1.892 0-3.758.11-5.593.322C5.307 2.7 4.5 3.65 4.5 4.757V19.5a2.25 2.25 0 002.25 2.25h10.5a2.25 2.25 0 002.25-2.25V4.757c0-1.108-.806-2.057-1.907-2.185A48.507 48.507 0 0012 2.25z"
									/>
								</svg>
								{matrices[matrixKey].determinant !== null
									? `Determinant = ${matrices[matrixKey].determinant}`
									: 'Find Determinant'}
							</button>
							<button
								type="button"
								on:click={transpose(matrixKey)}
								disabled={disableBtn[matrixKey].transpose}
								class="{disableBtn[matrixKey].transpose
									? 'cursor-not-allowed'
									: ''} inline-flex items-center justify-center rounded-md border border-transparent bg-indigo-600 px-6 py-3 text-sm font-semibold leading-5 text-white transition-all duration-200 hover:bg-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-600 focus:ring-offset-2"
							>
								<svg
									xmlns="http://www.w3.org/2000/svg"
									fill="none"
									viewBox="0 0 24 24"
									stroke-width="1.5"
									stroke="currentColor"
									class="mr-2 h-6 w-6"
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
								class="{disableBtn[matrixKey].inverse
									? 'cursor-not-allowed'
									: ''} inline-flex items-center justify-center rounded-md border border-transparent bg-indigo-600 px-6 py-3 text-sm font-semibold leading-5 text-white transition-all duration-200 hover:bg-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-600 focus:ring-offset-2"
							>
								<svg
									xmlns="http://www.w3.org/2000/svg"
									fill="none"
									viewBox="0 0 24 24"
									stroke-width="1.5"
									stroke="currentColor"
									class="mr-2 h-6 w-6"
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
	<section id="matrixTransposeViewer" class="py-5">
		<div class="grid grid-cols-3" transition:fade>
			<div
				class="col-start-2 mx-auto inline-flex items-center justify-center rounded-md border border-transparent bg-fuchsia-600 px-6 py-3 text-sm font-semibold leading-5 text-white transition-all duration-200"
			>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 24 24"
					stroke-width="1.5"
					stroke="currentColor"
					class="mr-2 h-5 w-5"
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

		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div
				transition:slide
				class="mx-auto mt-12 grid max-w-fit grid-cols-1 justify-between justify-items-start gap-y-12 gap-x-10 sm:mt-16 md:grid-cols-4"
			>
				{#each Object.keys(matrices) as matrixKey}
					{#if matrixTranspose.hasOwnProperty(matrixKey)}
						<div class="flex flex-col items-center justify-center " transition:fade>
							<div class="flex inline-flex flex-row items-center justify-center space-x-10">
								<span class="mb-1 text-xl font-bold">
									Transpose {matrices[matrixKey].name}
								</span>
								<button
									type="button"
									class="group inline-flex items-center justify-center rounded-md border border-transparent bg-fuchsia-600 px-2 py-1 text-sm leading-5 text-white transition-all duration-200"
								>
									<svg
										xmlns="http://www.w3.org/2000/svg"
										fill="none"
										viewBox="0 0 24 24"
										stroke-width="1.5"
										stroke="currentColor"
										class="mr-2 h-5 w-5"
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
										class="mx-auto my-3 w-7 rounded bg-white px-2 text-center"
										type="number"
										disabled
										value={matrixTranspose[matrixKey].length}
									/>
								</span>
								<span>
									Columns:
									<input
										class="mx-auto my-3 w-7 rounded bg-white px-2 text-center"
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

{#if Object.keys(matrixInverse).length}
	<section id="matrixInverseViewer" class="py-5">
		<div class="grid grid-cols-3" transition:fade>
			<div
				class="col-start-2 mx-auto inline-flex items-center justify-center rounded-md border border-transparent bg-teal-600 px-6 py-3 text-sm font-semibold leading-5 text-white transition-all duration-200"
			>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 24 24"
					stroke-width="1.5"
					stroke="currentColor"
					class="mr-2 h-5 w-5"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						d="M3 7.5L7.5 3m0 0L12 7.5M7.5 3v13.5m13.5 0L16.5 21m0 0L12 16.5m4.5 4.5V7.5"
					/>
				</svg>

				Calculated Inverse
			</div>
		</div>

		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div
				transition:slide
				class="mx-auto mt-12 grid max-w-fit grid-cols-1 justify-between justify-items-start gap-y-12 gap-x-10 sm:mt-16 md:grid-cols-4"
			>
				{#each Object.keys(matrices) as matrixKey}
					{#if matrixInverse.hasOwnProperty(matrixKey)}
						<div class="flex flex-col items-center justify-center " transition:fade>
							<div class="flex inline-flex flex-row items-center justify-center space-x-10">
								<span class="mb-1 text-xl font-bold">
									Inverse {matrices[matrixKey].name}
								</span>
								<button
									type="button"
									class="group inline-flex items-center justify-center rounded-md border border-transparent bg-teal-600 px-2 py-1 text-sm leading-5 text-white transition-all duration-200"
								>
									<svg
										xmlns="http://www.w3.org/2000/svg"
										fill="none"
										viewBox="0 0 24 24"
										stroke-width="1.5"
										stroke="currentColor"
										class="mr-2 h-5 w-5"
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
										class="mx-auto my-3 w-7 rounded bg-white px-2 text-center"
										type="number"
										disabled
										value={matrixInverse[matrixKey].length}
									/>
								</span>
								<span>
									Columns:
									<input
										class="mx-auto my-3 w-7 rounded bg-white px-2 text-center"
										type="number"
										disabled
										value={matrixInverse[matrixKey][0].length}
									/>
								</span>
							</div>
							<MatrixView
								rows={matrixInverse[matrixKey].length}
								columns={matrixInverse[matrixKey][0].length}
								matrix={matrixInverse[matrixKey]}
								bg="bg-teal-500"
							/>
						</div>
					{/if}
				{/each}
			</div>
		</div>
	</section>
{/if}

<Drawer {isOpen} on:clickAway={handleToggle}>
	<button class="text-bold m-12 text-xl" on:click={handleToggle}>Close</button>
</Drawer>

<div class="flex">
	<div class="fixed group transition duration-75 ease-in-out inline-block p-3 text-xs font-medium leading-tight text-white uppercase transition duration-150 ease-in-out bg-blue-600 rounded-full shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg bottom-5 right-5">
		<svg
			xmlns="http://www.w3.org/2000/svg"
			class="h-8 w-8 cursor-pointer duration-100 hover:scale-110"
			fill="none"
			viewBox="0 0 24 24"
			stroke="currentColor"
			stroke-width="2"
			on:click={handleToggle}
		>
			<path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16" />
		</svg>
	</div>
</div>
