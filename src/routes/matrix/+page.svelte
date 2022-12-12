<script lang="ts">
	import Header from '$lib/Components/Header.svelte';
	import toast from 'svelte-french-toast';
	import { fade, slide } from 'svelte/transition';
	import MatrixView from '$lib/Components/Matrix/MatrixView.svelte';
	import API from '$lib/utils/api';
	import Drawer from '$lib/Components/Matrix/Drawer.svelte';
	import { extractNumbersAndAlphabet, scrollToBottom, sleep } from "$lib/utils/jsHandlers";
	import { Icons } from "$lib/utils/icons";

	let newMatrixAddBtn: boolean = false;
	let disableBtn: Record<string, unknown> = {};

	let matrixInverse: Record<string, []> = {};
	let matrixTranspose: Record<string, []> = {};
	let matrixAdjoint: Record<string, []> = {};
	let advancedCalculator: Record<string, unknown> = {
		addition: {
			inputValue: '',
			disabled: false,
			error: null,
			answer: []
		},
		multiplication: {
			inputValue: '',
			disabled: false,
			error: null,
			answer: []
		}
	}

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
				adjoint: false,
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
		toast.success(
			`Easier said then done. It's really a joke for computer to find this kind of thing`
		);
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
		await sleep(100).then(() => scrollToBottom(`Transpose-${matrixKey}`));
	};

	const adjoint = async (matrixKey) => {
		disableBtn[matrixKey].adjoint = true;
		const currentMatrixDict = matrices[matrixKey];
		const response = await API.post('/matrix_adjoint', { matrix: matrices[matrixKey].matrix });
		if (response.error) {
			toast.error(response.message);
			disableBtn[matrixKey].adjoint = false;
			return;
		}
		matrixAdjoint[matrixKey] = response.result;
		toast.success('Easier said then done. You got the Inverse');
		await sleep(100).then(() => scrollToBottom(`Adjoint-${matrixKey}`));
		disableBtn[matrixKey].adjoint = false;
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
		// await sleep(100).then(() => scrollToBottom(`Inverse-${matrixKey}`));
		disableBtn[matrixKey].inverse = false;
	};

	const handleCalculations = async (calculatorKey) => {
		advancedCalculator[calculatorKey].disabled = true;
		const currentWorkingMatrices = advancedCalculator[calculatorKey].inputValue.split(",")
		if (currentWorkingMatrices.length < 2) {
			toast.error(`Please provide two or more matrices`)
			advancedCalculator[calculatorKey].error = `You have to provide at least two matrices for ${calculatorKey}`
			advancedCalculator[calculatorKey].disabled = false;
			return;
		}
		let finalMatricesData: Record<string, number> = {}
		let finalMatrixCollection = []
		for (const matricesKeyData of currentWorkingMatrices) {
			let { numbers, alphabet } = await extractNumbersAndAlphabet(matricesKeyData)
			if ( alphabet === null ) {
				toast.error(`Given matrix ${matricesKeyData} is not valid`)
				advancedCalculator[calculatorKey].error = `You have to provide matrix names to without that ${calculatorKey} is not going to take place.`
				advancedCalculator[calculatorKey].disabled = false;
				return;
			} if (numbers === null) {
				numbers = <RegExpMatchArray>['1']
			}
			const key = alphabet.join("")
			const multiplier = parseInt(numbers.join(""))
			if (!matrices.hasOwnProperty(key) ||  matrices[key] === 'empty') {
				toast.error(`Given matrix ${key} doesn't exist`)
				advancedCalculator[calculatorKey].error = "Please provide a existing matrix from the panel where you have all the matrices."
					advancedCalculator[calculatorKey].disabled = false;
				return;
			}
			const currentMatrix = matrices[key].matrix
			if (multiplier === 1) {
				finalMatrixCollection.push(currentMatrix)
			} else {
				const scalarProductMatrix = currentMatrix.map(
					row => row.map(
						col => col * multiplier
					)
				)
				finalMatrixCollection.push(scalarProductMatrix)
			}
		}

		const response = await API.post(`/matrix_${calculatorKey}`, { matrix: finalMatrixCollection });
		if (response.error) {
			toast.error(response.message);
			advancedCalculator[calculatorKey].disabled = false;
			advancedCalculator[calculatorKey].error = response.message
			return;
		}
		advancedCalculator[calculatorKey].answer = response.result;
		advancedCalculator[calculatorKey].disabled = false;
		toast.success('Easier said then done. You got the answer');
		advancedCalculator[calculatorKey].error = null
	}

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
								on:click={adjoint(matrixKey)}
								disabled={disableBtn[matrixKey].adjoint}
								class="{disableBtn[matrixKey].adjoint
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

								Calculate Adjoint
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
						<div
							id="Transpose-{matrixKey}"
							class="flex flex-col items-center justify-center "
							transition:fade
						>
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

{#if Object.keys(matrixAdjoint).length}
	<section id="matrixAdjointViewer" class="py-5">
		<div class="grid grid-cols-3" transition:fade>
			<div
				class="col-start-2 mx-auto inline-flex items-center justify-center rounded-md border border-transparent bg-sky-600 px-6 py-3 text-sm font-semibold leading-5 text-white transition-all duration-200"
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

				Calculated Adjnoint
			</div>
		</div>

		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div
				transition:slide
				class="mx-auto mt-12 grid max-w-fit grid-cols-1 justify-between justify-items-start gap-y-12 gap-x-10 sm:mt-16 md:grid-cols-4"
			>
				{#each Object.keys(matrices) as matrixKey}
					{#if matrixAdjoint.hasOwnProperty(matrixKey)}
						<div
							id="Adjoint-{matrixKey}"
							class="flex flex-col items-center justify-center "
							transition:fade
						>
							<div class="flex inline-flex flex-row items-center justify-center space-x-10">
								<span class="mb-1 text-xl font-bold">
									Adjoint {matrices[matrixKey].name}
								</span>
								<button
									type="button"
									class="group inline-flex items-center justify-center rounded-md border border-transparent bg-sky-600 px-2 py-1 text-sm leading-5 text-white transition-all duration-200"
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
										value={matrixAdjoint[matrixKey].length}
									/>
								</span>
								<span>
									Columns:
									<input
										class="mx-auto my-3 w-7 rounded bg-white px-2 text-center"
										type="number"
										disabled
										value={matrixAdjoint[matrixKey][0].length}
									/>
								</span>
							</div>
							<MatrixView
								rows={matrixAdjoint[matrixKey].length}
								columns={matrixAdjoint[matrixKey][0].length}
								matrix={matrixAdjoint[matrixKey]}
								bg="bg-sky-500"
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
						<div
							id="Inverse-{matrixKey}"
							class="flex flex-col items-center justify-center "
							transition:fade
						>
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
	<button class="text-bold m-12 flex flex-row text-xl text-red-700" on:click={handleToggle}>
		<svg
			xmlns="http://www.w3.org/2000/svg"
			fill="none"
			viewBox="0 0 24 24"
			stroke-width="1.5"
			stroke="currentColor"
			class="h-7 w-7"
		>
			<path
				stroke-linecap="round"
				stroke-linejoin="round"
				d="M9.75 9.75l4.5 4.5m0-4.5l-4.5 4.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
			/>
		</svg> Close
	</button>

	<div class="mx-auto max-w-7xl px-4 space-y-4 sm:px-6 lg:px-8">
		{#each Object.keys(advancedCalculator) as calculator}
		<div class="mx-auto max-w-xl">
			<div>
				<label for="additionText" class="capitalize text-sm font-medium text-gray-900">Multiple Matrix {calculator}</label>
				<div class="relative">
					<div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
						{@html Icons[calculator]}
<!--						<svg-->
<!--							xmlns="http://www.w3.org/2000/svg"-->
<!--							fill="none"-->
<!--							viewBox="0 0 24 24"-->
<!--							stroke-width="1.5"-->
<!--							stroke="currentColor"-->
<!--							class="h-5 w-5 text-gray-500 rotate-90"-->
<!--						>-->
<!--							<path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />-->
<!--						</svg>-->
					</div>
					<input
						type="text"
						id="additionText"
						bind:value={advancedCalculator[calculator].inputValue}
						class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-4 pl-10 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500"
						placeholder="Provide matrix name with comma e.g. A, B, C"
						required
					/>
					<button
						type="submit"
						on:click={handleCalculations(calculator)}
						disabled="{advancedCalculator[calculator].disabled}"
						class="absolute right-2.5 bottom-2.5 rounded-lg bg-blue-700 px-4 py-2 text-sm font-medium text-white hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300"
						>Calculate</button
					>
				</div>
				{#if advancedCalculator[calculator].error}
					<p class="mt-1 text-sm font-medium text-red-500">{advancedCalculator[calculator].error}</p>
				{/if}
				{#if advancedCalculator[calculator].answer.length > 0}
					<div
						id="New-{calculator}"
						class="flex flex-col items-center justify-center mt-4 "
						transition:fade
					>
						<div class="flex inline-flex flex-row items-center justify-center space-x-10">
								<span class="mb-1 text-xl font-bold capitalize">
									{calculator} {advancedCalculator[calculator].inputValue}
								</span>
<!--							<button-->
<!--								type="button"-->
<!--								class="group inline-flex items-center justify-center rounded-md border border-transparent bg-teal-600 px-2 py-1 text-sm leading-5 text-white transition-all duration-200"-->
<!--							>-->
<!--								<svg-->
<!--									xmlns="http://www.w3.org/2000/svg"-->
<!--									fill="none"-->
<!--									viewBox="0 0 24 24"-->
<!--									stroke-width="1.5"-->
<!--									stroke="currentColor"-->
<!--									class="mr-2 h-5 w-5"-->
<!--								>-->
<!--									<path-->
<!--										stroke-linecap="round"-->
<!--										stroke-linejoin="round"-->
<!--										d="M3 7.5L7.5 3m0 0L12 7.5M7.5 3v13.5m13.5 0L16.5 21m0 0L12 16.5m4.5 4.5V7.5"-->
<!--									/>-->
<!--								</svg>-->
<!--								&lt;!&ndash;{matrices[matrixKey].name}&ndash;&gt;-->
<!--							</button>-->
						</div>
						<div class="flex flex-row space-x-2">
								<span>
									Rows:
									<input
										class="mx-auto my-3 w-7 rounded bg-white px-2 text-center"
										type="number"
										disabled
										value={advancedCalculator[calculator].answer.length}
									/>
								</span>
							<span>
									Columns:
									<input
										class="mx-auto my-3 w-7 rounded bg-white px-2 text-center"
										type="number"
										disabled
										value={advancedCalculator[calculator].answer[0].length}
									/>
								</span>
						</div>
						<MatrixView
							rows={advancedCalculator[calculator].answer.length}
							columns={advancedCalculator[calculator].answer[0].length}
							matrix={advancedCalculator[calculator].answer}
							bg="bg-blue-500"
						/>
					</div>
					{/if}
			</div>
		</div>
			{/each}
	</div>

</Drawer>

<div class="flex">
	<div
		on:click={handleToggle}
		class="group flex flex-row items-center space-x-2 justify-center fixed bottom-10 right-5 inline-block rounded-full bg-indigo-600 p-3 font-medium uppercase leading-tight text-white shadow-md transition transition duration-75 duration-150 ease-in-out ease-in-out hover:bg-indigo-700 hover:shadow-lg focus:bg-indigo-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-indigo-800 active:shadow-lg md:right-32"
	>
		<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="h-6 w-6">
			<path stroke-linecap="round" stroke-linejoin="round" d="M15.75 15.75V18m-7.5-6.75h.008v.008H8.25v-.008zm0 2.25h.008v.008H8.25V13.5zm0 2.25h.008v.008H8.25v-.008zm0 2.25h.008v.008H8.25V18zm2.498-6.75h.007v.008h-.007v-.008zm0 2.25h.007v.008h-.007V13.5zm0 2.25h.007v.008h-.007v-.008zm0 2.25h.007v.008h-.007V18zm2.504-6.75h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V13.5zm0 2.25h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V18zm2.498-6.75h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V13.5zM8.25 6h7.5v2.25h-7.5V6zM12 2.25c-1.892 0-3.758.11-5.593.322C5.307 2.7 4.5 3.65 4.5 4.757V19.5a2.25 2.25 0 002.25 2.25h10.5a2.25 2.25 0 002.25-2.25V4.757c0-1.108-.806-2.057-1.907-2.185A48.507 48.507 0 0012 2.25z" />
		</svg>
		<span class="cursor-default text"> Advance Matrix Calculator </span>
	</div>
</div>
