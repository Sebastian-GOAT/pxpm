import { defineConfig } from 'tsup';

export default defineConfig({
  entry: { index: 'src/index.ts' },
  outDir: '.',
  format: ['esm'],
  dts: false,
  sourcemap: false,
  clean: false,
  minify: true,
  target: 'node16',
});