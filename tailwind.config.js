/** @type {import('tailwindcss').Config} */
const config = {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {
			colors: {
				background: '#1E1E03',
				primary: '#3D3206',
				accent: '#F9CD86',
				text: '#FDEBCE'
			},
			fontFamily: {
				sans: ['Gabriela'],
				Lato: ['Gabriela', 'sans-serif']
			}
		}
	},
	daisyui: {
		darkTheme: false
	},
	plugins: [require('daisyui')]
};

export default config;
