<script lang="ts">
	let all_calculators: { name: string; route: string; def: string; image: string }[] = [
		{
			name: 'General Calculator',
			route: '/general',
			def: `It's for all type of general calculations.`,
			image: 'matrix.jpeg'
		},
		{
			name: 'Matrix Calculator',
			route: '/matrix',
			def: `It's for all type of matrix calculations.`,
			image: 'matrix.jpeg'
		}
	];
</script>

<div class="overflow-x-hidden">
	<section class="relative py-12 sm:py-16 lg:pt-20 xl:pb-0">
		<div class="relative px-4 mx-auto sm:px-6 lg:px-8 max-w-7xl">
			<div class="max-w-3xl mx-auto text-center">
				<p
					class="inline-flex px-4 py-2 text-base text-gray-900 border border-[#D8B61C] rounded-full font-pj"
				>
					Made by Students, for Students
				</p>
				<h1
					class="mt-5 text-4xl font-bold leading-tight text-gray-900 sm:text-5xl sm:leading-tight lg:text-6xl lg:leading-tight font-pj"
				>
					A math companion for everyone
				</h1>
				<p class="max-w-md mx-auto mt-6 text-base leading-7 text-gray-600 font-inter">
					You can solve everything if you choose right a path for it.
				</p>

				<div class="relative inline-flex my-10 group">
					<div
						class="absolute mb-2 transition-all duration-1000 opacity-70 -inset-px bg-gradient-to-r from-[#D8B61C] via-[#d3e645] to-[#78D43A] rounded-xl blur-lg group-hover:opacity-100 group-hover:-inset-1 group-hover:duration-200 animate-tilt"
					/>

					<a
						href="/"
						title=""
						class="relative inline-flex items-center justify-center px-8 py-4 text-lg font-bold text-white transition-all duration-200 bg-gray-900 font-pj rounded-xl focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-900"
						role="button"
					>
						Check all the resources
					</a>
				</div>
			</div>
		</div>
	</section>
</div>
<section class="py-12 sm:py-16 lg:py-20">
	<div class="px-4 mx-auto sm:px-6 lg:px-8 max-w-7xl">
		<div class="max-w-lg mx-auto text-center">
			<h2 class="text-3xl font-bold text-gray-900 sm:text-4xl">One For All</h2>
			<p class="max-w-md mx-auto mt-5 text-base font-normal leading-7 text-gray-500">
				Ready to use general maths solver
			</p>
		</div>

		<div
			class="grid max-w-md grid-cols-1 mx-auto mt-12 gap-y-12 md:grid-cols-3 gap-x-8 sm:mt-16 md:max-w-none"
		>
			{#each all_calculators as calculator}
				<a data-sveltekit-prefetch href={calculator.route}>
					<div class="flex flex-col group">
						<a
							href={calculator.route}
							title=""
							class="flex overflow-hidden shrink-0 aspect-w-16 aspect-h-9"
						>
							<img
								class="object-cover w-full h-full transition-all duration-200 transform group-hover:scale-110"
								src={calculator.image}
								alt=""
							/>
						</a>
						<a href={calculator.route} title="" class="flex flex-col flex-1">
							<p class="mt-6 text-2xl font-bold text-gray-900">{calculator.name}</p>
							<p class="mt-4 text-sm leading-6 text-gray-500 line-clamp-2">
								{calculator.def}
							</p>
						</a>
					</div>
				</a>
			{/each}
		</div>
	</div>
</section>
