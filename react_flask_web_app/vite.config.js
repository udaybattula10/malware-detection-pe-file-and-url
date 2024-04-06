import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";
import { resolve } from "path";

// https://vitejs.dev/config/
// const root = resolve(__dirname,'src')

// const outDir = resolve(__dirname,'dist')
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      "/api": {
        target: "https://malware-detection-flask-api-intel.onrender.com",
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, " "),
      },
    },
    cors: false,
    headers: {},
  },
  build: {
    rollupOptions: {},
  },
});
