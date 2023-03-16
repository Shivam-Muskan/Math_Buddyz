<script>
	import Header from '$lib/Components/Header.svelte';

	const nurmericalCalcs = [
		{
			name: 'Bisection Method',
			description:
				'The bisection method is used to find the roots of a polynomial equation. It separates the interval and subdivides the interval in which the root of the equation lies. The principle behind this method is the intermediate theorem for continuous functions.',
			path: 'bisection-method',
			image: '/BisectionMethod.webp'
		},
		{
			name: 'Regula-Falsi Method',
			description:
				'Regula-Falsi method is described as the trial and error approach of using “false” or “test” values for the variable and then altering the test value according to the result. In this article, you will learn how to solve an equation in one variable using the false position method. Also, get solved examples on the regula falsi method here. ',
			path: 'regula-falsi-method',
			image: '/RegulaFalsiMethod.webp'
		},
		{
			name: 'Newton-Raphson Method',
			description:
				'The Newton-Raphson method begins with an initial estimate of the root, denoted x0≠xr, and uses the tangent of f(x) at x0 to improve on the estimate of the root',
			path: 'newton-raphson-method',
			image: '/NewtonRaphsonMethod.webp'
		},
		{
			name: 'Secant Method',
			description:
				'Secant method is also a recursive method for finding the root for the polynomials by successive approximation. It’s similar to the Regula-Falsi method but here we don’t need to check f(x1)f(x2)<0 again and again after every approximation',
			path: 'secant-method',
			image: '/SecantMethod.webp'
		},
		{
			name: 'Fixed Point Iteration Method',
			description:
				'The fixed point iteration method in numerical analysis is used to find an approximate solution to algebraic and transcendental equations. Sometimes, it becomes very tedious to find solutions to cubic, bi-quadratic and transcendental equations; then, we can apply specific numerical methods to find the solution; one among those methods is the fixed point iteration method.',
			path: 'fixed-point-iteration-method',
			image: '/FixedPointIterationMethod.webp'
		}
	];
</script>

<Header heading="Numerical Analysis" />

<section id="binaryCalculator" class="bg-gray-100 py-5 px-2">
	<div class="mx-auto grid max-w-7xl grid-cols-1 justify-items-center space-y-4 md:grid-cols-3">
		{#each nurmericalCalcs as calc}
			<div class="card card-compact w-96 bg-base-100 shadow-xl">
				<figure><img src={calc.image} alt="{calc.name} Image" /></figure>
				<div class="card-body text-gray-100">
					<h2 class="card-title">{calc.name}</h2>
					<p>{calc.description}</p>
					<div class="card-actions justify-end">
						<a href="/numerical-analysis/{calc.path}" class="btn-primary btn">Calculator</a>
					</div>
				</div>
			</div>
		{/each}
	</div>
</section>
