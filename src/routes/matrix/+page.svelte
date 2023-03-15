<script lang="ts">
	import Header from '$lib/Components/Header.svelte';
	import toast from 'svelte-french-toast';
	import { fade, slide, draw } from 'svelte/transition';
	import MatrixView from '$lib/Components/Matrix/MatrixView.svelte';
	import API from '$lib/utils/api';
	import Drawer from '$lib/Components/Matrix/Drawer.svelte';
	import {
		extractNumbersAndAlphabet,
		removeKey,
		scrollToBottom,
		sleep,
		Symbols
	} from '$lib/utils/jsHandlers';
	import { Icons } from '$lib/utils/icons';

	let newMatrixAddBtn: boolean = false;
	let disableBtn: Record<string, unknown> = {};

	let matrixInverse: Record<string, []> = {};
	let matrixTranspose: Record<string, []> = {};
	let matrixAdjoint: Record<string, []> = {};
	let advancedCalculator: Record<string, unknown> = {
		addition: {
			name: 'Multiple Matrix Addition',
			description: 'Provide matrix name with comma e.g. A, B, C',
			inputValue: '',
			disabled: false,
			error: null,
			answer: [],
			url: 'matrix_addition',
			isMultipleMatrix: true,
			isAnswerArray: true
		},
		multiplication: {
			name: 'Multiple Matrix Multiplication',
			description: 'Provide matrix name with comma e.g. A, B, C',
			inputValue: '',
			disabled: false,
			error: null,
			answer: [],
			url: 'matrix_multiplication',
			isMultipleMatrix: true,
			isAnswerArray: true
		},
		matrixType: {
			name: 'Find Matrix Type (Valid for Single Matrix)',
			description: 'Provide a matrix name to find type of a matrix e.g. scalar, square',
			inputValue: '',
			disabled: false,
			error: null,
			answer: null,
			url: 'matrix_type',
			isMultipleMatrix: false,
			isAnswerArray: false
		}
	};

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

	async function getRndInteger() {
		return Math.floor(Math.random() * (68 - 1)) + 1;
	}

	const newMatrix = async (preDefinedMatrix) => {
		let newMatrixValue = [
			[await getRndInteger(), await getRndInteger(), await getRndInteger()],
			[await getRndInteger(), await getRndInteger(), await getRndInteger()],
			[await getRndInteger(), await getRndInteger(), await getRndInteger()]
		];
		if (preDefinedMatrix.length) {
			newMatrixValue = preDefinedMatrix;
		}
		const keyWithValue = Object.keys(matrices).find((key) => matrices[key] === 'empty');

		if (keyWithValue) {
			matrices[keyWithValue] = {
				name: keyWithValue.toString(),
				rows: 3,
				columns: 3,
				determinant: null,
				trace: null,
				matrix: newMatrixValue
			};

			disableBtn[keyWithValue] = {
				trace: false,
				transpose: false,
				determinant: false,
				adjoint: false,
				inverse: false
			};
			toast.success(`New matrix added ${keyWithValue}`);
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
		console.log(newColumns, event.target.value, matrixDict.matrix[0].length);
		if (matrixDict.matrix[0].length < newColumns) {
			const valuesToBeAdded = newColumns - matrixDict.matrix[0].length;
			const newColumnsData = new Array(valuesToBeAdded).fill(0);
			for (let i = 0; i < matrixDict.rows; i++) {
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
		if (matrixAdjoint.hasOwnProperty(matrixKey))
			matrixAdjoint = removeKey(matrixKey, matrixAdjoint);
		if (matrixInverse.hasOwnProperty(matrixKey))
			matrixInverse = removeKey(matrixKey, matrixInverse);
		if (matrixTranspose.hasOwnProperty(matrixKey))
			matrixTranspose = removeKey(matrixKey, matrixTranspose);
		matrices[matrixKey] = 'empty';
	};

	const determinant = async (matrixKey) => {
		disableBtn[matrixKey].determinant = true;
		const currentMatrixDict = matrices[matrixKey];
		console.log(currentMatrixDict);
		let response;
		try {
			response = await API.post('/matrix_determinant/', { matrix: currentMatrixDict.matrix });
		} catch (e) {
			toast.error(`Unable to complete current request for determinant of matrix ${matrixKey}`);
			disableBtn[matrixKey].determinant = false;
			return;
		}
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

	const matrixTrace = async (matrixKey) => {
		disableBtn[matrixKey].trace = true;
		const currentMatrixDict = matrices[matrixKey];
		let response;
		try {
			response = await API.post('/matrix_trace/', { matrix: currentMatrixDict.matrix });
		} catch (e) {
			toast.error(`Unable to complete current request for trace of matrix ${matrixKey}`);
			disableBtn[matrixKey].trace = false;
			return;
		}
		if (response.error) {
			toast.error(response.message);
			disableBtn[matrixKey].trace = false;
			return;
		}
		currentMatrixDict.trace = response.result;
		matrices[matrixKey] = currentMatrixDict;
		toast.success(
			`Easier said then done. It's really a joke for computer to find this kind of thing`
		);
		disableBtn[matrixKey].trace = false;
	};

	const transpose = async (matrixKey) => {
		disableBtn[matrixKey].transpose = true;
		const currentMatrixDict = matrices[matrixKey];
		let response;
		try {
			response = await API.post('/matrix_transpose/', { matrix: matrices[matrixKey].matrix });
		} catch (e) {
			toast.error(`Unable to complete current request for transpose of matrix ${matrixKey}`);
			disableBtn[matrixKey].transpose = false;
			return;
		}
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
		let response;
		try {
			response = await API.post('/matrix_adjoint/', { matrix: matrices[matrixKey].matrix });
		} catch (e) {
			toast.error(`Unable to complete current request for adjoint of matrix ${matrixKey}`);
			disableBtn[matrixKey].adjoint = false;
			return;
		}

		if (response.error) {
			toast.error(response.message);
			disableBtn[matrixKey].adjoint = false;
			return;
		}
		matrixAdjoint[matrixKey] = response.result;
		toast.success('Easier said then done. You got the Adjoint');
		await sleep(100).then(() => scrollToBottom(`Adjoint-${matrixKey}`));
		disableBtn[matrixKey].adjoint = false;
	};

	const inverse = async (matrixKey) => {
		disableBtn[matrixKey].inverse = true;
		const currentMatrixDict = matrices[matrixKey];
		let response;
		try {
			response = await API.post('/matrix_inverse/', { matrix: matrices[matrixKey].matrix });
		} catch (e) {
			toast.error(`Unable to complete current request for inverse of matrix ${matrixKey}`);
			disableBtn[matrixKey].inverse = false;
			return;
		}
		if (response.error) {
			toast.error(response.message);
			disableBtn[matrixKey].inverse = false;
			return;
		}
		matrices[matrixKey].determinant = response.determinant;
		matrixInverse[matrixKey] = response.result;
		toast.success('Easier said then done. You got the Inverse');
		await sleep(100).then(() => scrollToBottom(`Inverse-${matrixKey}`));
		disableBtn[matrixKey].inverse = false;
	};

	const handleCalculations = async (calculatorKey) => {
		advancedCalculator[calculatorKey].disabled = true;
		const currentWorkingMatrices = advancedCalculator[calculatorKey].inputValue.split(',');
		if (!advancedCalculator[calculatorKey].isMultipleMatrix && currentWorkingMatrices.length > 1) {
			toast.error(
				`You have to provide only one matrices for ${advancedCalculator[calculatorKey].name}`
			);
			advancedCalculator[
				calculatorKey
			].error = `You have to provide only one matrices for ${advancedCalculator[calculatorKey].name}`;
			advancedCalculator[calculatorKey].disabled = false;
			return;
		}
		if (advancedCalculator[calculatorKey].isMultipleMatrix && currentWorkingMatrices.length < 2) {
			toast.error(
				`You have to provide at least two matrices for ${advancedCalculator[calculatorKey].name}`
			);
			advancedCalculator[
				calculatorKey
			].error = `You have to provide at least two matrices for ${advancedCalculator[calculatorKey].name}`;
			advancedCalculator[calculatorKey].disabled = false;
			return;
		}
		let finalMatricesData: Record<string, number> = {};
		let finalMatrixCollection = [];
		for (const matricesKeyData of currentWorkingMatrices) {
			let { numbers, alphabet } = await extractNumbersAndAlphabet(matricesKeyData);
			if (alphabet === null) {
				toast.error(`Given matrix ${matricesKeyData} is not valid`);
				advancedCalculator[
					calculatorKey
				].error = `You have to provide matrices, without that ${advancedCalculator[calculatorKey].name} is not going to calculated.`;
				advancedCalculator[calculatorKey].disabled = false;
				return;
			}
			if (numbers === null) {
				numbers = <RegExpMatchArray>['1'];
			}
			const key = alphabet.join('');
			const multiplier = parseInt(numbers.join(''));
			if (!matrices.hasOwnProperty(key) || matrices[key] === 'empty') {
				toast.error(`Given matrix ${key} doesn't exist`);
				advancedCalculator[calculatorKey].error =
					'Please provide a existing matrix from the panel where you have all the matrices.';
				advancedCalculator[calculatorKey].disabled = false;
				return;
			}
			const currentMatrix = matrices[key].matrix;
			if (multiplier === 1) {
				finalMatrixCollection.push(currentMatrix);
			} else {
				const scalarProductMatrix = currentMatrix.map((row) => row.map((col) => col * multiplier));
				finalMatrixCollection.push(scalarProductMatrix);
			}
		}
		let response;
		try {
			response = await API.post(advancedCalculator[calculatorKey].url, {
				matrix: finalMatrixCollection
			});
		} catch (e) {
			toast.error(`Unable to complete this request for ${advancedCalculator[calculatorKey].name}`);
			advancedCalculator[calculatorKey].disabled = false;
			advancedCalculator[calculatorKey].error = response.message;
		}
		if (response.error) {
			toast.error(response.message);
			advancedCalculator[calculatorKey].disabled = false;
			advancedCalculator[calculatorKey].error = response.message;
			return;
		}
		advancedCalculator[calculatorKey].answer = response.result;
		advancedCalculator[calculatorKey].disabled = false;
		toast.success('Easier said then done. You got the answer');
		advancedCalculator[calculatorKey].error = null;
	};

	let isOpen = false;
	const handleToggle = () => {
		isOpen = !isOpen;
	};
</script>

<Header heading="Matrix Calculator" />

<section id="matrixEditor" class="py-5">
	<div class="flex">
		<button
			type="button"
			on:click={newMatrix}
			disabled={newMatrixAddBtn}
			class="mx-auto flex items-center justify-center rounded-md border border-transparent bg-indigo-600 px-6 py-3 text-sm font-semibold leading-5 text-white transition-all duration-200 hover:bg-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-600 focus:ring-offset-2"
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
									class="mx-auto my-3 w-7 rounded border border-gray-800 bg-gray-100 px-2 text-center text-gray-900"
									type="number"
									on:input={numberOfRows(event, matrixKey)}
									value={matrices[matrixKey].rows}
								/>
							</span>
							<span>
								Columns:
								<input
									class="mx-auto my-3 w-7 rounded border border-gray-800 bg-gray-100 px-2 text-center text-gray-900"
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
											class="mx-auto my-3 w-16 rounded border border-gray-800 bg-gray-100 px-2 py-1 text-center text-gray-900 "
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
									{#if disableBtn[matrixKey].determinant}
										<path
											transition:draw
											stroke-linecap="round"
											stroke-linejoin="round"
											d="M15.75 15.75V18m-7.5-6.75h.008v.008H8.25v-.008zm0 2.25h.008v.008H8.25V13.5zm0 2.25h.008v.008H8.25v-.008zm0 2.25h.008v.008H8.25V18zm2.498-6.75h.007v.008h-.007v-.008zm0 2.25h.007v.008h-.007V13.5zm0 2.25h.007v.008h-.007v-.008zm0 2.25h.007v.008h-.007V18zm2.504-6.75h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V13.5zm0 2.25h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V18zm2.498-6.75h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V13.5zM8.25 6h7.5v2.25h-7.5V6zM12 2.25c-1.892 0-3.758.11-5.593.322C5.307 2.7 4.5 3.65 4.5 4.757V19.5a2.25 2.25 0 002.25 2.25h10.5a2.25 2.25 0 002.25-2.25V4.757c0-1.108-.806-2.057-1.907-2.185A48.507 48.507 0 0012 2.25z"
										/>
									{:else}
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											d="M15.75 15.75V18m-7.5-6.75h.008v.008H8.25v-.008zm0 2.25h.008v.008H8.25V13.5zm0 2.25h.008v.008H8.25v-.008zm0 2.25h.008v.008H8.25V18zm2.498-6.75h.007v.008h-.007v-.008zm0 2.25h.007v.008h-.007V13.5zm0 2.25h.007v.008h-.007v-.008zm0 2.25h.007v.008h-.007V18zm2.504-6.75h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V13.5zm0 2.25h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V18zm2.498-6.75h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V13.5zM8.25 6h7.5v2.25h-7.5V6zM12 2.25c-1.892 0-3.758.11-5.593.322C5.307 2.7 4.5 3.65 4.5 4.757V19.5a2.25 2.25 0 002.25 2.25h10.5a2.25 2.25 0 002.25-2.25V4.757c0-1.108-.806-2.057-1.907-2.185A48.507 48.507 0 0012 2.25z"
										/>
									{/if}
								</svg>
								{matrices[matrixKey].determinant !== null
									? `Determinant = ${matrices[matrixKey].determinant}`
									: 'Find Determinant'}
							</button>
							<button
								type="button"
								on:click={matrixTrace(matrixKey)}
								disabled={disableBtn[matrixKey].trace}
								class="{disableBtn[matrixKey].trace
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
									{#if disableBtn[matrixKey].trace}
										<path
											transition:draw
											stroke-linecap="round"
											stroke-linejoin="round"
											d="M15.75 15.75V18m-7.5-6.75h.008v.008H8.25v-.008zm0 2.25h.008v.008H8.25V13.5zm0 2.25h.008v.008H8.25v-.008zm0 2.25h.008v.008H8.25V18zm2.498-6.75h.007v.008h-.007v-.008zm0 2.25h.007v.008h-.007V13.5zm0 2.25h.007v.008h-.007v-.008zm0 2.25h.007v.008h-.007V18zm2.504-6.75h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V13.5zm0 2.25h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V18zm2.498-6.75h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V13.5zM8.25 6h7.5v2.25h-7.5V6zM12 2.25c-1.892 0-3.758.11-5.593.322C5.307 2.7 4.5 3.65 4.5 4.757V19.5a2.25 2.25 0 002.25 2.25h10.5a2.25 2.25 0 002.25-2.25V4.757c0-1.108-.806-2.057-1.907-2.185A48.507 48.507 0 0012 2.25z"
										/>
									{:else}
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											d="M15.75 15.75V18m-7.5-6.75h.008v.008H8.25v-.008zm0 2.25h.008v.008H8.25V13.5zm0 2.25h.008v.008H8.25v-.008zm0 2.25h.008v.008H8.25V18zm2.498-6.75h.007v.008h-.007v-.008zm0 2.25h.007v.008h-.007V13.5zm0 2.25h.007v.008h-.007v-.008zm0 2.25h.007v.008h-.007V18zm2.504-6.75h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V13.5zm0 2.25h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V18zm2.498-6.75h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V13.5zM8.25 6h7.5v2.25h-7.5V6zM12 2.25c-1.892 0-3.758.11-5.593.322C5.307 2.7 4.5 3.65 4.5 4.757V19.5a2.25 2.25 0 002.25 2.25h10.5a2.25 2.25 0 002.25-2.25V4.757c0-1.108-.806-2.057-1.907-2.185A48.507 48.507 0 0012 2.25z"
										/>
									{/if}
								</svg>
								{matrices[matrixKey].trace !== null
									? `Matrix Trace = ${matrices[matrixKey].trace}`
									: 'Find Matrix Trace'}
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
									{#if disableBtn[matrixKey].transpose}
										<path
											transition:draw
											stroke-linecap="round"
											stroke-linejoin="round"
											d="M19.5 12c0-1.232-.046-2.453-.138-3.662a4.006 4.006 0 00-3.7-3.7 48.678 48.678 0 00-7.324 0 4.006 4.006 0 00-3.7 3.7c-.017.22-.032.441-.046.662M19.5 12l3-3m-3 3l-3-3m-12 3c0 1.232.046 2.453.138 3.662a4.006 4.006 0 003.7 3.7 48.656 48.656 0 007.324 0 4.006 4.006 0 003.7-3.7c.017-.22.032-.441.046-.662M4.5 12l3 3m-3-3l-3 3"
										/>
									{:else}
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											d="M19.5 12c0-1.232-.046-2.453-.138-3.662a4.006 4.006 0 00-3.7-3.7 48.678 48.678 0 00-7.324 0 4.006 4.006 0 00-3.7 3.7c-.017.22-.032.441-.046.662M19.5 12l3-3m-3 3l-3-3m-12 3c0 1.232.046 2.453.138 3.662a4.006 4.006 0 003.7 3.7 48.656 48.656 0 007.324 0 4.006 4.006 0 003.7-3.7c.017-.22.032-.441.046-.662M4.5 12l3 3m-3-3l-3 3"
										/>
									{/if}
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
									viewBox="0 0 20 20"
									fill="currentColor"
									class="mr-2 h-6 w-6 {disableBtn[matrixKey].adjoint ? 'animate-spin' : ''}"
								>
									<path
										fill-rule="evenodd"
										d="M15.312 11.424a5.5 5.5 0 01-9.201 2.466l-.312-.311h2.433a.75.75 0 000-1.5H3.989a.75.75 0 00-.75.75v4.242a.75.75 0 001.5 0v-2.43l.31.31a7 7 0 0011.712-3.138.75.75 0 00-1.449-.39zm1.23-3.723a.75.75 0 00.219-.53V2.929a.75.75 0 00-1.5 0V5.36l-.31-.31A7 7 0 003.239 8.188a.75.75 0 101.448.389A5.5 5.5 0 0113.89 6.11l.311.31h-2.432a.75.75 0 000 1.5h4.243a.75.75 0 00.53-.219z"
										clip-rule="evenodd"
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
									{#if disableBtn[matrixKey].inverse}
										<path
											transition:draw
											stroke-linecap="round"
											stroke-linejoin="round"
											d="M3 7.5L7.5 3m0 0L12 7.5M7.5 3v13.5m13.5 0L16.5 21m0 0L12 16.5m4.5 4.5V7.5"
										/>
									{:else}
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											d="M3 7.5L7.5 3m0 0L12 7.5M7.5 3v13.5m13.5 0L16.5 21m0 0L12 16.5m4.5 4.5V7.5"
										/>
									{/if}
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

<div class="mb-10">
	{#if Object.keys(matrixTranspose).length}
		<section id="matrixTransposeViewer" class="py-5">
			<div class="flex" transition:fade>
				<div
					class="mx-auto inline-flex items-center justify-center rounded-md border border-transparent bg-fuchsia-600 px-6 py-3 text-sm font-semibold leading-5 text-white transition-all duration-200"
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
							d="M19.5 12c0-1.232-.046-2.453-.138-3.662a4.006 4.006 0 00-3.7-3.7 48.678 48.678 0 00-7.324 0 4.006 4.006 0 00-3.7 3.7c-.017.22-.032.441-.046.662M19.5 12l3-3m-3 3l-3-3m-12 3c0 1.232.046 2.453.138 3.662a4.006 4.006 0 003.7 3.7 48.656 48.656 0 007.324 0 4.006 4.006 0 003.7-3.7c.017-.22.032-.441.046-.662M4.5 12l3 3m-3-3l-3 3"
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
												d="M19.5 12c0-1.232-.046-2.453-.138-3.662a4.006 4.006 0 00-3.7-3.7 48.678 48.678 0 00-7.324 0 4.006 4.006 0 00-3.7 3.7c-.017.22-.032.441-.046.662M19.5 12l3-3m-3 3l-3-3m-12 3c0 1.232.046 2.453.138 3.662a4.006 4.006 0 003.7 3.7 48.656 48.656 0 007.324 0 4.006 4.006 0 003.7-3.7c.017-.22.032-.441.046-.662M4.5 12l3 3m-3-3l-3 3"
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
								<div class="mx-auto mt-5 flex flex-col space-y-3">
									<button
										type="button"
										on:click={newMatrix(matrixTranspose[matrixKey])}
										class="inline-flex items-center justify-center rounded-md border border-transparent bg-fuchsia-600 px-6 py-3 text-sm font-semibold leading-5 text-white transition-all duration-200 hover:bg-fuchsia-500 focus:outline-none focus:ring-2 focus:ring-fuchsia-600 focus:ring-offset-2"
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
												d="M12 4.5v15m7.5-7.5h-15"
											/>
										</svg>

										Add as New Matrix
									</button>
								</div>
							</div>
						{/if}
					{/each}
				</div>
			</div>
		</section>
	{/if}

	{#if Object.keys(matrixAdjoint).length > 0}
		<section id="matrixAdjointViewer" class="py-5">
			<div class="grid grid-cols-3" transition:fade>
				<div
					class="col-start-2 mx-auto inline-flex items-center justify-center rounded-md border border-transparent bg-sky-600 px-6 py-3 text-sm font-semibold leading-5 text-white transition-all duration-200"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						viewBox="0 0 20 20"
						fill="currentColor"
						class="mr-2 h-5 w-5"
					>
						<path
							fill-rule="evenodd"
							d="M15.312 11.424a5.5 5.5 0 01-9.201 2.466l-.312-.311h2.433a.75.75 0 000-1.5H3.989a.75.75 0 00-.75.75v4.242a.75.75 0 001.5 0v-2.43l.31.31a7 7 0 0011.712-3.138.75.75 0 00-1.449-.39zm1.23-3.723a.75.75 0 00.219-.53V2.929a.75.75 0 00-1.5 0V5.36l-.31-.31A7 7 0 003.239 8.188a.75.75 0 101.448.389A5.5 5.5 0 0113.89 6.11l.311.31h-2.432a.75.75 0 000 1.5h4.243a.75.75 0 00.53-.219z"
							clip-rule="evenodd"
						/>
					</svg>

					Calculated Adjoint
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
											viewBox="0 0 20 20"
											fill="currentColor"
											class="mr-2 h-5 w-5"
										>
											<path
												fill-rule="evenodd"
												d="M15.312 11.424a5.5 5.5 0 01-9.201 2.466l-.312-.311h2.433a.75.75 0 000-1.5H3.989a.75.75 0 00-.75.75v4.242a.75.75 0 001.5 0v-2.43l.31.31a7 7 0 0011.712-3.138.75.75 0 00-1.449-.39zm1.23-3.723a.75.75 0 00.219-.53V2.929a.75.75 0 00-1.5 0V5.36l-.31-.31A7 7 0 003.239 8.188a.75.75 0 101.448.389A5.5 5.5 0 0113.89 6.11l.311.31h-2.432a.75.75 0 000 1.5h4.243a.75.75 0 00.53-.219z"
												clip-rule="evenodd"
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
								<div class="mx-auto mt-5 flex flex-col space-y-3">
									<button
										type="button"
										on:click={newMatrix(matrixAdjoint[matrixKey])}
										class="inline-flex items-center justify-center rounded-md border border-transparent bg-sky-600 px-6 py-3 text-sm font-semibold leading-5 text-white transition-all duration-200 hover:bg-sky-500 focus:outline-none focus:ring-2 focus:ring-sky-600 focus:ring-offset-2"
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
												d="M12 4.5v15m7.5-7.5h-15"
											/>
										</svg>

										Add as New Matrix
									</button>
								</div>
							</div>
						{/if}
					{/each}
				</div>
			</div>
		</section>
	{/if}

	{#if Object.keys(matrixInverse).length > 0}
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
								<div class="mx-auto mt-5 flex flex-col space-y-3">
									<button
										type="button"
										on:click={newMatrix(matrixInverse[matrixKey])}
										class="inline-flex items-center justify-center rounded-md border border-transparent bg-teal-600 px-6 py-3 text-sm font-semibold leading-5 text-white transition-all duration-200 hover:bg-teal-500 focus:outline-none focus:ring-2 focus:ring-teal-600 focus:ring-offset-2"
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
												d="M12 4.5v15m7.5-7.5h-15"
											/>
										</svg>

										Add as New Matrix
									</button>
								</div>
							</div>
						{/if}
					{/each}
				</div>
			</div>
		</section>
	{/if}
</div>
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

	<div class="mx-auto max-w-7xl space-y-4 px-4 sm:px-6 lg:px-8">
		{#each Object.keys(advancedCalculator) as calculator}
			<div class="mx-auto max-w-xl">
				<div>
					<label for={calculator} class="text-sm font-medium capitalize text-gray-900"
						>{advancedCalculator[calculator].name}</label
					>
					<div class="relative">
						<div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
							{@html Icons[calculator]}
						</div>
						<input
							type="text"
							id={calculator}
							bind:value={advancedCalculator[calculator].inputValue}
							class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-4 pl-10 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500"
							placeholder={advancedCalculator[calculator].description}
							required
						/>
						<button
							type="submit"
							on:click={handleCalculations(calculator)}
							disabled={advancedCalculator[calculator].disabled}
							class="absolute right-2.5 bottom-2.5 rounded-lg bg-blue-700 px-4 py-2 text-sm font-medium text-white hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300"
							>Calculate</button
						>
					</div>
					{#if advancedCalculator[calculator].error}
						<p class="mt-1 text-sm font-medium text-red-500">
							{advancedCalculator[calculator].error}
						</p>
					{/if}
					{#if advancedCalculator[calculator].isAnswerArray && advancedCalculator[calculator].answer.length > 0}
						<div
							id="New-{calculator}"
							class="mt-4 flex flex-col items-center justify-center "
							transition:slide
						>
							<div class="flex inline-flex flex-row items-center justify-center space-x-10">
								<span class="mb-1 text-xl font-bold capitalize">
									{calculator}
									{advancedCalculator[calculator].inputValue.replace(/,/g, Symbols[calculator])}
								</span>
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
					{:else if !advancedCalculator[calculator].isAnswerArray && advancedCalculator[calculator].answer !== null}
						<div class="mt-4 flex rounded-md bg-indigo-50 p-4 text-sm text-indigo-500">
							<svg
								xmlns="http://www.w3.org/2000/svg"
								viewBox="0 0 20 20"
								fill="currentColor"
								class="mr-3 h-5 w-5 flex-shrink-0"
							>
								<path
									fill-rule="evenodd"
									d="M19 10.5a8.5 8.5 0 11-17 0 8.5 8.5 0 0117 0zM8.25 9.75A.75.75 0 019 9h.253a1.75 1.75 0 011.709 2.13l-.46 2.066a.25.25 0 00.245.304H11a.75.75 0 010 1.5h-.253a1.75 1.75 0 01-1.709-2.13l.46-2.066a.25.25 0 00-.245-.304H9a.75.75 0 01-.75-.75zM10 7a1 1 0 100-2 1 1 0 000 2z"
									clip-rule="evenodd"
								/>
							</svg>
							<div>
								<h4 class="font-bold">Matrix Type</h4>
								<div class="mt-1">
									{#each Object.keys(advancedCalculator[calculator].answer) as matrixType}
										<p>{matrixType}: {advancedCalculator[calculator].answer[matrixType] ? 'Yes' : 'No'}</p>
									{/each}
								</div>
							</div>
						</div>
					{/if}
				</div>
			</div>
		{/each}
	</div>
</Drawer>

<div class="flex">
	<div on:click={handleToggle} class="sideItems bottom-36 -right-28 md:bottom-10 md:right-5">
		<svg
			xmlns="http://www.w3.org/2000/svg"
			fill="none"
			viewBox="0 0 24 24"
			stroke-width="1.5"
			stroke="currentColor"
			class="h-6 w-6"
		>
			<path
				stroke-linecap="round"
				stroke-linejoin="round"
				d="M15.75 15.75V18m-7.5-6.75h.008v.008H8.25v-.008zm0 2.25h.008v.008H8.25V13.5zm0 2.25h.008v.008H8.25v-.008zm0 2.25h.008v.008H8.25V18zm2.498-6.75h.007v.008h-.007v-.008zm0 2.25h.007v.008h-.007V13.5zm0 2.25h.007v.008h-.007v-.008zm0 2.25h.007v.008h-.007V18zm2.504-6.75h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V13.5zm0 2.25h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V18zm2.498-6.75h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V13.5zM8.25 6h7.5v2.25h-7.5V6zM12 2.25c-1.892 0-3.758.11-5.593.322C5.307 2.7 4.5 3.65 4.5 4.757V19.5a2.25 2.25 0 002.25 2.25h10.5a2.25 2.25 0 002.25-2.25V4.757c0-1.108-.806-2.057-1.907-2.185A48.507 48.507 0 0012 2.25z"
			/>
		</svg>
		<span class="text cursor-default"> Advance Matrix Calculator </span>
	</div>

	<div class="sideItems bottom-[22rem] -right-4 md:bottom-24 md:right-5">
		<svg
			xmlns="http://www.w3.org/2000/svg"
			fill="none"
			viewBox="0 0 24 24"
			stroke-width="1.5"
			stroke="currentColor"
			class="h-6 w-6"
		>
			<path
				stroke-linecap="round"
				d="M15.75 10.5l4.72-4.72a.75.75 0 011.28.53v11.38a.75.75 0 01-1.28.53l-4.72-4.72M4.5 18.75h9a2.25 2.25 0 002.25-2.25v-9a2.25 2.25 0 00-2.25-2.25h-9A2.25 2.25 0 002.25 7.5v9a2.25 2.25 0 002.25 2.25z"
			/>
		</svg>
		<span class="text cursor-default"> Guide </span>
	</div>
</div>

<style>
	.sideItems {
		@apply fixed inline-block flex rotate-90 flex-row items-center justify-center space-x-2 rounded-full bg-indigo-600 p-3 font-medium uppercase leading-tight text-white shadow-md transition transition duration-75 duration-150 ease-in-out ease-in-out hover:bg-indigo-700 hover:shadow-lg focus:bg-indigo-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-indigo-800 active:shadow-lg md:right-32 md:rotate-0;
	}
</style>
