<template>
    <UApp>
        <NuxtLayout>
            <NuxtPage />
        </NuxtLayout>
    </UApp>
</template>

<style>
@import "tailwindcss";
@import "@nuxt/ui";

:root {
    --primary: black;

    --bg: black;
    --fg: white;
}

.dark {
    --bg: black;
    --fg: white;
}

@theme inline {
    --color-primary: var(--primary);

    --color-bg: var(--bg);
    --color-fg: var(--fg);
}

body {
    min-height: 100vh;
    background-color: var(--bg);
    color: var(--fg);
}
</style>