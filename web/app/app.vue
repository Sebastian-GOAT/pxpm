<template>
    <UApp>
        <NuxtLayout>
            <NuxtPage />
        </NuxtLayout>
    </UApp>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');
@import "tailwindcss";
@import "@nuxt/ui";

:root {
    --primary: #1173D4;

    --bg: #F6F7F8;
    --fg: black;

    --bg-card: #1C242D; /* Change to light mode */
}

.dark {
    --bg: #101922;
    --fg: white;

    --bg-card: #1C242D;
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
    font-family: "Inter", sans-serif;
}
</style>