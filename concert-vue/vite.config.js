import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
const backendPath = '../concerts_django';
// https://vitejs.dev/config/
export default defineConfig({
    plugins: [vue()],
    base: '/static/vite',
    server: {
        watch: {
            ignored: [],
        },
    },
    build: {
        manifest: true,
        emptyOutDir: true,
        rollupOptions: {
            input: {
                vue_concerts_edit: "./src/apps/concert_edit/main.js",
            },
        },
    },
});