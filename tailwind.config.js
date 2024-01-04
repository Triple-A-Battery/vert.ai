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
				Lato: ['Lato', 'sans-serif']
			}
		}
	},
	plugins: [require('daisyui')]
};

export default config;
