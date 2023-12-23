// import autoprefixer from 'autoprefixer'
// import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// // https://vitejs.dev/config/
// export default defineConfig({
//   plugins: [react()],
// })
import { defineConfig } from 'vite'
// import reactRefresh from '@vitejs/plugin-react-refresh'
import { resolve } from 'path'
import postcss from 'postcss'
import autoprefixer from 'autoprefixer'
import tailwindcss from 'tailwindcss'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  css: {
    postcss: {
      plugins: [
        autoprefixer,
        tailwindcss(resolve(__dirname, './tailwind.config.js')),
      ],
    },
  },
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src'),
    },
  },
  build: {
    outDir: 'build',
    assetsDir: 'assets',
    sourcemap: true,
  }
})